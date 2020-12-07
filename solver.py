#!/usr/bin/env python3


from board import Board
from command import Command
from element import Element
import random

""" This class should contain the movement generation algorithm."""
class DirectionSolver:

    def __init__(self):
        self._board = None

    def get(self, board_string):
        self._board = Board(board_string)
        return self.next_command()

    """ Implement your logic here """
    def next_command(self):
      #  _command = Command('RIGHT').to_string()
      #  print(self._board.to_string())
      #  print("Sending Command: {}\n".format(_command))
      #  return _command
        _command = Command('RIGHT').to_string()
        print(self._board.to_string())
        #print("hero - ", self._board.get_hero())
        heroPlace = self._board.get_hero()
        exitPlace = self._board.get_exits()
        #print(type(exitPlace[0]))
        print("hero x-", heroPlace.get_x())
        print("hero y-", heroPlace.get_y())
        print("exit x-", exitPlace[0].get_x())
        print("exit_y-", exitPlace[0].get_y())
        #wallinR = False

        wallinR_PointList = self._board._find_all(Element('WALL_RIGHT'))
        print("wall in right", wallinR_PointList)

        angleinR_PointList = self._board._find_all(Element('ANGLE_IN_RIGHT'))
        print("anglr in right", angleinR_PointList)

        wbl_PointList = self._board._find_all(Element('WALL_BACK_ANGLE_LEFT'))
        print("WALL_BACK_ANGLE_LEFT", wbl_PointList)

        wbr_PointList = self._board._find_all(Element('WALL_BACK_ANGLE_RIGHT'))
        print("anglr in right", wbr_PointList)

        wl_PointList = self._board._find_all(Element('WALL_LEFT'))
        print("WALL_LEFT", wl_PointList)

        angleinL_PointList = self._board._find_all(Element('ANGLE_IN_LEFT'))
        print("ANGLE_IN_LEFT", angleinL_PointList)

        empty_PointList = self._board._find_all(Element('EMPTY'))
      #  print("you can go ", empty_PointList)
        

        #wallinL = self._board._find_all(Element('WALL_LEFT'))
        #print("wall in left", wallinL)
        #wallinF = self._board._find_all(Element('WALL_FRONT'))
        #print("wall in front", wallinF)
        #wallinB = self._board._find_all(Element('WALL_BACK'))
        #print("wall in back", wallinB)
       # space = self._board._find_all(Element('SPACE'))
       # print("space in", space)

        hinx = heroPlace.get_x()
        hiny = heroPlace.get_y()
        exinx = exitPlace[0].get_x()
        exiny = exitPlace[0].get_y()
        #whatinR = self._board.get_at(hinx, hiny)
        #print("in R", whatinR)
        #righthend = [hinx+1,hiny]
        righthend = []
        righthend.insert(0,hinx+1)
        righthend.insert(1,hiny)

        print("rh-",righthend)
        blockedway = False
        rightclear = False
        leftclear = False
        upclear = False
        downclear = False

        if(self._board.is_at(hinx + 1, hiny,Element('WALL_RIGHT'))):
            blockedway = True
            print("wall in righthend")
        if(self._board.is_at(hinx + 1, hiny, Element('ANGLE_IN_RIGHT'))):
            blockedway = True
            print("angle in right")
        if(self._board.is_at(hinx + 1, hiny, Element('WALL_BACK_ANGLE_LEFT'))):
            blockedway = True
            print("wall angle")

        if(self._board.is_at(hinx + 1, hiny, Element('EMPTY'))):
            rightclear = True
        if(self._board.is_at(hinx - 1, hiny, Element('EMPTY'))):
            leftclear = True  
        if(self._board.is_at(hinx, hiny + 1, Element('EMPTY'))):
            upclear = True
        if(self._board.is_at(hinx - 1, hiny, Element('EMPTY'))):
            downclear = True


       # print(type(wallinRList[1]))      
       # if (righthend in wallinRList):
            #wallinR = True
       #     print("dont go to right")

        
        if(hinx < exinx and not blockedway):
            _command = Command('RIGHT').to_string()
        elif(hiny < exiny):
            _command = Command('DOWN').to_string()
        elif(hinx > exinx):
            _command = Command('LEFT').to_string()
        elif(hiny > exiny):
            _command = Command('UP').to_string()
        else:
            waylist = ['UP','DOWN','LEFT','RIGHT']
            randway = random.choice(waylist)
            print("rand command",randway)
            _command = Command(randway).to_string()

                
        print("Sending Command: {}\n".format(_command))
        return _command


if __name__ == '__main__':
    raise RuntimeError("This module is not intended to be ran from CLI")
