from collections import deque

class Game:
    def getScore(self, rolls):
        score = 0
        frame = []
        rolls = deque(rolls)

        while len(rolls) > 0:
            points   = 0
            frame[:] = []

            if self.__isTenthFrame(rolls):
                points = sum(rolls)
                rolls.clear()
            else:
                frame.append(rolls.popleft())
                points = frame[0]
                if self.__isStrike(frame):
                    points += rolls[0] + rolls[1]
                else:
                    frame.append(rolls.popleft())
                    points += frame[1]
                    if self.__isSpare(frame):
                        points += rolls[0]
            score += points

        return score

    def __addToScore(self, points):  self.score += points
    def __isTenthFrame(self, rolls): return len(rolls) <= 3
    def __isStrike(self, frame):     return frame[0] == 10
    def __isSpare(self, frame):      return sum(frame) == 10
