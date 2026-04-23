import os
from openai import OpenAI

#构造与大模型交互的客户端对象(DEEPSEEK_API_KEY环境变量的名字)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")


#与大模型进行交互()
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant,you name is 园园"},
        {"role": "user", "content": "你叫啥名字,你可以做什么呢？"},
    ],
    stream=False
)


#输出大模型返回的结果
print(response.choices[0].message.content)