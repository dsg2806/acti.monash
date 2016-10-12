import csv

file = open('Actigraphy data_Adult.csv')
bedtimes = []
min_bedtime = ()
max_bedtime = ()
avg_bedtime = ()

get_up_times = []
min_get_up_time = ()
max_get_up_time = ()
avg_get_up_time = ()

time_in_beds = []
min_time_in_bed = ()
max_time_in_bed = ()
avg_time_in_bed = ()

total_sleep_times = []
min_total_sleep_time = ()
max_total_sleep_time = ()
avg_total_sleep_time = ()

onset_latencys = []
min_onset_latency = ()
max_onset_latency = ()
avg_onset_latency = ()

sleep_efficiencys = []
min_sleep_efficiency = ()
max_sleep_efficiency = ()
avg_sleep_efficiency = ()

wasos = []
min_waso = ()
max_waso = ()
avg_waso = ()

awaks = []
min_awak = ()
max_awak = ()
avg_awak = ()

for i in file:
    i = i.split(',')

    #print(i)
    #print(file)
    if '------------------------ Statistics ------------------------' in i[0]:
        break
for i in file:
    collum = 0
    i = i.split(',')
    for collum in i:
        print(collum)
    #print(i)
    if 'SLEEP' in i[0]:
        #print(i[4])
        bedtimes.append(i[4])
    if '-------------------- Epoch-by-Epoch Data -------------------' in i[0]:
        break

print(bedtimes)
