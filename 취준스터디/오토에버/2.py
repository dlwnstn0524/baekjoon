import sys

H, W, r, h0, w0, h1, w1 = map(int, sys.stdin.readline().split())
answer = []

# 각 키패드의 중심 좌표를 저장하는 딕셔너리 정의
key_dic = {}
key_dic["1"] = (h0+r, w0+r)
key_dic["2"] = (h0+r, w0+w1+3*r)
key_dic["3"] = (h0+r, w0+2*w1+5*r)

key_dic["4"] = (h0+h1+3*r, w0+r)
key_dic["5"] = (h0+h1+3*r, w0+w1+3*r)
key_dic["6"] = (h0+h1+3*r, w0+2*w1+5*r)

key_dic["7"] = (h0+2*h1+5*r, w0+r)
key_dic["8"] = (h0+2*h1+5*r, w0+w1+3*r)
key_dic["9"] = (h0+2*h1+5*r, w0+2*w1+5*r)

key_dic["BACK"] = (h0+3*h1+7*r, w0+r)
key_dic["0"] = (h0+3*h1+7*r, w0+w1+3*r)
key_dic["OK"] = (h0+3*h1+7*r, w0+2*w1+5*r)

N = int(sys.stdin.readline())
current = ''

# 사용자의 터치 좌표를 기준으로 연산하는 반복문
for _ in range(N):
  x, y = map(int, sys.stdin.readline().split())
  pressed = ''

  # 좌표를 기준으로 각 키패드의 중심의 좌표를 기준으로 거리가 반지름 이하인 지점 탐색
  for key, value in key_dic.items():
    dis = (x - value[0])**2 + (y - value[1])**2
    if dis <= r**2:
      pressed = key
      break

  # 아무것도 눌리지 않았을때는 통과
  if pressed == '':
    continue
  
  else:
    
    # "BACK"이 눌렸을 경우 현재 버퍼의 길이가 0이라면 그대로 유지, 아니라면 하나 지우기
    if pressed == "BACK":
      if len(current) == 0:
        continue
      else:
        current = current[:len(current)-1]

    # "OK"가 눌렸을때 현재 버퍼의 길이가 0이 아니라면 answer 리스트에 해당 버퍼의 문자열 추가 및 버퍼 초기화
    elif pressed == "OK" and len(current) != 0:
      answer.append(current)
      current = ''

    # 숫자가 눌렸을 경우 현재 버퍼 상태에 눌린 숫자 추가
    else:
      current += pressed

print(len(answer))
for i in answer:
  print(i)