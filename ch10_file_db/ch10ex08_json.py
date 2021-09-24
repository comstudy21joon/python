from pprint import pprint

hello = [[1,2],[3,4],[5,6]]
pprint(hello, width=15, indent=8)
s = "무궁화 무궁화 우리나라 꽃 삼천리 강산에 우리나라 꽃"

pprint(s, width=10, indent=4)

json_data = '''{"id":"kim",
   "name":"\uae40\ubc94\uc900",
   "age": 60
}'''

print(json_data)
pprint(json_data)