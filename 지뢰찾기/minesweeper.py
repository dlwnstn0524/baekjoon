from board import Board

"""
minesweeper.py에 있는 코드는 여러분이 자유롭게 수정하여 사용할 수 있습니다.
find_mines() 함수는 반드시 있어야하는 함수입니다. 없으면, 평가되지 않습니다. 매개변수도 수정하면 안됩니다.
나머지 함수들은 여러분이 사용할 수 있도록, 미리 만들어 놓았습니다. 여러분의 지뢰찾는 방식에 따라,
수정하여 사용할 수 있습니다.
"""

def collectWindow(board, i, j, to_find = -1, size = 18):    # (i, j) 주변에 -1 값을 가지는 격자(좌표를) collect에 모으는 함수
    collect = []
    for s in range(max(i-1, 0), min(i+2, size)):
        for t in range(max(j-1, 0), min(j+2, size)):
            if board[s][t] == to_find:                      
                collect.append((s,t))                       # collect 리스트에 지뢰가 있는 좌표 추가
    return collect


def printBoard(board, size):                                # Board 출력
    s = list(map(lambda x : list(map(lambda y: '* ' if y == -1 else '? ' if y == None else '  ' if y == 0 else f'{y} ', x)), board))    # Board의 __repr_() 같은
    print("")
    print("\n".join("".join(s[i]) for i in range(size)))
    print("-"*50)
    print("")
    return


def reveal(board, s, t):    # 좌표 (s, t)를 여는 함수

    """
    (s,t)위치의 격자를 엽니다. (reveal)
    지뢰가 없다면, 주변의 지뢰가 몇개가 있는지 알려줍니다.
    만약 지뢰가 있는 위치를 열었다면, 게임이 종료됩니다. (Game Over)
    """

    global gameBoard
    v = gameBoard.reveal(s, t)          # gameBoard.reveal은 Board의 (s, t) 위치를 보여주고 Board를 넘어가면 범위를 벗어났단는 문장 출력 리턴 값: Board[s][t]
    board[s][t] = v
    # print('{}, {} revealed'.format(s, t))
    return v


def mark(board, s, t):      # (s, t)에 지뢰가 있다면 -1 값을 mark
    """
    (s, t) 위치의 격자에 지뢰가 있을 것이라고 표시합니다.
    """
    board[s][t] = -1
    #print('{}, {} marked'.format(s, t))
    return


def reveal_zeros(board, i, j, size = 18):
    """
    (i, j) 위치의 격자를 밝히고 그 격자 주변에 지뢰가 없다는 것이 밝혀지면,
    그 위치부터 시작하여, 최대한 넓게 격자들을 밝혀냅니다.
    더 좋게 개선할 수 있는 코드입니다.
    """
    if i < 0 or j < 0 or i >= size or j >= size:    # 함수의 매개변수 값들이 조건에 맞지 않으면
        return

    v = reveal(board, i, j)                          # reveal -> board의 (i, j)를 보여줌
    if v != 0:
        return
       
    for s in range(max(0, i-1), min(size, i+2)):
        for t in range(max(0, j-1), min(size, j+2)):
            if s == i and t == j:
                continue                              # 반복문 처음으로
            if board[s][t] != None:
                continue
            v = reveal(board, s, t)
            if v == 0:
                reveal_zeros(board, s, t)


def auto_reveal(board,  base = 1, size = 18):   # 자동으로 지뢰를 열어주는 함수
    print("Starting auto_reveal...")
    count = 0                   # count reveal or mark
    for (i, j) in [(i, j) for i in range(size) for j in range(size)]:
        if board[i][j] != base:
            continue
        mines = collectWindow(board, i, j, -1)  # 먼저 주변에 밝혀진 지뢰찾기, return은 collect[]
        num = len(mines)                        # 18*18

        if num == base:
            unknowns = collectWindow(board, i, j, None)
            for (s, t) in unknowns: 
                count += 1
                v = reveal(board, s,t)
                if v == 0:
                    reveal_zeros(board, s, t)
        elif num > base:
            print("Something Wrong")
            return 0
        elif num < base:
            unknowns = collectWindow(board, i, j, None)
            if len(unknowns) + num == base:
                for (s, t) in unknowns:
                    mark(board, s, t) 
                    count += 1 
    return count


def find_mines(board, size = 18):       # 지뢰 찾기 함수

    """
    여러분이 생각한 지뢰찾는 방법을 코딩합니다.
    반드시 있어야하는 함수입니다. 평가할 때, 이 함수를 호출합니다.
    """

    while auto_reveal(board, 1) > 0:
        continue
    printBoard(board, size)


if __name__ == "__main__":      # board에서 minesweeper로 돌아오면 __name__은 __main__이 됨.

    gameBoard = Board()
    board = gameBoard.init_playboard()      # 시작할 때의 초기화 된 board

    printBoard(board, 18)                   # 크기가 18인 board 출력

    # (11, 10)의 위치 주변에는 지뢰가 없는 것으로 설정되어 있습니다.
    # (11, 10)의 위치에서 아래 처럼 reveal_zero를 먼저 실행하면 좋습니다.
    if reveal(board, 11,10) == 0:           # (11, 10)을 연다
        reveal_zeros(board, 11, 10)

    print("\n========================\n")

    find_mines(board)                       # board의 지뢰를 찾음

    #print(gameBoard.__board)
    gameBoard.evaluate(board)               # 지뢰 찾기 게임을 평가 Correct, Incorret, Total Reveal 출력

