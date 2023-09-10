def time_conversion(sec):
    hour_time = sec // 3600
    min_time = (sec % 3600) // 60
    return str(hour_time) + 'ч. ' + str(min_time) + "мин. "

list_time = [3600, 3601, 3500, 323500]
for i in list_time:
    print(i,'=', time_conversion(i))