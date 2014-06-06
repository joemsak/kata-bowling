from collections import deque

class Game:
    def getScore(self, rolls):
        score = 0
        rolls = deque(rolls)
        while len(rolls) > 0:
            if self.__isTenthFrame(rolls):
                points = sum(rolls)
                rolls.clear()
                score += points
            else:
                frame  = [rolls.popleft()]
                score += frame[0]
                score += self.__getScoreFromFrame(rolls, frame)

        return score

    def __getScoreFromFrame(self, rolls, frame):
        if    self.__isStrike(frame): return rolls[0] + rolls[1]
        else: frame.append(rolls.popleft())
        if    self.__isSpare(frame):  return frame[1] + rolls[0]
        else:                         return frame[1]

    def __isTenthFrame(self, rolls): return len(rolls) <= 3
    def __isStrike(self, frame):     return frame[0] == 10
    def __isSpare(self, frame):      return sum(frame) == 10
