const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const n = Number(input[0]);
const students = [];

for (let i = 1; i <= n; i++) {
    const [name, dd, mm, yyyy] = input[i].split(" ");
    students.push({ name, day: Number(dd), month: Number(mm), year: Number(yyyy) });
}

students.sort((a, b) => {
    if (a.year !== b.year) return a.year - b.year;
    if (a.month !== b.month) return a.month - b.month;
    if (a.day !== b.day) return (a.day = b.day);
});

console.log(students[n - 1].name); // 가장 적은 사람
console.log(students[0].name); // 가장 많은 사람
