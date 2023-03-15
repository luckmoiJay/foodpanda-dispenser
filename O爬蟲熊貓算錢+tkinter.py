import tkinter as tk
from tkinter.constants import *
import requests
import json
import pandas as pd
import numpy

def plus():
    print("你點擊了按鈕")
'''
餐廳名稱: 台北永和豆漿 (台中霧峰店)
下單時間: 2023-01-05 02:10:53
訂單完成時間: 2023-01-05 02:28:11
地址: 413 Taichung City 柳豐一街 78
order_code: i7ja-ufgd
餐點: 冰紅茶 20
餐點: 韭菜盒 30
餐點: 蘑菇鐵板麵 100
餐點: 豆漿【熱】 20
餐點: 花生酥餅 18
小計: 188
總價格: 188
折扣 0
付款方式:信用卡
'''

order_1_title_text = ''
order_2_title_text = ''
order_3_title_text = ''
order_4_title_text = ''
order_5_title_text = ''
order_6_title_text = ''
order_7_title_text = ''
order_8_title_text = ''
order_1_money_text = ''
order_2_money_text = ''
order_3_money_text = ''
order_4_money_text = ''
order_5_money_text = ''
order_6_money_text = ''
order_7_money_text = ''
order_8_money_text = ''
restaurant_name_text = ''
order_time_text = ''
order_completion_time_text = ''
order_address_text = ''
order_code_text = ''
subtotal_text = ''
total_text = ''
discount_text = ''
payment_type_text = ''
time = -1
def out ():
    reset()
    restaurant_name['text'] = (data['餐廳名稱'][time])
    order_time['text'] = (data['下單時間'][time])
    order_completion_time['text'] = (data['訂單完成時間'][time])
    order_address['text'] = (data['地址'][time])
    subtotal['text'] = (data['小計'][time])
    total['text'] = (data['總價格'][time])
    discount['text'] = (data['折扣'][time])
    common['text'] = (data['折扣'][time]/2)
    payment_type['text'] = (data['付款方式'][time])
    cont['text'] = ('第'+str(time+1)+'單')
    # order
    try:
        order_1_title['text'] =  ('1.'+data['餐點'][time][0])
        order_2_title['text'] =  ('2.'+data['餐點'][time][1])
        order_3_title['text'] =  ('3.'+data['餐點'][time][2])
        order_4_title['text'] =  ('4.'+data['餐點'][time][3])
        order_5_title['text'] =  ('5.'+data['餐點'][time][4])
        order_6_title['text'] =  ('6.'+data['餐點'][time][5])
        order_7_title['text'] =  ('7.'+data['餐點'][time][6])
        order_8_title['text'] =  ('8.'+data['餐點'][time][7])
    except:
        pass
    try:
        order_1_money['text'] =  (data['餐點價格'][time][0])
        order_2_money['text'] =  (data['餐點價格'][time][1])
        order_3_money['text'] =  (data['餐點價格'][time][2])
        order_4_money['text'] =  (data['餐點價格'][time][3])
        order_5_money['text'] =  (data['餐點價格'][time][4])
        order_6_money['text'] =  (data['餐點價格'][time][5])
        order_7_money['text'] =  (data['餐點價格'][time][6])
        order_8_money['text'] =  (data['餐點價格'][time][7])
    except:
        pass

    print ('out執行成功')

def reset():
    order_1_title['text'] =  ('')
    order_2_title['text'] =  ('')
    order_3_title['text'] =  ('')
    order_4_title['text'] =  ('')
    order_5_title['text'] =  ('')
    order_6_title['text'] =  ('')
    order_7_title['text'] =  ('')
    order_8_title['text'] =  ('')

    order_1_money['text'] =  ('')
    order_2_money['text'] =  ('')
    order_3_money['text'] =  ('')
    order_4_money['text'] =  ('')
    order_5_money['text'] =  ('')
    order_6_money['text'] =  ('')
    order_7_money['text'] =  ('')
    order_8_money['text'] =  ('')

def next():
    global time
    time += 1
    out()
    whos()
    print('------------------------------')

def last():
    global time
    time -= 1
    out()
    whos()
    print('------------------------------')


