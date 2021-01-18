import random

import requests,time

t = time.time()
t = int(round(t * 1000))
print(int(round(t)))

header={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-Hans-US;q=1, zh-Hant-US;q=0.9, en-US;q=0.8, zh-Hant-TW;q=0.7, ja-JP;q=0.6","Connection": "keep-alive","Content-Length": "876","Content-Type": "application/x-www-form-urlencoded","Host": "ios.baertt.com","User-Agent": "KDApp/1.8.0 (iPhone; iOS 14.2; Scale/2.00)",}

def qiandao():
    data={"cookie":"MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY",
"cookie_id":"MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY",
"app_version":"1.8.0",
"channel":"80000000",
"device_type":"1"}
    res=requests.post(url='https://kd.youth.cn/TaskCenter/getSign',headers=header,data=data)
    print(res)



def shipin():
    data=('p=9NwGV8Ov71o=GvDnjwMsu_ld4qx0YVkhCGk95BHaDHeUTCFMGsGqhi1dtO1C4WuBYfVS51_7tnsgwho308taCyWi2yKJtkSHTvTzP2kXMkya-8EmcKPLqPfWBn71wrAjTXUfjUwfJL5JOqtPa5dyS53avCqxoY4ajTlIcQhiDXTnGQY14rrx1-EBit3wB_JmeXsPbDbd3Oo54IEzS0m6EbOBXJW4nS9qgL5TaDMpJyX3CfmFaRyVwI1CvMQthgwG4V9Ylcxs4-DRvhYT2XZb5cuDutoDowYlKFrBF8x509Gijkt9mV5YwokA086voDOKW1lwGwPZk3zhvt1Q8BMvk5UnjWwNr8GRDoWtlzyMHs9TciEm5Y5QwUwZJFinPU1-1JCpfaGdImweJXQSlhdHXuOt-VBftYfDYF9e9GS6ngRFLg2O5Hb4yZYjXKJ629KKIEqpsTo9bP8fIxS4hCG6-66JmlAtOO6JS78bWrJci8-j6HNBYNCxQCFhRt5JxpqYMHfzjwQGOvL9b1F0YtBDjdzz84Hpd_DKXt6PYnZxU7ompbIBQnfMoK2g50MMPZojqqi7daCkN-RxX9wfSE-2H1NHKTqXqfMexxgQgqwfpKJh29qtOVfRl_qETNoGOmPF2b79gUurzV0EbbXjBk3EdQBTRZY1A58r0EGfSXH-pD8m1zP6K6Yc4H06a2K7xnoTtYTYDk83klEWPWq-IYnUb-7K2C1-coL-VLas2UOdvuVGPRuNmOLZmFfd7PulujZswQ_dMI_k2vz5jlmi4YrRiRhm-ieK276I0LW-KvT_8zUeTOYbyhAhB8fwmX1r-dlmJexGtIxcYHJw44Opan8hriY_fVXz8acT6A==')
    res = requests.post(url='https://ios.baertt.com/v5/article/complete.json',headers=header,data=data)
    # print(res.json()['message'],"获取金币"+res.json()["read_score"])
    # print("获取金币:"+str(res.json()["items"]["read_score"]))
    print(res.text)

def yueduwenzhang():
    data=['p=9NwGV8Ov71o=GvDnjwMsu_ld4qx0YVkhCGk95BHaDHeUTCFMGsGqhi1dtO1C4WuBYfVS51_7tnsgwho308taCyWi2yKJtkSHTvTzP2kXMkya-8EmcKPLqPfWBn71wrAjTXUfjUwfJL5JOqtPa5dyS53avCqxoY4ajTlIcQhiDXTnGQY14rrx1-EBit3wB_JmeXsPbDbd3Oo54IEzS0m6EbOBXJW4nS9qgL5TaDMpJyX3CfmFaRyVwI1CvMQthgwG4V9Ylcxs4-DRvhYT2XZb5cuDutoDowYlKOcRF60147wOKfnuJyOEDeoXtF1Q6i7oerl-vVts9lst8Leo-whgXzujrDZ4mESBhS1w4abzXtuSovTDRA59qA31BhjcFPIPSrfjcKI1xjX6JVbi5dVkplODszgIFt4vtpIUoxR5Iz7BTty796USGIiRknApY5JX_4rtF8vanWgzTurRn9_EHA5kjE1bZFfyhkzM3yGg8_E029PLDpm4lxhH8BXWILib7uIpsnntanMRKqoYm45Syj9rNRFZgWd-K2VdIS_sSeGdsnUSLiQ2oavdfl7MEN2h-t72yC3yTmPwr52Iw7FUsbxriK1szTwSJYZ8O458paNaTK4-HDZnTnWjQtSXqc7DurI6askUupBCChe-DjCBt382NlHvBQNYUOGZTjo8u5BikV3ujq-pUDc3Sjune5NR1f20_66IlKB6DRD8fZRZGaJ-cKf6dEQicvHvpLO5FXx0EoOP2SMNnozVV8HyhxqKwbaSJhmYHkhIdyqUMF8Vglm2viJpYAFXRkxlexcMLIwiyWmDYMkIr-ToeIF1LqIPqO6KyeRx7_9wuDdlW5WvM0nKbk5v9YpCcA==','p=9NwGV8Ov71o=GvDnjwMsu_ld4qx0YVkhCGk95BHaDHeUTCFMGsGqhi1dtO1C4WuBYfVS51_7tnsgwho308taCyWi2yKJtkSHTvTzP2kXMkya-8EmcKPLqPfWBn71wrAjTXUfjUwfJL5JOqtPa5dyS53avCqxoY4ajTlIcQhiDXTnGQY14rrx1-EBit3wB_JmeXsPbDbd3Oo54IEzS0m6EbOBXJW4nS9qgL5TaDMpJyX3CfmFaRyVwI1CvMQthgwG4V9Ylcxs4-DRvhYT2XZb5ctf_JUGW1x4FB6s5IrQ7cvxooQB4SL86y2zLYCoU2UR1ENVenT3EmCk0cjMImaa7pwcLmdNX5BNY5A3CZ1pY8SUNih1sxYcPoPaFM6wTeQSkepuisnBTVnvXt09nHmBgSoSOKfpgCEMaVKVCbZ_DRW9xi0IL8jQTRcf-AlVkvPz84u-ErrmBW8koQtuJZKaiV6zAU0iCAoQoom3wPEnL0ded5hNTtja1EsBmnuuVAvHWLVxQN1xk967R1N4h7baFjEdvP77nR9XO_1axVDk8gwY9j-0DYtGZBC9hO-CTvh4V6D32ESL4PO4MvmCKaC74XOKl546Bmoc_cVzl__LW-bM36n5ZoYkLzGSuepKmxX54DqB26w_tTiln6rC-9Qasd8N3yn0mk76Jjre6S8P_7a8RqNxvqtEvYa9Afg5ODDgITKRzE8J6CNYLYwE8fAQudFbjonLxDsqbve-uIG4_tDd4uvT-MaGy62Bnj06DAo7MEZa61fgDcglYTQNALw0XftejuUv2ziwTPIwiDauaqz-2Rvn89Ws4CPSgcJ5R8xQLXB4B_XMZQY4-U4_irDtuigwZMuxTJJX8Q==']
    value=[0,1]
    i=random.choice(value)
    res = requests.post(url='https://ios.baertt.com/v5/article/complete.json', headers=header, data=data[i])
    # print(res.json(),"获取金币"+res.json()["items"]["score"])
    # print("获取金币:"+str(res.json()["items"]["read_score"]))
    print(res.json())
def jingxihongbao():
    data=('p=9NwGV8Ov71o=GvDnjwMsu_ka-LJ9wnbNzBhA0cz3iHWgEqXEh3bkBC0KSg93aV2LC-S2kpFYl_sQgZd-rfBZbgQX8-9JlXjq_HD3U4VdJ0FUw7V5oD5274GNkOv0xICutG3-lH4ryy26yNVY9ePaN_wC5z1kUrmjhoDDI0Vau-fqBoBjAgUzoOsW5VgxWu5zgWUcaoD2SbMT8s1X5Lz_AAxtYdvua5hQkqV3BuLbagxKLD9REcxg1-yXLmiTycVHeCkVSaSEW6Jwc-ubt-_IWF_AQvdCA8cgxOerY9WPi7kDHP6tuGl5yyUGpVXr2Mz2Z7Z32pDEmorB6uv2Qi2qU9erspBm_sGkDlm5K5W5Yacl_aKz313Aokl3EXxQV1CQPVKBv3lJszoxAvzgsyGmL-vhBHESWzd91Cl4oKDDAQVK9PGEaS_OSfDI5yG2ibV5TwIz-mV55jXOgvBPWW8bYb86MEpTodzzltx7hS5IncKBk88Q5ijZRdDDhnL4I7Xf83L7FydNMfLIwP3TWem_gshhtXp6Pb01abN62c2jfh-5JaKo0bQW99vRa370Xo-n45H5QzfkFpWBU680y8zBheTNApXVp4Ilyxr6WwfqNsyUKlaGapXEtJp7l_AInWoWrUS1rXzkYCEVTXZ0FUVxASzxH4pLeMhqM8KnL_aYegM1V0aXEA-0W9Qoy8rFw9SYIaJ5-VXQcHsaND3e3bCdyKSy3QfBelqRUFqcbr_LNY0VwQtYAg7s2uuPfkCgM1a47JggoGFocMt2-0Lx23DLoelUT3wzhaCOg62tlj4WueEGLHj0Q5MagJ0-vPKiOYpFaxPgP5HWekzKiLaszZM2A5lmkog_yIPzIg==')
    res=requests.post(url='https://ios.baertt.com/v5/article/red_packet.json',headers=header,data=data)
    # print(res.json(),"获取金币"+res.json()["items"]["score"])
    # print("获取金币:"+str(res.json()["items"]["score"]))
    print(res.json())

def shichang():
    data=('p=9NwGV8Ov71o=gW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATLz_D093IYRATKdFRTOOErqT8a0W-9iD_Sj_om7qE3yONtPqIKuP_xWkvElGbib-uRwf5PYfT9LIOtuyk64FBq4_A8MTjvddm9oc5VJi2QO5wp2baAjk77xAUfiyiWB3NQ2vz-mdBFvavR3u7tY3UCXD3Hnb5hvQ_ckYeBkcOMcKZBQgAAhIujSX0M5XFNWdVN1gQjnCmhb3vBkxur3myvtsWEdVC0tIfTZtAk9oIbu0MhPMTNfj0VIwGIzBEO9Vxqj2FriyeFN94ID1r7nRSQMJ47TAi8oustRDVERYCQhnDcOQlVh3Hkrghy8QDjhZoMTsbMnClNrybAmUwIAw4LnMOxRDcapZTt5JVf-yv5AXdOnTelGTyZwjEuFqqxhMM0IOZ1RdcxHA6g7-d1NtYFhJMHPqBctwb2R09flfZFeMP-57VuJtGCslTQeuDuAe4XkjHp_ybK_WRyZgARx8GHq_S9VNMwFGVg0lz4gFDLHqotCuhwR2Ze9bNLRiinuV2lFRG6fqV39OkKhzchBNp97uNWQaSf2yGL2Zkrl4DQKxB8zfzuOm5GjFxBbCoCHNZE')
    res=requests.post(url='https://ios.baertt.com/v5/user/stay.json',headers=header,data=data)
    # print(res.json(),"获取金币"+res.json()["reward"]["score"])
    # print("获取金币:"+str(res.json()["reward"]["score"]))
    print(res.json())

def choujiang():
    header={"Accept": "application/json","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Type": "application/x-www-form-urlencoded","Cookie": "Hm_lpvt_268f0a31fc0d047e5253dd69ad3a4775=1610169254; Hm_lvt_268f0a31fc0d047e5253dd69ad3a4775=1610169129,1610169233,1610169254; sensorsdata2019jssdkcross=%7B%22distinct_id%22%3A%2251940599%22%2C%22%24device_id%22%3A%221763575b1a613a-0871492e6bc0dd8-754c1551-370944-1763575b1a710d6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221763575b1a613a-0871492e6bc0dd8-754c1551-370944-1763575b1a710d6%22%7D; Hm_lvt_6c30047a5b80400b0fd3f410638b8f0c=1610169126","Host": "kd.youth.cn","Origin": "https://kd.youth.cn","Referer": "https://kd.youth.cn/html/rotaryTable/index.html?uuid=1dd528208ba88da3d1572edd27b5c8ae&sign=b132053ccab97213d18173117d8743a8&channel_code=80000000&uid=51940599&channel=80000000&access=WIfI&app_version=1.8.0&device_platform=iphone&cookie_id=edfb98c33168786704b5badae06693c5&openudid=1dd528208ba88da3d1572edd27b5c8ae&device_type=1&device_brand=iphone&sm_device_id=20190930204732d6bf45fbb1b1b8a70a973cdb43ca179701e2bd8328ac8959&device_id=48724486&version_code=180&os_version=14.2&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY&device_model=iPhone_6_Plus&subv=1.5.1&&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY&cookie_id=edfb98c33168786704b5badae06693c5","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","X-Requested-With": "XMLHttpRequest",}
    res=requests.post(url='https://kd.youth.cn/WebApi/RotaryTable/turnRotary?_=%s'%t,headers=header)
    # print(res.json(),"获取金币"+res.json()["data"]["score"])
    # print("获取金币:"+str(res.json()["data"]["score"]))
    print(res.json())


def tuisong():
    data=('p=9NwGV8Ov71o=GvDnjwMsu_ld4qx0YVkhCGk95BHaDHeUTCFMGsGqhi1dtO1C4WuBYfVS51_7tnsgwho308taCyWi2yKJtkSHTvTzP2kXMkya-8EmcKPLqPfWBn71wrAjTXUfjUwfJL5JOqtPa5dyS53avCqxoY4ajTlIcQhiDXTnGQY14rrx1-EBit3wB_JmeXsPbDbd3Oo54IEzS0m6EbOBXJW4nS9qgL5TaDMpJyX3CfmFaRyVwI1CvMQthgwG4V9Ylcxs4-DRvhYT2XZb5ctf_JUGW1x4FMkS8ISDBLN-HNIg0-CMBHkQ92E5Rqwh_bdJgn3r3Z2WdgXSY5dDrqamoWVTTx4-YIisDLvvweowIwoYgeUwpbSKOYxr6qfIbyXJk8IyiG7YQk0zSbGhziGqO2GZQiE3itepoW4cpRqTu4c_LAWbPz2uNsiF4_2j1BIBXzU706Q_fs92ab1ohDwgT8_VrANO3B8wwHMuMsbIQNd-miIMTQ7tj08MKuP-KJZBli8TnkF_sISWGiQOUz8X0_tpN2c_GW1vAWPKoO9ud_WC5Txb4ci21M8b6W18Xjm1CL7nIr9rIHBMD6L7L429UEV9emSKuSUd6cmZ-SAFZ1BTcw_kfmVdkyrrDZ1dSShbfg_NSGQWfCR-ZKgYo5OBB6Tdjq8BxoZV4YmKob96II_KF5WCfQOHVqxTaYeiuq-MLb0dtnGriXC-XiIgA0NYXGdlT7iwtCYtBN6ZVwtAysQCE93RHvT_TStwRRrj8Agf4TFIHBQrO0VqSpXyjn-wE0wC5Z5HEuhlxh7Qs-mCnsWG0wOudDehFZzI04Iki2t_vkUoIrOcmHqGRo3T3QvEh_YWp_nYrg==')
    res=requests.post(url='https://ios.baertt.com/v5/article/complete.json',headers=header,data=data)
    # print(res.json())
    # print("获取金币:"+str(res.json()["items"]["score"]))
    print(res.json())

def kanguanggao():
    data={'type':'taskCenter'}
    header={"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Content-Length": "15","Content-Type": "application/x-www-form-urlencoded","Cookie": "Hm_lpvt_6c30047a5b80400b0fd3f410638b8f0c=1610879165; Hm_lvt_6c30047a5b80400b0fd3f410638b8f0c=1610877995,1610878032,1610878335,1610879165; sensorsdata2019jssdkcross=%7B%22distinct_id%22%3A%2251940599%22%2C%22%24device_id%22%3A%22176e5a8275ae1d-0c2efd1d5e48108-754c1551-370944-176e5a8275b14c4%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22176e5a8275ae1d-0c2efd1d5e48108-754c1551-370944-176e5a8275b14c4%22%7D; Hm_lvt_268f0a31fc0d047e5253dd69ad3a4775=1610877716,1610877914,1610878852,1610879119","Host": "kd.youth.cn","Origin": "https://kd.youth.cn","Referer": "https://kd.youth.cn/html/taskCenter/index.html?uuid=1dd528208ba88da3d1572edd27b5c8ae&sign=a141824b46af7cd3728cde9b02f85fbe&channel_code=80000000&uid=51940599&channel=80000000&access=Wlan&app_version=1.8.0&device_platform=iphone&cookie_id=edfb98c33168786704b5badae06693c5&openudid=1dd528208ba88da3d1572edd27b5c8ae&device_type=1&device_brand=iphone&sm_device_id=20190930204732d6bf45fbb1b1b8a70a973cdb43ca179701e2bd8328ac8959&device_id=48724486&version_code=180&os_version=14.2&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY&device_model=iPhone_6_Plus&subv=1.5.1&&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY&cookie_id=edfb98c33168786704b5badae06693c5","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","X-Requested-With": "XMLHttpRequest",}
    res=requests.post(url='https://kd.youth.cn/taskCenter/getAdVideoReward',headers=header,data=data)
    # print("获取金币"+res.json()["score"])
    # print("获取金币:"+str(res.json()["score"]))
    print(res.json())



if __name__ == '__main__':
    qiandao()
    time.sleep(5)
    yueduwenzhang()
    time.sleep(5)
    shipin()
    time.sleep(5)
    jingxihongbao()
    time.sleep(5)
    shichang()
    time.sleep(5)
    choujiang()
    time.sleep(5)
    tuisong()
    time.sleep(5)
    kanguanggao()
    time.sleep(5)