import time

from binary_search import binary_search
from hash_table_search import hash_table
from linear_search import linear_search
from variables import names, big_names, _100k_names as large_names


def search(function, array, item, search_len="Small"):
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
    # search(binary_search, names, "Mark")
    # search(hash_table, names, "Mark")
    # search(linear_search, names, "Mark")
    #
    # # Small Search Found
    # search(binary_search, names, "Paul Stanley")
    # search(hash_table, names, "Paul Stanley")
    # search(linear_search, names, "Paul Stanley")
    #
    # # Big Search Not Found
    # search(binary_search, big_names, "Mark", "Big")
    # search(hash_table, big_names, "Mark", "Big")
    # search(linear_search, big_names, "Mark", "Big")

    # Large Search Not Found
    search(binary_search, large_names, "Paul Stanley", "Big")
    search(hash_table, large_names, "Cynthia Luna", "Big")
    search(linear_search, large_names, "Cynthia Luna", "Big")

    # Large Search Found
    search(binary_search, large_names, "Vanessa Evans", "Big")
    search(hash_table, large_names, "Vanessa Evans", "Big")
    search(linear_search, large_names, "Vanessa Evans", "Big")

"""
    Couldn't Find: Mark in Binary Search
    Elapsed time: 0.03 milliseconds small
    
    Couldn't Find: Mark in Hash Table Search
    Elapsed time: 0.06 milliseconds small
    
    Couldn't Find: Mark in Linear Search
    Elapsed time: 0.02 milliseconds small
    
    Found: Paul Stanley in Binary Search
    Elapsed time: 0.01 milliseconds small
    
    Found: Paul Stanley in Hash Table Search
    Elapsed time: 0.05 milliseconds small
    
    Found: Paul Stanley in Linear Search
    Elapsed time: 0.02 milliseconds small
    
    Couldn't Find: Mark in Binary Search
    Elapsed time: 0.02 milliseconds Big
    
    Couldn't Find: Mark in Hash Table Search
    Elapsed time: 4.37 milliseconds Big
    
    Couldn't Find: Mark in Linear Search
    Elapsed time: 1.42 milliseconds Big
    
    Couldn't Find: Cynthia Luna in Binary Search
    Elapsed time: 0.02 milliseconds Big
    
    Found: Cynthia Luna in Hash Table Search
    Elapsed time: 6.69 milliseconds Big
    
    Found: Cynthia Luna in Linear Search
    Elapsed time: 1.33 milliseconds Big
    
    Couldn't Find: Paul Stanley in Binary Search
    Elapsed time: 45.44 milliseconds Large
    
    Couldn't Find: Cynthia Luna in Hash Table Search
    Elapsed time: 28.11 milliseconds Large
    
    Couldn't Find: Cynthia Luna in Linear Search
    Elapsed time: 8.78 milliseconds Large
    
    Found: Vanessa Evans in Binary Search
    Elapsed time: 42.70 milliseconds Large
    
    Found: Vanessa Evans in Hash Table Search
    Elapsed time: 22.37 milliseconds Large
    
    Found: Vanessa Evans in Linear Search
    Elapsed time: 2.99 milliseconds Large
    
    
    Process finished with exit code 0


"""
