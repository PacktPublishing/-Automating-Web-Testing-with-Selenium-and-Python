# Creating a test report 

Example: Goal to have nice report that will de available in html format. 

Limitation: unittest doesn't give a lot of options, we need to write our own report generator/parser

## [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html)

3rd party code, python2 compatible 

## pytest-html

`pip install pytest-html`

`pytest -v result.py --html=pytest_report.html --self-contained-html`

