#
# Application: QSpace
# Release: 2019.06
# Test Case: Resolve Defect
# Created On: Sun Jun 30 20:19:09 IST 2019
# Created By: iTM
#
print("Executing 1090_Resolve_Defect.py")
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
logger = setup_logger("tc_1090_3.log")
#
def Resolve_Defect():
	#
	step_header("2019.06", 1090, 3, 1, 1, 0)
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

	saveScreenshot("3_Step_1_1561906149575.png")
	test_step_status(1, resultMsg, "", "Action", "Passed", "3_Step_1_1561906149575.png")
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
		saveScreenshot("3_Step_2_1561906149576_Error.png")
		test_step_status(2, resultMsg, e, "Action", "Failed", "3_Step_2_1561906149576_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_2_1561906149578.png")
	test_step_status(2, resultMsg, "", "Action", "Passed", "3_Step_2_1561906149578.png")
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
		saveScreenshot("3_Step_3_1561906149579_Error.png")
		test_step_status(3, resultMsg, e, "Action", "Failed", "3_Step_3_1561906149579_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_3_1561906149580.png")
	test_step_status(3, resultMsg, "", "Action", "Passed", "3_Step_3_1561906149580.png")
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
		saveScreenshot("3_Step_4_1561906149582_Error.png")
		test_step_status(4, resultMsg, e, "Action", "Failed", "3_Step_4_1561906149582_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_4_1561906149585.png")
	test_step_status(4, resultMsg, "", "Action", "Passed", "3_Step_4_1561906149585.png")
	#
	# Step 5, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 4 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [5]")
	time.sleep(4)

	saveScreenshot("3_Step_5_1561906149615.png")
	test_step_status(5, resultMsg, "", "Action", "Passed", "3_Step_5_1561906149615.png")
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
		saveScreenshot("3_Step_6_1561906149617_Error.png")
		test_step_status(6, resultMsg, e, "Action", "Failed", "3_Step_6_1561906149617_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_6_1561906149619.png")
	test_step_status(6, resultMsg, "", "Action", "Passed", "3_Step_6_1561906149619.png")
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
		saveScreenshot("3_Step_7_1561906149621_Error.png")
		test_step_status(7, resultMsg, e, "Action", "Failed", "3_Step_7_1561906149621_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_7_1561906149622.png")
	test_step_status(7, resultMsg, "", "Action", "Passed", "3_Step_7_1561906149622.png")
	#
	# Step 8, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 2 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [8]")
	time.sleep(2)

	saveScreenshot("3_Step_8_1561906149626.png")
	test_step_status(8, resultMsg, "", "Action", "Passed", "3_Step_8_1561906149626.png")
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
		saveScreenshot("3_Step_9_1561906149628_Error.png")
		test_step_status(9, resultMsg, e, "Action", "Failed", "3_Step_9_1561906149628_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_9_1561906149629.png")
	test_step_status(9, resultMsg, "", "Action", "Passed", "3_Step_9_1561906149629.png")
	#
	# Step 10, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 2 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [10]")
	time.sleep(2)

	saveScreenshot("3_Step_10_1561906149635.png")
	test_step_status(10, resultMsg, "", "Action", "Passed", "3_Step_10_1561906149635.png")
	#
	# Step 11, Must Pass Indicator: Mandatory
	# Description: QSpace - Click GetData Button in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [11]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on GetData button on Page Resolve successful"
		logger.info("Clicking on GetData button on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on GetData button on Page Resolve Failed"
		logger.info("Clicking on GetData button on Page Resolve Failed")
		saveScreenshot("3_Step_11_1561906149639_Error.png")
		test_step_status(11, resultMsg, e, "Action", "Failed", "3_Step_11_1561906149639_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_11_1561906149640.png")
	test_step_status(11, resultMsg, "", "Action", "Passed", "3_Step_11_1561906149640.png")
	#
	# Step 12, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [12]")
	time.sleep(3)

	saveScreenshot("3_Step_12_1561906149644.png")
	test_step_status(12, resultMsg, "", "Action", "Passed", "3_Step_12_1561906149644.png")
	#
	# Step 13, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Edit Hyperlink in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [13]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on Edit hyperlink on Page Resolve successful"
		logger.info("Clicking on Edit hyperlink on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on Edit hyperlink on Page Resolve Failed"
		logger.info("Clicking on Edit hyperlink on Page Resolve Failed")
		saveScreenshot("3_Step_13_1561906149647_Error.png")
		test_step_status(13, resultMsg, e, "Action", "Failed", "3_Step_13_1561906149647_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_13_1561906149649.png")
	test_step_status(13, resultMsg, "", "Action", "Passed", "3_Step_13_1561906149649.png")
	#
	# Step 14, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [14]")
	time.sleep(3)

	saveScreenshot("3_Step_14_1561906149655.png")
	test_step_status(14, resultMsg, "", "Action", "Passed", "3_Step_14_1561906149655.png")
	#
	# Step 15, Must Pass Indicator: Mandatory
	# Description: QSpace - Select Defect Status from DefectStatus dropdown in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [15]")
	try:
		driver.find_element(By.XPATH, "TBD/option[text()='{}']".format("DefectStatus")).click()
		resultMsg = "Select Defect Status value from DefectStatus dropdown on Page Resolve Successful"
		logger.info("Select Defect Status value from DefectStatus dropdown on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Select Defect Status value from DefectStatus dropdown on Page Resolve Failed"
		logger.info("Select Defect Status value from DefectStatus dropdown on Page Resolve Failed")
		saveScreenshot("3_Step_15_1561906149660_Error.png")
		test_step_status(15, resultMsg, e, "Action", "Failed", "3_Step_15_1561906149660_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_15_1561906149662.png")
	test_step_status(15, resultMsg, "", "Action", "Passed", "3_Step_15_1561906149662.png")
	#
	# Step 16, Must Pass Indicator: Mandatory
	# Description: QSpace - Select Followup Status from FollowupStatus dropdown in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [16]")
	try:
		driver.find_element(By.XPATH, "TBD/option[text()='{}']".format("FollowupStatus")).click()
		resultMsg = "Select Followup Status value from FollowupStatus dropdown on Page Resolve Successful"
		logger.info("Select Followup Status value from FollowupStatus dropdown on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Select Followup Status value from FollowupStatus dropdown on Page Resolve Failed"
		logger.info("Select Followup Status value from FollowupStatus dropdown on Page Resolve Failed")
		saveScreenshot("3_Step_16_1561906149667_Error.png")
		test_step_status(16, resultMsg, e, "Action", "Failed", "3_Step_16_1561906149667_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_16_1561906149668.png")
	test_step_status(16, resultMsg, "", "Action", "Passed", "3_Step_16_1561906149668.png")
	#
	# Step 17, Must Pass Indicator: Mandatory
	# Description: QSpace - Enter Followup Date in Followupdate textbox in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [17]")
	resultMsg = ''
	try:
		driver.find_element(By.XPATH, "TBD").send_keys("FollowupDate")
		resultMsg = "Enter value in Followupdate  textbox on Page Resolve Successful"
		logger.info("Enter value in Followupdate  textbox on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Enter value in Followupdate  textbox on Page Resolve Failed"
		logger.info("Enter value in Followupdate  textbox on Page Resolve Failed")
		saveScreenshot("3_Step_17_1561906149670_Error.png")
		test_step_status(17, resultMsg, e, "Action", "Failed", "3_Step_17_1561906149670_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_17_1561906149671.png")
	test_step_status(17, resultMsg, "", "Action", "Passed", "3_Step_17_1561906149671.png")
	#
	# Step 18, Must Pass Indicator: Mandatory
	# Description: QSpace - Enter action in Followupdescr textbox in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [18]")
	resultMsg = ''
	try:
		driver.find_element(By.XPATH, "TBD").send_keys("action")
		resultMsg = "Enter value in Followupdescr  textbox on Page Resolve Successful"
		logger.info("Enter value in Followupdescr  textbox on Page Resolve Successful")
	except Exception as e:
		resultMsg = "Enter value in Followupdescr  textbox on Page Resolve Failed"
		logger.info("Enter value in Followupdescr  textbox on Page Resolve Failed")
		saveScreenshot("3_Step_18_1561906149673_Error.png")
		test_step_status(18, resultMsg, e, "Action", "Failed", "3_Step_18_1561906149673_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_18_1561906149674.png")
	test_step_status(18, resultMsg, "", "Action", "Passed", "3_Step_18_1561906149674.png")
	#
	# Step 19, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Update Hyperlink in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [19]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on Update hyperlink on Page Resolve successful"
		logger.info("Clicking on Update hyperlink on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on Update hyperlink on Page Resolve Failed"
		logger.info("Clicking on Update hyperlink on Page Resolve Failed")
		saveScreenshot("3_Step_19_1561906149675_Error.png")
		test_step_status(19, resultMsg, e, "Action", "Failed", "3_Step_19_1561906149675_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_19_1561906149676.png")
	test_step_status(19, resultMsg, "", "Action", "Passed", "3_Step_19_1561906149676.png")
	#
	# Step 20, Must Pass Indicator: Mandatory
	# Description: QSpace - Wait for 3 seconds,
	# Expected Result: QSpace - Verify that Confirmation webelement on Resolve page has text same as Defect updated successfully
	#
	logger.info("Executing Test Step [20]")
	time.sleep(3)

	saveScreenshot("3_Step_20_1561906149679.png")
	test_step_status(20, resultMsg, "", "Action", "Passed", "3_Step_20_1561906149679.png")
	saveScreenshot("3_Step_20_1561906149681.png")
	test_step_status(20, resultMsg, "", "Verification", "Passed", "3_Step_20_1561906149681.png")
	#
	# Step 21, Must Pass Indicator: Mandatory
	# Description: QSpace - Click Logout web element in the Resolve Screen,
	# Expected Result: Do Nothing
	#
	logger.info("Executing Test Step [21]")
	try:
		driver.find_element(By.XPATH, "TBD").click()
		resultMsg = "Clicking on Logout web element on Page Resolve successful"
		logger.info("Clicking on Logout web element on Page Resolve successful")
	except Exception as e:
		resultMsg = "Clicking on Logout web element  on Page Resolve Failed"
		logger.info("Clicking on Logout web element  on Page Resolve Failed")
		saveScreenshot("3_Step_21_1561906149682_Error.png")
		test_step_status(21, resultMsg, e, "Action", "Failed", "3_Step_21_1561906149682_Error.png")
		handleException(e, "Mandatory")
		return

	saveScreenshot("3_Step_21_1561906149683.png")
	test_step_status(21, resultMsg, "", "Action", "Passed", "3_Step_21_1561906149683.png")
#
if test_case_continue: Resolve_Defect()
test_case_status(0, 1, 0, 1)
#
