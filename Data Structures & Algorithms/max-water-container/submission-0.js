class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0;
        let right = heights.length - 1;
        let maxWater = 0;

        while (left < right) {
            const width = right - left;
            const height = Math.min(heights[left], heights[right])
            const water = width * height

            maxWater = Math.max(maxWater, water)

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxWater;
    }
}
