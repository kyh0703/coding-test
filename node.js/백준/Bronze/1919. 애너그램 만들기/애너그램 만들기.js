const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const a = input[0]
const b = input[1]

let arr = new Array(26).fill(0)

for (const i of a) {
  arr[i.charCodeAt(0) - 'a'.charCodeAt(0)]++
}

for (const i of b) {
  arr[i.charCodeAt(0) - 'a'.charCodeAt(0)]--
}

let answer = 0

for (let i = 0; i < 26; i++) {
  answer += Math.abs(arr[i])
}

console.log(answer)