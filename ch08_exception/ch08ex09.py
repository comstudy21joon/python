import logging

logging.basicConfig(level=logging.DEBUG)

debug_logger = logging.getLogger('debug_log')
debug_logger.setLevel(logging.DEBUG)

logFileHandler = logging.FileHandler('debug.log')
logFileHandler.setLevel(logging.DEBUG)

debug_logger.addHandler(logFileHandler)

logging.debug("DEBUG log message - Console")
debug_logger.debug("DEBUG log message - File")