from openai import OpenAI

client = OpenAI(api_key="sk-2753fd79ea1143a3af3abc6d4a241c6f", base_url="http://127.0.0.1:1234/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你好吗"},
    ],
    stream=False
)

print(response.choices[0].message.content)