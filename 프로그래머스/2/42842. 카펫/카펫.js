function solution(brown, yellow) {
    var answer = [];
    // 노란색 가로:m 세로:n
    // m*n = yellow
    
    // 2m+2n+4 = brown
    
    // m 과 n 은 yellow 의 약수
    // yellow 의 약수부터 구하기.
    
    // 세로 n 돌리기
    for (let n = 1; n*n <= yellow; n++) {
        if (yellow % n !== 0) continue;
        
        // 가로 m
        let m = yellow / n
        
        if ((2*m + 2*n + 4) === brown) {
            answer.push(m+2)
            answer.push(n+2)
            break
        } else {continue}
        
    }
    
    return answer;
}