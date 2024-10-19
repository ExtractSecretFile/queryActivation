import sys

from query import query_by_activation_code

filename = sys.argv[1]
with open(filename, encoding="utf-8") as f:
    content = f.read()

alnums = "".join(c for c in content if c.isalnum()).lower()
length = 8

while alnums:
    key = alnums[:8]
    alnums = alnums[8:]
    info = query_by_activation_code(key)
    print(key, info)
