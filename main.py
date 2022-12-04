from IA import *
import sys

if __name__ == '__main__':
    args = sys.argv[1:]

    computer = None
    board = None

    for arg in args:
        argsplt = arg.split('=')
        if len(argsplt) == 2:
            if argsplt[0] == 'computer':
                computer = int(argsplt[1])
            elif argsplt[0] == 'board':
                board = list(map(lambda itm: int(itm), argsplt[1].replace('[', '').replace(']', '').split(',')))

    if computer == None:
        computer = 2

    if board == None:
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    node = Node(board, computer)
    ia = IA(node)
    ia.run()

    if ia.check_win(node.get_board(), computer):
        print("result=COMPUTER WIN!" + " board=" + str(node.get_board()))
    elif ia.check_win(node.get_board(), 1 if computer == 2 else 2):
        print("result=YOU WIN!" + " board=" + str(node.get_board()))
    else:
        best = None
        for child in node.get_children():
            print(child)
            if best is None or (child.get_point() > best.get_point()):
                best = child

        print(">>", best)