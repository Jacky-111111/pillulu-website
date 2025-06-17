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
                    "content": "你是一个智能药物管家帮忙提供药物信息，根据用户给你的药物名称，搜索权威来源（FDA、药监局公开数据库、药典、Drugs.com）来给出药物名称、别名/商品名、生产厂家、剂型/规格、主要用途、推荐剂量、不适用人群、服药建议、注意事项等。"
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


