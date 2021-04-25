import json
import time,requests
from datetime import datetime, timezone, timedelta
import traceback

YOUTH_HEADER={"Accept": "application/json","Accept-Encoding": "gzip, deflate, br","Accept-Language": "zh-cn","Connection": "keep-alive","Cookie": "Hm_lpvt_268f0a31fc0d047e5253dd69ad3a4775=1610169254; Hm_lvt_268f0a31fc0d047e5253dd69ad3a4775=1610169129,1610169233,1610169254; sensorsdata2019jssdkcross=%7B%22distinct_id%22%3A%2251940599%22%2C%22%24device_id%22%3A%221763575b1a613a-0871492e6bc0dd8-754c1551-370944-1763575b1a710d6%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221763575b1a613a-0871492e6bc0dd8-754c1551-370944-1763575b1a710d6%22%7D; Hm_lvt_6c30047a5b80400b0fd3f410638b8f0c=1610169126","Host": "kd.youth.cn","Origin": "https://kd.youth.cn","Referer": "https://kd.youth.cn/html/rotaryTable/index.html?uuid=1dd528208ba88da3d1572edd27b5c8ae&sign=b132053ccab97213d18173117d8743a8&channel_code=80000000&uid=51940599&channel=80000000&access=WIfI&app_version=1.8.0&device_platform=iphone&cookie_id=edfb98c33168786704b5badae06693c5&openudid=1dd528208ba88da3d1572edd27b5c8ae&device_type=1&device_brand=iphone&sm_device_id=20190930204732d6bf45fbb1b1b8a70a973cdb43ca179701e2bd8328ac8959&device_id=48724486&version_code=180&os_version=14.2&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY&device_model=iPhone_6_Plus&subv=1.5.1&&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY&cookie_id=edfb98c33168786704b5badae06693c5","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","X-Requested-With": "XMLHttpRequest"}
YOUTH_READBODY=('p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W53Koq9jCJJep6rrYcDySREuDHMDEvQ6_7zhF5sXybN0vgly4aaNcTXLnRadnWvYd8ftoz7bcJjuBfsX6oRl7-4eNgUhVbOVk9KWtiHbSN1CYj5f4-fGi-zQwmrynJswaNzDxa5oj90TLmCWN41l7kS_Qw2-wNtocus2Eda5wJsbkmamXYvzel8biuw8y9QvwzOv1B7mvYihlWsALqfx7aZgA3rwoJSv5Xs2hNGtROSgQeM50TGcrgx02H-pasJb0nHFlcnWEbdP-EzlGa-vHo8eYq4vvZ_TXGjod-4b6VwD7lZ2JMZNn62lnkvi1qHA8Pvbnyt0h0hN1Yq6Zebv-1KFazZQRiPWr6EIHkpWp4tJXOgPUXpslNaxYRIMIBmDoXjtmSIC6-ZCZPgT5-M08GIFYdM4-3cfdrPnCzis1T9T2RhudxqiZCifFauh9qHuDpuD2G8MqWgduoK3ISSwScINLJe9kLcL9TDRIoZzpdttnpLBBs1Df2ps-Xwcn5ctzkjqrvv0mcfHk3bv54TSr5tPdHcm3bShwwsQUOMBVSrn_bORDmHMliwj0xdA76wMKvA%3D%3D','p=9NwGV8Ov71o=GvDnjwMsu_ld4qx0YVkhCGk95BHaDHeUTCFMGsGqhi1dtO1C4WuBYfVS51_7tnsgwho308taCyWi2yKJtkSHTvTzP2kXMkya-8EmcKPLqPfWBn71wrAjTXUfjUwfJL5JOqtPa5dyS53avCqxoY4ajTlIcQhiDXTnGQY14rrx1-EBit3wB_JmeXsPbDbd3Oo54IEzS0m6EbOBXJW4nS9qgL5TaDMpJyX3CfmFaRyVwI1CvMQthgwG4V9Ylcxs4-DRvhYT2XZb5cuDutoDowYlKOcRF60147wOKfnuJyOEDeoXtF1Q6i7oerl-vVts9lst8Leo-whgXzujrDZ4mESBhS1w4abzXtuSovTDRA59qA31BhjcFPIPSrfjcKI1xjX6JVbi5dVkplODszgIFt4vtpIUoxR5Iz7BTty796USGIiRknApY5JX_4rtF8vanWgzTurRn9_EHA5kjE1bZFfyhkzM3yGg8_E029PLDpm4lxhH8BXWILib7uIpsnntanMRKqoYm45Syj9rNRFZgWd-K2VdIS_sSeGdsnUSLiQ2oavdfl7MEN2h-t72yC3yTmPwr52Iw7FUsbxriK1szTwSJYZ8O458paNaTK4-HDZnTnWjQtSXqc7DurI6askUupBCChe-DjCBt382NlHvBQNYUOGZTjo8u5BikV3ujq-pUDc3Sjune5NR1f20_66IlKB6DRD8fZRZGaJ-cKf6dEQicvHvpLO5FXx0EoOP2SMNnozVV8HyhxqKwbaSJhmYHkhIdyqUMF8Vglm2viJpYAFXRkxlexcMLIwiyWmDYMkIr-ToeIF1LqIPqO6KyeRx7_9wuDdlW5WvM0nKbk5v9YpCcA==','p=9NwGV8Ov71o=GvDnjwMsu_ld4qx0YVkhCGk95BHaDHeUTCFMGsGqhi1dtO1C4WuBYfVS51_7tnsgwho308taCyWi2yKJtkSHTvTzP2kXMkya-8EmcKPLqPfWBn71wrAjTXUfjUwfJL5JOqtPa5dyS53avCqxoY4ajTlIcQhiDXTnGQY14rrx1-EBit3wB_JmeXsPbDbd3Oo54IEzS0m6EbOBXJW4nS9qgL5TaDMpJyX3CfmFaRyVwI1CvMQthgwG4V9Ylcxs4-DRvhYT2XZb5ctf_JUGW1x4FB6s5IrQ7cvxooQB4SL86y2zLYCoU2UR1ENVenT3EmCk0cjMImaa7pwcLmdNX5BNY5A3CZ1pY8SUNih1sxYcPoPaFM6wTeQSkepuisnBTVnvXt09nHmBgSoSOKfpgCEMaVKVCbZ_DRW9xi0IL8jQTRcf-AlVkvPz84u-ErrmBW8koQtuJZKaiV6zAU0iCAoQoom3wPEnL0ded5hNTtja1EsBmnuuVAvHWLVxQN1xk967R1N4h7baFjEdvP77nR9XO_1axVDk8gwY9j-0DYtGZBC9hO-CTvh4V6D32ESL4PO4MvmCKaC74XOKl546Bmoc_cVzl__LW-bM36n5ZoYkLzGSuepKmxX54DqB26w_tTiln6rC-9Qasd8N3yn0mk76Jjre6S8P_7a8RqNxvqtEvYa9Afg5ODDgITKRzE8J6CNYLYwE8fAQudFbjonLxDsqbve-uIG4_tDd4uvT-MaGy62Bnj06DAo7MEZa61fgDcglYTQNALw0XftejuUv2ziwTPIwiDauaqz-2Rvn89Ws4CPSgcJ5R8xQLXB4B_XMZQY4-U4_irDtuigwZMuxTJJX8Q==','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATLz_D093IYRATKdFRTOOErqT8a0W-9iD_Sj_om7qE3yONtPqIKuP_xWkvElGbib-uRwf5PYfT9LIOtuyk64FBq4_A8MTjvddm9oc5VJi2QO5wp2baAjk77xAUfiyiWB3NQ2vz-mdBFvavR3u7tY3UCXD3Hnb5hvQ_ckYeBkcOMcKZBQgAAhIujSX0M5XFNWdVN1gQjnCmhb3vBkxur3myvtsWEdVC0tIfTZtAk9oIbu0MhPMTNfj0VIU9VH8GaX23aj4PCD4iptKhcxelBxlKks29rJtyXNT28a4ySfFKtHBJLGT3lQCORyzD-G5-0QuecLoE14xRyjDS7pES6c93K421iLokhQFV3JH4z0zRfbBhCMJn6N0MulCGWe7b0qhw8eE-bGyh0tAY98mG4ishv8dch4glVzW7YetHNDph8roFY7hSsfG1gyXcorJbQJcm1x7AOHfQt9GFf5jo89bFrOFNcdHO0nZhpUhIU-NvZ9qi-P_ntdkM_rC6umaqmChQzdqurZDvo4LFgDw9EzVsD-lgp9GnBuRVkywv0nkNPH107UQmaghRv4OvQPd3qfiJg%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W51cKDKeaRhMKEg8tyWO4z6Bn1Y1UikGAIEAmUXIubBmSNMLtNfcMXUsgn8LM5XI_sDpgu9Ys3_J6PNyPJIeLPkVGfPAe2R0TWO4gP-fLyteHSVAg5apMpzmJijq1WriL0IaPCYahTH38GfEOAlU06enidgRTcGJ-JAV94PZcFzNJyXh-sXrPFqL1hzQWhS4bc5VoW0LEHZOT1Y1G_WaQIo8g86FQbxdn_PHTHfdctdMEukOvtvOqMiiHbIy9pzNFZVd6O-TYXo9Vt2UcL9V2GonLMU-Y-diBQWfyCWPYE0zCk3o3lhwxoiI2DZf01OsTU0aEBfDuN3itcjTgTEjNvyYcqA8EnnMfTTylK_o9YnnddEzGVhD1OZbmm9_35B_qK4ILob_koOqcnpgZWPtht8olx6iCPgALMeBwUrGRoIHItEFivsqugX03TNH5rmPzEyXc0kO5iqPk3BKUkXcDpdqnwhy_lP1c187qQI3vna-Wb3RTuXPvyoAg5q_QBBCMKJq8njtY1up9cOdljZWKhuY1dB8IQOrZykAq6w0pgIUqcYWhfs1QAhM-dyxFZTICTA%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W51cKDKeaRhMKEg8tyWO4z6Bn1Y1UikGAIEAmUXIubBmSNMLtNfcMXUsgn8LM5XI_sDpgu9Ys3_J6PNyPJIeLPkVGfPAe2R0TWO4gP-fLyteHSVAg5apMpzmJijq1WriL0IaPCYahTH38GfEOAlU06enidgRTcGJ-JAV94PZcFzNJyXh-sXrPFqL1hzQWhS4bc5VoW0LEHZOT1Y1G_WaQIo8g86FQbxdn_PHTHfdctdMEukOvtvOqMiiHbIy9pzNFZVd6O-TYXo9VuQNciRXhJRvH_S8tHgoQ0PDUEnzVHy6cJ1lzhmwbsZEeMXTAcEcyq4mmtOfn67vEHfdGUvXsdbxEAhSX_fbFz2gX1MZMBrIhiMAw6Pvb7nFADwEDAJw2v-yv1Vud3KwYiWOo-4Em5LRnLP87vRGZqC2ajBdudjYzULFtz-XPKJkPuMbmkvln5IwBVB1hd_19EV1DOCo0s5maEBDmNJgBvCTvTYZNSdWVoRNg5BJwBjv8ISS08qA_m4S6Pw05BINSOU_U52EyGXJZ7nTXLvvqvTRDRffnyf1-AkTHtyuoTMjJSMoTy_8iXg%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W568UVpHgcRkwD_pBsqWF-B8VEBK6YToAfjKlxKFmSKUuzncU6OMu93aiyjVFQydcdGUH_cEgZ_SCm-ehFe-Q0r0YqAh7ubCg4GTCeCoSgPRPzkHezQWrax6OnHf8As0n2LV5zEASPYy8p7jJqaT5gh6iEZeSirrheHNc9Erc4SVEvYGouvz-lGfBIWzloCBheUQbT4Bok7XiCHyow2BY-8j_nYoXn2XjrBogqM4Nap1yCIYz2nmTQDR5oGVfCXI7orwrZXVraaDjjbjN1SZblycoNFGmGUdiw7MVn4KTtY34Q2F3Uajk5ZR1GhEE6gIdUlO0FYLn5WV57WshW6oN6szeuiCW94klfc8QUfiLgUdzyxGOFR9vMnq0-ZF32o9_2Z0EsZ_Hr94F_V6Bh1-LBgqN5DyA1-EUJruo65SGfcjbGzcWnc-4ulMLY4PepyPLJSu5-MVpDDN5hrk9U8-Jam3G9bdjvOV1Sie4rTirvqT1un63_-8PxOiXn-Xc8saHAdyIuUB-u4Ls533lj7iSsesfTRMT35UINYywPZx26pRbyilOm3uXeFyobFCy170K9w%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W5yWKtf5xKrcBU5_Q61XLEuYGJt2ZSvftUYEfThBrynnEFNiTzcjDmfQ6jP7r4lDf4RhYCCwwkph1BZSIcNhVNBOMk6-N4BYeoEyR4ak9gtt5hvPmJf0Dz143f7rjxe5aIt2nN947MgZBwsRYoErpmuQ7197g7Ux52eZIbRCZSD0oyHU1Wdufji13DdIm4EiXd2dFvPWohvhA4_v5E2mDfLSlAxdsHF-aCp8uhGJHUJi3Rie00RCYjaChkjzFp0PLDBSTNDRuNCyZNx8WorA96eIQARmCZlH0iYUCKA_X2kt5VWtFTy1dLd63qRyn9FUlNwWWJdYHSfeDgMsepQqJZr7as6PtRelHpQZ0FJJLqSrJDY8zAUnJfHXWiOH9dIYesRMNga5_kKKDTZXZ5H4cub1Z14XNPFPpUSe7ufZYIP9kRRv_hCg_pBZwW2RInzHzk7J4_IWCzRaErfNP7w5Suo0arBIqFfV7dPlk-jeh4LTb5VaFLYSa8TAfP1SaSrbKcjqnEV68TNldKGzav71LJLUz01qaq6hqy22SkGkni5fO47iiY24ViqMXcieRmKcpQg%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W5wlp8pY2mfZsAwm_XM6ugmm3xRr9l8X9mQ4c_11EWin9qlSsJlM-KEGw-jloY_qzwvYf0refztI-Ir2xelYJfcVsz2Y3WZHCYcoFLSxC445UzL7k1kRyX0GmqeIYHAafhi91u2KKiy6O9C8y-cl7JjuBwwGIhT_8qV6SyxVlhzLYVmJUrYOa-FBZWx81WVKH9I2CjqrGhlN3l-tg7WztwT4w6bGVhNfnP5HeTqQL52HnuK2BQp72Rikzs7w-0BM0JQ0qQToWCz8MChkS6kpE5Y__0mKT1p3zbuljVJwYuBtVTqKmJvl2Ffg3Rc_JH-F70ljCNNspBSbbxcAvrSK6P4P8xmhMQdMsIEHQ1S8dSw-EeCdhk3Un9XdQ1l3onRheseVIPKcMqE5fzsE03Ylm5oF_izD3YI1s1W-kNnzJxSg518IzZ1YzDtTDp2Z2pkQ6xaFiLlGsqvlb5jdrtwPFvg3hww3NH_UMInd05Bqg3flsty76VLi9NHhwJuGsji_VFiBj78RGflpHLjumkeCnp-dUez_ffJde_pzoYVMzfKg7qGv6mR2dctblnn3883Bpcw%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W55VGrIGS4CW5HUzGcWRYFuorBlwpKaT7YyOEI2jxcQgGoZznjy1kA65rdjXE7B16zKWNbAP-mJnXeFC_MDfy8YUTbcIbIJi20q0MyPfokV253XgYmP9-uej4KwUc99g78p-93mLWRqUtkluLvtVjZmD-htNlfK4PriTVg8E_W_b4uU3elJbQ0NG2XwaQpWlVQMZvSuOy4UQdy7z21kopYk4MdjgaNoIBvDxkvtyQm_I7iWex4qgWlVV_fBcnSEb4nB0I5JvZB0D90UrgYT98z0TXRy2xl9nmBqaCJdkTUuNrEHYWFzhnUI4tf85VobNMni531IMpjDbj_I5qpfPXtO8UiFfhV71_9kp5sA06iKSPU8FU4C0wGw61FCMSodShIuuDAGPxraZ9A6Cgf8UG0LEdMYoUMAL2AvtNT6BPrMQIZsbLEogZztmj6N5H2cmdGL1RWU3WlnIM62yMh_gJmSxk9s4KHhyeNItfGxs3yNp9zX5PzAMz3S2JgifJnmHu6IXjz0D-qyIXtwNfSBFrDiMf0TwyHwdlTKaSU94xF3wPARDN1shYUWKV6f0-jWQL4w%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W53HeKimAKL23Vi_xUZNlZOb_feuV7_E6kjmZvdzyPQ0vOsb1w7FLi488AONow4qloG2CzoIKNUEVjg6w3dKeL3RrgdbGS2MsgV2PHKDN6rarYiVnctsLbgMkX6pey2gIKxZ66xD_KNIHv01OqoQ08oC8-T9jiYy3n09NoSdGah7loCeyJdT6CXWCLYqg7HaAODT7YE2UMote9pdlnjBtLm9tA-5KaFUjzO2DumcVxSq30F6D0HZhJ5knMW2trTfzbo74uf0_IlCMdVpeDfDSCv4SuucicmzrTMMV6N56DKaQ8Royy84houoTlb4CSbTibVpHfnGHSNUfPjaa8ilpGSJre8pp9R_pd1TAFNltJQf2CBjoo6HmowyruYVa9hA5AavM3EqywAtGfFQqrjOPET6gOgNtTN_bbXu9QKVYNGpW7bcoAXkB4U7UOxeia3QyzM_GhPK47LMtAnnBNBXjLiEigAzWdPLAEwLIiF9NKuk9kA8y3P4jEggGFXq1eEuApbBqbQOfsgo2o9YXjlSkwr4oZjAnmIl-Qy4llAkZGdGpP5snkcX6zx5Cki0ZDz1TbA%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W5zoHHifqeNLovGzItZ-5h3BMnFRfmdEwt-0vF3lvoDxbeuZjwY6OR7q_BU-4gFpegL0OTlaQrAn188cGV-ZVAhDfVDJElpJ3Hr1JACa5qD7fv6_LWkBG2AI6WINgGTTKRgfuyv0QrJh5Yr7xRO4tV375QVaZlRj0ZLSYrVoaJkby-ZmoYD8gj-sLV_lIjOOgbAGGvPXO9LP85aoCJVK5kONcRklZU5WSGPcMOQEAw18NEqrn9lOfTjq7ts3tIEHwT6vZ5iY3i8zQwK-PY1wIrP8iACdk5KXlRzT1TljZr-Sc0x98WLOMQahD49JWTV3J320xoGJ1Vcd9yzAp_OthNb5hlMfYJDrwOX5Cg1jP3KVhIZl4GTRJ7m_DawQkroQslvmCi0CkV1lR2vYM3uWKeU3MeOFIvXuncjYkk3KAQojPgfZqqTwCWjD5Cb63ys4CWTcWed678aUlBzfmiLQLl7cBEqtTeY0B324GZrY_Sjyo-7Ezliwq70OlRma54ZUDKGrRJYc_ggW4oePv4HaFxlBpcYBUBJ5-ELJH69ap2QYfHxOZ9Ph69ewkrmaVb93a9w%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W5yuhA34ugkcOvPPTYBoqlndywlNMPbdeZ9GL3SKPd8Jmiz2zI0vOSSP7xe2cYFDNB7laKm_756izkmbH39B247HIRd6_sNA6ItqcCqdm5a_LfbdqsSB3yR-FrAjbrH1__qg-J3HqTYQ1__9CGRr5HGfknmzD9mQMNfuiYbFy6aru8d4bnQZHA6VJzJmFFfcR8xRF-KkQH0Pac1ALZEzv2Wg24jBjwIb2lF_WISMtPAkC89TcGAqxF2vFstQsU20MXNstWp9FPsn6W2avn7qbgnXUNmM4-in_imzhMJ4jSPUXo2n_LJXHVEzhzsTMD-DZcsETMcgSDGTMn0_wTbOnNw8LA5AAIn8ZHDU4lYxYPh6nquVViWV16dusdrmRFIs5dZsnkBQbXfvI6fk7h_0tEvvBWbF7MReVsS_EVlmEYE4m8QDk1SuAmPoWHlKYboYbpmqpDLCJmsWg4nnFGFS8gvZYYpyVPnZ1_J5ywjuLQe8RdCMWv_AJH6Pqf6soppfRWYl3epEbQox_QqjsuqFuZcG7KeqrXSS9m_4NaeTJXFe-2IM6Ewt3yExoeJbNIzUFew%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W5xvyEnSiYcVY0hVxmp0wILsyFsRQ7koxO-p-Mufx5RMSnFhJVtcmx5tPduOrWzjtze-leW0oGC0t68zvPHhkOctjn2pLAyc46XtFaxwCIvXwqrB35y8pZ_wY6gAI4Gq--6ccg04jBj68jtwrLqe-2DVhS_FKYhIO_35Uh3eaP5qYVoH5l9Vuk4PbHN6IG2LuEyI4uWeoRiUZql7D1cfnIJwqPVbV6IKLXsuptwBhM-AAwmJVGcLDLPnlCY8nOMk7fiEjudZ2U-qpjGf7AJhaILqYRPhrZ1usueK730_7TA9IaAaTn4gYQewIgBZBfQu-phuKGC2Dq5wTlio3Pt5drpRa_80oho4pEaQQEiItaCATvI0_zNG06kAvTGKwlAXc4CJfYxQWqEr_tf1utiaYuvKUhUCu0YUVtTptB4CJYr8LPTARrpaEKgb0KRtsDkoaQxKt_u42KcfsvwTU6VtxbP_l0kq9qoP9WBy6RsQyHiJkbYYc8QBS4pSUiop3ExBILQ3EwOiaPGz3AOAgAV4g75pwthxx-b76-JtPEbcXN1gqfDr4KScws9GZDmwplGpT9w%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W5zoHHifqeNLovGzItZ-5h3BMnFRfmdEwt-0vF3lvoDxbeuZjwY6OR7q_BU-4gFpegL0OTlaQrAn188cGV-ZVAhDfVDJElpJ3Hr1JACa5qD7fv6_LWkBG2AI6WINgGTTKRgfuyv0QrJh5Yr7xRO4tV375QVaZlRj0ZLSYrVoaJkby-ZmoYD8gj-sLV_lIjOOgbAGGvPXO9LP85aoCJVK5kONcRklZU5WSGPcMOQEAw18NEqrn9lOfTjq7ts3tIEHwT6vZ5iY3i8zQrW9E-WAZ5JwngdXHux54WAVlH646El1l2DoYYyTF39kxdIIz9rBnPmL0k1y2lbeA3P0MZWcqMZlpkjxWNQJtmpYFiMdTGP0ODbEVsqSU2KbxrGBGf8Eu3Z494xbjPj74oY6bOeyCcHPLBygzMbh90W3p6wff6V91VKJ6i_IFVHj5A1boEhR3tPUbL-B0ebaJr4N901lrMUHQ6xMIofbQEogcen8Zj_6ngES-ElGrvs0TWb2NifJOUGk3LBj51hHJKLLVSVXFwA0M3WDC858tASgnRTGK0REK31cp83xVCR_Vrb8bg7zL8w%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W59ilUBejuYYnPe0XwXoup0ZF2xZMr13pXbE_fScc4PYCVoYHgIgLcwpSs7MMMvPNHpWSrzENtsFI0EFojGnWGzGeHaTFjWxjjSNGVwm45bojLKCg-ZcQ5GdamCMMrddRz8Kc8LF0m-xbb5FkSomwKWafzZlNQAdntwVz1AUP80nfnSoHcXzS-UzErU0-rTXcVq7CozcMORZIM6XLAd1ZQYf6g0DOzA1lwXNls8MOCXzwXnF4dJy4IoU5rK0oxhWXuOl9GwrDjUXdC50RLKFcTjP5nM07m-bbi7RY1aVeifX3dHXMFN157zqcQv8O2ybM4F0XBvRygy77Sdn1QZXlBM_zLfFXMRafHxzCNawaAryMiiIczGE7w24QBxRNXXQmQZdlp8oORezodYB2vytt_mcJfHIYoXGmX-Yqm4Mj7fy-Tvew2CVYSPW4pmvHvJvUyBga5IkfUjyrH2gB8yDxBJFV9euk6brGgNpDKE2YV6Vlq8Qk97_aZpvtVXZOOPQf3nvYB7x2LqneFIVn1vbEL0XRz4CbUVx6MfUftb4cv4BHC7NYAhz3tNvXeTqkb_kmYg%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W57yb8M3QY7JWGIXw1KfWl3siDm4pIw9JN8bOxaSAMY-hDsxsNV_bJuUjkdqw2y2NZ4gUU64b-6AZ8ruzg1-lVTOMqfCRW0vyjBhTem6BdjU7SfOGmCSxT4xni-uVfaJX2ow--nEOHFzZ0SHpZyRBnahKThiUN8tFbhC59Ny1HTpSFoc8Jh0T6KoWLmkVOlHbgR26myQA_rXUkJcolBJ2vTB-iM1bFRfuszF4_3pg6gkhtOsAv5tztACgeXDXR6upyFp8Q--HLh2areZo1GxIJDBYX7V4-hsWWq2HkhwtcEz3SRswzIjrOgICrjsdBe6QFzjmTH_MF9k3WZtgLIvVbVZfn_TLLqqMnfr9DDXCdJ-N6YsHu87lIbq3SLyJlcV-nkRJ4ICjYUtjbbwlmNqL_Fz2hJt7J2hjOXcro3oG7aYk9EON-UynmQ6FkauOOtPYvvbSR0ghSwjy4b3kRwlTjxfB1k0SMm373IbolaOdwMi-kdpozIOQFKqrrXBBu4D3Ou82xu2po5IwH4xTTyQLqH8EoCK9HKamh91iBipEtmzJTKaTlzqIf1d-uLwMwhj87w%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W54A32GWYYd-iG3L5mQRgTEaxLjEJkaeKKIWghsM23_jYOpP9zXvgU-Jw4RbBp5q-46ZOp0Qrka6CZb334hYtUFfQd7YBmRIe3LpKTOULuqZhSYL43-8F0OZb3jrrsMlfqTLC3Vdflc8BdXBVG8OUv85CPChzW43z9X_inDEPs5v3zVqqw6-bA0AI6anXnPQAunEHi3D383Gm11UQUwOrXyz_VMohM0DP5ga_x106rrcHAkjRiQvVYF1Px164X7kFfx2kXtpb6bL1o1e1Mt_8dfPYZZBTVuZHrSUfhEhwbFI8MV9PrjuIZmhs4eq3rGhg1AEFeZE8pIUi7Oq3dWybA07rbwRujUg8u0ELNN67U2GwyFq00WjRddtuaRMGyQYbDsxwymugCw6gTmXEf9U9xWPA1LlsuuV1j_Y8MQWWXZcbbx3hH2xP5eRItTpalr6n8_GV2NqiweW_QYh3QmTPHkbJSauuu25fdC0mfYhawrtk39YF9VdBNFCSTmr_YYfPStRM9DmVWCKFo2LAuGtWkqR4GVj6tHutpZc1PWYgh8iKetJJyg-qyPe7nUFdimdEIw%3D%3D','p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATJpDKbt6E6W52K1oZ2pOSNvf_H1S01P7k4g4dhfxZKn2UTnZDEA9f5xN4q2jXBkMAIvWqWw67FN6H115RXxvrQbu_GmwRofX3y286H-Qef_ktjowNGC-90KHaft6EwPo6mHIhudZBQUrdzsUTxAaGGy55mvS9wSxXAa2oB9rP5Tq2emcatVqWicAIspflz_n-uJDywbsDfXUCfNejbiKs-Y9CqavuptWS_Hop_nQVNV9JcWZpT3UfTgcKw__XPtuQ_o73-NJB3PWdPf7m8h0OnM53-tRXg5H5BmtwrUAng1U20bEJlbEDxULgfPui4agKSOQiKxUrSC1fnpa8Q1wDBmzzyMAIbnIvOA7DReVsuDV271gdcoFn-6VwPY5G59h9lR_FeKPvGnS1wHX-HhlnBqbgxdsaN7ar4dMnlx_WA0t4QtBG6AlQqt3B9z-9ZiA413EmmGjad4knhJLqwX0TTZ4Pu0zUUaoy5dq_OuM0CBg-nS6lTsdSjGYH7VN2-FpNBTanSfJsRitF2kjn6IB1SV3JB7rxt6A1f3n8n4FAMjS54qS8-IBGVDfEUiU3Aua04KVt6UuNLRTA%3D%3D')
YOUTH_REDBODY={'p=9NwGV8Ov71o=GvDnjwMsu_ka-LJ9wnbNzBhA0cz3iHWgEqXEh3bkBC0KSg93aV2LC-S2kpFYl_sQgZd-rfBZbgQX8-9JlXjq_HD3U4VdJ0FUw7V5oD5274GNkOv0xICutG3-lH4ryy26yNVY9ePaN_wC5z1kUrmjhoDDI0Vau-fqBoBjAgUzoOsW5VgxWu5zgWUcaoD2SbMT8s1X5Lz_AAxtYdvua5hQkqV3BuLbagxKLD9REcxg1-yXLmiTycVHeCkVSaSEW6Jwc-ubt-_IWF_AQvdCA8cgxOerY9WPi7kDHP6tuGl5yyUGpVXr2Mz2Z7Z32pDEmorB6uv2Qi2qU9erspBm_sGkDlm5K5W5Yacl_aKz313Aokl3EXxQV1CQPVKBv3lJszoxAvzgsyGmL-vhBHESWzd91Cl4oKDDAQVK9PGEaS_OSfDI5yG2ibV5TwIz-mV55jXOgvBPWW8bYb86MEpTodzzltx7hS5IncKBk88Q5ijZRdDDhnL4I7Xf83L7FydNMfLIwP3TWem_gshhtXp6Pb01abN62c2jfh-5JaKo0bQW99vRa370Xo-n45H5QzfkFpWBU680y8zBheTNApXVp4Ilyxr6WwfqNsyUKlaGapXEtJp7l_AInWoWrUS1rXzkYCEVTXZ0FUVxASzxH4pLeMhqM8KnL_aYegM1V0aXEA-0W9Qoy8rFw9SYIaJ5-VXQcHsaND3e3bCdyKSy3QfBelqRUFqcbr_LNY0VwQtYAg7s2uuPfkCgM1a47JggoGFocMt2-0Lx23DLoelUT3wzhaCOg62tlj4WueEGLHj0Q5MagJ0-vPKiOYpFaxPgP5HWekzKiLaszZM2A5lmkog_yIPzIg=='}
YOUTH_READTIMEBODY={'p=9NwGV8Ov71o=gW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmZ4B0fZBEJVJLd6NpD1t2rsPgKIPESyHM_WWQ9Di8eTARetclf4o8zDdLAEaIRVg54LZRakoHMlArRKlXlZjQW6sFqXdSeATLz_D093IYRATKdFRTOOErqT8a0W-9iD_Sj_om7qE3yONtPqIKuP_xWkvElGbib-uRwf5PYfT9LIOtuyk64FBq4_A8MTjvddm9oc5VJi2QO5wp2baAjk77xAUfiyiWB3NQ2vz-mdBFvavR3u7tY3UCXD3Hnb5hvQ_ckYeBkcOMcKZBQgAAhIujSX0M5XFNWdVN1gQjnCmhb3vBkxur3myvtsWEdVC0tIfTZtAk9oIbu0MhPMTNfj0VIwGIzBEO9Vxqj2FriyeFN94ID1r7nRSQMJ47TAi8oustRDVERYCQhnDcOQlVh3Hkrghy8QDjhZoMTsbMnClNrybAmUwIAw4LnMOxRDcapZTt5JVf-yv5AXdOnTelGTyZwjEuFqqxhMM0IOZ1RdcxHA6g7-d1NtYFhJMHPqBctwb2R09flfZFeMP-57VuJtGCslTQeuDuAe4XkjHp_ybK_WRyZgARx8GHq_S9VNMwFGVg0lz4gFDLHqotCuhwR2Ze9bNLRiinuV2lFRG6fqV39OkKhzchBNp97uNWQaSf2yGL2Zkrl4DQKxB8zfzuOm5GjFxBbCoCHNZE'}
YOUTH_SHAREBODY='access=WIFI&app_version=1.8.2&article_id=36384198&channel=80000000&channel_code=80000000&cid=80000000&client_version=1.8.2&device_brand=iphone&device_id=48724486&device_model=iPhone&device_platform=iphone&device_type=iphone&from=0&is_hot=0&isnew=1&mobile_type=2&net_type=1&openudid=1dd528208ba88da3d1572edd27b5c8ae&os_version=14.2&phone_code=1dd528208ba88da3d1572edd27b5c8ae&phone_network=WIFI&platform=3&request_time=1613800601&resolution=828x1792&sign=c7b34d42c964c24554e89f6cd20e478a&sm_device_id=20190930204732d6bf45fbb1b1b8a70a973cdb43ca179701e2bd8328ac8959&stype=WEIXIN&szlm_ddid=D2UPBRS7Zjh2IxE5ZeFknVGVsPPEKVY%2BuJt6UZzFTN47wX43&time=1613800602&uid=51940599&uuid=1dd528208ba88da3d1572edd27b5c8ae'
YOUTH_STARTBODY='access=WIFI&app_version=1.8.2&channel=80000000&channel_code=80000000&cid=80000000&client_version=1.8.2&device_brand=iphone&device_id=48724486&device_model=iPhone&device_platform=iphone&device_type=iphone&isnew=1&mobile_type=2&net_type=1&openudid=1dd528208ba88da3d1572edd27b5c8ae&os_version=14.2&phone_code=1dd528208ba88da3d1572edd27b5c8ae&phone_network=WIFI&platform=3&request_time=1613799793&resolution=828x1792&sm_device_id=20190930204732d6bf45fbb1b1b8a70a973cdb43ca179701e2bd8328ac8959&szlm_ddid=D2UPBRS7Zjh2IxE5ZeFknVGVsPPEKVY%2BuJt6UZzFTN47wX43&time=1613799793&token=97b8cd0175e2dae9311a593de2683b9a&uid=51940599&uuid=1dd528208ba88da3d1572edd27b5c8ae'
YOUTH_WITHDRAWBODY='p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_kF97hamPuz4ZZk3rmRrVU_m2Z51XN3szZYaCPxNG07BYjyjwYkBVGTfTGYPVecze9u-jGHCQmfvey4yZrPyKR-cA01PbV3h61GBiHFc-skGrpoDK0eliCfJPX7f9_IVT-MEKcW_xpZBatH4KAexZ7tz4DKRYyIP8OmYeIgjnjRygIB0qTBZrh2BDf3Sttd3rs7YVvdVqQDAwq4UlWKqXiFKG2EuaouWQVr-Uu9U64DmN7LodloG1HnpwoYix-kgzs2CO59WvW8uhBp0zoEfFP_clDu6rEYFwr7Zx80cI7hlMP6IvjJzEndcDeWVGl1jN0cRK1h3w2HXtwQ6Nx7o4jkjTlKNQDmde43UK9eACHvzCpzA4O2OR09-LEp42AQIsL1qhUnIlKtMk0D_B6u9d3Mcrcq854GrucAc9dNqZetl8wNYVx4MviS2tUqruWR183D00z6KUKL5U6foO7zQsGtm4oppUCEmse8sEU1T3BiYTU789rspt32ckbYYY4AiAZOirUVTp4h3yKVoSXqkp_l67mKG3CBa6-zTfK3_VNsTWUAQ5XkRvg5PAMffMn0zDnJmWSIWXZZMFcK0G1cOQGAvvkb3s0PWP1zxhRwSq8HutTm3qLOeiCwMzU1If_5hw4JD2W1Kg_ObwJaSDySAuMTBu9LtfpqR-Brl2aQ__vT6XIMH38oELt96afJfCD8ooZaR716Hrgqp9FRKwbIx2lDTjUxRoymuUb_DmtjIzUT3NjlogN2I3sJxVJzk2xwryQHSCB6_pjxPPLl_MX6XtddUc3ikzCsmsRbr4_YKyrUw%3D'
data={
        'cookie': 'MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66Fz2Kwp4luhoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLCnl7KEjIaYrt-mapqGcXY',
        'cookie_id': 'edfb98c33168786704b5badae06693c5',
        'app_version': '1.8.2',
        'channel': '80000000',
        'device_type': '1'}
