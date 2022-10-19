
from enum import Enum

class Result(Enum):
    EQUAL = 0
    WINS = 1
    LOSES = 2 

class Play(object):
    """
    Represents a play
    """
    def description(self):
        pass

    def compare(self, otherPlay):
        """
        It compares itself with the other play and returns a Result
        """
        pass

class Paper(Play):
    
    def description(self):
        return "Paper"

    def compare(self, otherPlay):
        """
        Compares paper agains other plays and returns a Result
        """
        result = None
        if type(otherPlay) == Paper:
            result = Result.EQUAL
        elif type(otherPlay) == Scissors:
            result = Result.LOSES
        else:
            result = Result.WINS
        return result

class Scissors(Play):

    def description(self):
        return "Scissors"

    def compare(self, otherPlay):
        """
        Compares scissor agains other plays and returns a Result
        """
        result = None
        if type(otherPlay) == Paper:
            result = Result.WINS
        elif type(otherPlay) == Scissors:
            result = Result.EQUAL
        else:
            result = Result.LOSES
        return result

class Rock(Play):

    def description(self):
        return "Rock"

    def compare(self, otherPlay):
        """
        Compares scissor agains other plays and returns a Result
        """
        result = None
        if type(otherPlay) == Paper:
            result = Result.LOSES
        elif type(otherPlay) == Scissors:
            result = Result.WINS
        else:
            result = Result.EQUAL
        return result

# r = Rock()
# p = Paper()
# s = Scissors()
# print(s.compare(p))