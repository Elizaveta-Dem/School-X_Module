from import_this import RACE_DATA

def time_h_m(FinishedTimeSeconds: str) -> str:
    time_hour = str(FinishedTimeSeconds // 3600)
    if len(time_hour) < 2:
       time_hour = '0' + time_hour
    time_min = str((FinishedTimeSeconds % 3600) // 60)
    if len(time_min) < 2:
        time_min = '0' + time_min
    time_sec = str(FinishedTimeSeconds%60)
    if len(time_sec) < 2:
        time_sec = '0' + time_sec
    return (time_hour,time_min,time_sec)
 

win_finish: str = ""   

for i in RACE_DATA.values():
    if i.get('FinishedPlace') == 1:
        win_finish = str(f"Выиграл  {i.get('RacerName')}!!!! Поздравляем!!")
        break
win_finish += "\n"+"_"*len(win_finish)
print(win_finish)
print("")
print("Первые три места:")

# pl: str = "" 
# for i in RACE_DATA.values():
#     if i.get('FinishedPlace') == 2:
#         pl = f"Гонщик {i.get('RacerName')} на 2 месте"
#         break
# print(pl)

for i in range(3):
    num_finish = i+1
    winners_info = str(f"\tГонщик на {'первом' if num_finish == 1 else 'втором' if num_finish == 2 else 'третьем'} месте:\n")
    for i in RACE_DATA.values():
        if i.get('FinishedPlace') == num_finish:
            winners_info += str(f"\t\tИмя: {i.get('RacerName')}\n")
            winners_info += str(f"\t\tКоманда: {i.get('RacerTeam')}\n")
            winners_time = time_h_m(i.get('FinishedTimeSeconds',0))
            winners_info += str(f"\t\tВремя: {winners_time[0]}:{winners_time[1]}:{winners_time[2]}\n")

    print(winners_info)
            