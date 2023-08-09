def solution(genres, plays):
    answer = []
    info = []
    genres_cnt = dict()
    for i in range(len(genres)):
        info.append((genres[i], plays[i], i))
    info = sorted(info, key=lambda x: (x[0], -x[1], x[2]))
    for genre, play, idx in info:
        if genre not in genres_cnt.keys():
            genres_cnt[genre] = play
        else:
            genres_cnt[genre] += play
    genres_cnt = sorted(genres_cnt.items(), key = lambda x: -x[1])
    print(genres_cnt)
    
    for i in genres_cnt: # 같은 장르 내에서는 최대 2곡까지 조건대로 수록
        count = 0
        for j in info:
            if i[0] == j[0]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(j[2])
    return answer