# Headless 

## Chrome 

Install chromedriver: http://chromedriver.chromium.org/downloads

```python
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.set_headless()
# opts.headless = True
# opts.add_argument('headless')
driver = webdriver.Chrome(options=opts)
```

## Firefox 

Install geckodriver: https://github.com/mozilla/geckodriver/releases

```python
from selenium import webdriver
opts = webdriver.FirefoxOptions()
opts.set_headless()
# opts.headless = True
# opts.add_argument('headless')
driver = webdriver.Firefox(options=opts)
```

## PhantomJS (archived)

Project: https://github.com/ariya/phantomjs
Install PhantomJS webdriver: http://phantomjs.org/download.html

#### Running PhantomJS in Docker container

```bash
docker run -d -p 8910:8910 wernight/phantomjs phantomjs --webdriver=8910
```

```python
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor='http://127.0.0.1:8910',
    desired_capabilities=DesiredCapabilities.PHANTOMJS)
```