YOUTH_HOST="https://kd.youth.cn/WebApi/"

def get_standard_time():
  """
  获取utc时间和北京时间
  :return:
  """
  # <class 'datetime.datetime'>
  utc_datetime = datetime.utcnow().replace(tzinfo=timezone.utc)  # utc时间
  beijing_datetime = utc_datetime.astimezone(timezone(timedelta(hours=8)))  # 北京时间
  return beijing_datetime

def pretty_dict(dict):
    """
    格式化输出 json 或者 dict 格式的变量
    :param dict:
    :return:
    """
    return print(json.dumps(dict, indent=4, ensure_ascii=False))

def sign(header):
  """
  签到
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://kd.youth.cn/TaskCenter/sign'
  try:
    response = requests.post(url=url, headers=header, timeout=30,verify=False).json()
    print('签到')
    print(response)
    if response['status'] == 1:
      return response
    else:
      return
  except:
    print(traceback.format_exc())
    return

def signInfo(headers):
  """
  签到详情
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://kd.youth.cn/TaskCenter/getSign'
  try:
    response = requests.post(url=url, headers=headers, timeout=30,verify=False).json()
    print('签到详情')
    print(response)
    if response['status'] == 1:
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def punchCard(headers):
  """
  打卡报名
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}PunchCard/signUp'
  try:
    response = requests.post(url=url, headers=headers, timeout=30,verify=False).json()
    print('打卡报名')
    print(response)
    if response['code'] == 1:
      return response
    else:
      return
  except:
    print(traceback.format_exc())
    return

def doCard(headers):
  """
  早起打卡
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}PunchCard/doCard'
  try:
    response = requests.post(url=url, headers=headers, timeout=30,verify=False).json()
    print('早起打卡')
    print(response)
    if response['code'] == 1:
      shareCard(headers=headers)
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def shareCard(headers):
  """
  打卡分享
  :param headers:
  :return:
  """
  time.sleep(0.3)
  startUrl = f'{YOUTH_HOST}PunchCard/shareStart'
  endUrl = f'{YOUTH_HOST}PunchCard/shareEnd'
  try:
    response = requests.post(url=startUrl, headers=headers, timeout=30,verify=False).json()
    print('打卡分享')
    print(response)
    if response['code'] == 1:
      time.sleep(0.3)
      responseEnd = requests.post(url=endUrl, headers=headers, timeout=30,verify=False).json()
      if responseEnd['code'] == 1:
        return responseEnd
    else:
      return
  except:
    print(traceback.format_exc())
    return

