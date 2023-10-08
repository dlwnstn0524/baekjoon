# 딕셔너리의 순서보장이 안된다고 가정한 풀이

def solution(id_list, report, k):
		# 자료구조
    reporter_info = dict(zip(id_list, [[0, set()] for _ in range(len(id_list))])) # 신고자 기준
    reported_info = dict(zip(id_list, [0]*len(id_list)))  # 신고 결과 집계 {'muzi':0, ...}
    exclusive_reports = set()  # 중복이 제거된 튜플 (신고한자, 신고받은자) 받아줄 자료구조
    answer = [0]*len(id_list)
		
		# 사용로직
    for each_report in report:  # 신고한자 - 신고된자 정보 리스트를 쓸만하게 변형
        exclusive_report = tuple(each_report.split())  # (신고한사람, 신고당한사람)
        exclusive_reports.add(exclusive_report)  # 여러번 신고하더라도 튜플 + 셋으로 중복 제거용
        reporter_info[exclusive_report[0]][1].add(exclusive_report[1])  # {'muzi': [메일횟수, set( 여기 신고자 넣어줌 )]...}

    for exclusive_report in exclusive_reports:  # 중복이 제거된 신고된자들 1개씩 카운트
        reported_info[exclusive_report[1]] += 1

    for reported, cnt in reported_info.items():  # 신고된자 자료구조에서 정보를 모두 뽑으면서
        if cnt >= k:  # 신고 결과 횟수 누적치에 도달했는 신고된자라면?
            for each_reporter in reporter_info.keys():
                if reported in reporter_info[each_reporter][1]:  # 만약 어떤 사람의 신고자 셋에 들어있다면?
                    reporter_info[each_reporter][0] += 1  # 그 사람의 이메일 받을 횟수를 증가시킨다

    for idx, each_reporter in enumerate(id_list):  # 3.7 이하 딕셔너리 순서보장이 안되므로 위해 리스트에서 뽑아서 순서 맞춤
        answer[idx] = reporter_info[each_reporter][0]  # test case 1 => [2, 1, 1, 0] 이 되도록

    return answer