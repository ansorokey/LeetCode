We are given an array of integers. Our goal is to find the GREATEST common divisor between the largest and smallest values in the array.

The GCD is the largest integer thagt can divide both numbers evenly.

In order to do this, we need to find the min and max values in the array.
After finding both, we iterate from 1 to the smallest number and overwrite the largest value that divides both evenly.
Return that.
