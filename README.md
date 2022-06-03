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
for three models: linear regression, random forest and XGBoost respectively. We can get corresponding results

Through `final_result(input_path:str, output_path:str)`,\
we can get our prediction result

You can `test` the package to get an overview of these functions and corresponding parameters:
```bash
$ brane --debug test predict
```

You should push the package into your brane instance to be able to import it in your remote session or jupyterlab notebook.
```bash
$ brane push predict
```
