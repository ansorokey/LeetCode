var moveZeroes = function(nums) {
    let cur = 0;
    let zero1 = -1;

    while(cur < nums.length) {

        if(nums[cur] === 0) {

            if(zero1 === -1) {
                zero1 = cur;
            }

        } else {
            if(zero1 > -1) {
                [nums[zero1], nums[cur]] = [nums[cur], nums[zero1]]
                let temp = zero1;
                zero1 = -1;
                cur = temp;
            }

        }

        cur += 1;
    }
};

let nums = [0,1,0,3,12]
console.log(nums);
moveZeroes(nums);
console.log(nums);
