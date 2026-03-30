const fs = require('fs')
const input = fs.readFileSync(0, 'utf-8').trim().split('\n')

const [N, K] = input[0].split(' ').map(Number)
const arr = input[1].split(' ').map(Number)

let left = 0
let answer = 0
const count = new Map()

for (let right = 0; right < N; right++) {
  const val = arr[right]

  count.set(val, (count.get(val) || 0) + 1)
  while (count.get(val) > K) {
    const leftVal = arr[left]
    count.set(leftVal, count.get(leftVal) - 1)
    left++
  }

  answer = Math.max(answer, right - left + 1)
}

console.log(answer)