def luckDraw(headers):
  """
  打卡分享
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}PunchCard/luckdraw'
  try:
    response = requests.post(url=url, headers=headers, timeout=30,verify=False).json()
    print('七日签到')
    print(response)
    if response['code'] == 1:
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return
def timePacket(headers):
  """
  计时红包
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}TimePacket/getReward'
  try:
    response = requests.post(url=url, data=f'{headers["Referer"].split("?")[1]}', headers=headers, timeout=30).json()
    print('计时红包')
    print(response)
    return
  except:
    print(traceback.format_exc())
    return

def watchWelfareVideo(headers):
  """
  观看福利视频
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}NewTaskIos/recordNum?{headers["Referer"].split("?")[1]}'
  try:
    response = requests.get(url=url, headers=headers, timeout=30).json()
    print('观看福利视频')
    print(response)
    return
  except:
    print(traceback.format_exc())
    return
def shareArticle(headers,body):
  """
  分享文章
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://focu.youth.cn/article/s?signature=0Z3Jgv96wqmVPeM7obRdNpHXgAmRhxNPJ6y4jpGDnANbo8KXQr&uid=46308484&phone_code=26170a068d9b9563e7028f197c8a4a2b&scid=33007686&time=1602937887&app_version=1.7.8&sign=d21dd80d0c6563f6f810dd76d7e0aef2'
  readUrl = 'https://focus.youth.cn/article/s?signature=0Z3Jgv96wqmVPeM7obRdNpHXgAmRhxNPJ6y4jpGDnANbo8KXQr&uid=46308484&phone_code=26170a068d9b9563e7028f197c8a4a2b&scid=33007686&time=1602937887&app_version=1.7.8&sign=d21dd80d0c6563f6f810dd76d7e0aef2'
  try:
    response1 = requests.post(url=url, headers=headers, timeout=30,verify=False)
    print('分享文章1')
    print(response1)
    time.sleep(0.3)
    response2 = requests.post(url=readUrl, headers=headers, timeout=30,verify=False)
    print('分享文章2')
    print(response2)
    return
  except:
    print(traceback.format_exc())
    return
