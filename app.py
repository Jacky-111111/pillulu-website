from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 示例 POST 路由
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('message')
    return f"你说：{user_input}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
