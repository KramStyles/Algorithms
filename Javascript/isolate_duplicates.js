test = "aaaabbcdefffffffg"
//  ["aa[aa]bbcdeff[fffff]g", 2]

function isolate(){
    let words = [];
    let initial = [];
    let hold = "";
    let counter = 0;

    for (i in test){
        if (!initial.includes(test[i])){
                initial.push(test[i]);
        }
    }

    for (x in initial) {
        for (char in test) {
            if (test[char] == initial[x]){
                hold += initial[x];
            }
        }
        words.push(hold);
        hold = "";
    }

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

console.log(isolate("aaasssssssddddffgkkkkkuueyyryrhhsgfhjjsnnnnnnjjfmgjghjdjjjjdhyteghsjckjdheyebnfjhhgnjdfyfggbejjwtyjfjcbdgdhdjfjeeebddhdychdjdjmkj"))