(ns kata-bowling.core)
(declare score-frame advance-frame)

(defn score [rolls]
  (loop [score 0 balls rolls]
    (cond (empty? balls) score
          :else (recur (+ score (score-frame balls))
                       (advance-frame balls)))))

(defn spare? [balls]
  (= 10 (+ (first balls) (second balls))))

(defn strike? [balls]
  (= 10 (first balls)))

(defn last-frame? [balls]
  (= 3 (count balls)))

(defn balls-to-score [balls]
  (if (or (last-frame? balls) (spare? balls) (strike? balls)) 3 2))

(defn balls-to-drop [balls]
  (cond (last-frame? balls) 3
        (strike? balls) 1
        :else 2))

(defn score-frame [balls]
  (reduce + (take (balls-to-score balls) balls)))

(defn advance-frame [balls]
  (drop (balls-to-drop balls) balls))
