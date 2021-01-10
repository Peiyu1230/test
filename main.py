import time,requests
t=time.time()
print (int(round(t * 1000)))
# Cookie='pgv_info=ssid=s9297787938; pgv_pvid=2081597120; ts_last=/mp/v2/index.html; ts_refer=wzq.tenpay.com/mp/v2/index.html; ts_sid=1666296620; ts_uid=7134277380; wzq_channel=..orv53p00gf001; qlappid=wx9cf8c670ebd68ce4; qlskey=v0954858a115ffa52cf965924b34adc7; qluin=085e9858e6c6eb624b3752eb1@wx.tenpay.com; qq_logtype=16; wx_session_time=1610240719000; wzq_qlappid=wx9cf8c670ebd68ce4; wzq_qlskey=v0954858a115ffa52cf965924b34adc7; wzq_qluin=os-ppuM2THXiv0dZ67s7tFczHRx8'
posturl='https://zqact.tenpay.com/cgi-bin/activity_task_continue.fcgi?t=%s'%t
postheader={'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-cn',
'Connection': 'keep-alive',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie': 'pgv_info=ssid=s9297787938; pgv_pvid=2081597120; ts_last=/mp/v2/index.html; ts_refer=wzq.tenpay.com/mp/v2/index.html; ts_sid=1666296620; ts_uid=7134277380; wzq_channel=..orv53p00gf001; qlappid=wx9cf8c670ebd68ce4; qlskey=v0954858a115ffa52cf965924b34adc7; qluin=085e9858e6c6eb624b3752eb1@wx.tenpay.com; qq_logtype=16; wx_session_time=1610240719000; wzq_qlappid=wx9cf8c670ebd68ce4; wzq_qlskey=v0954858a115ffa52cf965924b34adc7; wzq_qluin=os-ppuM2THXiv0dZ67s7tFczHRx8',
'Host': 'zqact.tenpay.com',
'Origin': 'https://zqact.tenpay.com',
'Referer': 'https://zqact.tenpay.com/mp/v2/index.html',
'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.18(0x17001233) NetType/WIFI Language/zh_CN}'
            }
postbody={'_h5ver':'2.0.1','action':'home','type':'wzq_welfare_growth','actid':'1031'}
def yuedu():
    respones=requests.post(url=posturl,data=postbody,headers=postheader).json()
    print(respones)
def dianzan():
    data={'_h5ver':'2.0.1','actid':'1100','tid':'4','id':'4','task_ticket':'12101101320430876706660135700167',
'action':'taskdone'
}
    respones=requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s'%t,data=data,headers=postheader)
    print(respones.json()['reward_desc'])
def shequ():
    data = {'_h5ver': '2.0.1', 'actid': '1100', 'tid': '31', 'id': '16',
            'task_ticket': '12101101333371087011428266870018',
            'action': 'taskdone'
            }
    respones = requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s' % t, data=data,
                             headers=postheader)
    print(respones.json())
def zixuangu():
    data = {'_h5ver': '2.0.1', 'actid': '1100', 'tid': '2', 'id': '2',
            'task_ticket': '12101101341010432509449180570199',
            'action': 'taskdone'
            }
    respones = requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s' % t, data=data,
                             headers=postheader)
    print(respones.json())
def share():
    data = {'url':'https://wzq.tenpay.com/mp/mocktrade/index.html?stat_data=Owf06p00qz003'
            }
    respones = requests.post(url='https://wzq.tenpay.com/cgi-bin/wxapi_sign.fcgi?action=2', data=data,
                             headers=postheader)
    print(respones.json())

def shareText():
    data = {'_h5ver': '2.0.1', 'actid': '1100', 'tid': '29', 'id': '15',
            'task_ticket': '12101101530410180851209261380012',
            'action': 'taskdone'
            }
    respones = requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s'%t, data=data,
                             headers=postheader)
    print(respones.json())
def sharefriends():
    data = {'_h5ver': '2.0.1', 'actid': '1100', 'tid': '7', 'id': '11',
            'task_ticket': '12101101539240398955017135330079',
            'action': 'taskdone'
            }
    respones = requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s'%t, data=data,
                             headers=postheader)
    print(respones.json())
zixuangu()
time.sleep(1)
yuedu()
time.sleep(1)
dianzan()
time.sleep(1)
shequ()
time.sleep(1)
share()
time.sleep(1)
shareText()
sharefriends()
print("已完成")