def threeShare(headers, action):
  """
  三餐分享
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}ShareNew/execExtractTask'
  headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
  body = f'{headers["Referer"].split("?")[1]}&action={action}'
  try:
    response = requests.post(url=url, data=body, headers=headers, timeout=30).json()
    print('三餐分享')
    print(response)
    return
  except:
    print(traceback.format_exc())
    return
def openBox(headers):
  """
  开启宝箱
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}invite/openHourRed'
  try:
    response = requests.post(url=url, headers=headers, timeout=30,verify=False).json()
    print('开启宝箱')
    print(response)
    if response['code'] == 1:
      share_box_res = shareBox(headers=headers)
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def shareBox(headers):
  """
  宝箱分享
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}invite/shareEnd'
  try:
    response = requests.post(url=url, headers=headers, timeout=30,verify=False).json()
    print('宝箱分享')
    print(response)
    if response['code'] == 1:
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def friendList(headers):
  """
  好友列表
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}ShareSignNew/getFriendActiveList'
  try:
    response = requests.get(url=url, headers=headers, timeout=30,verify=False).json()
    print('好友列表')
    print(response)
    if response['error_code'] == '0':
      if len(response['data']['active_list']) > 0:
        for friend in response['data']['active_list']:
          if friend['button'] == 1:
            time.sleep(1)
            friendSign(headers=headers, uid=friend['uid'])
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def friendSign(headers, uid):
  """
  好友签到
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}ShareSignNew/sendScoreV2?friend_uid={uid}'
  try:
    response = requests.get(url=url, headers=headers, timeout=30,verify=False).json()
    print('好友签到')
    print(response)
    if response['error_code'] == '0':
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return
def sendTwentyScore(headers, action):
  """
  每日任务
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}NewTaskIos/sendTwentyScore?{headers["Referer"].split("?")[1]}&action={action}'
  try:
    response = requests.get(url=url, headers=headers, timeout=30).json()
    print(f'每日任务 {action}')
    print(response)
    if response['status'] == 1:
      return response
    else:
      return
  except:
    print(traceback.format_exc())
    return

