## kada-gx-plugin

kada-gx-plugin generates validation results in a format for loading into the K Platform.

Plugin has been tested for only Great Expectations versions `0.15.41` - `0.18.19`.

Results will continue to be written to existing validation stores if other checkpoint actions are defined eg `StoreValidationResultAction`.

### Steps to use the KadaStoreValidationResultsAction from the plugin

1. Install the plugin by `pip install kada-gx-plugin` to write to a local filesystem or `pip install kada-gx-plugin[azure]` to write to an Azure blob store. Additional azure dependencies will be required.

2. In your required `checkpoint`, add the following action to your checkpoint `.yml` file. `AZURE_BLOB_SAS_URL` is the container SAS token which is provided by KADA. `prefix` should be updated to the landing folder found in K Platform Source onboarding.

>#### Checkpoint action for writing to local filesystem
```yml
  - name: store_kada_validation_result
    action:
      class_name: KadaStoreValidationResultsAction
      module_name: kada_ge_store_plugin.kada_store_validation
      prefix: lz/ge_landing/landing
      test_directory: /tmp/test_ge_results
```
This will write validation result files to /tmp/test_ge_results/lz/ge_landing/landing

>#### Checkpoint action for writing to Azure blob store

```yml
  - name: store_kada_validation_result
    action:
      class_name: KadaStoreValidationResultsAction
      module_name: kada_ge_store_plugin.kada_store_validation
      prefix: lz/ge_landing/landing
      azure_blob_sas_url: ${AZURE_BLOB_SAS_URL}
```

3. Defined the variable `AZURE_BLOB_SAS_URL`. In `uncommited/config_variables.yml` add the variable `AZURE_BLOB_SAS_URL: <SAS url blob >` or alternatively set `AZURE_BLOB_SAS_URL` in the environment variables.