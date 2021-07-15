/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

/* Clarification
    move the last item in the array to the front k amount of times
*/

/* Approach (O(n))
    for loop
    pop method and the unshift method
*/

/* PC
    loop(0 - k - 1)
        let lastNum = nums.pop();
        nums.unshift(lastNum);
    return nums;
*/

var rotate = function(nums, k) {
    

    // console.log("length before we sliced", nums.length)
    if(nums.length < k) {
        for(let i = 0; i < k; i++) {
            let lastNum = nums.pop();
            nums.unshift(lastNum);
        }
         return nums;
    }
    let lastNumbers = nums.splice(nums.length - (k));
    // console.log(lastNumbers)
    // console.log("length after we sliced", nums.length)
    // console.log(nums.length)
    nums.unshift(...lastNumbers);

    return nums;
};