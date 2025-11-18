import requests

params = {"a": "j", "encode": "json", "charset": "utf-8"}
response = requests.get("https://v1.hitokoto.cn", params=params)

print(response.json())

if response.status_code == 200:
    data = response.json()
    hitokoto = data.get("hitokoto")
    from_who = data["from_who"] if data["from_who"] else "未知"
    print(f"{hitokoto} - {from_who}")
