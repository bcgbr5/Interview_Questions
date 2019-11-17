using System;
using System.Collections.Generic;

namespace BowlingScoring
{
    public class BowlingGame
    {
        public List<Frame> Frames = new List<Frame>();
        
        public int ScoreGame(List<int> Rolls)
        {
            int score = 0;
            foreach(int roll in Rolls)
            {
                if (Frames.Count > 0)
                {
                    if (Frames[Frames.Count - 1].secondBall != null || Frames[Frames.Count - 1].isStrike)//If the last frame is full
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
        public int? FirstBonusBall  = null;
        public int? SecondBonusBall = null;  
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
                if(lastFrame.isStrike && lastFrame.FirstBonusBall != null)
                {
                    lastFrame.SecondBonusBall = pins;
                }
                else if((lastFrame.isSpare||lastFrame.isStrike) && lastFrame.FirstBonusBall == null)
                {
                    lastFrame.FirstBonusBall = pins;
                    if (containingList.Count >= 3 && containingList[containingList.Count - 3].isStrike && containingList[containingList.Count - 3].SecondBonusBall == null)
                    {
                        containingList[containingList.Count - 3].SecondBonusBall = pins;
                    }
                }
            }
            else if(isStrike == false)
            {
                secondBall = pins;
                isSpare |= secondBall + firstBall == 10;
                if (lastFrame.isStrike)
                {
                    lastFrame.SecondBonusBall = pins;
                }
            }
            else//This shouldn't ever get triggered, but essentially, if we somehow get here, this just adds a new Frame and rolls adds the score to it
            {
                containingList.Add(new Frame(containingList, this));
                containingList[containingList.Count - 1].Roll(pins);

            }
        }
        public int GetScore()
        {
            return (firstBall ?? 0) + (secondBall ?? 0) + (SecondBonusBall ?? 0) + (FirstBonusBall ?? 0);
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
                isStrike |= firstBall == 10;
                
            }
            else// (isStrike == false)
            {
                secondBall = pins;
                isSpare |= firstBall + secondBall == 10;
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
