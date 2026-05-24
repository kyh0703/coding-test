class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = []

        for (const i of s) {
            if (i === '(' || i === '[' || i === '{') {
                stack.push(i)
            } else if (i === ')' || i === ']' || i === '}') {
                const v = stack.pop()
                if (i === ')' && v !== '(') return false 
                if (i === ']' && v !== '[') return false
                if (i === '}' && v !== '{') return false
            }
        }

        return stack.length === 0
    }
}
