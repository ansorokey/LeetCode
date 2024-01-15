/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    // essentially, we want to returna new array that's double the given array
    // any element at index i should also be at index i + n where n is the length of nums

    let ans = new Array(nums.length * 2);
    for(let i = 0; i < nums.length; i++) {
        ans[i] = nums[i];
        ans[i + nums.length] = nums[i];
    }

    return ans;
};
