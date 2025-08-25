const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();
const N = parseInt(input);

/**
 * M + (M 의 각 자리수 합) = N
 * N자리 수의 각 자리 수 합의 최댓값 = 9 * N
 *
 * M의 범위는
 * N - 9 * 자리수 <= M < N
 *
 * N - 9 * 자리수 부터 N-1 까지 루프 돌면서, 생성지 구함.
 *
 *  */

const digits = String(N).length;
let start = Math.max(1, N - 9 * digits);
let answer = 0;

function digitSum(x) {
    let sum = 0;
    while (x) {
        sum += x % 10;
        x = Math.floor(x / 10);
    }
    return sum;
}
for (let m = start; m < N; m++) {
    if (m + digitSum(m) === N) {
        answer = m;
        break;
    }
}
console.log(answer);
