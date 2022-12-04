from .node import Node

class IA:

    def __init__(self, node: Node) -> None:
        self.__DEEPNESS = 10
        self.__node = node

    def run(self, level = 0, node = None):
        root = self.__node if node is None else node

        win_for_x = self.check_win(root.get_board(), 1)
        win_for_o = self.check_win(root.get_board(), 2)

        if (win_for_x and root.get_turn() == 1) or (win_for_o and root.get_turn() == 2):
            root.set_point(1)
            return
        elif (win_for_o and root.get_turn() == 1) or (win_for_x and root.get_turn() == 2):
            root.set_point(-1)
            return
        else:
            root.set_point(0)

        next_children = root.calc_next()
        for child in next_children:
            if level <= self.__DEEPNESS:
                self.run(level + 1, child)

        if level == 0:
            self.calc_points()

    def calc_points(self, node = None):
        root = self.__node if node is None else node
        children = root.get_children()
        if len(children) > 0:
            for child in children:
                child: Node = child
                self.calc_points(child)
        else:
            parent: Node = root.get_parent()
            if parent:
                parent.set_point(parent.get_point() + root.get_point())



    def check_win(self, board, turn = 1):
        # horizontal check
        for i in range(0, 8, 3):
            if board[i] == turn and board[i+1] == turn and board[i+2] == turn:
                return True
        
        # vertical check
        for i in range(0, 3, 1):
            if board[i] == turn and board[i+3] == turn and board[i+6] == turn:
                return True

        # diagonal check
        if (board[0] == turn and board[4] == turn and board[8] == turn) or (board[2] == turn and board[4] == turn and board[6] == turn):
            return True

        return False
