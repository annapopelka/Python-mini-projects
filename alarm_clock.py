import datetime
import winsound

hour = int(input('Enter hour: '))
minutes = int(input('Enter minutes: '))
amPm = str(input('am or pm: '))

if (amPm == 'pm'):
    hour += 12

while True:
    if(hour == datetime.datetime.now().hour and minutes == datetime.datetime.now().minute):
        print('Get up!')
        winsound.PlaySound('audio', winsound.SND_FILENAME)
        break

