def solution(clothes):
    answer = 0
    clothe_dic = dict()
    for name, cate in clothes:
        if cate not in clothe_dic.keys():
            clothe_dic[cate] = 1
        else:
            clothe_dic[cate] += 1
    cnt = 1
    for i in clothe_dic.keys():
        cnt *= (clothe_dic[i] + 1)
    return cnt - 1