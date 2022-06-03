# WSCS4b_predict
[![build](https://github.com/Yuluuuuan/WSCS4b_predict/actions/workflows/build.yml/badge.svg)](https://github.com/Yuluuuuan/WSCS4b_predict/actions/workflows/build.yml)
[![unit_test](https://github.com/Yuluuuuan/WSCS4b_predict/actions/workflows/unit_test.yml/badge.svg)](https://github.com/Yuluuuuan/WSCS4b_predict/actions/workflows/unit_test.yml)

This is a Brane package for training model and predicting. 

Make sure you have brane installed.

Import the package as follows:
```bash
$ brane import Yuluuuuan/WSCS4b_predict
```
Set the environment variable. It shows where the data files are.

```bash
$ export INPUT_PATH='/data'
$ export OUTPUT_PATH='/data'
```

There are four functions in this package:

`run_LR(input_path: str, output_path:str)` \
`run_RF(input_path: str, output_path:str)`\
`run_xgboost(input_path: str, output_path:str)` \
for training three models: linear regression, random forest and XGBoost respectively and predicting the corresponding sales data.

Through `final_result(input_path:str, output_path:str)`,\
we can get files in the format of sample_submission and the result file with other detailed information seperately from the XGBoost prediction value.

The file with all information can be used in visualization part.

You can `test` the package to get an overview of these functions and corresponding parameters:
```bash
$ brane --debug test predict
```

You should push the package into your brane instance to be able to import it in your remote session or jupyterlab notebook.
```bash
$ brane push predict
```
