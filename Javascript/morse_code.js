const MORSE_CODE = {
    "-.-.--": "!",
    ".-..-.": '"',
    "...-..-": "$",
    ".-...": "&",
    ".----.": "'",
    "-.--.": "(",
    "-.--.-": ")",
    ".-.-.": "+",
    "--..--": ",",
    "-....-": "-",
    ".-.-.-": ".",
    "-..-.": "/",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "---...": ":",
    "-.-.-.": ";",
    "-...-": "=",
    "..--..": "?",
    ".--.-.": "@",
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "..--.-": "_",
    "...---...": "SOS",
};

test1 = "-.. . -.-. .- -.. . ...- ..."
test2 = "-.. . -.-. .- -.. . ...-   ..."

function morse(code) {
    if (code.search('   ') > -1) {
        word = '';
        code = code.split('   ');
        code.forEach(words => {
            // debugger;
            let initial = "";
            words = words.split(' ')
            words.forEach(letter => {
                initial += MORSE_CODE[letter];
            });
            word += (initial + " ");
        });
    } else {
        code = code.split(' ');
        word = "";
        code.forEach(symbol => {
            word += MORSE_CODE[symbol]
        });
    }

    return word.trim();

}