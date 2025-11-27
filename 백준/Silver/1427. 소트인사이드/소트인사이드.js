const fs = require("fs");

const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const main = () => {
    let N = Number(input[0]);
    let stringN = String(N);
    let answer = ""
    let arr = stringN.split("");
    arr.sort((a, b) => {
        return b - a;
    });
    
    for (let i = 0; i < arr.length; i++) {
        answer = answer + arr[i]
    }

    console.log(answer)
};

main();
