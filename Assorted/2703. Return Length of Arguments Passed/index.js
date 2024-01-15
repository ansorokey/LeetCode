/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
	// a function that only needs to count the number of args passed in to the function
    // when '...' is used in the parameter list, it represents a variable number of args
    // could be 0, could be 100
    // can only come at the end of the parameter list, passed into function as an array

    let numArgs = 0;

    for(let arg in args) {
        numArgs += 1;
    };

    return numArgs;
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
