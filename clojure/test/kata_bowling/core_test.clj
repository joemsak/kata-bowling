(ns kata-bowling.core-test
  (:require [clojure.test :refer :all]
            [kata-bowling.core :refer :all :as game]))

(defn assert-scored [score rolls]
  (is (= score (game/score rolls))))

(deftest simple-games-test
  (testing "Rolling all gutters will score 0"
    (assert-scored 0 (repeat 20 0)))

  (testing "Rolling all 1s will score 20"
    (assert-scored 20 (repeat 20 1))))

(deftest spare-games-test
  (testing "Roll a spare followed by 3 then all gutters scores 16"
    (assert-scored 16  (concat [5 5 3] (repeat 17 0))))

  (testing "A game of all gutter-spares scores 100"
    (assert-scored 100 (take 20 (cycle [0 10]))))

  (testing "A game of all 9-spares with a 9 on 10th frame scores 190"
    (let [nine-spares (take 20 (cycle [9 1]))]
      (assert-scored 190 (concat nine-spares [9])))))

(deftest strikes-games-test
  (testing "A strike with all gutters will score 10"
    (assert-scored 10 (concat [10] (repeat 18 0))))

  (testing "A strike, 2, 2, then all gutters, will score 18"
    (assert-scored 18 (concat [10 2 2] (repeat 16 0))))

  (testing "A perfect game is 300"
    (assert-scored 300 (repeat 12 10))))

(deftest integration-test
  (testing "A couple complex games"
    (let [first-nine-frames [10 4 5 0 9 5 3 10 10 4 5 8 2 3 0]] ;113
      (assert-scored 143 (concat first-nine-frames [10 10 10]))
      (assert-scored 133 (concat first-nine-frames [3 7 10]))
      (assert-scored 120 (concat first-nine-frames [1 6])))))
