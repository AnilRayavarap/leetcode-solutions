// Last updated: 10/5/2025, 8:31:08 AM
let isPalindrome = function(x) {
    let result = Number(String(x).split('').reverse('').join(''))
    if(result == x) {
        return true;
    } else {
        return false;
    }
}
