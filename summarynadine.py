import csv

file = open('Actigraphy data_Adult.csv')

sleep_start_times = []
sleep_end_times = []
sleep_durations = []

def time_24hr(time):
    if 'PM' in time:
        time = time.strip(' PM')
        time = time.split(':')
        if int(time[0]) < 12:
            time[0] = int(time[0]) + 12
            time[0] = str(time[0])
        time = ":".join(time)
        return(time)
    elif 'AM' in time:
        time = time.strip(' AM')
        time = time.split(':')
        if int(time[0]) == 12:
            time[0] = 0
            time[0] = str(time[0])
        time = ":".join(time)
        return(time)

def string_to_list(time):
    time = time.split(':')
    time[0] = int(time[0])
    time[1] = int(time[1])
    time[2] = int(time[2])
    return(time)

for line in file:
    line = line.strip('"')
    line = line.strip('",\n')
    line = line.split('","')

#Extracting row by row of recorded sleep times
    if 'SLEEP' in line:
#Append start times
        time1 = time_24hr(line[4])
        sleep_start_times.append(time1)

#Append end time
        time2 = time_24hr(line[7])
        sleep_end_times.append(time2)

#Calculate duration and append to sleep_durations
        time1 = [int(part) for part in time1.split(":")]
        time2 = [int(part) for part in time2.split(":")]
        time3 = [0,0,0]
        if time1[0] > time2[0]:
            hour_difference = 24 - time1[0]
            time3[0] = time3[0] + hour_difference
        time3[0] = time3[0] + time2[0]
        minute_difference = time1[1] - time2[1]
        if minute_difference < 0:
            time3[0] = time3[0] - 1
            time3[1] = 60 + minute_difference
        else:
            time3[1] = minute_difference
        sleep_durations.append(time3)


#Minimums for time values - incomplete
    min_bedtime = min(sleep_start_times)
    min_get_up_time = min(sleep_end_times)
    min_hours_of_sleep = min(sleep_durations)

#Maximums for time values - incomplete
    max_bedtime = max(sleep_start_times)
    max_get_up_time = max(sleep_end_times)
    max_hours_of_sleep = max(sleep_durations)

#Averages for time values - incomplete
    avg_bedtime = avg(sleep_start_times)
    avg_get_up_time = avg(sleep_end_times)
    avg_hours_of_sleep = avg(sleep_durations)

#Minimums for all except time
    if 'Sleep Summary' in line and 'Minimum(n)' in line:
        min_onset_latency = line[20]
        min_efficiency = line[21]
        min_waso = line[23]
        min_awakenings = line[25]

#Maximums for all except time
    if 'Sleep Summary' in line and 'Maximum(n)' in line:
        max_onset_latency = line[20]
        max_efficiency = line[21]
        max_waso = line[23]
        max_awakenings = line[25]

#Averages for all except time
    if 'Sleep Summary' in line and 'Average(n)' in line:
        #print(line)
        avg_onset_latency = line[20]
        avg_efficiency = line[21]
        avg_waso = line[23]
        avg_awakenings = line[25]
