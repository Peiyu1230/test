import time,os

import requests

header={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-Hans-US;q=1, zh-Hant-US;q=0.9, en-US;q=0.8, zh-Hant-TW;q=0.7, ja-JP;q=0.6","Connection": "keep-alive","Content-Length": "876","Content-Type": "application/x-www-form-urlencoded","Host": "ios.baertt.com","User-Agent": "KDApp/1.8.0 (iPhone; iOS 14.2; Scale/2.00)",}
data=os.environ["RDATA"]
print(data)

