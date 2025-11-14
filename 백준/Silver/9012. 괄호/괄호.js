const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");
const T = Number(input[0]);

for (let i = 0; i < T; i++) {
    const s = input[i + 1].trim();

    let stack = [];
    let ok = true;

    for (let char of s) {
        // "("" 받으면 스택에 넣기
        if (char === "(") {
            stack.push(char);
        } else {
            if (stack.length === 0) {
                // ")" 받았는데 스택이 비어있을 때
                ok = false;
                break;
            }
            stack.pop();
        }
    }

    if (stack.length !== 0) {
        ok = false;
    }
    console.log(ok ? "YES" : "NO");
}
