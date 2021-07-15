/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */

/* Clarification
    move zero's to the end of the array
*/

/* Psuedo Code
    1. loop through the array
    2. if curr num is zero, splice it
    3. push the spliced number into the nums array
    4. return nums array
*/
var moveZeroes = function(nums) {
   for(let i = 0; i < nums.length; i++) { //nums is 0
       if(nums[i] === 0) { //nums[0] === 0
           let zero = nums.splice(i, 1);
           nums.push(zero);
           i--;
       }
   }
   return nums;
};