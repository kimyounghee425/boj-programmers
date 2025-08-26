// function solution(s){
//     let count = 0;
//     for (let char of s) {
//         if (char === "(") {
//             count ++;
//         } else {
//             count --;
//         }
//         // 중간에 닫는괄호 더 많아지면 false
//         if (count < 0) return false
//     }
//     return (count === 0)
// }


// 스택을 사용한 풀이
function solution(s) {
    const stack = []
    for (let char of s) {
        if (char === "(") {
            stack.push("(");
        } else {
            if (stack.length === 0) return false
            stack.pop()
        }
    }
    return stack.length === 0
}