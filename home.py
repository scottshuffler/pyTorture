import time 
# the time you leave in military time including zeros and only numbers (163000)
quitting_time_hour = 16
quitting_time_minute = 30
quitting_time_second = 00

while True:
    curr_time_hour = time.strftime("%H")
    curr_time_minute = time.strftime("%M")
    curr_time_second = time.strftime("%S")
    if quitting_time_hour >= int(curr_time_hour) and quitting_time_minute >= int(curr_time_minute):
        diff_time_hours = quitting_time_hour - int(curr_time_hour)
        diff_time_minutes = quitting_time_minute - int(curr_time_minute)
        diff_time_seconds = 60 - int(curr_time_second)
        print("You have " + str(diff_time_hours) + " hour(s) " + str(abs(diff_time_minutes)) + " minutes and " + str(abs(diff_time_seconds)) + " seconds remaining of work.")
    else:
        print("GO THE FUCK HOME")
    time.sleep(1)
