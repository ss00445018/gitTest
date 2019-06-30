#
# Application: QSpace
# Release: 2019.06
# Test Case: Add_Review_Defect
# Created On: Sun Jun 30 20:19:09 IST 2019
# Created By: iTM
#
print("Executing 1089_Add_Review_Defect.py")
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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
	logger.error(e)
	if mustPassIndicator == "Mandatory":
		global test_case_continue
		test_case_continue = False
#
# Variables
test_case_continue = True
driver = get_driver()
#
logger = setup_logger("tc_1089_1.log")
#
def Add_Review_Defect():
	#
	step_header("2019.06", 1089, 1, 1, 1, 0)
	#
	# Step 1, Must Pass Indicator: Mandatory
	# Description: Launch QSpace application using Qspace Url,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [1]")

	global driver
	try:
		driver = initialize_driver(testData["browserType"])
		driver.delete_all_cookies()
		driver.get("QspaceUrl")
		set_driver(driver)
		resultMsg = "Launch QSpace Application Successful"
		logger.info("Launch QSpace Application Successful")
	except Exception as e:
		resultMsg = "Launch QSpace Application Unsuccessful"
		logger.info("Launch QSpace Application Unsuccessful")
		test_step_status(1, resultMsg, e, "Action", "Failed", "")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_1_1561906149107.png")
	test_step_status(1, resultMsg, "", "Action", "Passed", "1_Step_1_1561906149107.png")
	#
	# Step 2, Must Pass Indicator: Mandatory
	# Description: QSpace - Enter UserName in txtUserName textbox in the Login Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [2]")
	resultMsg = ''
	try:
		driver.find_element(By.XPATH, "TBD").send_keys("UserName")
		resultMsg = "Enter value in txtUserName  textbox on Page Login Successful"
		logger.info("Enter value in txtUserName  textbox on Page Login Successful")
	except Exception as e:
		resultMsg = "Enter value in txtUserName  textbox on Page Login Failed"
		logger.info("Enter value in txtUserName  textbox on Page Login Failed")
		saveScreenshot("1_Step_2_1561906149117_Error.png")
		test_step_status(2, resultMsg, e, "Action", "Failed", "1_Step_2_1561906149117_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_2_1561906149119.png")
	test_step_status(2, resultMsg, "", "Action", "Passed", "1_Step_2_1561906149119.png")
	#
	# Step 3, Must Pass Indicator: Mandatory
	# Description: QSpace - Enter Password in txtPassword textbox in the Login Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [3]")
	resultMsg = ''
	try:
		driver.find_element(By.XPATH, "TBD").send_keys("Password")
		resultMsg = "Enter value in txtPassword  textbox on Page Login Successful"
		logger.info("Enter value in txtPassword  textbox on Page Login Successful")
	except Exception as e:
		resultMsg = "Enter value in txtPassword  textbox on Page Login Failed"
		logger.info("Enter value in txtPassword  textbox on Page Login Failed")
		saveScreenshot("1_Step_3_1561906149123_Error.png")
		test_step_status(3, resultMsg, e, "Action", "Failed", "1_Step_3_1561906149123_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_3_1561906149125.png")
	test_step_status(3, resultMsg, "", "Action", "Passed", "1_Step_3_1561906149125.png")
	#
	# Step 4, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Go Button in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [4]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on Go button on Page Resolve successful"
		logger.info("Clicking on Go button on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on Go button on Page Resolve Failed"
		logger.info("Clicking on Go button on Page Resolve Failed")
		saveScreenshot("1_Step_4_1561906149128_Error.png")
		test_step_status(4, resultMsg, e, "Action", "Failed", "1_Step_4_1561906149128_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_4_1561906149130.png")
	test_step_status(4, resultMsg, "", "Action", "Passed", "1_Step_4_1561906149130.png")
	#
	# Step 5, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 4 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [5]")
	time.sleep(4)

	saveScreenshot("1_Step_5_1561906149136.png")
	test_step_status(5, resultMsg, "", "Action", "Passed", "1_Step_5_1561906149136.png")
	#
	# Step 6, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait Until Resolve web element is displayed in the Main Screen [max 30 secs],
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [6]")
	try:
		WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "TBD")))
		resultMsg = "Wait for Resolve web element on Main Page successful"
		logger.info("Wait for Resolve web element on Main Page successful")
	except Exception as e:
		resultMsg = "Wait for Resolve web element on Main Page failed"
		logger.info("Wait for Resolve web element on Main Page failed")
		saveScreenshot("1_Step_6_1561906149150_Error.png")
		test_step_status(6, resultMsg, e, "Action", "Failed", "1_Step_6_1561906149150_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_6_1561906149152.png")
	test_step_status(6, resultMsg, "", "Action", "Passed", "1_Step_6_1561906149152.png")
	#
	# Step 7, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Resolve Hyperlink in the Main Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [7]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on Resolve hyperlink on Page Main successful"
		logger.info("Clicking on Resolve hyperlink on Page Main successful")
	except Exception as e:
		resultMsg = "Clicking on Resolve hyperlink on Page Main Failed"
		logger.info("Clicking on Resolve hyperlink on Page Main Failed")
		saveScreenshot("1_Step_7_1561906149155_Error.png")
		test_step_status(7, resultMsg, e, "Action", "Failed", "1_Step_7_1561906149155_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_7_1561906149156.png")
	test_step_status(7, resultMsg, "", "Action", "Passed", "1_Step_7_1561906149156.png")
	#
	# Step 8, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 2 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [8]")
	time.sleep(2)

	saveScreenshot("1_Step_8_1561906149159.png")
	test_step_status(8, resultMsg, "", "Action", "Passed", "1_Step_8_1561906149159.png")
	#
	# Step 9, Must Pass Indicator: Mandatory
	# Description: QSpace - Select User Role from Role dropdown in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [9]")
	try:
		driver.find_element(By.XPATH, "TBD/option[text()='{}']".format("UserRole")).click()
		resultMsg = "Select User Role value from Role dropdown on Page Resolve Successful"
		logger.info("Select User Role value from Role dropdown on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Select User Role value from Role dropdown on Page Resolve Failed"
		logger.info("Select User Role value from Role dropdown on Page Resolve Failed")
		saveScreenshot("1_Step_9_1561906149161_Error.png")
		test_step_status(9, resultMsg, e, "Action", "Failed", "1_Step_9_1561906149161_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_9_1561906149162.png")
	test_step_status(9, resultMsg, "", "Action", "Passed", "1_Step_9_1561906149162.png")
	#
	# Step 10, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 2 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [10]")
	time.sleep(2)

	saveScreenshot("1_Step_10_1561906149165.png")
	test_step_status(10, resultMsg, "", "Action", "Passed", "1_Step_10_1561906149165.png")
	#
	# Step 11, Must Pass Indicator: Mandatory
	# Description: QSpace - Select AddDefect radio button in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [11]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Selecting AddDefect radio button on Page Resolve successful"
		logger.info("Selecting AddDefect radio button on Page Resolve successful")
	except Exception as e:
		resultMsg = "Selecting AddDefect radio button on Page Resolve Failed"
		logger.info("Selecting AddDefect radio button on Page Resolve Failed")
		saveScreenshot("1_Step_11_1561906149174_Error.png")
		test_step_status(11, resultMsg, e, "Action", "Failed", "1_Step_11_1561906149174_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_11_1561906149175.png")
	test_step_status(11, resultMsg, "", "Action", "Passed", "1_Step_11_1561906149175.png")
	#
	# Step 12, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [12]")
	time.sleep(3)

	saveScreenshot("1_Step_12_1561906149178.png")
	test_step_status(12, resultMsg, "", "Action", "Passed", "1_Step_12_1561906149178.png")
	#
	# Step 13, Must Pass Indicator: Mandatory
	# Description: QSpace - Click GetData Button in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [13]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on GetData button on Page Resolve successful"
		logger.info("Clicking on GetData button on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on GetData button on Page Resolve Failed"
		logger.info("Clicking on GetData button on Page Resolve Failed")
		saveScreenshot("1_Step_13_1561906149180_Error.png")
		test_step_status(13, resultMsg, e, "Action", "Failed", "1_Step_13_1561906149180_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_13_1561906149181.png")
	test_step_status(13, resultMsg, "", "Action", "Passed", "1_Step_13_1561906149181.png")
	#
	# Step 14, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [14]")
	time.sleep(3)

	saveScreenshot("1_Step_14_1561906149184.png")
	test_step_status(14, resultMsg, "", "Action", "Passed", "1_Step_14_1561906149184.png")
	#
	# Step 15, Must Pass Indicator: Mandatory
	# Description: QSpace - Click btnAddDefects Button in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [15]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on btnAddDefects button on Page Resolve successful"
		logger.info("Clicking on btnAddDefects button on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on btnAddDefects button on Page Resolve Failed"
		logger.info("Clicking on btnAddDefects button on Page Resolve Failed")
		saveScreenshot("1_Step_15_1561906149186_Error.png")
		test_step_status(15, resultMsg, e, "Action", "Failed", "1_Step_15_1561906149186_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_15_1561906149189.png")
	test_step_status(15, resultMsg, "", "Action", "Passed", "1_Step_15_1561906149189.png")
	#
	# Step 16, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [16]")
	time.sleep(3)

	saveScreenshot("1_Step_16_1561906149196.png")
	test_step_status(16, resultMsg, "", "Action", "Passed", "1_Step_16_1561906149196.png")
	#
	# Step 17, Must Pass Indicator: Mandatory
	# Description: QSpace - Enter Defect Description in Description textbox in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [17]")
	resultMsg = ''
	try:
		driver.find_element(By.XPATH, "TBD").send_keys("DefectDescription")
		resultMsg = "Enter value in Description  textbox on Page Resolve Successful"
		logger.info("Enter value in Description  textbox on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Enter value in Description  textbox on Page Resolve Failed"
		logger.info("Enter value in Description  textbox on Page Resolve Failed")
		saveScreenshot("1_Step_17_1561906149199_Error.png")
		test_step_status(17, resultMsg, e, "Action", "Failed", "1_Step_17_1561906149199_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_17_1561906149201.png")
	test_step_status(17, resultMsg, "", "Action", "Passed", "1_Step_17_1561906149201.png")
	#
	# Step 18, Must Pass Indicator: Mandatory
	# Description: QSpace - Select Defect Severity from Severity dropdown in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [18]")
	try:
		driver.find_element(By.XPATH, "TBD/option[text()='{}']".format("DefectSeverity")).click()
		resultMsg = "Select Defect Severity value from Severity dropdown on Page Resolve Successful"
		logger.info("Select Defect Severity value from Severity dropdown on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Select Defect Severity value from Severity dropdown on Page Resolve Failed"
		logger.info("Select Defect Severity value from Severity dropdown on Page Resolve Failed")
		saveScreenshot("1_Step_18_1561906149204_Error.png")
		test_step_status(18, resultMsg, e, "Action", "Failed", "1_Step_18_1561906149204_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_18_1561906149206.png")
	test_step_status(18, resultMsg, "", "Action", "Passed", "1_Step_18_1561906149206.png")
	#
	# Step 19, Must Pass Indicator: Mandatory
	# Description: QSpace - Select Detected User from DetectedBy dropdown in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [19]")
	try:
		driver.find_element(By.XPATH, "TBD/option[text()='{}']".format("DetectedUser")).click()
		resultMsg = "Select Detected User value from DetectedBy dropdown on Page Resolve Successful"
		logger.info("Select Detected User value from DetectedBy dropdown on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Select Detected User value from DetectedBy dropdown on Page Resolve Failed"
		logger.info("Select Detected User value from DetectedBy dropdown on Page Resolve Failed")
		saveScreenshot("1_Step_19_1561906149209_Error.png")
		test_step_status(19, resultMsg, e, "Action", "Failed", "1_Step_19_1561906149209_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_19_1561906149210.png")
	test_step_status(19, resultMsg, "", "Action", "Passed", "1_Step_19_1561906149210.png")
	#
	# Step 20, Must Pass Indicator: Mandatory
	# Description: QSpace - Select SDLC Phase from IntroducedIn dropdown in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [20]")
	try:
		driver.find_element(By.XPATH, "TBD/option[text()='{}']".format("SDLCPhase")).click()
		resultMsg = "Select SDLC Phase value from IntroducedIn dropdown on Page Resolve Successful"
		logger.info("Select SDLC Phase value from IntroducedIn dropdown on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Select SDLC Phase value from IntroducedIn dropdown on Page Resolve Failed"
		logger.info("Select SDLC Phase value from IntroducedIn dropdown on Page Resolve Failed")
		saveScreenshot("1_Step_20_1561906149213_Error.png")
		test_step_status(20, resultMsg, e, "Action", "Failed", "1_Step_20_1561906149213_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_20_1561906149214.png")
	test_step_status(20, resultMsg, "", "Action", "Passed", "1_Step_20_1561906149214.png")
	#
	# Step 21, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [21]")
	time.sleep(3)

	saveScreenshot("1_Step_21_1561906149217.png")
	test_step_status(21, resultMsg, "", "Action", "Passed", "1_Step_21_1561906149217.png")
	#
	# Step 22, Must Pass Indicator: Mandatory
	# Description: QSpace - Select Test Case Attribute from Class dropdown in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [22]")
	try:
		driver.find_element(By.XPATH, "TBD/option[text()='{}']".format("TestCaseAttribute")).click()
		resultMsg = "Select Test Case Attribute value from Class dropdown on Page Resolve Successful"
		logger.info("Select Test Case Attribute value from Class dropdown on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Select Test Case Attribute value from Class dropdown on Page Resolve Failed"
		logger.info("Select Test Case Attribute value from Class dropdown on Page Resolve Failed")
		saveScreenshot("1_Step_22_1561906149220_Error.png")
		test_step_status(22, resultMsg, e, "Action", "Failed", "1_Step_22_1561906149220_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_22_1561906149222.png")
	test_step_status(22, resultMsg, "", "Action", "Passed", "1_Step_22_1561906149222.png")
	#
	# Step 23, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [23]")
	time.sleep(3)

	saveScreenshot("1_Step_23_1561906149224.png")
	test_step_status(23, resultMsg, "", "Action", "Passed", "1_Step_23_1561906149224.png")
	#
	# Step 24, Must Pass Indicator: Mandatory
	# Description: QSpace - Select Defect Class from SubClass dropdown in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [24]")
	try:
		driver.find_element(By.XPATH, "TBD/option[text()='{}']".format("DefectClass")).click()
		resultMsg = "Select Defect Class value from SubClass dropdown on Page Resolve Successful"
		logger.info("Select Defect Class value from SubClass dropdown on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Select Defect Class value from SubClass dropdown on Page Resolve Failed"
		logger.info("Select Defect Class value from SubClass dropdown on Page Resolve Failed")
		saveScreenshot("1_Step_24_1561906149226_Error.png")
		test_step_status(24, resultMsg, e, "Action", "Failed", "1_Step_24_1561906149226_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_24_1561906149228.png")
	test_step_status(24, resultMsg, "", "Action", "Passed", "1_Step_24_1561906149228.png")
	#
	# Step 25, Must Pass Indicator: Mandatory
	# Description: QSpace - Enter Defect Raised Date in DetectionDate textbox in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [25]")
	resultMsg = ''
	try:
		driver.find_element(By.XPATH, "TBD").send_keys("DefectRaisedDate")
		resultMsg = "Enter value in DetectionDate  textbox on Page Resolve Successful"
		logger.info("Enter value in DetectionDate  textbox on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Enter value in DetectionDate  textbox on Page Resolve Failed"
		logger.info("Enter value in DetectionDate  textbox on Page Resolve Failed")
		saveScreenshot("1_Step_25_1561906149230_Error.png")
		test_step_status(25, resultMsg, e, "Action", "Failed", "1_Step_25_1561906149230_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_25_1561906149231.png")
	test_step_status(25, resultMsg, "", "Action", "Passed", "1_Step_25_1561906149231.png")
	#
	# Step 26, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Update Hyperlink in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [26]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on Update hyperlink on Page Resolve successful"
		logger.info("Clicking on Update hyperlink on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on Update hyperlink on Page Resolve Failed"
		logger.info("Clicking on Update hyperlink on Page Resolve Failed")
		saveScreenshot("1_Step_26_1561906149232_Error.png")
		test_step_status(26, resultMsg, e, "Action", "Failed", "1_Step_26_1561906149232_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_26_1561906149234.png")
	test_step_status(26, resultMsg, "", "Action", "Passed", "1_Step_26_1561906149234.png")
	#
	# Step 27, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: QSpace - Verify that Confirmation webelement on Resolve page has text same as Defect added successfully
	#
	logger.info("Executing Test Step [27]")
	time.sleep(3)

	saveScreenshot("1_Step_27_1561906149238.png")
	test_step_status(27, resultMsg, "", "Action", "Passed", "1_Step_27_1561906149238.png")
	saveScreenshot("1_Step_27_1561906149242.png")
	test_step_status(27, resultMsg, "", "Verification", "Passed", "1_Step_27_1561906149242.png")
	#
	# Step 28, Must Pass Indicator: Mandatory
	# Description: QSpace - Click FinishAdding Button in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [28]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on FinishAdding button on Page Resolve successful"
		logger.info("Clicking on FinishAdding button on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on FinishAdding button on Page Resolve Failed"
		logger.info("Clicking on FinishAdding button on Page Resolve Failed")
		saveScreenshot("1_Step_28_1561906149244_Error.png")
		test_step_status(28, resultMsg, e, "Action", "Failed", "1_Step_28_1561906149244_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_28_1561906149245.png")
	test_step_status(28, resultMsg, "", "Action", "Passed", "1_Step_28_1561906149245.png")
	#
	# Step 29, Must Pass Indicator: Mandatory
	# Description: QSpace - Dismiss Confirmation alert pop-up by clicking OK button,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [29]")
	try:
		alert = driver.switch_to_alert()
		alert.accept()
		resultMsg = "Clicking on OK button on Alert Confirmation successful"
		logger.info("Clicking on OK button on Alert Confirmation successful")
	except Exception as e:
		resultMsg = "Clicking on OK button on Alert Confirmation Failed"
		logger.info("Clicking on OK button on Alert Confirmation Failed")
		saveScreenshot("1_Step_29_1561906149247_Error.png")
		test_step_status(29, resultMsg, e, "Action", "Failed", "1_Step_29_1561906149247_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_29_1561906149249.png")
	test_step_status(29, resultMsg, "", "Action", "Passed", "1_Step_29_1561906149249.png")
	#
	# Step 30, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Logout web element in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [30]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on Logout web element on Page Resolve successful"
		logger.info("Clicking on Logout web element on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on Logout web element  on Page Resolve Failed"
		logger.info("Clicking on Logout web element  on Page Resolve Failed")
		saveScreenshot("1_Step_30_1561906149251_Error.png")
		test_step_status(30, resultMsg, e, "Action", "Failed", "1_Step_30_1561906149251_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("1_Step_30_1561906149253.png")
	test_step_status(30, resultMsg, "", "Action", "Passed", "1_Step_30_1561906149253.png")
#
if test_case_continue: Add_Review_Defect()
test_case_status(0, 1, 0, 1)
#
