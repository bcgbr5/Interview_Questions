using System;
using System.Collections.Generic;

namespace BowlingScoring
{
    public class BowlingScore
    {
        public List<Frame> Frames = new List<Frame>();
        
        public int ScoreGame(List<int> Rolls)
        {
            int score = 0;
            foreach(int roll in Rolls)
            {
                if (Frames.Count > 0)
                {
                    if (Frames[Frames.Count - 1].secondBall != null)//If the last frame is full
                    {
                        Frames.Add(new Frame(Frames, Frames[Frames.Count - 1]));
                        Frames[Frames.Count - 1].Roll(roll);
                    }
                    else
                    {
                        Frames[Frames.Count - 1].Roll(roll);
                    }
                }
                else
                {
                    Frames.Add(new FirstFrame());
                    Frames[0].Roll(roll);
                }
            }
            foreach (Frame frame in Frames) { score += frame.GetScore(); }
            return score;
        }
    }

    public class Frame
    {
        public List<Frame> containingList;
        public int? firstBall = null;
        public int? secondBall = null;
        public int? SpareBonus  = 0;
        public int? StrikeBonus = 0;  
        public bool isSpare = false;
        public bool isStrike = false;
        public Frame lastFrame;
        public virtual void Roll(int pins)
        {
            if(firstBall == null)
            {
                firstBall = pins;
                if(firstBall == 10)
                {
                    isStrike = true;
                    secondBall = 0;
                }
                if(lastFrame.isStrike && lastFrame.SpareBonus != null)
                {
                    lastFrame.StrikeBonus += pins;
                }
                else if((lastFrame.isSpare||lastFrame.isStrike && lastFrame.SpareBonus == null)
                {
                    lastFrame.StrikeBonus += pins;
                }
            }
            else if(isStrike == false)
            {
                secondBall = pins;
                if(secondBall + firstBall == 10)
                {
                    isSpare = true;
                }
                if (lastFrame.isStrike)
                {
                    lastFrame.bonus += pins;
                }
            }
            else
            {
                containingList.Add(new Frame());

            }
        }
        public int GetScore()
        {
            return (firstBall ?? 0) + (secondBall ?? 0) +  bonus;
        }
        public Frame(List<Frame> containingList, Frame lastFrame)
        {
            this.lastFrame = lastFrame;
            this.containingList = containingList;
        }
        public Frame()
        {

        }
    }

    public class FirstFrame : Frame
    {
        public override void Roll(int pins)
        {
            if (firstBall == null)
            {
                firstBall = pins;
                
            }
            else if (isStrike == false)
            {
                secondBall = pins;
            }
        }
    }

    public class LastFrame : Frame
    {
        public override void Roll(int pins)
        {
            /*TODO*/
        }
    }

}
