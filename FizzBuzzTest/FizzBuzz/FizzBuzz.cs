using System;
using System.Collections.Generic;


namespace FizzBuzzNS
{
    public class FizzBuzz
    {
        public String ProccessNumber(int input)
        {
            string result = "";
            /*The obvious followup is how to do this without the double comparison*/
            if (input % 3 == 0)
            {
                result += "Fizz";
            }
            if (input % 5 == 0)
            {
                result += "Buzz";
            }
            if (result == "")
            {
                return input.ToString();
            }
            return result;
        }
        public List<string> ProccessInput(List<int> inputs)
        {
            List<string> results = new List<string>();
            foreach(int input in inputs)
            {
                results.Add(ProccessNumber(input));
            }
            return results;
        }
    }
    public class ModifiedFizzBuzz : FizzBuzz //This isn't strictly neccisary. I'm doing it so the old tests remain valid
    {
        public new String ProccessNumber(int input)
        {
            string result = "";
            /*The obvious followup is how to do this without the double comparison*/
            if (input % 3 == 0 || input.ToString().Contains("3"))
            {
                result += "Fizz";
            }
            if (input % 5 == 0 || input.ToString().Contains("5"))
            {
                result += "Buzz";
            }
            if (result == "")
            {
                return input.ToString();
            }
            return result;
        }
        public new List<string> ProccessInput(List<int> inputs)
        {
            List<string> results = new List<string>();
            foreach (int input in inputs)
            {
                results.Add(ProccessNumber(input));
            }
            return results;
        }
    }
}