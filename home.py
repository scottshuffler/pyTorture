import time 
# the time you leave in military time including zeros and only numbers (163000)
starting_time = 900
quitting_time = 1630


while True:
    quitting_time_h = quitting_time / 100
    quitting_time_m = quitting_time % 100

    starting_time_h = starting_time / 100
    starting_time_m = starting_time % 100

    curr_time_hour = int(time.strftime("%H"))
    curr_time_minute = int(time.strftime("%M"))
    curr_time_second = int(time.strftime("%S"))

    quitting_time_in_seconds = (quitting_time_h * 3600) + (quitting_time_m * 60)
    starting_time_in_seconds = (starting_time_h * 3600) + (starting_time_m * 60)
    current_time_in_seconds = (curr_time_hour * 60 * 60) + (curr_time_minute * 60) + curr_time_second

    if quitting_time_in_seconds > current_time_in_seconds >= starting_time_in_seconds:
        diff_time_in_seconds = quitting_time_in_seconds - current_time_in_seconds
        remaining_time_in_seconds = diff_time_in_seconds % 60
        remaining_time_in_minutes = int(((diff_time_in_seconds - remaining_time_in_seconds) / 60) % 60)
        remaining_time_in_hours = int(((diff_time_in_seconds - (60 * remaining_time_in_minutes) - remaining_time_in_seconds) / 3600))

        print("You have " + str(remaining_time_in_hours) + " hour(s) " + str(remaining_time_in_minutes) + " minutes and " + str(remaining_time_in_seconds) + " seconds remaining of work.")
        time.sleep(1)
    else:
        print("IT'S TIME TO GO HOME")
        time.sleep(quitting_time_in_seconds - starting_time_in_seconds)
