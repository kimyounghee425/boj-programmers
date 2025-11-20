const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const main = () => {
    let [N, M] = input[0].split(" ").map(Number);
    let count = 0;
    let index = 1;
    const S = new Set();

    for (let i = 0; i < N; i++) {
        S.add(input[index]);
        index++;
    }

    for (let i = 0; i < M; i++) {
        if (S.has(input[index])) {
            count++;
        }
        index++;
    }
    console.log(count)
};

main();
