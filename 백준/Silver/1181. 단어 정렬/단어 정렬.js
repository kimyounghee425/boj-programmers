const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const sortFn = (a, b) => {
    if (a.length > b.length) return 1;
    else if (a.length === b.length) {
        if (a === b) arr.pop(a);
    }
};

const solution = (arr) => {
    arr.sort((a, b) => {
        if (a.length !== b.length) return a.length - b.length;
        return a.localeCompare(b);
    });

    const answer = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== arr[i + 1]) {
            answer.push(arr[i]);
        }
    }

    for (let i = 0; i < answer.length; i++) {
        console.log(answer[i]);
    }
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
