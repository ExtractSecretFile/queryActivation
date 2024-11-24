import subprocess

from querylib import query_by_encrypted_sn

machine_code = input("请输入注册码: ")
enc_sn = (
    subprocess.check_output(["./code_to_key"], input=machine_code.encode())
    .decode("utf-8")
    .strip()
)

print("将查询授权码:", enc_sn)
query_by_encrypted_sn(enc_sn)
