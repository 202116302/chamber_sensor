import os
from datetime import datetime
from picamera import PiCamera
from time import sleep


output_dir = "/home/pi/camera/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



camera = PiCamera()
camera.vflip = True
camera.hflip = True
camera.start_preview()

#for i in range(10):
#   sleep(10)
#   camera.capture('/home/pi/image%s.jpg' % i)


date_str = "20230104"
now = datetime.now()
date_str = now.strftime("%Y%m%d_%H%M")
sleep(5)
camera.capture(os.path.join(output_dir, f"image_{date_str}.jpg"))

camera.stop_preview()
