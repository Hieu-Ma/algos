/**
 * @param {number} x
 * @return {boolean}
 */

/* Clarification
    return true or false if the number is the same forwards and             backwards
*/

/* Setup sample I/O's identify edge cases 
    
*/

/* Approach (O(n)
    use toString on x
    loop through each character
    add characters to a empty string
    if the new string is equivalent to the toString method we used on x
    return true
    else return false
*/

/* Psuedocode
    let stringX = x.toString();
    let reverse = "";
    for(stringX.length -> 0) {
        reverse += stringX[i]
    }
    return reverse === stringX
*/

var isPalindrome = function(x) {
   let stringX = x.toString();
   let reverse = "";
   for(let i = stringX.length - 1; i >= 0; i--) {
       reverse += stringX[i];
   }
   return reverse === stringX;
};