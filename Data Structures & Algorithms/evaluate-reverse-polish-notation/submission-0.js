class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = []
        const operators = ["+", "-", "*", "/"]

        for (const token of tokens) {
            if (operators.includes(token)) {
                const right = stack.pop()
                const left = stack.pop()
                if (token === '+') {
                    stack.push(left + right)
                } else if (token === '-') {
                    stack.push(left - right)
                } else if (token === '*') {
                    stack.push(left * right)
                } else if (token === '/') {
                    stack.push(Math.trunc(left / right))
                }
            } else {
                stack.push(Number(token))
            }
        }
        
        return stack.pop()
    }
}
