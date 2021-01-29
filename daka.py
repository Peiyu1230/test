# -*- coding: utf8 -*-

import requests

data={
	"data": {
		"emp_no": "26322",
		"name": "裴宇",
		"imei": "F821E8A3-36FA-46C6-9889-5455B92BFB62",
		"record_type": "2",
		"record_address": "undefined北京市海淀区彩和坊路",
		"token": "0d13168bb4614543a19da6a724914f81",
		"versionNo": "1.7.8"
	}
}


header={'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-cn',
'Connection':'keep-alive',
'Content-Type':'application/json; charset=UTF-8',
'Host':'app.farben.com.cn',
'Origin':'file://',
'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44)'}
res=requests.post(url="https://app.farben.com.cn/app/clock/addEpidemicClock",headers=header,json=data)
print(res.text)
