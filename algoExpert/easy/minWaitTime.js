/* Clarification 
	adding the total amount of time, that the elements have to wait.
*/

/* Edge Cases 
	1. Will we be given elements that aren't numbers?
*/

/* Approach
	1. have a value that stores the running sum
	2. loop through queries, skipping first number, and adding the queue times to the running sum
	3. return running sum
	
	TC O(n) | SC O(1)
*/

/* Psuedo Code
	let runningSum = 0;
	let sum = 0;
	for(let i = 1; i < queries.length; i++) {
		if(queries[i--]) {
			queries[i--] += runningSum
		}
		sum += runningSum
	}
*/
"3 5 6 8"
"3 5 6 8 = 17"
function minimumWaitingTime(queries) {
  // Write your code here.
	let runningSum = 0;
	let sum = 0;
	for(let i = 1; i < queries.length; i++) {
		let prev = i - 1;
		if(queries[prev]) {
			runningSum += queries[prev] 
		}
		sum += runningSum
		console.log(sum)
	}
  return sum;
}

// Do not edit the line below.
exports.minimumWaitingTime = minimumWaitingTime;