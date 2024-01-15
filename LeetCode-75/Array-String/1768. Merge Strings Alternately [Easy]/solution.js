function mergeAlternately(word1, word2) {
    let i = k = j = 0
    
    res = new Array(word1 + word2)

    while( i < word1.length | j < word2.length) {
        if( !!word1[i] ) {
            res[k] = word1[i]
            i += 1;
            k += 1;
        }

        if( !!word2[j] ) {
            res[k] = word2[j]
            j += 1;
            k += 1;
        }        
    }

    console.log(res.join(''))
};

mergeAlternately('cat', 'dog') // 'cdaotg'

// Submission 1:
// time: 58ms - 31.14%
// space: 43.8mb - 5.53%