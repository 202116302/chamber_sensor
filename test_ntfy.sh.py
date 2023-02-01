import requests
from datetime import datetime
import time

def main():
    while True:
        try:

            now = datetime.now()

            data1 = requests.get(
                "https://api.thingspeak.com/channels/1999882/feeds.json?api_key=HN55139L0VGN5XNM&results=1")
            data2 = requests.get(
                "https://api.thingspeak.com/channels/1999883/feeds.json?api_key=XP1R5CVUPVXTNJT0&results=1")
            data3 = requests.get(
                "https://api.thingspeak.com/channels/1930822/feeds.json?api_key=WAE2NS9GNFFBFH6F&results=1")
            data4 = requests.get(
                "https://api.thingspeak.com/channels/1999884/feeds.json?api_key=TYCQQ3CFQME0PITO&results=1")

            pi1 = data1.json()
            pi2 = data2.json()
            pi3 = data3.json()
            pi4 = data4.json()

            pi1_temp = pi1['feeds'][0]['field1']
            pi1_humid = pi1['feeds'][0]['field2']

            pi2_temp = pi2['feeds'][0]['field1']
            pi2_humid = pi2['feeds'][0]['field2']

            pi3_temp = pi3['feeds'][0]['field1']
            pi3_humid = pi3['feeds'][0]['field2']

            pi4_temp = pi4['feeds'][0]['field1']
            pi4_humid = pi4['feeds'][0]['field2']


            if float(pi1_humid) < 50:
                requests.post("https://ntfy.sh/hyejin1",
                          data=f"챔버1 목마름 습도:{pi1_humid}%".encode(encoding='utf-8'))

            elif float(pi2_humid) < 50:
                requests.post("https://ntfy.sh/hyejin1",
                              data=f"챔버2 목마름 습도:{pi2_humid}%".encode(encoding='utf-8'))

            elif float(pi3_humid) < 50:
                requests.post("https://ntfy.sh/hyejin1",
                              data=f"챔버3 목마름 습도:{pi3_humid}%".encode(encoding='utf-8'))

            elif float(pi4_humid) < 50:
                requests.post("https://ntfy.sh/hyejin1",
                              data=f"챔버4 목마름 습도:{pi4_humid}%".encode(encoding='utf-8'))

            else:
                pass

            if float(pi1_temp) < 20:
                requests.post("https://ntfy.sh/hyejin1",
                              data=f"챔버1 추웡 온도:{pi1_temp}°C".encode(encoding='utf-8'))

            elif float(pi2_temp) < 20:
                requests.post("https://ntfy.sh/hyejin1",
                              data=f"챔버2 추웡  온도:{pi2_temp}°C".encode(encoding='utf-8'))

            elif float(pi3_temp) < 20:
                requests.post("https://ntfy.sh/hyejin1",
                              data=f"챔버3 추웡  온도:{pi3_temp}°C".encode(encoding='utf-8'))

            elif float(pi4_temp) < 20:
                requests.post("https://ntfy.sh/hyejin1",
                              data=f"챔버4 추웡  온도:{pi4_temp}°C".encode(encoding='utf-8'))

            else:
                pass

            print("done")
            time.sleep(300)


        except:
            time.sleep(120)




if __name__ == '__main__':
    main()
