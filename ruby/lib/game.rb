class Game
  def score(rolls)
    score = 0
    while rolls.size > 0 do
      if is_tenth_frame?(rolls) # this is bad, actually
        score += get_tenth_frame_score(rolls)
      else
        frame = [rolls.shift]
        score += get_frame_score(rolls, frame)
      end
    end
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

  def get_tenth_frame_score(rolls)
    points = rolls.inject(&:+)
    rolls.clear
    points
  end

  def get_strike_points(rolls)
    rolls[0] + rolls[1]
  end

  def get_spare_points(rolls)
    rolls[0]
  end

  def is_tenth_frame?(rolls)
    rolls.size <= 3
  end

  def is_strike?(frame)
    frame[0] == 10
  end

  def is_spare?(frame)
    frame[0] + frame[1] == 10
  end
end
