(ns kata-bowling.core)
(declare score-frame advance-frame)

(defn score [game-rolls]
  (loop [score 0 rolls game-rolls]
    (cond (empty? rolls) score
          :else (recur (+ score (score-frame rolls))
                       (advance-frame rolls)))))

(defn spare? [rolls]
  (= 10 (+ (first rolls) (second rolls))))

(defn strike? [rolls]
  (= 10 (first rolls)))

(defn bonus-ball-rolled? [rolls]
  (= 3 (count rolls)))

(defn rolls-to-score [rolls]
  (if (or (spare? rolls) (strike? rolls)) 3 2))

(defn rolls-to-drop [rolls]
  (cond (bonus-ball-rolled? rolls) 3
        (strike? rolls) 1
        :else 2))

(defn score-frame [rolls]
  (reduce + (take (rolls-to-score rolls) rolls)))

(defn advance-frame [rolls]
  (drop (rolls-to-drop rolls) rolls))
