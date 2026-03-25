const input = require("fs").readFileSync(0, "utf-8").trim().split("\n");
const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const x = Number(input[2]);

arr.sort((a, b) => a - b);
let [left, right] = [0, n - 1]
let count = 0

while (left < right) {
  const sum = arr[left] + arr[right]
  if (sum === x) {
    count++
    left++
    right++
  } else if (sum < x) {
    left++
  } else {
    right--
  }
}

console.log(count)