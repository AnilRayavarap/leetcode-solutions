// Last updated: 10/5/2025, 8:31:04 AM
class MyStack  {
    constructor() {
        this.q1 = [];
        this.q2 = [];
    }


push(x) {
    this.q2.push(x);

    while(this.q1.length > 0) {
        this.q2.push(this.q1.shift());
    }

    [this.q1, this.q2] = [this.q2, this.q1];
}

pop() {
    return this.q1.shift();
}

top() {
    return this.q1[0];
}

empty() {
    return this.q1.length === 0;
}

}

const myStack = new MyStack();
myStack.push(1);
myStack.push(2);
console.log(myStack.top());
console.log(myStack.pop());
console.log(myStack.empty());