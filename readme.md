## 定义

机器码：未经加密。客户运行脚本第一行可以看到的9位机器码

授权码：机器码运行 code_to_key 输入之后得到的授权激活密码

激活码：在线服务器注册，可以对应单个的授权码

## 脚本环境准备

因IP地理位置查询功能需要，在最近版本中已加入从 ipipfree.db 查询地理位置

首次使用前需要创建虚拟环境，因 ubuntu/kylin 不同版本的python3版本不同，可运行：

```bash
bash create_env.sh
```

若看到报错 apt install python3.XX-venv ，则

```bash
sudo apt-get install ...
# ...为复制过来的python3.XX-venv
```


方可再次运行上述命令，创建环境

运行其他脚本前，每次需要先加载环境：

```bash
source load_env.sh
```

## 脚本解释

query-*.py 为查询脚本，其中：

| 名称             | 用法                                                             |
| ---------------- | ---------------------------------------------------------------- |
| query-batch.py   | `python3 query-batch.py [文本文件位置]`<br>（不带方括号）        |
| query-single.py  | `python3 query-single.py` <br>输入激活码，查询授权码、IP、时间   |
| query-rev.py     | `python3 query-rev.py` <br>输入授权码，查询激活码、IP、时间      |
| query-rev-enc.py | `python3 query-rev-enc.py ` <br>输入机器码，查询激活码、IP、时间 |

由于使用了免费数据库，若需细查IP位置请使用 [ipip.net](https://www.ipip.net/)