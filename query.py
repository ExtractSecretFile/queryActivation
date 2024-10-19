import os
import json
import requests

import ipdb

db = ipdb.City("db/ipipfree.ipdb")

BASE_URL = os.environ.get("ESF_BASE_URL", "http://8.134.130.103:8000")


def ip_location(ip: str):
    if ip is None:
        return "未知"

    ip_info = db.find_info(ip, "CN")
    region = ip_info.region_name

    if region == "本机地址":
        return region

    city = ip_info.city_name
    return f"{region}省{city}市"


def query_by_activation_code(activation_code):
    response = requests.post(
        f"{BASE_URL}/validate",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"serial_number": activation_code}),
        timeout=10,
    )

    data = response.json()

    if "error" in data and data["error"]:
        print(data)
        return "激活码不存在"
    elif "used" in data:
        if data["used"]:
            machine_codes = data["regkey"]
            reg_times = data.get("regtime", None)
            source_ips = data.get("source_ip", None)

            results = []
            for machine_code, reg_time, source_ip in zip(
                machine_codes, reg_times, source_ips
            ):
                location = ip_location(source_ip)
                results.append(
                    f"已激活: {machine_code} 激活于: {reg_time} 位置: {location} IP: {source_ip}"
                )

            return "\n".join(results)
        else:
            return "未激活"
    else:
        return "未知错误"


def query_by_encrypted_sn(sn):
    response = requests.post(
        f"{BASE_URL}/reverse",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"registeration_code": sn}),
        timeout=None,
    )

    data = response.json()

    if "error" in data and data["error"]:
        print("注册码未激活")
    elif "serial_number" in data:
        sn = data["serial_number"]
        reg_time = data.get("register_time", None)
        source_ip = data.get("source_ip", None)
        location = ip_location(source_ip)
        if sn:
            print(f"激活码: {sn}")
            print(f"注册于: {reg_time}")
            print(f"位置: {location}")
            print(f"IP: {source_ip}")
        else:
            print("未注册")
    else:
        print("未知错误")
