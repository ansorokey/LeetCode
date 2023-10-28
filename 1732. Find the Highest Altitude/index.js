// var largestAltitude = function(gain) {
//     let altitudes = new Array(gain.length + 1);

//     // the first point is always 0
//     altitudes[0] = 0;
//     let lastAlt = 0;
//     let maxAlt = altitudes[0];

//     for(let i = 0; i < gain.length; i++) {
//         altitudes[i + 1] = lastAlt + gain[i];
//         lastAlt = altitudes[i + 1];

//         if(lastAlt > maxAlt) maxAlt = lastAlt;
//     }

//     return maxAlt;
// };

// refactor: do we really need to store an array of all the values?
//we don't need t ostore values, we just need to keep track of the largest one
var largestAltitude = function(gain) {
    // the first point is always 0
    let lastAlt = 0;
    //if we only have one point, then the highest point is the only point
    let maxAlt = 0;

    //we iterate through gains
    for(let i = 0; i < gain.length; i++) {
        let newAlt = lastAlt + gain[i];
        lastAlt = altitudes[i + 1];

        if(newAlt > maxAlt) maxAlt = lastAlt;
    }

    return maxAlt;
};

console.log(largestAltitude([-5,1,5,0,-7]))
