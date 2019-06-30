import logging

def setup_logger(log_file, level=logging.INFO):
	log_folder = "./Results/Logs/"
	handler = logging.FileHandler(log_folder + log_file)
	formatter = logging.Formatter("%(asctime)s %(message)s")
	handler.setFormatter(formatter)

	logger = logging.getLogger()
	logger.setLevel(level)
	logger.addHandler(handler)

	return logger
