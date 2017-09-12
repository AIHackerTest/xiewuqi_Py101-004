from flask import Flask
from WeatherAPI import show_weather

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '这个函数怎么写'
        
if __name__ == '__main__':
    app.run(debug = True)
    
    