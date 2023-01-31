# chamber_sensor
~~~~~~~~~~~~~~~~~~~~~~~~
raspberry pi  

      ip 
1 192.168.0.171  -  sudo python3 sensor_1.py
2 192.168.0.172  -  python3 sensor_2.py
3 192.168.0.173  -  sudo python3 sensor_3.py
4 192.168.0.174  -  sudo python3.9 sensor_4.py


camera.py 
라즈베리 파이 터미널에서 실행 후 crontab -e 

*/30 * * * * python3.7 /home/pi/camera/camera.py 추가 혹은 ( */30 * * * * python3.7 camera.py가 있는 파일 경로)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

![image](https://user-images.githubusercontent.com/100981830/214483837-b6024e96-0808-470b-8931-6b0f8f109ad2.png)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

error 

read error - 값이 들어오지 않음 ( 주로 온습도 센서 고장) 

OSError(121, I/O error) - 광센서 고장 

URLError - api로 데이터 전송시 에러? 주로 일시적인 오류 