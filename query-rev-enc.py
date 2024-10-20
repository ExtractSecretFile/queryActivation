import subprocess

from querylib import query_by_encrypted_sn

machine_code = input("请输入注册码: ")
enc_sn = (
    subprocess.check_output(["sh", "-c", f"echo {machine_code} | ./code_to_key"])
    .decode("utf-8")
    .strip()
)

query_by_encrypted_sn(enc_sn)