def Jays():
    print('小杰的')

def Wans():
    print('挽挽的')

def whos():
    Jay = 0
    Wan = 0
    whos_list = [radioVar1.get(),radioVar2.get(),radioVar3.get(),radioVar4.get(),radioVar5.get(),radioVar6.get(),radioVar7.get(),radioVar8.get()]
    print (whos_list)
    
    for num in whos_list:
        if num ==0:
            pass
        elif num%2 != 0:
            try:
                print((data['餐點'][time-1][(whos_list.index(num))]),'是小杰的')
                to_excel.append([(data['餐廳名稱'][time-1]),(data['餐點'][time-1][(whos_list.index(num))]),int(data['餐點價格'][time-1][(whos_list.index(num))]),(None)])
            except IndexError:
                print('按錯了喔')
        else:
            try:
                print((data['餐點'][time-1][(whos_list.index(num))]),'是挽挽的')
                to_excel.append([(data['餐廳名稱'][time-1]),(data['餐點'][time-1][(whos_list.index(num))]),(None),int(data['餐點價格'][time-1][(whos_list.index(num))])])
            except IndexError:
                print('按錯了喔')
    if sum(whos_list) != 0:
        for num in whos_list:
            if num ==0:
                pass
            elif num%2 != 0:
                Jay += 1
            else:
                Wan += 1
        if Jay >= 1 and Wan >=1:
            to_excel.append([(None),('折扣'),((data['折扣'][time-1]*-1)/2),((data['折扣'][time-1]*-1)/2)])
        elif Jay >= 1 and Wan==0:
            to_excel.append([(None),('折扣'),((data['折扣'][time-1]*-1)),(None)])  
        else:
            to_excel.append([(None),('折扣'),(None),((data['折扣'][time-1]*-1))])
    resetVar()

def resetVar(): 
    try:
        print('清除選項')
    finally :
        radioVar1.set(0) 
        radioVar2.set(0)
        radioVar3.set(0)
        radioVar4.set(0)
        radioVar5.set(0)
        radioVar6.set(0)
        radioVar7.set(0)
        radioVar8.set(0)

def output():
    df = pd.DataFrame(to_excel,columns=['餐廳名稱','項目','小杰的','挽挽的'])
    df.to_excel("熊貓算錢.xlsx",index=False)
    print('輸出成功')
# -----------------------------------------------
window = tk.Tk()
window.title('熊貓貓算錢錢')
window.geometry('800x600')
window.resizable(False, False) #可否自行調整視窗大小
# window.iconbitmap('icon.ico')

# -----------------------------------------------

# 需要先獲取 order_history 裡面的 authorization 頭
url = 'https://tw.fd-api.com/api/v5/orders/order_history?include=order_products,order_details&language_id=6&offset=0&limit=20'
header = {
'accept': 'application/json, text/plain, */*'
,'accept-encoding': 'gzip, deflate, br'
,'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImtleW1ha2VyLXZvbG8tZnAtdHciLCJ0eXAiOiJKV1QifQ.eyJpZCI6IjlnMXptZ3UzcHZkdXI5eWM3cHJjZ3E1eWVhbHRncTh3bm5mbWowbXoiLCJjbGllbnRfaWQiOiJ2b2xvIiwidXNlcl9pZCI6InR3MnU1aTZ2IiwiZXhwaXJlcyI6MTY3Nzc2OTY1MiwidG9rZW5fdHlwZSI6ImJlYXJlciIsInNjb3BlIjoiQVBJX0NVU1RPTUVSIEFQSV9SRUdJU1RFUkVEX0NVU1RPTUVSIn0.X1N28Z66kTWtE-gXZnxD80KG284s2lbwCJzDMypp-ylrbEW-gudrdaLYythkswxBTaYEjQ0NrU7VHA8r-h59nBi5eBKtqGKQn1KSW140WnVcTh_k2-WMFN6zW1pBUCJvbZMvaM6U6jfKuWxTlEmmogC4y6OHW1bOOicGpeTU2kpgB4LxGSxMruBmW0DZIBCQMtf5LXoyhgGH9mvYTOFgYTnJ4KtvbuJHkRweI9SHuSrIViHa1WL7vHK1uNYwp-uZMV1lpvNOMvRSaGIc7OeTVnH3cZH7g45Buv64-nHcp-Yl-CgTDs6JHcUjs-PLiI1qU7-YmfWt37fBzy9R8XFH7A'
# ,'if-modified-since': 'Mon, 13 Feb 2023 17:50:07 GMT'
# ,'origin': 'https://www.foodpanda.com.tw'
# ,'referer': 'https://www.foodpanda.com.tw/'
,'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"'
,'sec-ch-ua-mobile': '?0'
,'sec-ch-ua-platform': '"Windows"'
,'sec-fetch-dest': 'empty'
,'sec-fetch-mode': 'cors'
,'sec-fetch-site': 'cross-site'
,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
,'x-fp-api-key': 'volo'
,'x-pd-language-id': '6'
}
res = requests.get(url,headers=header)
text = (res.text)
text = json.loads(text)


