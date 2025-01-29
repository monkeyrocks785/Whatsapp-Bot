import pywhatkit as kit

number = str(input('Enter the number here : '))
msg = str(input('Enter the message here : '))
time_h = int(input('Enter the hour in 24-hour format here : '))
time_m = int(input('Enter the minutes here : '))

kit.sendwhatmsg(number, msg, time_h, time_m)