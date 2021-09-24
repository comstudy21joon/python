import logging

logging.basicConfig(filename='logfile.txt', level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')

logging.debug("Some message")