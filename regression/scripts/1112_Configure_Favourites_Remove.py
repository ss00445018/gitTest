#
# Application: QSpace
# Release: 2019.06
# Test Case: Configure_Favourites_Remove
# Created On: Mon Sep 30 09:13:09 IST 2019
# Created By: iTM
#
print("Executing 1112_Configure_Favourites_Remove.py")
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from common.LoggerFactory import setup_logger
from common.ResultFactory import step_header, test_step_status, test_case_status
from common.Driver import set_driver, get_driver, initialize_driver
from common.RunSetup import testData, update_current_data

screenshotpath = "./Results/Evidences/"
def saveScreenshot(filename):
	name = screenshotpath + filename
	driver.get_screenshot_as_file(name)

def handleException(e, mustPassIndicator):
	logger.error("Error {}".format(e))
	if mustPassIndicator == "Mandatory":
		global test_case_continue
		test_case_continue = False
#
# Variables
test_case_continue = True
driver = get_driver("QSPACE")
#
logger = setup_logger("tc_{}_{}.log".format(testData["tcId"], testData["runId"]))
#
def Configure_Favourites_Remove():
	#
	step_header(testData["release"], testData["tcId"], testData["runId"], testData["batchId"], testData["iter"], testData["callingStep"])
	#
	# Step 1, Must Pass Indicator: Mandatory
	# Description: Launch QSpace application,
	# Expected Result: QSpace - Wait Until txtUserName web element is displayed in the Login Page [max 100 secs]
	#
	logger.info("Executing Test Step [1]")

	global driver
	try:
		driver = initialize_driver(testData["browserType"])
		driver.delete_all_cookies()
		driver.get(testData["QSPACE"])
		set_driver(driver, "QSPACE")
		resultMsg = "Launch QSpace Application Successful"
		logger.info("Launch QSpace Application Successful")
	except Exception as e:
		resultMsg = "Launch QSpace Application Unsuccessful"
		logger.info("Launch QSpace Application Unsuccessful")
		test_step_status(1, resultMsg, e, "Action", "Failed", "")
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_1_1569814989476.png".format(testData["runId"]))
	test_step_status(1, resultMsg, "", "Action", "Passed", "{}_Step_1_1569814989476.png".format(testData["runId"]))
	try:
		WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//input[@id='txtLogin']")))
		resultMsg = "Wait for txtUserName webelement on Page Login successful"
		logger.info("Wait for txtUserName webelement on Page Login successful")
	except Exception as e:
		resultMsg = "Wait for txtUserName webelement on Page Login Failed"
		logger.info("Wait for txtUserName webelement on Page Login Failed")
		saveScreenshot("{}_Step_1_1569814989503_Error.png".format(testData["runId"]))
		test_step_status(1, resultMsg, e, "Verification", "Failed", "{}_Step_1_1569814989503_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_1_1569814989507.png".format(testData["runId"]))
	test_step_status(1, resultMsg, "", "Verification", "Passed", "{}_Step_1_1569814989507.png".format(testData["runId"]))
	#
	# Step 2, Must Pass Indicator: Mandatory
	# Description: QSpace - Enter UserName in txtUserName textbox in the Login Page,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [2]")
	try:
		driver.find_element(By.XPATH, "//input[@id='txtLogin']").send_keys(testData["USERNAME"])
		resultMsg = "Enter value in txtUserName  textbox on Page Login Successful"
		logger.info("Enter value in txtUserName  textbox on Page Login Successful")
	except Exception as e:
		resultMsg = "Enter value in txtUserName  textbox on Page Login Failed"
		logger.info("Enter value in txtUserName  textbox on Page Login Failed")
		saveScreenshot("{}_Step_2_1569814989523_Error.png".format(testData["runId"]))
		test_step_status(2, resultMsg, e, "Action", "Failed", "{}_Step_2_1569814989523_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_2_1569814989526.png".format(testData["runId"]))
	test_step_status(2, resultMsg, "", "Action", "Passed", "{}_Step_2_1569814989526.png".format(testData["runId"]))
	#
	# Step 3, Must Pass Indicator: Mandatory
	# Description: QSpace - Enter Password in txtPassword textbox in the Login Page,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [3]")
	try:
		driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys(testData["PASSWORD"])
		resultMsg = "Enter value in txtPassword  textbox on Page Login Successful"
		logger.info("Enter value in txtPassword  textbox on Page Login Successful")
	except Exception as e:
		resultMsg = "Enter value in txtPassword  textbox on Page Login Failed"
		logger.info("Enter value in txtPassword  textbox on Page Login Failed")
		saveScreenshot("{}_Step_3_1569814989536_Error.png".format(testData["runId"]))
		test_step_status(3, resultMsg, e, "Action", "Failed", "{}_Step_3_1569814989536_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_3_1569814989547.png".format(testData["runId"]))
	test_step_status(3, resultMsg, "", "Action", "Passed", "{}_Step_3_1569814989547.png".format(testData["runId"]))
	#
	# Step 4, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Go Button in the Resolve Page,
	# Expected Result: QSpace - Wait Until Resolve web element is displayed in the Main Page [max 20 secs]
	#
	logger.info("Executing Test Step [4]")
	try:
		driver.find_element(By.XPATH, "//*[@id='imgLogin']").click()
		resultMsg = "Clicking on Go button on Page Resolve successful"
		logger.info("Clicking on Go button on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on Go button on Page Resolve Failed"
		logger.info("Clicking on Go button on Page Resolve Failed")
		saveScreenshot("{}_Step_4_1569814989566_Error.png".format(testData["runId"]))
		test_step_status(4, resultMsg, e, "Action", "Failed", "{}_Step_4_1569814989566_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_4_1569814989568.png".format(testData["runId"]))
	test_step_status(4, resultMsg, "", "Action", "Passed", "{}_Step_4_1569814989568.png".format(testData["runId"]))
	try:
		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Resolve']")))
		resultMsg = "Wait for Resolve webelement on Page Main successful"
		logger.info("Wait for Resolve webelement on Page Main successful")
	except Exception as e:
		resultMsg = "See additional message and/or iAF logs"
		logger.info("See additional message and/or iAF logs")
		saveScreenshot("{}_Step_4_1569814989571_Error.png".format(testData["runId"]))
		test_step_status(4, resultMsg, e, "Verification", "Failed", "{}_Step_4_1569814989571_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_4_1569814989580.png".format(testData["runId"]))
	test_step_status(4, resultMsg, "", "Verification", "Passed", "{}_Step_4_1569814989580.png".format(testData["runId"]))
	#
	# Step 5, Must Pass Indicator: Mandatory
	# Description: QSpace - Click ConfigureFavourites Button in the Main Page,
	# Expected Result: QSpace - Wait Until FavouritesSave web element is displayed in the Main Page [max 20 secs]
	#
	logger.info("Executing Test Step [5]")
	try:
		driver.find_element(By.XPATH, "//span[text()='Configure Favorites']").click()
		resultMsg = "Clicking on ConfigureFavourites button on Page Main successful"
		logger.info("Clicking on ConfigureFavourites button on Page Main successful")
	except Exception as e:
		resultMsg = "Clicking on ConfigureFavourites button on Page Main Failed"
		logger.info("Clicking on ConfigureFavourites button on Page Main Failed")
		saveScreenshot("{}_Step_5_1569814989598_Error.png".format(testData["runId"]))
		test_step_status(5, resultMsg, e, "Action", "Failed", "{}_Step_5_1569814989598_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_5_1569814989602.png".format(testData["runId"]))
	test_step_status(5, resultMsg, "", "Action", "Passed", "{}_Step_5_1569814989602.png".format(testData["runId"]))
	try:
		WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='btnSave']")))
		resultMsg = "Wait for FavouritesSave webelement on Page Main successful"
		logger.info("Wait for FavouritesSave webelement on Page Main successful")
	except Exception as e:
		resultMsg = "See additional message and/or iAF logs"
		logger.info("See additional message and/or iAF logs")
		saveScreenshot("{}_Step_5_1569814989605_Error.png".format(testData["runId"]))
		test_step_status(5, resultMsg, e, "Verification", "Failed", "{}_Step_5_1569814989605_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_5_1569814989609.png".format(testData["runId"]))
	test_step_status(5, resultMsg, "", "Verification", "Passed", "{}_Step_5_1569814989609.png".format(testData["runId"]))
	#
	# Step 6, Must Pass Indicator: Mandatory
	# Description: QSpace - Click FavouritesItem webelement in the Main Page having FavouritesItem value,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [6]")
	try:
		driver.find_element(By.XPATH, "//option[text()='{}']".format(testData["FAVOURITESITEM"])).click()
		resultMsg = "Click on FavouritesItem webelement is successful"
		logger.info("Click on FavouritesItem webelement is successful")
	except Exception as e:
		resultMsg = "Click on FavouritesItem webelement is failed"
		logger.info("Click on FavouritesItem webelement is failed")
		saveScreenshot("{}_Step_6_1569814989617_Error.png".format(testData["runId"]))
		test_step_status(6, resultMsg, e, "Action", "Failed", "{}_Step_6_1569814989617_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_6_1569814989622.png".format(testData["runId"]))
	test_step_status(6, resultMsg, "", "Action", "Passed", "{}_Step_6_1569814989622.png".format(testData["runId"]))
	#
	# Step 7, Must Pass Indicator: Mandatory
	# Description: QSpace - Click RemoveFavourites Button in the Main Page,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [7]")
	try:
		driver.find_element(By.XPATH, "//input[@id='btnRemove']").click()
		resultMsg = "Clicking on RemoveFavourites button on Page Main successful"
		logger.info("Clicking on RemoveFavourites button on Page Main successful")
	except Exception as e:
		resultMsg = "Clicking on RemoveFavourites button on Page Main Failed"
		logger.info("Clicking on RemoveFavourites button on Page Main Failed")
		saveScreenshot("{}_Step_7_1569814989627_Error.png".format(testData["runId"]))
		test_step_status(7, resultMsg, e, "Action", "Failed", "{}_Step_7_1569814989627_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_7_1569814989631.png".format(testData["runId"]))
	test_step_status(7, resultMsg, "", "Action", "Passed", "{}_Step_7_1569814989631.png".format(testData["runId"]))
	#
	# Step 8, Must Pass Indicator: Mandatory
	# Description: QSpace - Click FavouritesSave Button in the Main Page,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [8]")
	try:
		driver.find_element(By.XPATH, "//input[@id='btnSave']").click()
		resultMsg = "Clicking on FavouritesSave button on Page Main successful"
		logger.info("Clicking on FavouritesSave button on Page Main successful")
	except Exception as e:
		resultMsg = "Clicking on FavouritesSave button on Page Main Failed"
		logger.info("Clicking on FavouritesSave button on Page Main Failed")
		saveScreenshot("{}_Step_8_1569814989633_Error.png".format(testData["runId"]))
		test_step_status(8, resultMsg, e, "Action", "Failed", "{}_Step_8_1569814989633_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_8_1569814989634.png".format(testData["runId"]))
	test_step_status(8, resultMsg, "", "Action", "Passed", "{}_Step_8_1569814989634.png".format(testData["runId"]))
	#
	# Step 9, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Logout Button in the Main Page,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [9]")
	try:
		driver.find_element(By.XPATH, "//input[@id='imgbtnLogout']").click()
		resultMsg = "Clicking on Logout button on Page Main successful"
		logger.info("Clicking on Logout button on Page Main successful")
	except Exception as e:
		resultMsg = "Clicking on Logout button on Page Main Failed"
		logger.info("Clicking on Logout button on Page Main Failed")
		saveScreenshot("{}_Step_9_1569814989637_Error.png".format(testData["runId"]))
		test_step_status(9, resultMsg, e, "Action", "Failed", "{}_Step_9_1569814989637_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

	saveScreenshot("{}_Step_9_1569814989639.png".format(testData["runId"]))
	test_step_status(9, resultMsg, "", "Action", "Passed", "{}_Step_9_1569814989639.png".format(testData["runId"]))
	#
	# Step 10, Must Pass Indicator: Mandatory
	# Description: QSpace - Close Application,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [10]")
	try:
		driver.quit()
		resultMsg = "Close Application QSpace successful"
		logger.info("Close Application QSpace successful")
	except Exception as e:
		resultMsg = "Close Application QSpace Failed"
		logger.info("Close Application QSpace Failed")
		saveScreenshot("{}_Step_10_1569814989641_Error.png".format(testData["runId"]))
		test_step_status(10, resultMsg, e, "Action", "Failed", "{}_Step_10_1569814989641_Error.png".format(testData["runId"]))
		handleException(e, "Mandatory")
		return

#
if test_case_continue: Configure_Favourites_Remove()
test_case_status(testData["dispatchId"], testData["batchId"], testData["callingStep"], testData["iter"], testData["tcName"])
#
