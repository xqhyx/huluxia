import time
import request_data


username = "18********7" #此处填写登录的手机号
password = ""        #此处填写密码

request_data.Sign_in(username,password)#登录
while True:
    request_data.experience_sign()#签到
    request_data.exp_time()#查询经验
    time.sleep(60*60*24)#24小时执行一次



