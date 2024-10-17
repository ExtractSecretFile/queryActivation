import json
import requests
import subprocess

machine_code = input("请输入注册码: ")
enc_sn = (
    subprocess.check_output(["sh", "-c", f"echo {machine_code} | ./code_to_key"])
    .decode("utf-8")
    .strip()
)

response = requests.post(
    "http://8.134.130.103:8000/reverse",
    headers={"Content-Type": "application/json"},
    data=json.dumps({"registeration_code": enc_sn}),
    timeout=None,
)

data = response.json()

if "error" in data and data["error"]:
    print("注册码未激活")
elif "serial_number" in data:
    sn = data["serial_number"]
    reg_time = data["register_time"]
    if sn:
        print(f"激活码：{sn}")
        print(f"注册于：{reg_time}")
    else:
        print("未注册")
else:
    print("未知错误")
