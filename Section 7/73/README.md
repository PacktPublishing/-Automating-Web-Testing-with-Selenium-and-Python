# Managing test results 

## [TestRestult class in unittest](https://docs.python.org/3.6/library/unittest.html#unittest.TestResult)

`python -i result.py`

- result.testsRun
- result.failures
- result.errors
- result.skipped

## nose example 

`pip install nose`
`nosetests -v result.py`

## pytest example 

`pip install pytest`
`python -v result.py`

### json output example with pytest 

`pip install pytest-json`
`pytest -v result.py --json=report.json`
