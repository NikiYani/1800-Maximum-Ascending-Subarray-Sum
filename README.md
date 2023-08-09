# 1800. Maximum Ascending Subarray Sum

Given an array of positive integers nums, return the maximum </br>
possible sum of an ascending subarray in nums. </br>

A subarray is defined as a contiguous sequence of numbers in an array. </br>

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for </br>
all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending. </br>

## Example 1:

Input: nums = [10,20,30,5,10,50] </br>
Output: 65 </br>
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65. </br>

## Example 2:

Input: nums = [10,20,30,40,50] </br>
Output: 150 </br>
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150. </br>

## Example 3:

Input: nums = [12,17,15,13,10,11,12] </br>
Output: 33 </br>
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33. </br>

## Constraints:

1 <= nums.length <= 100 </br>
1 <= nums[i] <= 100 </br>
