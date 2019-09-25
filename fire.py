from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import options

from selenium.webdriver.

opts = Options()
opts.set_headless()
assert opts.headless # without GUI

browser = Firefox(options=opts)
browser.get('http://192.168.0.38:8080')