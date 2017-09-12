# cding:utf-8

# 把数据字典化
dict = {}

with open("weather_info.txt") as f: # 打开文件
    for line in f: # 读取每行文件
        (key, val) = line.split(',') # 把文件转换为字典
        dict[key] = val 
    
        
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
              输入help，显示帮助文档；
              输入history，显示查询历史；
              输入quit，退出程序
             ''')
     # 查询天气功能       
    elif user_input in dict.keys():
        weather = '{}的天气是：{}'.format(user_input,dict[user_input])
        print(weather)
        history.append(weather)
    # history 功能   
    elif user_input == 'history':
        for item in history:
            print(item)
        
    else:
        print("命令错误")
        

    




        