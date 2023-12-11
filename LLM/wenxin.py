import requests
import json
#修改成自己的api key和secret key
API_KEY = ""
SECRET_KEY = ""
 
 
def wenxin(s1,s2):
    history_baidu=[]
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    # 注意message必须是奇数条
    history_baidu.append({
            "role": "user",
            "content": s1
        })
    payload = json.dumps({
    "messages":history_baidu 
    })
    headers = {
            'Content-Type': 'application/json'
        }
    res = requests.request("POST", url, headers=headers, data=payload).json()['result']
    history_baidu.append({
        "role":"assistant",
        "content":res
    })
    history_baidu.append({
            "role": "user",
            "content": s2
    })
    payload = json.dumps({
    "messages":history_baidu 
    })
    headers = {
            'Content-Type': 'application/json'
    }
    res2 = requests.request("POST", url, headers=headers, data=payload).json()['result']
    return [res,res2] 
 
 
 
 
def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
 

