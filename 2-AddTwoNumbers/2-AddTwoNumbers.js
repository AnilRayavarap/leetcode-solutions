// Last updated: 10/5/2025, 8:31:09 AM
var addTwoNumbers = function(l1, l2) {
    let newList = new ListNode(); //creating new node.
    let ptr = newList; //create a pointer to point that node.
    let sum = 0; //initialise sum for the nodes that we aregoing to traverse
    
    //validating the nodes.
    if(l1 === null && l2 === null) {
        return 0;
    }
    if(l1 === null) {
        return l2;
    }
    if(l2 === null) {
        return l1;
    }
    
    //loop over both linked list until the largest linked list is traversed.
    while(l1 || l2) {
          if(l1 && l2) { //check if both nodes exist.
              sum += l1.val + l2.val; //add node value to sum , this sum will also
              //hold the carry of previous sum. Since we do not have the 
              //previous sum we're starting with sum = 0.
        } else if(l1) { //if l2 is reached at its end then procedd with l1;
            sum = sum+l1.val;
    } else { // if l1 is reached at its end then procedd with l2
            sum += l2.val;
    }
    
    if(sum > 9) { //check is sum is greater than 9
        let rem = sum % 10; //get the remainder and add it to a newNode
                //newList we are creating.
        /* Rem = let's sum is 12, we'll take 2 as remainder and add it to
        newlist*/
        newList.next = new ListNode(rem);
    } else {
        newList.next = new ListNode(sum);
    }
    sum = parseInt(sum/10); //we need to take carry. 
    /*In case if it double digit, eg: 12 the carry will be 1 */
    newList = newList.next;
    //treverse the nodes according to their existance.
    if(l1 && l2) {
        l1 = l1.next;
        l2 = l2.next;
    } else if(l1) { //if l1 exist
        l1 = l1.next;
    } else {    //if l2 exist
        l2 = l2.next;
    }
}


if(sum !== 0) {
    newList.next = new ListNode(sum)
    newList = newList.next;
}
return ptr.next;
};