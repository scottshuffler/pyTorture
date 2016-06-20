import time
import sys

# the time you start and leave in military time including zeros and only numbers (1630)
starting_time = 900
quitting_time = 1630


def main(argv):
    while True:
        quitting_time_h = int(quitting_time / 100)
        quitting_time_m = int(quitting_time % 100)

        starting_time_h = int(starting_time / 100)
        starting_time_m = int(starting_time % 100)

        curr_time_hour = int(time.strftime("%H"))
        curr_time_minute = int(time.strftime("%M"))
        curr_time_second = int(time.strftime("%S"))

        quitting_time_in_seconds = (quitting_time_h * 3600) + (quitting_time_m * 60)
        starting_time_in_seconds = (starting_time_h * 3600) + (starting_time_m * 60)
        current_time_in_seconds = (curr_time_hour * 60 * 60) + (curr_time_minute * 60) + curr_time_second

        if quitting_time_in_seconds > current_time_in_seconds >= starting_time_in_seconds:
            diff_time_in_seconds = quitting_time_in_seconds - current_time_in_seconds
            remaining_time_in_seconds = int(diff_time_in_seconds % 60)
            remaining_time_in_minutes = int(((diff_time_in_seconds - remaining_time_in_seconds) / 60) % 60)
            remaining_time_in_hours = int(
                ((diff_time_in_seconds - (60 * remaining_time_in_minutes) - remaining_time_in_seconds) / 3600))

            sys.stdout.write("Time remaining at work: " + str(remaining_time_in_hours).zfill(2) + ":" + str(
                remaining_time_in_minutes).zfill(2) + ":" + str(remaining_time_in_seconds).zfill(2) + "   \r")
            sys.stdout.flush()
            time.sleep(1)
        else:
            total_time = int(24 - (quitting_time_h - starting_time_h))
            print("IT'S TIME TO GO HOME")
            print("DON'T WORRY WE'LL SEE YOU IN ABOUT " + str(total_time) + " HOURS :)")
            for x in range(quitting_time_in_seconds - starting_time_in_seconds):
                time.sleep(1)


if __name__ == '__main__':
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    # if len(sys.argv) < 5:
    #     print("USAGE: python main.py -s 900 -f 1630")
    # else:
    main(sys.argv[1:])
