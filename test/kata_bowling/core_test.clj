(ns kata-bowling.core-test
  (:require [clojure.test :refer :all]
            [kata-bowling.core :refer :all :as game]))

(defn assert-scored [score rolls]
  (is (= score (game/score rolls))))

(deftest all-gutters-scores-zero-test
  (testing "Rolling all gutters will score 0"
    (assert-scored 0 (repeat 20 0))))

(deftest all-ones-will-score-twenty-test
  (testing "Rolling all 1s will score 20"
    (assert-scored 20 (repeat 20 1))))

(deftest a-spare-followed-by-three-and-gutters-scores-sixteen-test
  (testing "Roll a spare followed by 3 then all gutters scores 16"
    (let [rolls (concat [5 5 3] (repeat 17 0))]
      (assert-scored 16 rolls))))

(deftest all-gutter-spares-scores-one-hundred-test
  (testing "A game of all gutter-spares scores 100"
    (assert-scored 100 (take 20 (cycle [0 10])))))

(deftest all-nine-spares-with-nine-scores-one-hundred-ninety-test
  (testing "A game of all 9-spares with a 9 on 10th frame scores 190"
    (let [nine-spares (take 20 (cycle [9 1]))]
      (assert-scored 190 (concat nine-spares [9])))))

(deftest a-strike-followed-by-gutters-scores-ten
  (testing "A strike with all gutters will score 10"
    (assert-scored 10 (concat [10] (repeat 18 0)))))

(deftest a-strike-followed-by-two-and-two-then-gutters-scores-eighteen-test
  (testing "A strike, 2, 2, then all gutters, will score 18"
    (assert-scored 18 (concat [10 2 2] (repeat 16 0)))))

(deftest perfect-game-test
  (testing "A game of all strikes is 300"
    (assert-scored 300 (repeat 12 10))))

(deftest a-crazy-game-test
  (testing "A couple complex games"
    (let [first-nine-frames [10 4 5 0 9 5 3 10 10 4 5 8 2 3 0]] ;113
      (assert-scored 143 (concat first-nine-frames [10 10 10]))
      (assert-scored 133 (concat first-nine-frames [3 7 10]))
      (assert-scored 120 (concat first-nine-frames [1 6])))))
