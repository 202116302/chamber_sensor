import pandas as pd
from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    url1 = "https://api.thingspeak.com/channels/1999882/feeds.csv?api_key=HN55139L0VGN5XNM&results=50"
    url2 = "https://api.thingspeak.com/channels/1999883/feeds.csv?api_key=XP1R5CVUPVXTNJT0&results=10000"
    url3 = "https://api.thingspeak.com/channels/1930822/feeds.csv?api_key=WAE2NS9GNFFBFH6F&results=10000"
    url4 = "https://api.thingspeak.com/channels/1999884/feeds.csv?api_key=TYCQQ3CFQME0PITO&results=2"

    pi1 = pd.read_csv(url1)
    pi2 = pd.read_csv(url2)
    pi3 = pd.read_csv(url3)
    pi4 = pd.read_csv(url4)

    pi_list = [pi1, pi2, pi3, pi4]
    for i in pi_list:
        i = i.rename(columns={'field1': 'temperture', 'field2': 'humid', 'field3': 'lux'})
        i['created_at'] = i['created_at'].str.replace('UTC', '')
        i['created_at'] = pd.to_datetime(i['created_at'], format="%Y-%m-%d %H:%M:%S")
        i['created_at'] = i['created_at'] + timedelta(hours=9)


    print(pi1.columns)
    # sns.lineplot(data=pi1, x='created_at', y='field1')
    # plt.show()

if __name__ == '__main__':
    main()
