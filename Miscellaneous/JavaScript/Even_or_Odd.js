function checkEvenOrOdd(number) {
    if (number % 2 === 0) {
      return "Even";
    } else {
      return "Odd";
    }
  }
  
  // Example usage
  var inputNumber = 10; // You can replace this with any number you want to check
  var result = checkEvenOrOdd(inputNumber);
  
  console.log(inputNumber + " is " + result)
