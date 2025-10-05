// Last updated: 10/5/2025, 8:31:06 AM
class MyQueue  {
    constructor() {
        this.s1 = [];
        this.s2 = [];
    }
    push(x) { //pushing element to the back of Queue
        this.s1.push(x);
    }
    //Remove and return the front element.
    pop() {
        if(this.s2.length === 0) {
            while(this.s1.length > 0) {
                this.s2.push(this.s1.pop());
            }
        }
        return this.s2.pop();   
    }
    peek() { //Get the front element without removing it.
        if(this.s2.length === 0) {
            while(this.s1.length > 0) {
                this.s2.push(this.s1.pop());
            }
        }
        return this.s2[this.s2.length - 1];
    }
    //checking if Queue is empty.
    empty() {
        return this.s1.length === 0 && this.s2.length === 0;
    }

}

const myQueue = new MyQueue();
myQueue.push(1);
myQueue.push(2);
myQueue.peek();
myQueue.peek();
myQueue.pop();
myQueue.empty();