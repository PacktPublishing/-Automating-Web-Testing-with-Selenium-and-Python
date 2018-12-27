from selenium import webdriver
from bs4 import BeautifulSoup
import requests, sys, time


def sel(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    event_list = driver.find_element_by_css_selector('#content ul[class="list-recent-events menu"]')
    return BeautifulSoup(event_list.get_attribute('innerHTML'), 'html.parser')


def req(url):
    events_html = requests.get(url)
    return BeautifulSoup(events_html.content, 'html.parser')


if __name__ == '__main__':
    start = time.time() 
    try:
        html_list = eval(sys.argv[1])('https://www.python.org/events/')
    except IndexError:
        print('Error: Argument "sel" or "req" missing...')
        exit(1)
    times = html_list.select('time') # time html tag
    locations = html_list.select('.event-location') # event-location class
    for i in range(len(times)):
        print('{}\t{}'.format(times[i].text[:6], locations[i].text))
    print('------------------------------------------------')
    print('Runtime: {:.2f} s'.format(time.time()-start))