/**
 * @param {string} s
 * @return {number}
 */

/* Clarification
    increase count whenever characters don't repeat
*/

/* Sample I/O's and Edge Cases 
*/

/* Approach
    initialize a variable that stores a string
    intialize a variable that stores a count
    intialize a variable that stores the max
    loop through the string
    if next element isn't included in stored string,               increase count
    if it does include, reset count, store count into max,     reset string
    return max
*/

/* Psuedo Code
    let currStr = "";
    let count = 0;
    let max = 0;
    for(i -> s.length)
        if(ele isn't repeated) push into currStr
        else if (ele is repeated) {
            reset count
            store count into max
            reset string to ""
        }
    return max
*/

var lengthOfLongestSubstring = function(s) {
   let currStr = "";
   let count = 0;
   let max = 0;
   for(let i = 0; i < s.length; i++) {
       if(!currStr.includes(s[i])) {
           currStr += s[i];
           count++;
       } else {
           // count++;

           max = currStr.length;
           count = 0;
           currStr = "";
       }
   }
   return max;
};