# # -----------------------------------------------
# 資料導入
data = {
    '餐廳名稱':[]
    ,'下單時間':[]
    ,'訂單完成時間':[]
    ,'地址':[]
    ,'order_code':[]
    ,'餐點':[]
    ,'餐點價格':[]
    ,'小計':[]
    ,'總價格':[]
    ,'折扣':[]
    ,'付款方式':[]
}

to_excel = []

pd.Series(data)


print ('連線狀態',res)
item = (text['data']['items'])
for index in item:
    order_list = []
    order_price_list= []
    data['餐廳名稱'].append(index['vendor']['name'])
    data['下單時間'].append(index['ordered_at']['date']) # 訂單完成時間
    data['訂單完成時間'].append(index['confirmed_delivery_time']['date']) # 訂單完成時間
    data['地址'].append(index['order_address']) # 地址
    data['order_code'].append(index['order_code']) # order_code
    order_products = index['order_products'] # 設定餐點for
    for name in order_products:
        order_list.append(name['name']) # 輸出餐點
        order_price_list.append(str(name['total_price'])) # 輸出餐點價格

    data['餐點'].append(order_list) # 
    data['餐點價格'].append(order_price_list) # 

    data['小計'].append(index['subtotal']) # 原始價格
    data['總價格'].append(index['total_value']) # 最終價格
    data['折扣'].append(index['subtotal']-index['total_value']) #折扣 若為負數可能是運費以及袋子
    if index['payment_type_code'] == 'cybersource_creditcard':
        data['付款方式'].append('信用卡')
    else:
        data['付款方式'].append('現金支付')
    

# 選單
output_excel_button = tk.Button(text="output_excel",command=output)
a_button = tk.Button(text="盡情期待",command=plus)
b_button = tk.Button(text="盡情期待",command=plus)
c_button = tk.Button(text="盡情期待",command=plus)
d_button = tk.Button(text="清除選項",command=reset,width=10)
e_button = tk.Button(text="上一單",command=last,width=10)
f_button = tk.Button(text="下一單",command=next,width=10)

# 詳細資料
restaurant_name_title = tk.Label(window,text='餐廳名稱:'
                      ,font='10'
                      ,justify='left')
restaurant_name = tk.Label(window,text=restaurant_name_text
                      ,font='10'
                      ,justify='left')
order_time_title = tk.Label(window,text='下單時間:'
                      ,font='10'
                      ,justify='left')
order_time = tk.Label(window,text=order_time_text
                      ,font='10'
                      ,justify='left')
order_completion_time_title = tk.Label(window,text='訂單完成時間:'
                      ,font='10'
                      ,justify='left')
order_completion_time = tk.Label(window,text=order_completion_time_text
                      ,font='10'
                      ,justify='left')
order_address_title = tk.Label(window,text='地址:'
                      ,font='10'
                      ,justify='left')
order_address = tk.Label(window,text=order_address_text
                      ,font='10'
                      ,justify='left')
payment_type_title = tk.Label(window,text='付款方式:'
                      ,font='10'
                      ,justify='left')
payment_type = tk.Label(window,text=payment_type_text
                      ,font='10'
                      ,justify='left')
