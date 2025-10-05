// Last updated: 10/5/2025, 8:31:04 AM
function isValid(s) {
    const stack = [];
    const pairs = {
        ")" : "(",
        '}' : "{",
        "]" : "["
    }
    for(let ch of s) {
        if(ch === "(" || ch === "{" || ch === "[") {
            stack.push(ch);
        } else{
           let last = stack.pop();
           if(last !== pairs[ch]) {
            return false;
           }
        }
    }
    return stack.length === 0;
}
