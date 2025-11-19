const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");
const T = Number(input[0]);

const solution = (text, word) => {
    let count = 0; // 단어가 나온 횟수
    let index = 0;
    while (true) {
        const found = text.indexOf(word, index);
        if (found === -1) break;

        count++;
        index = found + word.length;
    }

    return count;
};

const main = () => {
    const text = input[0].trim();
    const word = input[1].trim();

    console.log(solution(text, word));
};

main();
