driver = None

def set_driver(_driver):
	global driver
	driver = _driver

def get_driver():
	return driver

def initialize_driver(browserType):
	from selenium import webdriver
	from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
	if browserType == "CHROME":
		chrome_options = webdriver.ChromeOptions()
		chrome_options.accept_untrusted_certs = True
		chrome_options.assume_untrusted_cert_issuer = True
		chrome_options.useAutomationExtension = False
		chrome_options.add_argument("--start-maximized")
		chrome_options.add_argument("--ignore-certificate-errors")
		cap = DesiredCapabilities.CHROME.copy()
		cap["acceptSslCerts"] = True
		cap["webStorageEnabled"] = True
		cap["nativeEvents"] = True
		cap["applicationCacheEnabled"] = True
		cap["javascriptEnabled"] = True
		driver = webdriver.Chrome(executable_path="c:/programData/IAF/bin/webdrivers/chromedriver.exe", chrome_options=chrome_options, desired_capabilities=cap)
	elif browserType == "FIREFOX":
		capabilities = DesiredCapabilities.FIREFOX
		capabilities['marionette'] = True
		driver = webdriver.Firefox(executable_path="c:/programData/IAF/bin/webdrivers/geckodriver.exe", capabilities=capabilities)
	return driver
