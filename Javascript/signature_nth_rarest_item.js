/*
Given a list of integers, create a function that returns the nth-rarest item. 
The function should be called nth_most_rare signature and its signarture nth_most_rate signature (list, n)
where list is the array of integers and n is the nth rarest term. 

For example in ([5,4,5,4,5,4,4,5,3,3,3,2,2,1,5]), if 2 is supplied as n, the answer is 2 as 2 is the 2nd rarest item
*/

const nth_most_rate = (list, n) => {
  let count_obj = {};

  // The foreach loop below creates an object of each item and it's number of occurrance.
  // e.g { '1': 1, '2': 2, '3': 3, '4': 4, '5': 5 }

  list.forEach((element) => {
    if (count_obj[element]) count_obj[element]++;
    else count_obj[element] = 1;
  });

  const keys = Object.keys(count_obj); // This gets all the keys in our object
  const nth_rare_item = keys.find((key) => count_obj[key] === n); // This gets the occurance / value that is the nth rare item

  /* The code below returns the nth rare item if it is a value and returns Not found if it's undefined
    You didn't mention what to return if it's not found
   */

  return nth_rare_item ? nth_rare_item : "Not found";
};

const list = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5];
const n = 2;

nth_most_rate(list, n);
