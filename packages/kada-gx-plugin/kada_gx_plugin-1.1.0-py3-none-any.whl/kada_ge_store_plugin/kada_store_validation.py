"""
Great Expectations plugin to send validation results to
Azure blob storage with custom filename and filepath.

This subpackage needs to be used in Great Expectations
checkpoints actions.
"""

import functools
import os
import json
import logging
from typing import Optional, Union

from great_expectations.core.config_substitutor import _ConfigurationSubstitutor
from great_expectations.checkpoint.actions import ValidationAction
from great_expectations.core.batch import Batch, batch_request_contains_runtime_parameters
from great_expectations.core.expectation_validation_result import ExpectationSuiteValidationResult
from great_expectations.data_asset.data_asset import DataAsset
from great_expectations.data_context.data_context import DataContext
from great_expectations.data_context.types.resource_identifiers import (
    ExpectationSuiteIdentifier,
    GXCloudIdentifier,
    ValidationResultIdentifier,
)
from great_expectations.exceptions import StoreBackendError
from great_expectations.validator.validator import Validator

logger = logging.getLogger(__name__)

class KadaStoreValidationResultsAction(ValidationAction):
    """Kada Store validation action. It inherits from
    great expection validation action class and implements the
    `_run` method.

    Attributes:
        data_context: great expectation data context
        prefix: The folder path in your container where the .json blob will be stored.
        azure_blob_sas_url: The SAS url for the Azure Storage Account container
        test_directory: Local directory to store the validation results
    """
    # pylint: disable=arguments-differ,unused-argument
    def __init__(
        self,
        data_context: DataContext,
        *args,
        test_directory=None,
        prefix=None,
        azure_blob_sas_url=None,
        **kwargs
    ):
        super().__init__(data_context, *args, **kwargs) # Use args and kwargs to be resiliant to change
        self.prefix = prefix
        self.azure_blob_sas_url = azure_blob_sas_url
        self.test_directory = test_directory

    # pylint: disable=arguments-differ,unused-argument
    def _run(
        self,
        validation_result_suite: ExpectationSuiteValidationResult,
        validation_result_suite_identifier: Union[
            ValidationResultIdentifier, GXCloudIdentifier
        ],
        data_asset: Union[Validator, DataAsset, Batch],
        expectation_suite_identifier: Optional[ExpectationSuiteIdentifier] = None,
        checkpoint_identifier=None,
        payload=None,
    ):
        """main function to implement great expectation hook

        Args:
            validation_result_suite: result suite returned when checkpoint is ran
            validation_result_suite_identifier: type of result suite
            data_asset:
            payload:
            expectation_suite_identifier: type of expectation suite
            checkpoint_identifier: identifier for the checkpoint
        """
        logger.debug("KadaStoreValidationAction.run")

        if validation_result_suite is None:
            logger.warning(
                'No validation_result_suite was passed to %s action. Skipping action.', type(self).__name__
            )
            return

        if not isinstance(
            validation_result_suite_identifier,
            (ValidationResultIdentifier, GXCloudIdentifier),
        ):
            raise TypeError(
               "validation_result_id must be of type ValidationResultIdentifier or GeCloudIdentifier, not {}".format(
                    type(validation_result_suite_identifier)
                )
            )
        
        batch_id = validation_result_suite_identifier.batch_identifier
        run_time = validation_result_suite_identifier.run_id.run_time.strftime('%Y%m%d%H%M%S%f')
        json_dict = validation_result_suite.to_json_dict()
        file_name = ''.join([batch_id,'_expectation_result_',run_time,'.json'])
            
        if self.test_directory:
            os.makedirs(f"{self.test_directory}/{self.prefix}", exist_ok=True)
            file_key = os.path.join(f"{self.test_directory}/{self.prefix}", file_name)
        if hasattr(data_asset, 'active_batch') and hasattr(data_asset.active_batch, 'data_asset') and hasattr(data_asset.active_batch.data_asset, 'batch_metadata'):
            # https://github.com/great-expectations/great_expectations/blob/864c6bb759c6344944817c4654787a37d37475d2/great_expectations/datasource/fluent/interfaces.py#L255
            # Batch metadata from te active asset is not subsituted, we need to do it manually
            config_variables = data_asset.active_batch.data_asset._datasource._data_context.config_variables 
            additional_meta = _ConfigurationSubstitutor().substitute_all_config_variables(
                data=data_asset.active_batch.data_asset.batch_metadata, replace_variables_dict=config_variables
            )
            json_dict['meta']['batch_spec'].update(additional_meta)
        json_dict['meta']['batch_spec'].update(json_dict['evaluation_parameters']) # Merge evaluation parameters into the batch spec
        if 'batch_spec_passthrough' in json_dict['meta']['batch_spec']: # Merge batch_spec_passthrough parameters into the batch spec caters for non fluent datasource assets
            json_dict['meta']['batch_spec'].update(json_dict['meta']['batch_spec']['batch_spec_passthrough'])
        if batch_request_contains_runtime_parameters(data_asset.active_batch.batch_request): # Append any runtime info to the batch_spec
            json_dict['meta']['batch_spec'].update(
                data_asset.active_batch.batch_request.get("runtime_parameters")
            )
        # Guard against different data types
        if 'batch_data' in json_dict['meta']['batch_spec']:
            json_dict['meta']['batch_spec']['batch_data'] = type(json_dict['meta']['batch_spec']['batch_data']).__name__
        json_object = json.dumps(json_dict, indent=2)
        if self.test_directory:
            with open(file_key, "w") as outfile:
                outfile.write(json_object)
        else:
            self.set(file_name, json_object)

    @property
    @functools.lru_cache()
    def _container_client(self):
        from azure.storage.blob import ContainerClient # Conditional importing

        if self.azure_blob_sas_url:
            return ContainerClient.from_container_url(self.azure_blob_sas_url)
        else:
            raise StoreBackendError(
                "Unable to initialize ServiceClient, credentials should be set"
            )

    def set(self, key, value, content_encoding="utf-8", **kwargs):
        """Set function to upload validation results to Azure Blob Storage

        Args:
            key: Filename for the validation results JSON
            value: Validation Results object to write in the JSON
        """
        from azure.storage.blob import ContentSettings # Conditional importing
        
        az_blob_key = os.path.join(self.prefix, key)

        if isinstance(value, str):
            if az_blob_key.endswith(".html"):
                my_content_settings = ContentSettings(content_type="text/html")
                self._container_client.upload_blob(
                    name=az_blob_key,
                    data=value,
                    encoding=content_encoding,
                    overwrite=True,
                    content_settings=my_content_settings,
                )
            else:
                self._container_client.upload_blob(
                    name=az_blob_key,
                    data=value,
                    encoding=content_encoding,
                    overwrite=True,
                )
        else:
            self._container_client.upload_blob(
                name=az_blob_key, data=value, overwrite=True
            )
        return az_blob_key
