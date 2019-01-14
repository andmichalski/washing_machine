import RPi.GPIO as GPIO
import datetime
import time

channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def callback(channel):
    time_now = str(datetime.datetime.now()) + '\n'
    with open('log.txt', 'a') as f:
        if GPIO.input(channel):
            f.write(time_now)
            print(time_now, " Movement Detected!")
        else:
            f.write(time_now)
            print(time_now, " Movement Detected!")


GPIO.add_event_detect(channel, GPIO.BOTH,
                      bouncetime=300)
GPIO.add_event_callback(channel,
                        callback)

if __name__ == '__main__':
    while True:
        time.sleep(1)
