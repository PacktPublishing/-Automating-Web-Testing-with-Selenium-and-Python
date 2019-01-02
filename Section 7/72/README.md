# Configuring headless to run in Grid 

## grid

`java -jar selenium-server-standalone-3.9.1.jar -role hub -cleanUpCycle 5000 -timeout 30`

`java -jar selenium-server-standalone-3.9.1.jar -role node -hub http://192.168.122.60:4444/grid/register/ -timeout 30 -maxSession 5`


## headless for grid 

```python
opts = webdriver.ChromeOptions()
opts.set_headless()
driver = webdriver.Remote(command_executor = 'http://192.168.122.60:4444/wd/hub', 
                        desired_capabilities = opts.to_capabilities())
```

```python
opts = webdriver.FirefoxOptions()
opts.set_headless()
driver = webdriver.Remote(command_executor = 'http://192.168.122.60:4444/wd/hub', 
                        desired_capabilities = opts.to_capabilities())
```


