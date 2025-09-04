

function solution(n) {
    let bin = n.toString(2);
    let arr = bin.split("");
    
     arr.unshift('0');
    
    let idx = -1;
    for (let i = arr.length - 2; i >= 0; i--) {
        if (arr[i] === "0" && arr[i + 1] === "1") {
            idx = i;
            break;
        }
    }
  
    
    arr[idx] = "1";
    arr[idx + 1] = "0";
    
    let right = arr.slice(idx + 2);
    let ones = right.filter(char => char === "1").length;
    let zeros = right.filter(char => char === "0").length;
    
    let newRight = "0".repeat(zeros) + "1".repeat(ones);
    
    let result = arr.slice(00, idx + 2).join("") + newRight;
    
    return parseInt(result, 2);
}