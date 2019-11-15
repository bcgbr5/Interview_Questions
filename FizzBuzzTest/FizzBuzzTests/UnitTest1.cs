using Microsoft.VisualStudio.TestTools.UnitTesting;
using FizzBuzzNS;
using System.Collections.Generic;
using System.Linq;

namespace FizzBuzzTests
{
    [TestClass]
    public class FizzBuzzTest
    {
        [TestMethod]
        public void ReturnNumber()
        {
            var sut = new FizzBuzz();
            Assert.AreEqual("2", sut.ProccessNumber(2));
        }
		[TestMethod]
		public void ReturnFizz()
		{
            var sut = new FizzBuzz();
            Assert.AreEqual("Fizz", sut.ProccessNumber(3));
        }
		[TestMethod]
		public void ReturnBuzz()
		{
            var sut = new FizzBuzz();
            Assert.AreEqual("Buzz", sut.ProccessNumber(5));
        }
		[TestMethod]
		public void ReturnFizzBuzz()
		{
            var sut = new FizzBuzz();
            Assert.AreEqual("FizzBuzz", sut.ProccessNumber(15));
        }

        [TestMethod]
        public void ReturnProccess1Through5()
        {
            var sut = new FizzBuzz();
            List<int> testList = new List<int>(Enumerable.Range(1, 15));
            string[] temp = { "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz" };
            List<string> expected = new List<string>(temp);
            //List<string> actual = new List<string>(temp);
            List<string> actual = sut.ProccessInput(testList);
            CollectionAssert.AreEqual(expected, actual);
        }

    }
}
