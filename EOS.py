import datetime
import requests
import json
import websocket
import telegram
import gc
t_api3 = '5377082749:AAHoZIECpTTeiYblW7v7Zj3yHtVCaCViXEY'
bot = telegram.Bot(token=t_api3)

key = 'https://api.coinbase.com/v2/prices/EOS-USD/spot'
# key1 = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

def Write_json(txt, files):
    with open(files, "w") as file:
        json.dump(txt, file)


def Read_json(files):
    with open(files, "r") as file:
        data = json.load(file)
    return data

def Take_ss_put(Update1):
    try:
        url = "https://getpantry.cloud/apiv1/pantry/68f5be2a-7af7-4cfb-bfc1-0505ff5437b8"

        payload = json.dumps({
        "name": "For Screen Shot Updated",
        "description": Update1
        })
        headers = {
        'Content-Type': 'application/json'
        }

        requests.request("PUT", url, headers=headers, data=payload)
    except Exception as ss123:
        pass

def Take_ss_get():
    try:
        url = "https://getpantry.cloud/apiv1/pantry/68f5be2a-7af7-4cfb-bfc1-0505ff5437b8"

        payload = ""
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
    except:
        pass    

def send():
    bot.send_document(chat_id="@mybotbug1",document=open('data2.json', 'rb'), filename="EOS_Plateform.json")    

def on_message(ws, message):
    sshot = Take_ss_get()
    # print(sshot)
    if sshot["description"] == "jsoneos":
        # print('new')
        send()
        Take_ss_put('Not screenshot')
    y = json.loads(message)
    time_UTC = str(y['tick']['time'])
    x_label = int(time_UTC[:10])
    xxx = datetime.datetime.fromtimestamp(int(x_label))
    New_Time = xxx.strftime('%H:%M:%S')
    New_btc = float(y['tick']['value'])
    data = requests.get(key)  
    data = data.json()
    # print(data)
    biance = float(data['data']['amount'])
    final121 = Read_json('data2.json')
    rf = {'time': New_Time, 'Bianry': New_btc, 'Coin': biance}
#     rf = {'time': x_label, 'Bianry': New_btc, 'Coin': biance}
    final121.append(rf)
    Write_json(final121, 'data2.json')
    gc.collect()
    # update_graph_scatter(New_Time, New_btc)

    

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

mylist = {"type": "getHistory", "uuid": 473796, "numberOfTicks": 2000}
xc = json.dumps(mylist, separators=(',', ':'))

def on_open(ws):
    print("Opened connection")
    ws.send(xc)
                 

if __name__ == "__main__":
    # websocket.enableTrace(True)
    try:
        ws = websocket.WebSocketApp("wss://api.binarystars.cc/wseos/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
        ws.run_forever()
        # app.run_server()
    except Exception as ed:
        dddd = f'EOS Json : {ed}'
        bot.send_message(chat_id="@mybotbug1", text=dddd)
