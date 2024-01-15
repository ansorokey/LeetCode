var numIdenticalPairs = function(nums) {
    let output = 0;

    let valOccur = {};

    for(let i = 0; i < nums.length; i++) {
        let cur = nums[i];
        // console.log(cur);

        if(cur in valOccur) {
            valOccur[cur] += 1;
        } else {
            valOccur[cur] = 1;
        }
    }

    function reverseFactorial(num) {
        let output = 0;
        for(let i = num; i > 1; i--) {
            output += i - 1;
        }
        return output;
    }

    for(key in valOccur) {
        if(valOccur[key] >= 2) {
            output += reverseFactorial(valOccur[key]);
        }
    }

    return output;
};

let tests = [
[1,2,3,1,1,3],
[1,1,1,1],
[1,2,3]]

tests.forEach(t => console.log(numIdenticalPairs(t)));
