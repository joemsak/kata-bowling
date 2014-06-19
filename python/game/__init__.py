from collections import deque

class Game:
    def getScore(self, rolls):
        score = 0
        rolls = deque(rolls)
        frame_number = 1

        while frame_number < 10:
            frame  = [rolls.popleft()]
            score += self.__getPointsFromFrame(frame, rolls)
            frame_number += 1

        score += sum(rolls)

        return score

    def __getPointsFromFrame(self, frame, rolls):
        points = frame[0]

        if self.__isStrike(frame):
            points += rolls[0] + rolls[1]
        else:
            frame.append(rolls.popleft())
            points += frame[1]

            if self.__isSpare(frame):
                points += rolls[0]

        return points

    def __isStrike(self, frame): return frame[0]   == 10
    def __isSpare(self, frame):  return sum(frame) == 10
