# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Pub/Sub message formatter and parser."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import enum
import traceback
from typing import Optional

import attr

from google.cloud import pubsub_v1
from google.rpc import code_pb2
from hcls_imaging_ml_toolkit import dicom_path
from hcls_imaging_ml_toolkit import exception


# Possible values for the "conflict" attribute of the Pub/Sub notification.
# The attribute controls how conflicts with existing DICOM instances containing
# inference module predictions are resolved.
class ConflictType(enum.Enum):
  # Raises an exception with status_code PREDICTION_EXISTS_ERROR.
  ABORT_CONFLICT = 1

  # Ignores conflicts and proceeds without change.
  IGNORE_CONFLICT = 2

  # Deletes all existing DICOM instances containing an inference module
  # prediction and then proceeds to create a new prediction.
  OVERWRITE_CONFLICT = 3


CONFLICT_MAP = {
    'abort': ConflictType.ABORT_CONFLICT,
    'ignore': ConflictType.IGNORE_CONFLICT,
    'overwrite': ConflictType.OVERWRITE_CONFLICT
}

DEFAULT_CONFLICT = ConflictType.ABORT_CONFLICT


@attr.s
class ParsedMessage(object):
  """ParsedMessage represents the parsed Pub/Sub message.

  Attributes:
    input_path: Path object referencing the DICOM resource specified in the
      message.
    conflict: Pub/Sub message attribute which determines behaviour of conflicts
      with existing DICOM instances containing inference module predictions.
    test: Pub/Sub message attribute determining whether the module is running in
      a test mode. When running in a test mode, the module might save
      (e.g. in a Structured Report) additional information which can help with
      debugging..
    output_dicom_store_path: DICOMStore path to write inference results to. This
      comes from parsing the optional Pub/Sub message |output_dicom_store_path|
      attribute. This allows for results to be written to a different
      DICOMStore.
  """
  input_path = attr.ib(type=dicom_path.Path)
  conflict = attr.ib(type=ConflictType, default=DEFAULT_CONFLICT)
  test = attr.ib(type=bool, default=False)
  output_dicom_store_path = attr.ib(
      type=Optional[dicom_path.Path], default=None)


def ParseMessage(message: pubsub_v1.types.PubsubMessage,
                 path_type: dicom_path.Type) -> ParsedMessage:
  """Parses input Pub/Sub message into a ParsedMessage object.

  Args:
    message: Pub/Sub message to be parsed. Expected to contain a DICOMweb path
      starting from "projects/" and down to the level of a Study UID,
      Series UID, or Instance UID.
    path_type: indicates the expected type of the DICOM resource the path in the
      message points to.

  Returns:
    ParsedMessage object representing parsed Pub/Sub message data.

  Raises:
    exception.CustomExceptionError with status code INVALID_ARGUMENT if the
      input doesn't match expected format.
  """
  input_path_str = message.data.decode()
  # Support both 'True' and 'true' for user convenience with manual invocation.
  test_attr = (message.attributes.get('test') in ['True', 'true'])
  conflict_attr = message.attributes.get('conflict')
  if conflict_attr and conflict_attr not in CONFLICT_MAP:
    raise exception.CustomExceptionError(
        'Unexpected value for conflict attribute: %s. Must be one of the '
        'following values: %s' % (conflict_attr, CONFLICT_MAP.keys()),
        code_pb2.Code.INVALID_ARGUMENT)
  conflict = CONFLICT_MAP[conflict_attr] if conflict_attr else DEFAULT_CONFLICT

  try:
    input_path = dicom_path.FromString(input_path_str, path_type)
    parsed_message = ParsedMessage(
        input_path=input_path, conflict=conflict, test=test_attr)

    # Set the output DICOM store path, if available.
    output_store_path_str = message.attributes.get('output_dicom_store_path')
    if output_store_path_str is not None:
      output_store_path = dicom_path.FromString(output_store_path_str,
                                                dicom_path.Type.STORE)
      parsed_message.output_dicom_store_path = output_store_path
    return parsed_message
  except ValueError as e:
    traceback.print_exc()
    raise exception.CustomExceptionError(str(e), code_pb2.Code.INVALID_ARGUMENT)
