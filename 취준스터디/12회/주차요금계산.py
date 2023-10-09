def solution(fees, records):
    infos = {}
    answer = []

    def total_fees(fees, parked_minutes):  # 주차요금 정산기
        fee = 0  # 최종 요금
        default_minutes, default_fee, unit_time, unit_fee = fees  # 기본시간(분), 기본요금, 단위시간(분), 단위요금
        if parked_minutes <= default_minutes:  # 기본 요금 나온 경우
            fee = default_fee
        elif parked_minutes > default_minutes:  # 기본 요금보다 많이 나온 경우
            base_minute = (parked_minutes-default_minutes)/unit_time
            if base_minute == int(base_minute):  # 부동소수점 문제 해결 => 49.0 == 49 => True
                fee = default_fee + int(base_minute) * unit_fee
            else:  # 실제로 내림을 하게 돼버리는 경우 올리기 위해 1개를 더해줍니다.
                fee = default_fee + (int(base_minute) + 1) * unit_fee

        return fee

    for record in records:  # 기록들을 돌면서 실행할 로직
        time_str, plate_num, action = record.split()  # 공백을 기준으로 스트링을 구분해서 리스트로 만들어줌
        if infos.get(plate_num, 'initial') == 'initial':  # 처음 입차한 경우
            infos[plate_num] = [0, time_str, 'IN']  # [누적 주차시간, 'hour:minute', 입출차여부]
        elif action == 'IN':  # 그 이외에 출차 후 입차를 다시 한 경우
            infos[plate_num][1] = time_str  # 시간만 갈아끼워 줍니다.
            infos[plate_num][2] = 'IN'  # 들어왔다고 기록
        elif action == 'OUT':  # 출차의 경우 => 출차시간 - 입차시간의 분 계산 후 더해줍니다.
            prev_hour_str, prev_minute_str = infos[plate_num][1].split(':')  # 기존 입차 시간, 분의 스트링
            new_hour_str, new_minute_str = time_str.split(':')  # 출차 시간, 분의 스트링
            hour_diff = int(new_hour_str) - int(prev_hour_str)
            minute_diff = int(new_minute_str) - int(prev_minute_str)
            infos[plate_num][0] += (hour_diff*60) + minute_diff  # 분으로 환산한 누적 출차-입차 시간
            infos[plate_num][2] = 'OUT'  # 나갔다고 기록

    plate_nums = list(infos.keys())
    plate_nums.sort(key=lambda x: int(x))  # 기준을 작은 번호판 숫자부터 sort => 결과는 문자열이 소팅됩니다.

    for plate_num in plate_nums:
        if infos[plate_num][2] == 'OUT':  # 이미 나가고 없는 차라면?
            total_minutes = infos[plate_num][0]  # 누적 주차시간을 가져오고
            answer.append(total_fees(fees, total_minutes))  # 주차요금 정산
        elif infos[plate_num][2] == 'IN':  # 출차가 아직 안된 차라면?
            prev_minutes = infos[plate_num][0]  # 이전까지의 누적 주차시간을 가져오고
            last_in_hour_str, last_in_minute_str = infos[plate_num][1].split(':')
            until_midnight_diff = (23-int(last_in_hour_str))*60 + (59-int(last_in_minute_str))  # 23:59분에서 빼줌
            answer.append(total_fees(fees, prev_minutes+until_midnight_diff))

    return answer