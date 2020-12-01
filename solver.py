#!/usr/bin/env python3


from board import Board
from command import Command

""" This class should contain the movement generation algorithm."""
class DirectionSolver:

    def __init__(self):
        self._board = None

    def get(self, board_string):
        self._board = Board(board_string)
        return self.next_command()

    """ Implement your logic here """
    def next_command(self):
        #_command = Command('RIGHT').to_string()
        print(self._board.to_string())
        #print("hero - ", self._board.get_hero())
        heroPlace = self._board.get_hero()
        exitPlace = self._board.get_exits()
        #print(type(exitPlace[0]))
        print("hero x-", heroPlace.get_x())
        print("hero y-", heroPlace.get_y())
        print("exit x-", exitPlace[0].get_x())
        print("exit_y-", exitPlace[0].get_y())

        print(self._board.get_walls())       

        hinx = heroPlace.get_x()
        hiny = heroPlace.get_y()
        xinx = exitPlace[0].get_x()
        xiny = exitPlace[0].get_y()

        if(hinx < xinx):
            _command = Command('RIGHT').to_string()
        elif(hiny < xiny):
            _command = Command('DOWN').to_string()
        elif(hinx > xinx):
            _command = Command('LEFT').to_string()
        elif(hiny > xiny):
            _command = Command('UP').to_string()
        

        print("Sending Command: {}\n".format(_command))
        return _command


if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
