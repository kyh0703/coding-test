class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map()

        for (const s of strs) {
            const key = [...s].sort().join('');

            if (!map.has(key)) {
                map.set(key, [])
            }

            map.get(key).push(s)
        }

        return [...map.values()]
    }
}
