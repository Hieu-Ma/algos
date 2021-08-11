# function isPalindrome(string) {
# //   // Write your code here.
# 	let newStr = ''
# 	for(let i = string.length - 1; i >= 0; i--) {
# 		newStr += string[i]
# 	}
# 	return newStr == string
# }

# // Do not edit the line below.
# exports.isPalindrome = isPalindrome;


"""
Clarification

Check if string is the same forwards and backwards
"""
"""
Approach

TC O(n^2) | SC O(n)

for loop
	pop off the end of the string, save it to a new string
return the comparison of input string with the new string
"""
"""
Pseudo Code
	newStr = ''
	for i in range(len(string), 0, -1):
		newStr.append(string[i])
	return newStr == string
"""

# def isPalindrome(string):
#     # Write your code here.
# 	newStr = ''
# 	for i in range(len(string) - 1, -1, -1):
# 		newStr += string[i]
# 	return newStr == string


def isPalindrome(string):
    # Write your code here.
    left = 0
	right = len(string) - 1

	while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
	return True
