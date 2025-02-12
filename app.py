from flask import Flask

# 創建 Flask 應用
app = Flask(__name__)

# 設置路由和視圖函數
@app.route('/')
def hello():
    return "Hello, Flask!"

# 啟動應用
if __name__ == '__main__':
    app.run(debug=True)
