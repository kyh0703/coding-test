function solution(rank, attendance) {
    const extract = []
    for (let i = 0; i < rank.length; i++) {
   		if (attendance[i]) {
    		extract.push({rank: rank[i], index: i})
        }
    }
    
    const [a, b, c] = extract.sort((a, b) => a.rank - b.rank)
   	return 10000 * a.index + 100 * b.index + c.index 
}