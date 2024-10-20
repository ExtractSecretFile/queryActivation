from querylib import query_by_activation_code

activation_code = input("请输入激活码: ")
result = query_by_activation_code(activation_code)
print(activation_code, result)
