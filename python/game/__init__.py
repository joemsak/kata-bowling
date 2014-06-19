from collections import deque

class Game:
    def getScore(self, rolls):
        score = 0
        rolls = deque(rolls)
        frame_index = 0
        while len(rolls) > 0:
            frame_index += 1
            if frame_index > 9:
                points = self.__getPointsFromTenthFrame(rolls)
                rolls.clear()
            else:
                frame  = [rolls.popleft()]
                points = self.__getPointsFromFrame(frame, rolls)
            score += points
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

    def __getPointsFromTenthFrame(self, rolls):
        return sum(rolls)

    def __isStrike(self, frame):     return frame[0] == 10
    def __isSpare(self, frame):      return sum(frame) == 10
