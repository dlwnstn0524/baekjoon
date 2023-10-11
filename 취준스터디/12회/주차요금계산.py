from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    parking_dict = {}
    fee_dict = defaultdict(list)
    total = []
    
    for record in records:
        time, car_num, state = record.split()
        if state == "IN":
            parking_dict[car_num] = time
        else:
            out_h, out_m = map(int, time.split(":"))
            in_h, in_m = map(int, parking_dict[car_num].split(":"))
            parking_dict.pop(car_num)
            minute = (out_h - in_h)*60 + out_m - in_m
            fee_dict[car_num].append(minute)
    
    for key in parking_dict.keys():
        in_h, in_m = map(int, parking_dict[key].split(":"))
        fee_dict[key].append((23-in_h)*60 + 59 - in_m)
        

    for key in fee_dict.keys():
        total.append((key, sum(fee_dict[key])))
    total.sort(key=lambda x: x[0])
    
    for i in range(len(total)):
        if total[i][1] >= fees[0]:
            fee = fees[1] + math.ceil((total[i][1] - fees[0])/fees[2]) * fees[3]
            answer.append(fee)
        else:
            answer.append(fees[1])
    
    return answer