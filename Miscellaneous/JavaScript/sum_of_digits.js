function sumOfDigits(number) {
    var numberString = number.toString();
    var sum = 0;
    for (var i = 0; i < numberString.length; i++) 
    {
        sum += parseInt(numberString[i]);
    }
    
      return sum;
    }
    
    // Example usage
    var inputNumber = 12; // You can replace this with any number
    var result = sumOfDigits(inputNumber);
    
    console.log("Sum of digits in " + inputNumber + " is: " + result);
