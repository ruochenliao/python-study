import hashlib
import time
import requests

# 配置参数
token = 'd77543b8-3e33-4780-bfa3-d213b88b33bb'
app_name = 'hrmd-test'
timestamp = str(int(time.time()))
signature_input = app_name + token + timestamp
hrgw_signature = hashlib.sha256(signature_input.encode('utf-8')).hexdigest()

# 设置请求头
headers = {
    'hrgw-appname': app_name,
    'hrgw-timestamp': timestamp,
    'hrgw-signature': hrgw_signature
}

# 请求体
data = {
    "timeZone": "Asia/Shanghai",
    "pageIndex": None,
    "countDisabled": False,
    "pagingDisabled": False,
    "pageSize": None,
    "timeout": 30,
    "queryCondition": {
        "type": "WHERE_SQL",
        "argMap": {
            "hrStatusIdList": [1, 3]
        },
        "whereSql": "",
        "dollarReplaceMap": None,
        "appendConditionList": None,
        "limit": None,
        "prevId": None,
        "genRowMd5": False,
        "fullPull": False,
        "sequenceNo": None,
        "dbKey": None,
        "dataScopeRightQuery": None,
        "dataScopeRightQueryList": None,
        "nulls": None,
        "userOrderBys": None,
        "userSelectList": None,
        "version": None,
        "test": False
    },
    "needQueryCountWithoutGrant": None
}

# 发送 POST 请求
url = 'http://uat-ntsgw.woa.com/api/esb/dos-interface-server/open-api/config/hrmd/md-api-public-core-staff-info/hrmd-test/data'
response = requests.post(url, json=data, headers=headers)
staff_id_set = {"hello_world"}
res = response.json()
for item in res['data']['content']:
    if item['staffId'] in staff_id_set:
        print(item['staffId'] + ' 重复 ' + item['staffName'])

    staff_id_set.add(item['staffId'])
print("prevId= " + str(res['data']['prevId']))

while res['data']['hasNext']:
    data['queryCondition']['prevId'] = res['data']['prevId']
    response = requests.post(url, json=data, headers=headers)
    res = response.json()

    for item in res['data']['content']:
        if item['staffId'] in staff_id_set:
            print(item['staffId'] + ' 重复 ' + item['staffName'])
        else:
            staff_id_set.add(item['staffId'])

    print("prevId= " + str(res['data']['prevId']))

print("没有重复")