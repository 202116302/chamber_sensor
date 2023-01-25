# chamber_sensor
~~~~~~~~~~~~~~~~~~~~~~~~
raspberry pi  

      ip 
chamber_1.py 192.168.0.171  -  sudo python3 sensor.py
chamber_2.py 192.168.0.172  -  python3 sensor.py
chamber_3.py 192.168.0.173  -  sudo python3 sensor.py
chamber_4.py 192.168.0.174  -  sudo python3.9 sensor.py


camera.py 
라즈베리 파이 터미널에서 실행 후 crontab -e 

*/30 * * * * python3.7 /home/pi/camera/camera.py 추가 혹은 ( */30 * * * * python3.7 camera.py가 있는 파일 경로)


![KakaoTalk_20230125_133400578](https://user-images.githubusercontent.com/100981830/214483790-731b8797-de3e-4b1e-8231-b82cf7ff07f3.png)
