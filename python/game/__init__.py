from collections import deque

class Game:
    def getScore(self, rolls):
        score = 0
        rolls = deque(rolls)
        frame_index = 0
        while len(rolls) > 0:
            frame_index += 1
            if frame_index > 9:
                points = sum(rolls)
                rolls.clear()
                score += points
            else:
                frame  = [rolls.popleft()]
                score += self.__getScoreFromFrame(rolls, frame)
        return score

    def __getScoreFromFrame(self, rolls, frame):
        points = frame[0]

        if self.__isStrike(frame):
            points += rolls[0] + rolls[1]
        else:
            frame.append(rolls.popleft())
            points += frame[1]

            if self.__isSpare(frame):
                points += rolls[0]

        return points

    def __isTenthFrame(self, rolls): return len(rolls) <= 3
    def __isStrike(self, frame):     return frame[0] == 10
    def __isSpare(self, frame):      return sum(frame) == 10
