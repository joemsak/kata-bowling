class Game
  def score(rolls)
    score = 0
    frame_number = 1 # this sucks but passes for now
    while frame_number < 10 do
      score += get_frame_score(rolls, [rolls.shift])
      frame_number += 1
    end
    score += rolls.inject(&:+)
    score
  end

  private
  def get_frame_score(rolls, frame)
    points = frame[0]
    if is_strike?(frame)
      points += get_strike_points(rolls)
    else
      frame << rolls.shift
      points += frame[1]
      points += get_spare_points(rolls) if is_spare?(frame)
    end
    points
  end

  def get_strike_points(rolls)
    rolls[0] + rolls[1]
  end

  def get_spare_points(rolls)
    rolls[0]
  end

  def is_strike?(frame)
    frame[0] == 10
  end

  def is_spare?(frame)
    frame[0] + frame[1] == 10
  end
end
