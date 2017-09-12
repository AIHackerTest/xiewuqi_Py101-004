# coding:utf-8
import requests
  
# 用requests导入api，与api进行交互
def fetch_weather(location):  
    result = requests.get('https://api.seniverse.com/v3/weather/now.json',
                          params={'key':'vs1u8pv7mvsi6xj8',
                                  'location': location,
                                  'language': 'zh-Hans',
                                  'unit':'c'}, timeout=10)
    return result.json()
    

def show_weather(location):
    weather_dic = fetch_weather(location) # 调用 fetcht_weather 函数
    # 抓取 api 里面的内容
    name = weather_dic['results'][0]['location']['name']
    text = weather_dic['results'][0]['now']['text']
    temp = weather_dic['results'][0]['now']['temperature']
    last_update = weather_dic['results'][0]['last_update']
    # 封装到 weather 
    weather = f"""{name} 的天气为 {text}, 温度为 {temp} 摄氏度.
        \n更新时间: {last_update}\n"""
    
    return weather
    
    # 如过 location 不是城市名，则程序报错怎么写。
    
    
def play():
    history = []

    while True:
        user_input = input('请输入指令：')
    
        if user_input == 'quit' or user_input == 'q':
            print("退出程序")
            exit(0)
            # help 功能    
        elif user_input == 'help' or user_input == 'h': 
            print('''
                  输入城市名，查询该城市的天气；
                  输入help or h，显示帮助文档；
                  输入history ，显示查询历史；
                  输入quit or q，退出程序。
                  ''')        
            # history 功能   
        elif user_input == 'history':
            for item in history:
                print(item)
        else:
           # 这里请求api，返回天气信息，输出
            print(show_weather(user_input))
            history.append(show_weather(user_input))
        
play()





        