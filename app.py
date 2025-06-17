from flask import Flask, render_template, request, jsonify
import httpx
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client with custom configuration
API_KEY = os.getenv("OPENAI_API_KEY")
API_BASE = os.getenv("OPENAI_API_BASE", "https://sat1600ap5.online/proxy/openai/v1")

if not API_KEY:
    raise ValueError("No OpenAI API key found. Please set OPENAI_API_KEY in .env file")

http_client = httpx.Client(
    base_url=API_BASE,
    headers={"Authorization": f"Bearer {API_KEY}"}
)
client = OpenAI(
    api_key=API_KEY,
    http_client=http_client
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_medicine_info', methods=['POST'])
def get_medicine_info():
    medicine_name = request.json.get('medicine_name')
    if not medicine_name:
        return jsonify({'error': 'No medicine name provided'}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """你是一个智能药物管家叫Pillulu，用户将提供药物的名称。你的任务是从权威来源中搜索相关信息，包括：

- FDA
- 国家药监局（NMPA）
- 药典数据库
- Drugs.com

⚠️ 如果以上来源都找不到，再考虑其他来源，但务必说明。

请以以下统一格式输出内容，不使用 Markdown，不要加星号或其他符号。字段之间空一行即可：

药物名称：  
别名/商品名：  
生产厂家：  
剂型/规格：  
主要用途：  
推荐剂量：  
不适用人群：  
服药建议：  
注意事项：  

资料来源：请列出你使用的数据库或网站名称（如 FDA、Drugs.com 等）。

如果找不到该药物的信息，请明确说明："未找到来自权威数据库的匹配信息，以下内容来自其他资料，准确性需核实。"

注意：内容应清晰、简洁、无花哨修饰，仅提供客观药物信息。"""
                },
                {
                    "role": "user",
                    "content": medicine_name
                }
            ]
        )
        return jsonify({'response': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