cont = tk.Label(window,text='0'
                ,font='10'
                ,justify='left')
# 餐點設置
order_title = tk.Label(window,text='餐點序列:'
                      ,font='10'
                      ,justify='left')

order_1_title = tk.Label(window,text='1.'+order_1_title_text
                      ,font='10'
                      ,justify='left')
order_1_money = tk.Label(window,text='0'
                      ,font='10'
                      ,justify='left')
order_2_title = tk.Label(window,text='2.'+order_2_title_text
                      ,font='10'
                      ,justify='left')
order_2_money = tk.Label(window,text='0'
                      ,font='10'
                      ,justify='left')
order_3_title = tk.Label(window,text='3.'+order_3_title_text
                      ,font='10'
                      ,justify='left')
order_3_money = tk.Label(window,text='0'
                      ,font='10'
                      ,justify='left')
order_4_title = tk.Label(window,text='4.'+order_4_title_text
                      ,font='10'
                      ,justify='left')
order_4_money = tk.Label(window,text='0'
                      ,font='10'
                      ,justify='left')
order_5_title = tk.Label(window,text='5.'+order_5_title_text
                      ,font='10'
                      ,justify='left')
order_5_money = tk.Label(window,text='0'
                      ,font='10'
                      ,justify='left')
order_6_title = tk.Label(window,text='6.'+order_6_title_text
                      ,font='10'
                      ,justify='left')
order_6_money = tk.Label(window,text='0'
                      ,font='10'
                      ,justify='left')
order_7_title = tk.Label(window,text='7.'+order_7_title_text
                      ,font='10'
                      ,justify='left')
order_7_money = tk.Label(window,text='0'
                      ,font='10'
                      ,justify='left')
order_8_title = tk.Label(window,text='8.'+order_8_title_text
                      ,font='10'
                      ,justify='left')
order_8_money = tk.Label(window,text='0'
                      ,font='10'
                      ,justify='left')

# 負擔金額
subtotal_title = tk.Label(window,text='小計:'
                      ,font='10'
                      ,justify='left')
subtotal = tk.Label(window,text=subtotal_text
                      ,font='10'
                      ,justify='left')
total_title = tk.Label(window,text='總價格:'
                      ,font='10'
                      ,justify='left')
total = tk.Label(window,text=total_text
                      ,font='10'
                      ,justify='left')

discount_title = tk.Label(window,text='折扣:'
                      ,font='10'
                      ,justify='left')
discount = tk.Label(window,text='請輸入'
                      ,font='10'
                      ,justify='left')
common_title = tk.Label(window,text='共同:'
                      ,font='10'
                      ,justify='left')
common = tk.Label(window,text='請輸入'
                      ,font='10'
                      ,justify='left')
Jay_money_title = tk.Label(window,text='挽挽的:'
                      ,font='10'
                      ,justify='left')
Jay_money = tk.Label(window,text='請輸入'
                      ,font='10'
                      ,justify='left')
Wan_money_title = tk.Label(window,text='小杰的:'
                      ,font='10'
                      ,justify='left')
Wan_money = tk.Label(window,text='請輸入'
                      ,font='10'
                      ,justify='left')

# 圈圈按鈕
radioVar1 = tk.IntVar()
radioVar2 = tk.IntVar()
radioVar3 = tk.IntVar()
radioVar4 = tk.IntVar()
radioVar5 = tk.IntVar()
radioVar6 = tk.IntVar()
radioVar7 = tk.IntVar()
radioVar8 = tk.IntVar()

Jay_title = tk.Label(window,text='小杰'
                      ,font='10'
                      ,justify='left')
radio1 = tk.Radiobutton(text='',variable=radioVar1, value=1,command=Jays) 
radio3 = tk.Radiobutton(text='',variable=radioVar2, value=3,command=Jays)
radio5 = tk.Radiobutton(text='',variable=radioVar3, value=5,command=Jays)
radio7 = tk.Radiobutton(text='',variable=radioVar4, value=7,command=Jays)
radio9 = tk.Radiobutton(text='',variable=radioVar5, value=9,command=Jays)
radio11 = tk.Radiobutton(text='',variable=radioVar6, value=11,command=Jays)
radio13 = tk.Radiobutton(text='',variable=radioVar7, value=13,command=Jays)
radio15 = tk.Radiobutton(text='',variable=radioVar8, value=15,command=Jays)

