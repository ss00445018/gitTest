import copy, datetime, json, time

def current_time():
	return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def current_epoch_time():
	return int(round(time.time()*1000))

def initialize_testcase():
	global step_status, _startTime, _instType, _step, evidenceList, _resultMsg
	_startTime = current_time()
	_instType = None
	_step = None
	step_status = []
	evidenceList = []
	_resultMsg = None
	
def step_header(release, tcId, runId, batchId, _iter, callingStep):
	initialize_testcase()
	global status
	status = {}
	status['release'] = release
	status['tcId'] = tcId
	status['runId'] = runId
	status['batchId'] = batchId
	status['iter'] = _iter
	status['callingStep'] = callingStep
	status['startTime'] = current_time()

def consolidte_resultMsg(instType, resultMsg):
	if instType == _instType:
		if instType == 'Action': return '{}; '.format(resultMsg)
		else: return '; {}'.format(resultMsg)
	else:
		global _resultMsg
		tmp_resultMsg = '{}; {}'.format(_resultMsg, resultMsg)
		_resultMsg = resultMsg
	return tmp_resultMsg
	
def test_step_status(step, resultMsg, errorMsgs, instType, _status, evidencePath):
	global _step, step_status, _instType, status
	if instType == _instType: 
		status['endTime'] = current_time()
		step_status.append(copy.deepcopy(status))
		status['startTime'] = current_time()
	_step = step
	status['docType'] = 'STEP'
	status['step'] = step
	status['resultMsg'] = consolidte_resultMsg(instType, resultMsg)
	status['logMsgs'] = [status['resultMsg']]
	_instType = instType
	status['errorMsgs'] = [] if errorMsgs == '' else [str(errorMsgs)]
	resultUrls = {}
	resultUrls['name'] = 'Step-{}-1'.format(step)
	epoch_time = current_epoch_time()
	resultUrls['evId'] = epoch_time
	resultUrls['evType'] = 'IMAGE'
	status['resultUrls'] = [resultUrls]
	status['status'] = _status
	if instType == 'Verification': 
		status['endTime'] = current_time()
		step_status.append(copy.deepcopy(status))
		status['startTime'] = current_time()
	_evidencePath = {}
	_evidencePath['evId'] = epoch_time
	_evidencePath['fileName'] = evidencePath
	evidenceList.append(_evidencePath)

def consolidate_status():
	for steps in step_status:
		if steps['status'] == "Failed": return 'Failed'
	return 'Passed'

def consolidate_executed_steps():
	executedSteps = []
	for step in step_status: 
		if step['step'] not in executedSteps: 
			executedSteps.append(step['step']) 
	return executedSteps

def test_case_status(dispatchId, batchId, callingStep, _iter):
	global test_case
	test_case = []
	if _instType == 'Action': 
		status['endTime'] = current_time()
		step_status.append(copy.deepcopy(status))
	data = {}
	data['docType'] = 'TESTCASE'  
	data['release'] = status['release']
	data['tcId'] = status['tcId']
	data['runId'] = status['runId']
	data['dispatchId'] = dispatchId
	data['batchId'] = batchId
	data['callingStep'] = callingStep
	data['iter'] = _iter
	data['debugLogUrl'] = 'tc_{}_{}.log'.format(status['tcId'], status['runId'])
	data['startTime'] = _startTime
	data['endTime'] = current_time()
	data['status'] = consolidate_status()
	data['executedSteps'] = consolidate_executed_steps()
	data['evidenceList'] = evidenceList  
	test_case.append(data)
	dump_testcase('{}_{}'.format(status['tcId'], status['runId']))
	
def dump_testcase(fileName):
	data = {}
	data['steps'] = step_status
	data['testCase'] = test_case
	_fileName = "./Results/tc_{}.json".format(fileName)
	with open(_fileName, 'w') as outfile:  
		json.dump(data, outfile, indent=4)
