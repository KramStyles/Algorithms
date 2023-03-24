import time

from binary_search import binary_search
from hash_table_search import hash_table
from linear_search import linear_search
from variables import names, big_names, _100k_names as large_names


def search(function, array, item, search_len="Small: Len(130)"):
    """
    This function runs a search using the algorithmic function given to it.
    It returns time taken to find a statement depending on the function used.
    """
    # Start measuring time
    start_time = time.perf_counter()

    # Run search algorithm
    function(array, item)

    # Calculate and display time elapsed
    end_time = time.perf_counter()
    elapsed = (end_time - start_time) * 1000
    print("Elapsed time: {:.2f} milliseconds {}\n".format(elapsed, search_len))


if __name__ == "__main__":
    # Small Search Not Found
    search(hash_table, names, "Mark")
    search(linear_search, names, "Mark")

    # Sort names for Binary Search
    names = sorted(names)
    search(binary_search, names, "Mark")

    # Small Search Found
    search(hash_table, names, "Paul Stanley")
    search(linear_search, names, "Paul Stanley")

    # Sort names for Binary Search
    names = sorted(names)
    search(binary_search, names, "Paul Stanley")

    # Big Search Not Found
    search(hash_table, big_names, "Mark", "Big : Len(13,000)")
    search(linear_search, big_names, "Mark", "Big : Len(13,000)")

    # Sort names for Binary Search
    big_names = sorted(big_names)
    search(binary_search, big_names, "Mark", "Big : Len(13,000)")

    # Big Search Found
    search(hash_table, big_names, "Cynthia Luna", "Big : Len(13,000)")
    search(linear_search, big_names, "Cynthia Luna", "Big : Len(13,000)")

    # Sort names for Binary Search
    big_names = sorted(big_names)
    search(binary_search, big_names, "Cynthia Luna", "Big : Len(13,000)")

    # Large Search Not Found
    search(hash_table, large_names, "Cynthia Luna", "Large : Len(100,000)")
    search(linear_search, large_names, "Cynthia Luna", "Large : Len(100,000)")

    # Sort names for Binary Search
    large_names = sorted(large_names)
    search(binary_search, large_names, "Paul Stanley", "Large : Len(100,000)")

    # Large Search Found
    search(hash_table, large_names, "Vanessa Evans", "Large : Len(100,000)")
    search(linear_search, large_names, "Vanessa Evans", "Large : Len(100,000)")
    
    # Sort names for Binary Search
    large_names = sorted(large_names)
    search(binary_search, large_names, "Vanessa Evans", "Large : Len(100,000)")

"""
    SPEED REPORT
    
    Couldn't Find: Mark in Hash Table Search
    Elapsed time: 0.12 milliseconds Small: Len(130)

    Couldn't Find: Mark in Linear Search
    Elapsed time: 0.02 milliseconds Small: Len(130)
    
    Couldn't Find: Mark in Binary Search
    Elapsed time: 0.01 milliseconds Small: Len(130)
    
    Found: Paul Stanley in Hash Table Search
    Elapsed time: 0.03 milliseconds Small: Len(130)
    
    Found: Paul Stanley in Linear Search
    Elapsed time: 0.01 milliseconds Small: Len(130)
    
    Found: Paul Stanley in Binary Search
    Elapsed time: 0.01 milliseconds Small: Len(130)
    
    Couldn't Find: Mark in Hash Table Search
    Elapsed time: 3.88 milliseconds Big : Len(13,000)
    
    Couldn't Find: Mark in Linear Search
    Elapsed time: 0.88 milliseconds Big : Len(13,000)
    
    Couldn't Find: Mark in Binary Search
    Elapsed time: 0.03 milliseconds Big : Len(13,000)
    
    Found: Cynthia Luna in Hash Table Search
    Elapsed time: 3.03 milliseconds Big : Len(13,000)
    
    Found: Cynthia Luna in Linear Search
    Elapsed time: 0.22 milliseconds Big : Len(13,000)
    
    Found: Cynthia Luna in Binary Search
    Elapsed time: 0.02 milliseconds Big : Len(13,000)
    
    Couldn't Find: Cynthia Luna in Hash Table Search
    Elapsed time: 30.58 milliseconds Large : Len(100,000)
    
    Couldn't Find: Cynthia Luna in Linear Search
    Elapsed time: 9.07 milliseconds Large : Len(100,000)
    
    Couldn't Find: Paul Stanley in Binary Search
    Elapsed time: 0.04 milliseconds Large : Len(100,000)
    
    Found: Vanessa Evans in Hash Table Search
    Elapsed time: 27.61 milliseconds Large : Len(100,000)
    
    Found: Vanessa Evans in Linear Search
    Elapsed time: 12.16 milliseconds Large : Len(100,000)
    
    Found: Vanessa Evans in Binary Search
    Elapsed time: 0.04 milliseconds Large : Len(100,000)

"""
