class BoardIndexOutOfRangeError(Exception):
    pass

class BoardRevealMineError(Exception):
    pass

loc1 = [(6, 0), (15, 9), (17, 6), (5, 12), (1, 16), (5, 3), (14, 0), (1, 2), (2, 3), (1, 11), (1, 11),
        (14, 12), (3, 7), (12, 1), (1, 16), (15, 8), (7, 16), (16, 17), (6, 1), (13, 12), (8, 7), (8, 9), (2, 7),
        (0, 3), (12, 16), (3, 5), (15, 4), (17, 7), (5, 10), (14, 10), (15, 16), (15, 13), (4, 2), (14, 15), (4, 12),
        (2, 14), (6, 9), (10, 15), (14, 16), (8, 12), (8, 4), (3, 8)]           #지뢰의 위치

class Board():
    def __init__(self, size = 18, num_mine = 40, loc = loc1):   #보드 초기화 값 class의 매개변수 첫번째는 self(거의 무조건), 사이즈, 지뢰의 수, 위치
        
        mine_loc = loc
        self.__board =  [[None for row in range(size)] for col in range(size)]
        self.size = size
        self.num_mine = num_mine

        for (s, t) in mine_loc:
            self.__board[s][t] = -1                     #지뢰가 s, t에 있으면 self.__board[s][t]는 -1

        for i in range(self.size):
            for j in range(self.size):
                if self.__board[i][j] == -1:            #self.__board[s][t]는 -1이면 계속하기
                    continue
                count = 0
                for s in range(max(i-1, 0), min(i+2, self.size)):
                    for t in range(max(j-1, 0), min(j+2, self.size)):
                        if s == i and t == j:
                            continue
                        if self.__board[s][t] == -1:
                            count += 1
                self.__board[i][j] = count              

    def reveal(self, s, t):                             # (s, t) 위치를 보여주는 함수
        if s < 0 or s >= self.size or t < 0 or t >= self.size:      # 좌표 위치가 board를 넘어가면
            print("The reveal index is out of range")               # 범위에 벗어났다는 문장 출력
            raise BoardIndexOutOfRangeError

        r = self.__board[s][t]

        if r == -1:                                       # r이 -1이면 지뢰를 열었다는 문장 출력 
            print("You've just revealed a mine.")
            raise BoardRevealMineError
        return r

    def collectAll(self, board, to_find = -1):
        collect = []
        for (i, j) in [(i, j) for i in range(self.size) for j in range(self.size)]:
            if board[i][j] == to_find:          # board의 좌표가 -1이면 (지뢰면)
                collect.append((i, j))          # collect 리스트에 좌표 추가
        return collect                          # collect 리스트 리턴


    def evaluate(self, play_board):             # 평가 하는 함수 
        if len(play_board) != self.size:        # play_board와 초기보드 size와 맞지 않으면
            print("Inappropriate board size")   # 부적절한 board size라는 문장 출력
            return  
        this = set(self.collectAll(self.__board))   # set -> 집합 자료형(순서, 중복 X) 초기  board
        that = set(self.collectAll(play_board))     # play 한 board

        print("Correct, Incorrect, Total Reveal: {}, {}, {}".format(len(this & that), len(that - this),     # & -> 교집합, - -> 차집합
            324 - len(self.collectAll(play_board, None))))


    def __repr__(self): # 지뢰가 있으면 *을 반환, 없으면 그 값(y)을 문자열로 출력해주는 함수
        s = list(map(lambda x : list(map(lambda y: f'{y} ' if y != -1 else '* ', x)), self.__board))    
        return "\n".join("".join(s[i]) for i in range(self.size))


    def init_playboard(self):   # 시작할 때의 board
        self.playboard = [[None for i in range(self.size)] for j in range(self.size)]
        return self.playboard

    def get_playboard(self):    # 게임을 하다가 확인하는 board
        return self.playboard
