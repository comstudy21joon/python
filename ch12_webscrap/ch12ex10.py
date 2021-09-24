import re

regex = re.compile(r'''
    (https?:\/\/)?
    ([\w.]+){1,2}
    (\.[\w]{2,4}){1,2}''', re.VERBOSE)