from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
import uvicorn
import requests


async def get_hitokoto():
    try:
        params = {"a": "j", "encode": "json", "charset": "utf-8"}
        response = requests.get("https://v1.hitokoto.cn", params=params)
        status_code = response.status_code
        if status_code == 200:
            data = response.json()
            hitokoto = data.get("hitokoto")
            from_who = data.get("from_who") if data.get("from_who") else "未知"
            return {"hitokoto": hitokoto, "from_who": from_who}
        elif status_code == 404:
            return {"error": "请求接口不存在"}
        else:
            return {"error": "请求一言接口失败"}
    except Exception as e:
        return {"error": f"其他错误：{str(e)}"}


async def homepage(request):
    result = await get_hitokoto()
    return JSONResponse(result)


app = Starlette(routes=[Route("/", homepage)])
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8899)
