import requests
import json

resp = requests.get('https://code.junookyo.xyz/api/ncov-moh/data.json?fbclid=IwAR1IeFuBOu6-akVwEqNdA2ZnRlbeItGss9hDa5Ob5wd-pzLpJf-lzRkxCWM')
r_dict = resp.json()
print(json.dumps(r_dict['data'],indent=4))
#print(r_dict['data']['global']['cases'])
def Convert(key): #convert dict to string 
      str1 = json.dumps(key)
      str2 = str1.replace('"',"") # delete "
      return str2

string1 = "so nguoi bi nhiem " + Convert(r_dict['data']['global']['cases'])
string2 = "so nguoi chet " + Convert(r_dict['data']['global']['deaths'])
string3 = "so nguoi khoi benh" + Convert(r_dict['data']['global']['recovered'])
data = {
	"messages":[
				{"text":"The Gioi"},
				{"text":string1},
				{"text":string2}
	]}
print(json.dumps(data['messages'],indent=4))