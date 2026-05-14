from fastapi import FastAPI

# 创建FastAPI的实例
app = FastAPI()

# 定义api接口--->该函数的返回值表示 API接口的返回数据
@app.get("/")    # 定义接口路径
def root():
    return {"message": "Hello World"}   # 返回一个字典

#定义api接口
@app.get("/items/{item_id}")     # 定义接口路径
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# 启动服务---uvicorn:Python 当中的轻量级Web服务器
if __name__ == "__main__":
    import uvicorn   # 启动服务
    uvicorn.run(app, host="127.0.0.1", port=8000)   # host: 127.0.0.1 --> 监听本机  port: 8000 --> 监听的端口