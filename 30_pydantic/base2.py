import json

# 内存中的对象
user = {"name": "Alice", "age": 30, "score": 99.5}

# --- 序列化：对象 -> JSON字符串（可存储/传输）---
json_string = json.dumps(user)
print(f"序列化后的JSON字符串: {json_string}")
print(f"序列化后的JSON字符串类型: {type(json_string)}")
# 输出: {"name": "Alice", "age": 30, "score": 99.5}

# 通常我们会把这个字符串写入文件
with open("user.json", "w") as f:
    f.write(json_string)

# --- 反序列化：JSON字符串 -> 对象 ---
# 从文件读取JSON字符串
with open("user.json", "r") as f:
    read_json_string = f.read()

# 还原成Python字典对象
restored_user = json.loads(read_json_string)
print(f"反序列化后得到的对象: {restored_user}")
# 输出: {'name': 'Alice', 'age': 30, 'score': 99.5}

# 验证它是不是真的对象
print(type(restored_user))  # <class 'dict'>
print(restored_user["name"])  # Alice
