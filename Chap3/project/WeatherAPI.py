# coding:utf-8
import requests

  
# 用requests导入api，与api进行交互
def fetch_weather(location):  
    result = requests.get('https://api.seniverse.com/v3/weather/now.json',
                          params={'key':'vs1u8pv7mvsi6xj8',
                                  'location': location,
                                  'language': 'zh-Hans',
                                  'unit':'c'}, timeout= 5)
    return result.json()
# print(fetch_weather('北京'))

def show_weather(location):
    weather_dic = fetch_weather(location) # 调用 fetcht_weather 
    # 抓取 api 里面的内容
    
    name = weather_dic['results'][0]['location']['name']
    text = weather_dic['results'][0]['now']['text']
    temp = weather_dic['results'][0]['now']['temperature']
    last_update = weather_dic['results'][0]['last_update']
    # 封装到 weather 
    weather = f"""{name} 的天气为 {text}, 温度为 {temp} 摄氏度.\n更新时间: {last_update}\n"""
    
    return weather
