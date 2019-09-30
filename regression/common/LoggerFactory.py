import logging, sys

def setup_logger(log_file, level=logging.INFO):
	log_folder = "./Results/Logs/"
	handler = logging.FileHandler(log_folder + log_file)
	formatter = logging.Formatter("%(asctime)s %(message)s")
	handler.setFormatter(formatter)

	sysHandler = logging.StreamHandler(sys.stdout)
	sysHandler.setLevel(logging.ERROR)

	logger = logging.getLogger()
	logger.setLevel(level)

	logger.addHandler(sysHandler)
	logger.addHandler(handler)

	return logger
