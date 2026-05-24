class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const set = new Set(nums)
        let longest = 0

        for (const num of set) {
            if (set.has(num - 1)) continue;

            let current = num
            let length = 1

            while (set.has(current + 1)) {
                length++
                current++
            }

            longest = Math.max(longest, length);
        }

        return longest
    }
}
