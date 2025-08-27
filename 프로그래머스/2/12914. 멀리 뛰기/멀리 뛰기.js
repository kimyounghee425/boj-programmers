// 이동할 칸 수 n

function nCk(n, k) { // 5, 3
    let result = 1n
    k = Math.min(n, n - k)
    for (let i = 1; i <= k; i++) {
        result = (result * BigInt(n - k + i)) / BigInt(i)
    }
    return result
}

function solution(n) {
    let answer = 1n;
    
    // 조합?
    // 2가 1개일 때 2개일 때, .... n/2 개 일 떄로 나누어서 그냥 합하면 되나?
    
    if (n === 1) {
        return Number(answer % 1234567n);
    } 
    
    for (let i = 1; i * 2 <= n; i++) {
        answer += nCk(n-i, i)
    }
    
    return Number(answer % 1234567n);
}