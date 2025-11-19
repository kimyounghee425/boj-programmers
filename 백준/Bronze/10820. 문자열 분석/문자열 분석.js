const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").split("\n");

const solution = (text) => {
    let lower = 0;
    let upper = 0;
    let digit = 0;
    let space = 0;

    for (ch of text) {
        if ("0" <= ch && ch <= "9") digit++;
        else if ("A" <= ch && ch <= "Z") upper++;
        else if ("a" <= ch && ch <= "z") lower++;
        else if (ch === " ") space++;
    }

    return `${lower} ${upper} ${digit} ${space}`;
};

const main = () => {
    input.pop()
    for (let line of input) {
        console.log(solution(line));
    }
};

main();
