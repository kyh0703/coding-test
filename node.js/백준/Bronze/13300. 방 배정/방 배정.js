const input = require("fs").readFileSync(0, "utf-8").trim().split("\n")
const [N, K] = input[0].split(" ").map(Number)

const boys = Array(6).fill(0)
const girls = Array(6).fill(0)

for (let i = 1; i <= N; i++) {
  const [S, Y] = input[i].split(" ").map(Number)
  if (S === 0) {
    girls[Y - 1]++
  } else {
    boys[Y - 1]++
  }
}

let count = 0

for (let i = 0; i < 6; i++) {
  count += Math.ceil(boys[i] / K)
  count += Math.ceil(girls[i] / K)
}

console.log(count)