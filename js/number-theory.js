console.log("Algorithm Lab JavaScript loaded!");
function gcd(a, b) {
    a = Math.abs(a);
    b = Math.abs(b);
let steps = 0;
while (b !== 0) {
    let remainder = a % b;
    a = b;
    b = remainder;
    steps+=1;
}
return {
    gcd: Math.abs(a),
    steps: steps
};
}
const calculateButton = document.getElementById("calculate-btn");
calculateButton.addEventListener("click", function() {
    console.log("Button clicked!");
    let inputA = document.getElementById("number-a").value;
    let inputB = document.getElementById("number-b").value;
    if (inputA === "" || inputB === "") {
    alert("Please enter both numbers.");
    return;
}
    let a = Number(inputA);
    let b = Number(inputB);
   if (!Number.isSafeInteger(a)) {
    alert("Please enter a valid, safely sized integer for Number A.");
    return;
}
if (!Number.isSafeInteger(b)) {
    alert("Please enter a valid, safely sized integer for Number B.");
    return;
}
if (a===0 && b===0) {
    alert("GCD is undefined when both numbers are zero.");
    return;
}
    console.log(a, b);
    const resultsDiv = document.getElementById("results");
    let result = gcd(a, b);
    console.log(result.gcd);
    console.log(result.steps);
    document.getElementById("gcd-value").textContent = result.gcd;
    document.getElementById("steps-value").textContent = result.steps;
});