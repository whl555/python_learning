import requests
import pandas as pd
import json

def excel_to_json(excel_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file, header=None, names=['userName', 'userAvatar', 'comment']).iloc[1:]

    # 创建一个空列表来存储结果
    result = []

    # 遍历每一行数据
    for _, row in df.iterrows():
        user_data = {
            "userName": row['userName'],
            "userAvatar": row['userAvatar'],
            "comment": row['comment']
        }
        result.append(user_data)

    # 转换为JSON格式
    return result  # 返回是一个Python对象而非JSON字符串

# 设置基本参数
id_value = 5941
created_time = 1734426820600
updated_time = 1734426820611
key_id = 983
active_history_id = 39144
excel_file = '/Users/wuhaolei/work/python/new_teacher.xlsx'
content = {
    "comments": excel_to_json(excel_file)
}
online_status = "OFFLINE"
start_time = 1734426812268
end_time = 2049786812268
priority = 0
created_by = "wuhaolei"
auditing_show_status = "SHOW"
cookie_value = 'fp=7f1c590237f6e245555f62b7adef05c5; ajs_user_id=a88755bd37230f6790e45ff881ba5aadc35eb24b; ajs_anonymous_id=ae03bb1f-5f35-4d5a-ac81-02b09655333a; _ga=GA1.2.1413996143.1728542807; _ga_7LKYHYLGRE=GS1.2.1728542807.1.0.1728542807.0.0.0; SESS=x3jAsbI5dZ3v2NZnCyfwW9E0odoNwO58jA%2Fek67en3sFvr7fVVMHbT04vK9Xs3J4; SESS_V2=Mogfe7RFybERi%2FffEr6ED2q0RJYPAk0FjVD2EVyR3jT90TKhRYEd4krH%2BNwbEBCz2IOirX7SIrjzW9CjeA%2FF8XRGIeMbBN916I3bsTaXjeBVzUoXOgdmKEEqXDXv9KzqJDGC3w8rnrMI4UI7vN2NAIEhAT%2Bkf3E60f8vT2SxPTI%3D'

# 设置头文件
headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': cookie_value,
    'origin': 'https://switch.zhenguanyu.com',
    'priority': 'u=1, i',
    'referer': 'https://switch.zhenguanyu.com/config/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# 设置URL
url = 'https://switch.zhenguanyu.com/orion-hubble-config-admin/api/values/5941'

# 创建数据
data_to_send = {
    "id": id_value,
    "createdTime": created_time,
    "updatedTime": updated_time,
    "keyId": key_id,
    "baseValueId": 0,
    "activeHistoryId": active_history_id,
    "name": "老师弹幕",  
    "content": json.dumps(content, ensure_ascii=False),  # JSON stringify the content.
    "onlineStatus": online_status,
    "startTime": start_time,
    "endTime": end_time,
    "priority": priority,
    "filterIds": [],
    "filterNames": [],
    "createdBy": created_by,
    "iosAuditingShowStatus": auditing_show_status,
    "androidAuditingShowStatus": auditing_show_status,
    "harmonyAuditingShowStatus": auditing_show_status,
    "time": [start_time, end_time]
}


def main():
    # 发送请求
    response = requests.put(url, headers=headers, data=json.dumps(data_to_send, ensure_ascii=False))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == '__main__':
    main()
