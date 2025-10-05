// Last updated: 10/5/2025, 8:31:05 AM
  var inorderTraversal = function(root) {
    let result = [];
    let stack = [];
    let current = root;

    while(current !== null || stack.length > 0) {
        
        //Going leftmost node.
        while(current !== null) {
            stack.push(current);
            current = current.left;
        }
         //root node
         current = stack.pop(); 
         result.push(current.val);

         //go to right
         current = current.right;

    }

    return result;
}