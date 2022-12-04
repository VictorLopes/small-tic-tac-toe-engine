from random import random

class Node:

    def __init__(self, board, turn = 1, parent = None) -> None:
        self.__TOTAL_CHILDREN = 9

        self.__board = board
        self.__turn = turn
        self.__children = []
        self.__point = 0
        self.__parent = parent

    def __empty_pos(self):
        pos = []
        for i in range(len(self.__board)):
            item = self.__board[i]
            if item == 0:
                pos.append(i)
        return pos.copy()

    def __add_child(self, child):
        if child not in self.__children:
            self.__children.append(child)

    def get_board(self):
        return self.__board

    def get_turn(self):
        return self.__turn

    def get_children(self):
        return self.__children

    def get_parent(self):
        return self.__parent

    def calc_next(self) -> list:
        empty_pos = self.__empty_pos()
        total_next = min(self.__TOTAL_CHILDREN, len(empty_pos))
        while ( len(self.__children) < total_next ):
            board = self.__board.copy()   
            choose_empty = round(random() * (len(empty_pos) - 1))
            chosen_pos = empty_pos[choose_empty]
            board[chosen_pos] = self.__turn
            self.__add_child(Node(board, 2 if self.__turn == 1 else 1, self))
        return self.__children.copy()

    def print_all(self, level = 0):
        print('>> [' + str(level) + ', ' + str(self.__point) + ", " + str(self.__turn) + ']', self.__board)
        for child in self.__children:
            print(child)
            child.print_all(level + 1)

    def set_point(self, point=0):
        self.__point = point

    def get_point(self):
        return self.__point

    def __eq__(self, __o: object) -> bool:
        return self.__board == __o.get_board()

    def __repr__(self) -> str:
        return 'points=' + str(self.__point) + ' board=' + str(self.__board)
    


