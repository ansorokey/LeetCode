var numIdenticalPairs = function(nums) {
    //  we want to track and return the number of good pairs

    let output = 0;

    //a good pair is a number that occurs more than once, and the index of the first is less than the index of the next
    // Let's not focus on the index too much since if the number occurs more than once,
    //the next index MUST be higher than the last
    //so our first task is to iterate through the nums and keep track of each occurance

    let valOccur = {};

    for(let i = 0; i < nums.length; i++) {
        let cur = nums[i];

        if(cur in valOccur) {
            valOccur[cur] += 1;
        } else {
            valOccur[cur] += 1;
        }
    }

    //now we have a map of each value and the times they appeared in nums
    //base don the examples provides,
    //1 - 0 pairs
    //1 1 - 1 pair
    //1 1 1 - 3 pair
    // 1 1 1 1 6 pair
    5 -> 10
    // the number of pairs appears to be the unique number of combinations


    return output;
  };
