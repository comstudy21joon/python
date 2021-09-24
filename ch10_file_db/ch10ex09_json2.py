from pprint import pprint
import json

json_data = '''{"id":"kim",
    "name":"김범준",
    "age": 60
}'''

obj = json.loads(json_data)

pprint(obj)