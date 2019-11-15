using System;
using System.Collections.Generic;

namespace FizzBuzzNS
{
    public class FizzBuzz
    {
        public String ProccessNumber(int input)
        {
            if (input % 3 == 0 && input % 5 == 0)
            {
                return ("FizzBuzz");
            }
            else if (input % 3 == 0)
            {
                return ("Fizz");
            }
            else if (input % 5 == 0)
            {
                return ("Buzz");
            }
            else
            {
                return input.ToString();
            }
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
}