class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.toLocaleLowerCase().replace(/[^a-z0-9]/g, "")
        const mid = Math.floor(s.length / 2)
        for (let i = 0; i < mid; i++) {
            if (s[i] !== s[s.length - 1 - i])
                return false
        }
        return true
    }
}