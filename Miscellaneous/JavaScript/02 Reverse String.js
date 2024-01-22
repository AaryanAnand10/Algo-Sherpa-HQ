function reverseString(){
    const str = prompt("Enter a word:");
    if (str===null || str === ""){
        alert("No word Entered");
    }
    const reversedstr = str.split('').reverse().join('');
    console.log("Reversed String:",reversedstr)
}
reverseString();