def watchAdVideo(headers):
  """watch
  看广告视频
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://kd.youth.cn/taskCenter/getAdVideoReward'
  headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
  try:
    response = requests.post(url=url, data="type=taskCenter", headers=headers, timeout=30).json()
    print('看广告视频')
    print(response)
    if response['status'] == 1:
      return response
    else:
      return
  except:
    print(traceback.format_exc())
    return

def watchGameVideo(body):
  """
  激励视频
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://ios.baertt.com/v5/Game/GameVideoReward.json'
  headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
  try:
    response = requests.post(url=url, headers=headers, data=body, timeout=30,verify=False).json()
    print('激励视频')
    print(response)
    if response['success'] == True:
      return response['items']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def visitReward(body):
  """
  回访奖励
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://ios.baertt.com/v5/mission/msgRed.json'
  headers = {
    'User-Agent': 'KDApp/1.8.0 (iPhone; iOS 14.2; Scale/3.00)',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
  }
  try:
    response = requests.post(url=url, data=body, headers=headers, timeout=30,verify=False).json()
    print('回访奖励')
    print(response)
    if response['success'] == True:
      return response['items']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def articleRed(body):
  """
  惊喜红包
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://ios.baertt.com/v5/article/red_packet.json'
  headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
  }
  try:
    response = requests.post(url=url, data=body, headers=headers, timeout=30,verify=False).json()
    print('惊喜红包')
    print(response)
    if response['success'] == True:
      return response['items']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def readTime(body):
  """
  阅读时长
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://ios.baertt.com/v5/user/stay.json'
  headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
  }
  try:
    response = requests.post(url=url, data=body, headers=headers, timeout=30,verify=False).json()
    print('阅读时长')
    print(response)
    if response['error_code'] == '0':
      return response
    else:
      return
  except:
    print(traceback.format_exc())
    return

def rotary(headers, body):
  """
  转盘任务
  :param headers:
  :return:
  """
  time.sleep(0.3)
  currentTime = time.time()
  url = f'{YOUTH_HOST}RotaryTable/turnRotary?_={currentTime}'
  try:
    response = requests.post(url=url, data=body, headers=headers, timeout=30,verify=False).json()
    print('转盘任务')
    print(response)
    return response
  except:
    print(traceback.format_exc())
    return

def rotaryChestReward(headers, body):
  """
  转盘宝箱
  :param headers:
  :return:
  """
  time.sleep(0.3)
  currentTime = time.time()
  url = f'{YOUTH_HOST}RotaryTable/getData?_={currentTime}'
  try:
    response = requests.post(url=url, data=body, headers=headers, timeout=30,verify=False).json()
    print('转盘宝箱')
    print(response)
    if response['status'] == 1:
      i = 0
      while (i <= 3):
        if response['data']['opened'] >= int(response['data']['chestOpen'][i]['times']):
          time.sleep(1)
          runRotary(headers=headers, body=f'{body}&num={i+1}')
        i += 1
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def runRotary(headers, body):
  """
  转盘宝箱
  :param headers:
  :return:
  """
  time.sleep(0.3)
  currentTime = time.time()
  url = f'{YOUTH_HOST}RotaryTable/chestReward?_={currentTime}'
  try:
    response = requests.post(url=url, data=body, headers=headers, timeout=30,verify=False).json()
    print('领取宝箱')
    print(response)
    if response['status'] == 1:
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def doubleRotary(headers, body):
  """
  转盘双倍
  :param headers:
  :return:
  """
  time.sleep(0.3)
  currentTime = time.time()
  url = f'{YOUTH_HOST}RotaryTable/toTurnDouble?_={currentTime}'
  try:
    response = requests.post(url=url, data=body, headers=headers, timeout=30,verify=False).json()
    print('转盘双倍')
    print(response)
    if response['status'] == 1:
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def incomeStat(headers):
  """
  收益统计
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'https://kd.youth.cn/wap/user/balance?{headers["Referer"].split("?")[1]}'
  try:
    response = requests.get(url=url, headers=headers, timeout=50,verify=False).json()
    print('收益统计')
    print(response)
    if response['status'] == 0:
      return response
    else:
      return
  except:
    print(traceback.format_exc())
    return
