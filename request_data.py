import sys
import requests
import time
import random
import hashlib

phone_brand_type_list =list(["MI","Huawei","Zhonxin","Meizu","OPPO","VIVO"]) #随机设备厂商
phone_brand_sign_list =list(["AHCE","ACGS","VGES","EDSX","WZSD","ERCA"])
device_code_random = random.randint(111,987)#随机设备识别码
device_code_random_str = str(device_code_random)
phone_brand_type_random = random.choice(phone_brand_type_list) #随机设备厂商
phone_brand_sign_random = random.choice(phone_brand_sign_list)
def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

def md5GBK(str1):
    m = hashlib.md5(str1.encode(encoding='gb2312'))
    return m.hexdigest()

def Sign_in(username,password):    
    sign_in_url="http://floor.huluxia.com/account/login/ANDROID/4.0?platform=2&gkey=000000&app_version=4.1.0.2&versioncode=20141445&market_id=floor_baidu&_key=&device_code=%5Bd%5Db04ce125-e22f-"+device_code_random_str+"d-a924-761be53db385"
    headers = {
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.8.1',
    }
    password_md5 = md5(password)
    sign_in_data="account="+username+"&login_type=2&password="+password_md5
    sign_in_return_json = requests.post(sign_in_url,headers=headers,data=sign_in_data).json()
    if sign_in_return_json['msg'] == "账号或密码错误":
        print(sign_in_return_json['msg'])
        sys.exit() 
    elif sign_in_return_json['msg'] == "":    
        print("登录成功!用户名："+sign_in_return_json['user']['nick'])
        key_txt = open('key.txt',mode='w')
        key_txt.write(sign_in_return_json['_key'])
        key_txt.close
        user_id_txt = open('user_id.txt',mode='w')
        user_id_txt.write(str(sign_in_return_json['user']["userID"]))
        user_id_txt.close
        return sign_in_return_json['_key']      
    elif sign_in_return_json['msg'] == "参数不合法":    
        print(sign_in_return_json['msg'])
        sys.exit() 
    else:
        print("未知错误,联系作者棉花糖1113335577")
        sys.exit() 

def experience_sign():  
    key = open("key.txt").read()  
    headers = {
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.8.1',
    }
    plate = {'44':'玩机教程','16':'玩机广场',"43":"实用软件","81":"手机美化","45":"原创技术","96":"技术分享","70":"福利活动","111":"Steam","4":"游戏","29":"次元阁","102":"LOL手游","71":"王者荣耀","105":"DNF手游","107":"三两影","90":"和平精英","115":"金铲铲之战","112":"使命召唤手游","21":"穿越火线","117":"幻塔","110":"原神","101":"跑跑卡丁车","56":"清凉一夏","3":"自拍","88":"QQ飞车","76":"娱乐天地","57":"头像签名","92":"模型玩具","98":"制图工坊","58":"恶搞","82":"3楼学院","77":"球球大作战","63":"我的世界","22":"英雄联盟","23":"地下城与勇士","113":"摩尔庄园手游","103":"明日之后","2":"泳池","108":"新游推荐","116":"骑士团"}                                                                                                                                                            

    for id,val in plate.items() :      
        experience_sign_url = "http://floor.huluxia.com/user/signin/ANDROID/4.0?platform=2&gkey=000000&app_version=4.1.0.9&versioncode=20141462&market_id=floor_tencent&_key="+key+"&device_code=%5Bd%5D55bccbf4-0"+device_code_random_str+"-45a6-8cab-80c000115fab&phone_brand_type="+phone_brand_type_random+"&cat_id="+ id
 
        time.sleep(1)
        sign_in_return_json = requests.get(experience_sign_url,headers=headers).json()
        if sign_in_return_json['msg'] == "":
            print(val+"板块签到成功，经验值+"+ str(sign_in_return_json['experienceVal']))
        else:
            print("未知错误,联系作者棉花糖1113335577")
            sys.exit() 
            
def exp_time():
    key = open("key.txt").read()
    user_id = open("user_id.txt").read()  
    headers = {
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'okhttp/3.8.1',
    }

    experience_sign_url = "http://floor.huluxia.com/user/info/ANDROID/2.1?platform=2&gkey=000000&app_version=4.1.0.9&versioncode=20141462&market_id=floor_tencent&_key="+key+"&device_code=%5Bd%5D55bccbf4-0"+device_code_random_str+"-45a6-8cab-80c000115fab&phone_brand_type=MI&user_id="+user_id
    time.sleep(1)
    sign_in_return_json = requests.get(experience_sign_url,headers=headers).json()
    if sign_in_return_json['msg'] == "":
        exp_late = sign_in_return_json['nextExp']-sign_in_return_json['exp']
        exp_late_time = exp_late/1950
        print("当前经验值为："+ str(sign_in_return_json['exp'])+",下一级所需经验值："+str(sign_in_return_json['nextExp'])+",还需要签到"+str(exp_late_time)+"天")
    else:
        print("未知错误,联系作者棉花糖1113335577")
        sys.exit() 


if __name__ == "__main__":
    username = "**********"
    password = "1113335577"
    Sign_in(username,password)
    experience_sign()
    exp_time()