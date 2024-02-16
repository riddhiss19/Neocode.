function factorial(n) {
    let result = 1;
    let currentNumber = 1;
    while (currentNumber <= n) {
        result *= currentNumber;
        currentNumber++;
    }
    return result;
}

console.log(factorial(5)); // Calculates and prints the factorial of 5
