/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
	// a function that only needs to count the number of args passed in to the function

    let numArgs = 0;

    for(let arg in args) {
        numArgs += 1;
    };

    return numArgs;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
