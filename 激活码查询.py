import requests
import json

activation_code = input("请输入激活码: ")

response = requests.post(
    "http://8.134.130.103:8000/validate",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"serial_number": activation_code}),
    timeout=10,
)

data = response.json()

if "error" in data and data["error"]:
    print("激活码不存在")
elif "used" in data:
    if data["used"]:
        machine_code = data["regkey"]
        regtime = data["regtime"]
        print(f"已激活：{machine_code}")
        print(f"激活于：{regtime}")
    else:
        print("未激活")
else:
    print("未知错误")
