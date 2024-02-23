/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

var merge = function(nums1, m, nums2, n) {
    // The nums given are already sorted from low to high values
        // The last n elements of nums1 are an exception, as those are spots we will be replacing
    //The goal is to merge the arrays nums1 and nums2 together into nums1 so that nums1 contains all the elements from both arrays, sorted and increasing
    // we do not return a new value, test results will check the reference value of nums1

    //first, a brute force approach
    //let's tackel this as though we were merging into a new array

    //to do that, we would need an array to store results
    //let output = [];

    // to be ever so slightly more efficient, let's declare the output array to be the exact size we need it to be. This will save a little bit of space reallocation when the array needs to dynamically resize;
    //remeber that the length of the final array should be the given length of the two integer arrays - m and n
    let output = new Array(m + n);

    //now we'd like to iterate through each array and perform a merge action on one value at a time
    //we can use two pointers to reference the index of the values as we iterate
    let p1 = 0;
    let p2 = 0;

    //let's also keep track of the current index of the output
    let cur = 0;

    //we don't know exactly which value we will be adding, so we don't have a set number of times to iterate. LEt's use a for loop, with the condition being the pointer is less than the length of the array
    while(p1 < m || p2 < n) {
        //since we're using an OR conditional, we want to make sure the value we're currently at is within bounds
        if(p1 >= m && p2 < n) {
            output[cur] = nums2[p2];
            p2 += 1;
        } else if(p2 >= n && p1 < m) {
            output[cur] = nums1[p1];
            p1 += 1;
        } else {
            if(nums1[p1] < nums2[p2]) {
                output[cur] = nums1[p1];
                p1 += 1;
            } else {
                output[cur] = nums2[p2];
                p2 += 1;
            }
        }

        // regardless of the action taken, move to the next spot
        cur += 1;
    }

    // now that we have a working output array, how can we turns nums 1 into the output while keeping reference?
    // we can iterate and write over the elements in num1 with the elements of the output
    for(let i = 0; i < nums1.length; i++) {
        nums1[i] = output[i];
    }
};

// nums1, m, nums2, m,
let tests = [
    [[1,2,3,0,0,0], 3, [2,5,6], 3]
]

tests.forEach(([nums1, m, nums2, n]) => {
    merge(nums1, m, nums2, n);
    console.log(nums1);
})
