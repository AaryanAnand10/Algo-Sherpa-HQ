function findLargestNumber(numbers) {
  if (numbers.length === 0) return "Array is empty";
  return Math.max(...numbers);
}

// Example usage
var numbersArray = [5, 12, 8, 22, 10];
var result = findLargestNumber(numbersArray);

console.log("The largest number is: " + result);
