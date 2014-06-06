require './lib/game'

describe Game do
  describe '#score' do
    let(:game)  { Game.new }
    let(:rolls) { [] }

    subject { game.score(rolls) }

    context 'when all gutters' do
      let(:rolls) { [0, 0] * 10 }
      it { should be_zero }
    end

    context 'when all 1s' do
      let(:rolls) { [1, 1] * 10 }
      it { should eq(20) }
    end

    context 'when a spare then one, then all gutters' do
      let(:rolls) { [1, 9] + [1, 0] + ([0, 0] * 8) }
      it { should eq(12) }
    end

    context 'when a strike then ones, then all gutters' do
      let(:rolls) { [10] + [1, 1] + ([0, 0] * 8) }
      it { should eq(14) }
    end

    context 'a perfect game' do
      let(:rolls) { [10] * 12 }
      it { should eq(300) }
    end

    context 'complex games' do
      let(:first_nine_frames) { [10, 10, 10, 10, 5, 5, 6, 4, 10, 10, 10] }

      context 'tenth frame all strikes' do
        let(:rolls) { first_nine_frames + [10, 10, 10] }
        it { should eq(261) }
      end

      context 'tenth frame has spare' do
        let(:rolls) { first_nine_frames + [5, 5, 10] }
        it { should eq(236) }
      end

      context 'tenth frame has no spare' do
        let(:rolls) { first_nine_frames + [5, 4] }
        it { should eq(224) }
      end
    end
  end
end
