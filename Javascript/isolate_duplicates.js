test = "aaaabbcdefffffffg"
//  ["aa[aa]bbcdeff[fffff]g", 2]

function isolate(test){
    let words = []; 
    let initial = [];
    let hold = "";
    let counter = 0;

    

    // For loop to get the uniques of the letters
    for (i in test){
        // Loop that goes through all the characters
        if (!initial.includes(test[i])){
                initial.push(test[i]);
                // If the letter is not in the initial, it pushes it to the array
        }
    }

    // Loop to push similar characters into a single array
    for (x in initial) {
        // going through characters in initial
        for (char in test) { // going through each word in our parameter
            if (test[char] == initial[x]){ // if they characters match, we join them together
                hold += initial[x];
            }
        }
        words.push(hold);
        hold = "";
    }

    debugger;
    // Loop to seperates them
    for (x in words){
        if (words[x].length > 2){
            hold += words[x].slice(0,2).concat('[', words[x].slice(2), ']');
            counter += 1;
        } else{
            hold += words[x];
        }
    }

    return [hold, counter];


}

// console.log(isolate("aaasssssssddddffgkkkkkuueyyryrhhsgfhjjsnnnnnnjjfmgjghjdjjjjdhyteghsjckjdheyebnfjhhgnjdfyfggbejjwtyjfjcbdgdhdjfjeeebddhdychdjsdfdsfdsflldkjkjjkcjdskjfjklfazdjmkj"))
console.log(isolate(test))