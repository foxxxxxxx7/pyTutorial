import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f'Alarm set for {alarm_time}')
    sound_file = 'spaceship Alarm.mp3'

    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)

    while (current_time := datetime.datetime.now().strftime('%H:%M:%S')) != alarm_time:
        print(current_time)
        time.sleep(1)

    print('WAKE UP!!! 😪')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input('Enter alarm time (HH:MM:SS): ')
    set_alarm(alarm_time)
