class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = {};

        for (let i = 0; i < nums.length; i++) {
            const n = nums[i]
            const diff = target - n

            if (map[diff] !== undefined) {
                return [map[diff], i];
            }

            map[n] = i
        }
    }
}