def withdraw(body):
  """
  自动提现
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://ios.baertt.com/v5/wechat/withdraw2.json'
  headers = {
    'User-Agent': 'KDApp/1.8.0 (iPhone; iOS 14.2; Scale/3.00)',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
  }
  try:
    response = requests.post(url=url, headers=headers, data=body, timeout=30).json()
    print('自动提现')
    print(response)
    if response['success'] == True:
      return response['items']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def bereadRed(headers):
  """
  时段红包
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = f'{YOUTH_HOST}Task/receiveBereadRed'
  try:
    response = requests.post(url=url, headers=headers, timeout=30).json()
    print('时段红包')
    print(response)
    if response['code'] == 1:
      return response['data']
    else:
      return
  except:
    print(traceback.format_exc())
    return

def startApp(headers, body):
  """
  启动App
  :param headers:
  :return:
  """
  time.sleep(0.3)
  url = 'https://ios.baertt.com/v6/count/start.json'
  headers = {
    'User-Agent': 'KDApp/1.8.0 (iPhone; iOS 14.2; Scale/3.00)',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
  }
  try:
    response = requests.post(url=url, headers=headers, data=body, timeout=30).json()
    print('启动App')
    print(response)
    if response['success'] == True:
      return response
    else:
      return
  except:
    print(traceback.format_exc())
    return
