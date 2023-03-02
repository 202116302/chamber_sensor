import pandas as pd
import os
from datetime import datetime, timedelta


def main():


    data_dir = 'data_dir/'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

        url1 = "https://api.thingspeak.com/channels/1999882/feeds.csv?api_key=HN55139L0VGN5XNM&results=5000"
        url2 = "https://api.thingspeak.com/channels/1999883/feeds.csv?api_key=XP1R5CVUPVXTNJT0&results=5000"
        url3 = "https://api.thingspeak.com/channels/1930822/feeds.csv?api_key=WAE2NS9GNFFBFH6F&results=5000"
        url4 = "https://api.thingspeak.com/channels/1999884/feeds.csv?api_key=TYCQQ3CFQME0PITO&results=5000"

        pi1 = pd.read_csv(url1)
        pi2 = pd.read_csv(url2)
        pi3 = pd.read_csv(url3)
        pi4 = pd.read_csv(url4)

        pi_list = [pi1, pi2, pi3, pi4]
        for i in pi_list:
            i['created_at'] = i['created_at'].str.replace('UTC', '')
            i['time'] = pd.to_datetime(i['created_at'], format="%Y-%m-%d %H:%M:%S")
            i['time'] = i['time'] + timedelta(hours=9)
            i['year'] = i['time'].dt.strftime("%Y")
            i['month'] = i['time'].dt.strftime("%m")
            i['day'] = i['time'].dt.strftime("%d")
            i['h_m'] = i['time'].dt.strftime("%H:%M")


        pi1 = pi1.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})
        pi2 = pi2.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})
        pi3 = pi3.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})
        pi4 = pi4.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})

        pi1.to_csv(data_dir + 'pi1.csv')
        pi2.to_csv(data_dir + 'pi2.csv')
        pi3.to_csv(data_dir + 'pi3.csv')
        pi4.to_csv(data_dir + 'pi4.csv')


    else:
        try:
            url1 = "https://api.thingspeak.com/channels/1999882/feeds.csv?api_key=HN55139L0VGN5XNM&results=2"
            url2 = "https://api.thingspeak.com/channels/1999883/feeds.csv?api_key=XP1R5CVUPVXTNJT0&results=2"
            url3 = "https://api.thingspeak.com/channels/1930822/feeds.csv?api_key=WAE2NS9GNFFBFH6F&results=2"
            url4 = "https://api.thingspeak.com/channels/1999884/feeds.csv?api_key=TYCQQ3CFQME0PITO&results=2"

            pi1_add = pd.read_csv(url1)
            pi2_add = pd.read_csv(url2)
            pi3_add= pd.read_csv(url3)
            pi4_add = pd.read_csv(url4)

            pi1 = pd.read_csv("data_dir/pi1.csv")
            pi2 = pd.read_csv("data_dir/pi2.csv")
            pi3 = pd.read_csv("data_dir/pi3.csv")
            pi4 = pd.read_csv("data_dir/pi4.csv")

            pi_list = [pi1_add, pi2_add, pi3_add, pi4_add]
            for i in pi_list:
                i['created_at'] = i['created_at'].str.replace('UTC', '')
                i['time'] = pd.to_datetime(i['created_at'], format="%Y-%m-%d %H:%M:%S")
                i['time'] = i['time'] + timedelta(hours=9)
                i['year'] = i['time'].dt.strftime("%Y")
                i['month'] = i['time'].dt.strftime("%m")
                i['day'] = i['time'].dt.strftime("%d")
                i['h_m'] = i['time'].dt.strftime("%H:%M")

            pi1_add = pi1_add.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})
            pi2_add = pi2_add.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})
            pi3_add = pi3_add.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})
            pi4_add = pi4_add.rename(columns={'field1': 'temperature', 'field2': 'humidity', 'field3': 'lux'})

            pi1 = pd.concat([pi1, pi1_add]).reset_index()
            pi2 = pd.concat([pi2, pi2_add]).reset_index()
            pi3 = pd.concat([pi3, pi3_add]).reset_index()
            pi4 = pd.concat([pi4, pi4_add]).reset_index()

            print(pi1.dtype)



            pi1.to_csv(data_dir + 'pi1.csv')
            pi2.to_csv(data_dir + 'pi2.csv')
            pi3.to_csv(data_dir + 'pi3.csv')
            pi4.to_csv(data_dir + 'pi4.csv')
        except ValueError:
            pass







if __name__ == '__main__':
    main()
