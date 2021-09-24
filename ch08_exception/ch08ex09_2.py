import logging
import logging.handlers

debug_logger = logging.getLogger('debug_log')
debug_logger.setLevel(logging.DEBUG)

file = "logging.log"
size = 1024
count = 10
logFileHandler = logging.handlers.RotatingFileHandler(filename=file, maxBytes=size, backupCount=count)
logFileHandler.setLevel(logging.DEBUG)

debug_logger.addHandler(logFileHandler)

for i in range(100) :
    debug_logger.debug("DEBUG log message - File")