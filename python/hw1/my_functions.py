# ISABELLA HENSON-VENDRELL

#Function 1
def sum_list(numbers):

    """
    create two python functions  the first function should take a 
    list as an input parameter and return an integer. The second function 
    can include any number of input parameters and return whatever you d like.
    """

    return sum(numbers)

#Function 2
def second_parameter(* args):
    #Creat and empty dictionary to store counts in its own argument
    counts = {}
    for num in args:
        # if the number doesn't exist in the dictionary, we intialize it to 0 and add 1
        counts[num] = counts.get(num,0) + 1
    return counts
   
# Test functions  
print("Testing for sum_list:")
print(sum_list([1, 2, 3, 4, 5]))  ## Expected output: 15
print(sum_list([-10, 20, -30, 40]))  # Expected output: 20
print(sum_list([7, 8, 9]))  # Expected output: 24

print("\nTesting for second_parameter:")
print(second_parameter(1, 2, 2, 3, 3, 3))  # Expected output: {1: 1, 2: 2, 3: 3}
print(second_parameter("grape", "banana", "grape", "orange", "banana", "grape"))  # Expected output: {'grape': 3, 'banana': 2, 'orange': 1}
print(second_parameter(True, False, True, True, True))  # Expected output: {True: 4, False: 1}