Wan_title = tk.Label(window,text='挽挽'
                      ,font='10'
                      ,justify='left')
radio2 = tk.Radiobutton(text='',variable=radioVar1, value=2,command=Wans) 
radio4 = tk.Radiobutton(text='',variable=radioVar2, value=4,command=Wans) 
radio6 = tk.Radiobutton(text='',variable=radioVar3, value=6,command=Wans) 
radio8 = tk.Radiobutton(text='',variable=radioVar4, value=8,command=Wans) 
radio10 = tk.Radiobutton(text='',variable=radioVar5, value=10,command=Wans) 
radio12 = tk.Radiobutton(text='',variable=radioVar6, value=12,command=Wans) 
radio14 = tk.Radiobutton(text='',variable=radioVar7, value=14,command=Wans) 
radio16 = tk.Radiobutton(text='',variable=radioVar8, value=16,command=Wans) 

# ------------------------------------------------------------

# 選單位置設定
output_excel_button.place(x=625,y=25)
a_button.place(x=525,y=25)
b_button.place(x=625,y=60)
c_button.place(x=525,y=60)
d_button.place(x=450,y=500)
e_button.place(x=550,y=500)
f_button.place(x=650,y=500)


# 詳細資料位置設定
restaurant_name_title.place(x=10,y=25)
restaurant_name.place(x=150,y=25)
order_time_title.place(x=10,y=50)
order_time.place(x=150,y=50)
order_completion_time_title.place(x=10,y=75)
order_completion_time.place(x=150,y=75)
order_address_title.place(x=10,y=100)
order_address.place(x=150,y=100)
payment_type_title.place(x=10,y=125)
payment_type.place(x=150,y=125)
cont.place(x=525,y=125)

# 餐點位置設定
order_title.place(x=10,y=175)
order_1_title.place(x=10,y=200)
order_2_title.place(x=10,y=225)
order_3_title.place(x=10,y=250)
order_4_title.place(x=10,y=275)
order_5_title.place(x=10,y=300)
order_6_title.place(x=10,y=325)
order_7_title.place(x=10,y=350)
order_8_title.place(x=10,y=375)

order_1_money.place(x=300,y=200)
order_2_money.place(x=300,y=225)
order_3_money.place(x=300,y=250)
order_4_money.place(x=300,y=275)
order_5_money.place(x=300,y=300)
order_6_money.place(x=300,y=325)
order_7_money.place(x=300,y=350)
order_8_money.place(x=300,y=375)

# 負擔金額位置設定
subtotal_title.place(x=525,y=200)
subtotal.place(x=525,y=225)
total_title.place(x=625,y=200)
total.place(x=625,y=225)

discount_title.place(x=525,y=275)
discount.place(x=525,y=300)
common_title.place(x=625,y=275)
common.place(x=625,y=300)
Jay_money_title.place(x=525,y=350)
Jay_money.place(x=525,y=375)
Wan_money_title.place(x=625,y=350)
Wan_money.place(x=625,y=375)

# 按鈕位置設定

# 圈圈按鈕位置設定
Jay_title.place(x=350,y=175)
radio1.place(x=362.5,y=200)
radio3.place(x=362.5,y=225)
radio5.place(x=362.5,y=250)
radio7.place(x=362.5,y=275)
radio9.place(x=362.5,y=300)
radio11.place(x=362.5,y=325)
radio13.place(x=362.5,y=350)
radio15.place(x=362.5,y=375)

Wan_title.place(x=400,y=175)
radio2.place(x=412.5,y=200)
radio4.place(x=412.5,y=225)
radio6.place(x=412.5,y=250)
radio8.place(x=412.5,y=275)
radio10.place(x=412.5,y=300)
radio12.place(x=412.5,y=325)
radio14.place(x=412.5,y=350)
radio16.place(x=412.5,y=375)

# --------------------------------------------
window.mainloop()