import time,requests
t=time.time()
t=int(round(t * 1000))
print (int(round(t * 1000)))
# pgv_info=ssid=s6655563124; pgv_pvid=6864233088; ts_last=/mp/v2/index.html; ts_refer=zqact.tenpay.com/mp/v2/index.html; ts_sid=8372776724; ts_uid=3188659426; wzq_channel=..osz92p00qb187; qlappid=wx9cf8c670ebd68ce4; qlskey=v0aaf8a82205ffaaf38f77a8658c42e9; qluin=085e9858e4e0d6d42f950b301@wx.tenpay.com; qq_logtype=16; wx_session_time=1610264376000; wzq_qlappid=wx9cf8c670ebd68ce4; wzq_qlskey=v0aaf8a82205ffaaf38f77a8658c42e9; wzq_qluin=os-ppuA4VWuEPjLKXeekytSg9YQM
#我的cookie
cookie = 'qluin=085e9858e6c6eb624b3752eb1@wx.tenpay.com;qlskey=v0954858a125ffaa673a2285b697737a;wzq_qlskey=v0954858a125ffaa673a2285b697737a;wzq_qluin=os-ppuM2THXiv0dZ67s7tFczHRx8'
#老铁的cookie
# cookie='qlskey=v0aaf8a82205ffaaf38f77a8658c42e9; qluin=085e9858e4e0d6d42f950b301@wx.tenpay.com;wzq_qlappid=wx9cf8c670ebd68ce4; wzq_qlskey=v0aaf8a82205ffaaf38f77a8658c42e9;'
# cookie='pgv_info=ssid=s9297787938; pgv_pvid=2081597120; ts_last=/mp/v2/index.html; ts_refer=wzq.tenpay.com/mp/v2/index.html; ts_sid=1666296620; ts_uid=7134277380; wzq_channel=..orv53p00gf001; qlappid=wx9cf8c670ebd68ce4; qlskey=v0954858a115ffa52cf965924b34adc7; qluin=085e9858e6c6eb624b3752eb1@wx.tenpay.com; qq_logtype=16; wx_session_time=1610240719000; wzq_qlappid=wx9cf8c670ebd68ce4; wzq_qlskey=v0954858a115ffa52cf965924b34adc7; wzq_qluin=os-ppuM2THXiv0dZ67s7tFczHRx8'
posturl='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s'%t
postheader={'Accept': 'application/json, text/plain, */*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-cn',
'Connection': 'keep-alive',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':cookie,
'Host': 'zqact.tenpay.com',
'Origin': 'https://zqact.tenpay.com',
'Referer': 'https://zqact.tenpay.com/mp/v2/index.html',
'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.18(0x17001233) NetType/WIFI Language/zh_CN}'
            }
postbody={'_h5ver':'2.0.1','actid':'1100','tid':'5','id':'1','task_ticket': '12101132116422260630116303690081',
            'action': 'taskdone'}
def yuedu():
    respones=requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s'%t,data=postbody,headers=postheader).json()
    print(respones)
def dianzan():
    data={'_h5ver':'2.0.1','actid':'1100','tid':'4','id':'4','task_ticket':'12101101320430876706660135700167',
'action':'taskdone'
}
    respones=requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s'%t,data=data,headers=postheader)
    print(respones.json())
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
def fenxiangwenzhang():
    data = {'_h5ver': '2.0.1', 'actid': '1100', 'tid': '28', 'id': '14',
            'task_ticket': '12101111929542672720740080890041',
            'action': 'taskdone'
            }
    respones = requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s' % t, data=data,
                             headers=postheader)
    print(respones.json())
def monijiaoyi():
    respones=requests.get(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?channel=0&gameid=190&type=3&scenes=0&qluin=os-ppuM2THXiv0dZ67s7tFczHRx8&qlskey=v0954858a125ffaa673a2285b697737a&action=taskdone&actid=1100&tid=13&id=6&task_ticket=12101111934291539668580120430214')
    print(respones.text)
def fenxianggupiao():
    data = {'_h5ver': '2.0.1', 'actid': '1100', 'tid': '22', 'id': '12',
            'task_ticket': '12101111956021119779428037860024',
            'action': 'taskdone'
            }
    respones = requests.post(url='https://wzq.tenpay.com/cgi-bin/activity_task.fcgi?t=%s' % t, data=data,
                             headers=postheader)
    print(respones.json())
def caizhangting():
    cookie = 'qluin=085e9858e6c6eb624b3752eb1@wx.tenpay.com;qlskey=v0954858a125ffaa673a2285b697737a;wzq_qlskey=v0954858a125ffaa673a2285b697737a;wzq_qluin=os-ppuM2THXiv0dZ67s7tFczHRx8'
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.18(0x17001233) NetType/WIFI Language/zh_CN',
        'Cookie': cookie,
        'referer': 'https://zqact.tenpay.com/activity/page/guessRiseFall/?act_id=3&act_tid=9&act_actid=1100&stat_data=orv53p00gf001&act_url=https%253A%252F%252Fzqact.tenpay.com%252Fmp%252Fv2%252Findex.html%2523%252Faccount%252Fcenter%253Fstat_data%253Dorv53p00gf001'}
    res = requests.get(
        "https://zqact.tenpay.com/cgi-bin/activity_task.fcgi?actid=1100&tid=9&id=3&task_ticket=12101111959440029063780060330141&action=taskdone&_=1610366384888",
        headers=headers)
    print(res.text)
def fenxiangzhangting():
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.18(0x17001233) NetType/WIFI Language/zh_CN',
        'Cookie': cookie,
        'referer': 'https://zqact.tenpay.com/activity/page/guessRiseFall/'}
    res=requests.get(url='https://zqact.tenpay.com/cgi-bin/activity_task.fcgi?actid=1103&tid=18&id=1&task_ticket=12101141849201699183460146320021&action=taskdone&_=1610621360837',headers=headers)
    print(res.text)
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
fenxiangwenzhang()
monijiaoyi()
fenxianggupiao()
caizhangting()
fenxiangzhangting()
print("已完成")
