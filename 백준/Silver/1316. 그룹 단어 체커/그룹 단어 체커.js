const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");
/**
 * 단어 길이가 1이면 그룹 단어
 *
 * 2이상이면
 * 같은 알파벳이 서로 인접한 인덱스에 없으면 그룹 단어 아님.
 *
 */
const checkGroup = (word) => {
    const visited = new Set();

    let prev = "";

    for (let char of word) {
        if (char !== prev) {
            if (visited.has(char)) {
                return false;
            }
            visited.add(char);
        }
        prev = char;
    }
    return true;
};

const solution = (arr) => {
    let answer = 0;
    for (let i = 0; i < arr.length; i++) {
        if (checkGroup(arr[i])) answer++;
    }
    console.log(answer)
};

const main = () => {
    let N = Number(input[0]);
    let arr = [];
    for (let i = 1; i < N + 1; i++) {
        arr.push(input[i]);
    }
    solution(arr);
};

main();