def run():
  title = f'📚中青看点'
  content = ''
  result = ''
  beijing_datetime = get_standard_time()
  print(f'\n【中青看点】{beijing_datetime.strftime("%Y-%m-%d %H:%M:%S")}')
  hour = beijing_datetime.hour
  # for i, account in enumerate(COOKIELIST):
  header = YOUTH_HEADER
  readBody = YOUTH_READBODY
  redBody = YOUTH_REDBODY
  readTimeBody = YOUTH_READTIMEBODY
  shareBody=YOUTH_SHAREBODY
  withdrawBody=YOUTH_WITHDRAWBODY

  rotaryBody = f'{header["Referer"].split("&")[15]}&{header["Referer"].split("&")[8]}'
  sign_res = sign(header=header)
  if sign_res and sign_res['status'] == 1:
    content += f'【签到结果】成功 🎉 明日+{sign_res["nextScore"]}青豆'
  # elif sign_res and sign_res['status'] == 2:
  #   # send(title=title, content=f'【账户{i+1}】Cookie已过期，请及时重新获取')
  #   continue

  sign_info = signInfo(headers=header)
  if sign_info:
    content += f'\n【账号】：{sign_info["user"]["nickname"]}'
    content += f'\n【签到】+{sign_info["sign_score"]}青豆 已连签{sign_info["sign_day"]}天'
    result += f'【账号】: {sign_info["user"]["nickname"]}'
  friendList(headers=header)
  if hour > 12:
    punch_card_res = punchCard(headers=header)
    if punch_card_res:
      content += f'\n【打卡报名】打卡报名{punch_card_res["msg"]} ✅'
  if hour >= 5 and hour <= 8:
    do_card_res = doCard(headers=header)
    if do_card_res:
      content += f'\n【早起打卡】{do_card_res["card_time"]} ✅'
  luck_draw_res = luckDraw(headers=header)
  if luck_draw_res:
    content += f'\n【七日签到】+{luck_draw_res["score"]}青豆'
  visit_reward_res = visitReward(body=readBody)
  if visit_reward_res:
    content += f'\n【回访奖励】+{visit_reward_res["score"]}青豆'
  if shareBody:
    shareArticle(headers=header, body=shareBody)
    for action in ['beread_extra_reward_one', 'beread_extra_reward_two', 'beread_extra_reward_three']:
      time.sleep(5)
      threeShare(headers=header, action=action)

  open_box_res = openBox(headers=header)
  if open_box_res:
    content += f'\n【开启宝箱】+{open_box_res["score"]}青豆 下次奖励{open_box_res["time"] / 60}分钟'
  watch_ad_video_res = watchAdVideo(headers=header)
  if watch_ad_video_res:
    content += f'\n【观看视频】+{watch_ad_video_res["score"]}个青豆'
  watch_game_video_res = watchGameVideo(body=readBody)
  if watch_game_video_res:
    content += f'\n【激励视频】{watch_game_video_res["score"]}个青豆'
  article_red_res = articleRed(body=redBody)
  if article_red_res:
    content += f'\n【惊喜红包】+{article_red_res["score"]}个青豆'
  read_time_res = readTime(body=readTimeBody)
  if read_time_res:
    content += f'\n【阅读时长】共计{read_time_res["time"] // 60}分钟'
  if (hour >= 6 and hour <= 8) or (hour >= 11 and hour <= 13) or (hour >= 19 and hour <= 21):
    beread_red_res = bereadRed(headers=header)
    if beread_red_res:
      content += f'\n【时段红包】：+{beread_red_res["score"]}个青豆'
  for i in range(0, 5):
    time.sleep(5)
    rotary_res = rotary(headers=header, body=rotaryBody)
    if rotary_res:
      if rotary_res['status'] == 0:
        break
      elif rotary_res['status'] == 1:
        content += f'\n【转盘抽奖】+{rotary_res["data"]["score"]}个青豆 剩余{rotary_res["data"]["remainTurn"]}次'
        if rotary_res['data']['doubleNum'] != 0:
          double_rotary_res = doubleRotary(headers=header, body=rotaryBody)
          if double_rotary_res:
            content += f'\n【转盘双倍】+{double_rotary_res["score"]}青豆 剩余{double_rotary_res["doubleNum"]}次'

  rotaryChestReward(headers=header, body=rotaryBody)
  for i in range(5):
    watchWelfareVideo(headers=header)
  timePacket(headers=header)
  for action in ['watch_article_reward', 'watch_video_reward', 'read_time_two_minutes', 'read_time_sixty_minutes',
                 'new_fresh_five_video_reward', 'first_share_article']:
    time.sleep(5)
    sendTwentyScore(headers=header, action=action)
  stat_res = incomeStat(headers=header)
  if stat_res['status'] == 0:
    for group in stat_res['history'][0]['group']:
      content += f'\n【{group["name"]}】：+{group["money"]}青豆'
    today_score = int(stat_res["user"]["today_score"])
    score = int(stat_res["user"]["score"])
    total_score = int(stat_res["user"]["total_score"])

    if score >= 100000 and withdrawBody:
      with_draw_res = withdraw(body=withdrawBody)
      if with_draw_res:
        result += f'\n【自动提现】：发起提现10元成功'
        content += f'\n【自动提现】：发起提现10元成功'
        # send(title=title, content=f'【账号】: {sign_info["user"]["nickname"]} 发起提现30元成功')
    result += f'\n【今日收益】+{"{:4.2f}".format(today_score / 10000)}'
    content += f'\n【今日收益】+{"{:4.2f}".format(today_score / 10000)}'
    result += f'\n【账户剩余】{"{:4.2f}".format(score / 10000)}'
    content += f'\n【账户剩余】{"{:4.2f}".format(score / 10000)}'
    result += f'\n【历史收益】{"{:4.2f}".format(total_score / 10000)}\n\n'
    content += f'\n【历史收益】{"{:4.2f}".format(total_score / 10000)}\n'
  else:
    pass
  print(content)

  # 每天 23:00 发送消息推送
#   if beijing_datetime.hour == 23 and beijing_datetime.minute >= 0 and beijing_datetime.minute < 5:
#     send(title=title, content=result)
#   elif not beijing_datetime.hour == 23:
#     print('未进行消息推送，原因：没到对应的推送时间点\n')
#   else:
#     print('未在规定的时间范围内\n')

if __name__ == '__main__':
    run()
