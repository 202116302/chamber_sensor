import pandas as pd
import os
from datetime import datetime, timedelta

def main():
    data_dir = './data_dir/'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    url1 = "https://api.thingspeak.com/channels/1999882/feeds.csv?api_key=HN55139L0VGN5XNM&results=20000"
    url2 = "https://api.thingspeak.com/channels/1999883/feeds.csv?api_key=XP1R5CVUPVXTNJT0&results=20000"
    url3 = "https://api.thingspeak.com/channels/1930822/feeds.csv?api_key=WAE2NS9GNFFBFH6F&results=19000"
    url4 = "https://api.thingspeak.com/channels/1999884/feeds.csv?api_key=TYCQQ3CFQME0PITO&results=19000"

    pi1 = pd.read_csv(url1)
    pi2 = pd.read_csv(url2)
    pi3 = pd.read_csv(url3)
    pi4 = pd.read_csv(url4)

    pi_list = [pi1, pi2, pi3, pi4]
    for i in pi_list:
        i['created_at'] = i['created_at'].str.replace('UTC', '')
        i['created_at'] = pd.to_datetime(i['created_at'], format="%Y-%m-%d %H:%M:%S")
        i['created_at'] = i['created_at'] + timedelta(hours=9)

    pi1 = pi1.rename(columns={'field1':'temperature', 'field2':'humidity', 'field3':'lux'})
    pi2 = pi2.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})
    pi3 = pi3.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})
    pi4 = pi4.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})


    pi1.to_csv(data_dir + 'pi1.csv')
    pi2.to_csv(data_dir + 'pi2.csv')
    pi3.to_csv(data_dir + 'pi3.csv')
    pi4.to_csv(data_dir + 'pi4.csv')

    print(pi1.head(5))
    # print(pi2.head(5))
    # print(pi3.head(5))
    # print(pi4.tail(5))



if __name__ == '__main__':
    main()