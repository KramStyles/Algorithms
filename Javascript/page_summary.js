function amountOfPages(summary){
    // Every book has n amount of pages. You will be given the summary which was made by adding 
    // up the number of digits contained in each page number in a book(from 1 to n). 
    // The task is to find how many pages a book has- n.

    // Example
    // When input is 25 (summary). The output must be 17(n). 
    // There are 9 one-digit pages and 8 two-digit pages(8 ones and 8 digits from 0 to 7)

    // Be aware that you'll get enormous books having up to 100.000 pages.

    // All input will be valid
    let pageCount = 0;
    let itr = 0;
    
    while (summary != pageCount){
      itr++;
      pageCount += String(itr).length
    }
    
    return itr
  }