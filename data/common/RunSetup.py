import os, json
testData = dict()

def init_folder(folder):
	if not os.path.exists(folder):
		os.makedirs(folder)

def init_evidence_folder():
	screenshot_path = "./Results/Evidences/"
	init_folder(screenshot_path)

def init_log_folder():
	log_folder = "./Results/Logs/"
	init_folder(log_folder)

def init_current_data(fileName):
	with open("./data/{}.json".format(fileName)) as f:
		global testData
		_data = json.load(f)

		for key, val in _data.items():
			if val.upper() != 'DEPENDENCYRUN':
				testData[key] = val

def update_current_data(key, val):
	global testData
	testData[key] = val

def clear_global_data():
	global testData
	testData = dict()


