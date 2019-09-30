import re

def checkWithExpectedResult(condition, expectedValue, actResult):
	if condition is "=":
		if isinstance(actResult, bool):
			return True if expectedValue == actResult else False
		if isinstance(actResult, str):
			ar = actResult.replace("(^ )|( $)", "")
			exp_val = expectedValue.replace("(^ )|( $)", "")
			return exp_val == ar
	if isinstance(actResult, int):
		if condition is ">":
			return int(actResult) > int(expectedValue)
		elif condition is "=":
			return int(actResult) == int(expectedValue)
	if condition.lower() == "in":
		if isinstance(actResult, str):
			ar = actResult.replace("(^ )|( $)", "")
			exp_val = expectedValue.replace("(^ )|( $)", "")
			return ar in exp_val
	if condition == "!=":
		if isinstance(actResult, str):
			ar = actResult.replace("(^ )|( $)", "")
			exp_val = expectedValue.replace("(^ )|( $)", "")
			return ar != exp_val
	return false

def SanitizeData(option, value):
	if option is "price":
		split_array = re.findall('\d+|\D+', value)
		process_array = []
		for i in split_array:
			try:
				check_value = int(i)
				process_array.append(str(i))
			except Exception as e:
				logger.info(e)
		str(process_array)
		result = str(process_array[0])+"."+str(process_array[1])
		return result
	elif option is "number":
		split_array = re.findall('\d+|\D+', value)
		process_array = []
		for i in split_array:
			try:
				check_value = int(i)
				process_array.append(str(i))
			except Exception as e:
				logger.info(e)
		string_array = [str(i) for i in process_array]
		result = ("".join(string_array))
		return result
	elif option is "characters":
		split_array = re.findall(r"[a-zA-z]+", value)
		result = ("".join(split_array))
		return result

def isDoubleValue(*args):
	step_status = False
	i = 0
	while i < (len(args)):
		split_array = re.findall('\d+|\D+', args[i])
		process_array = []
		for j in split_array:
			try:
				check_value = int(j)
				process_array.append(str(j))
			except Exception:
				pass
		result = process_array
		i += 1
	try:
		if result[1]:
			step_status = True
			return step_status
	except Exception:
		return step_status

def handleCalculation(operation, left_side, right_side):
	if operation is 'add':
		if isinstance(left_side, int) and isinstance(right_side, int):
			return int(left_side) + int(right_side)
		if isinstance(left_side, float) and isinstance(right_side, float):
			calculation = float(left_side) + float(right_side)
			result = "{0:.2f}".format(calculation)
			return str(result)
	if operation is 'subtract':
		if isinstance(left_side, int) and isinstance(right_side, int):
			return int(left_side) - int(right_side)
		if isinstance(left_side, float) and isinstance(right_side, float):
			calculation = float(left_side) - float(right_side)
			result = "{0:.2f}".format(calculation)
			return str(result)
	if operation is 'multiply':
		if isinstance(left_side, int) and isinstance(right_side, int):
			if int(left_side) == 0:
				left_side = 1
			return int(left_side) * int(right_side)
		if isinstance(left_side, float) and isinstance(right_side, float):
			if float(left_side) == 0.0:
				left_side = 1.0
			result = float(left_side) * float(right_side)
			return result
	if operation is 'divide':
		if isinstance(left_side, int) and isinstance(right_side, int):
			return int(left_side) / int(right_side)
		if isinstance(left_side, float) and isinstance(right_side, float):
			result = float(left_side) / float(right_side)
			return result
