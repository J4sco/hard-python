def revert(input_list):
    result_list = []
    for i in range (len(input_list)):
        result_list.append(input_list[len(input_list)-1-i])
    return result_list 

def is_positive(n):
    if n >= 0: result = True
    else: result = False
    return result

def no_duplicates(input_list):
    result_list = []
    element_set = set()
    for element in input_list:
        if element not in element_set:
            result_list.append(element)
            element_set.add(element)
    return result_list

def is_even(n):
    if n % 2 == 0: return True
    else: return False 

def is_palindrome(input_list):
    n = len(input_list)
    temp_flag = True
    if is_even(n):
        for i in range (int(len(input_list)/2)):
            if input_list[i] != input_list[len(input_list)-1-i]: 
                temp_flag = False
    else:
        for i in range (int((len(input_list)+1)/2)):
            if input_list[i] != input_list[len(input_list)-1-i]: 
                temp_flag = False
    return temp_flag

def factorial(n):
    fact = 1
    if n == 0: 
        return fact
    else:
        for number in range(1, n+1):
            fact = fact * number
    return fact
    

def main():
    print("\nBegin funciton-testing script\n")

    print("First function to be tested: \"revert(list)\"")
    a = input("Insert the elements of a list divided by commas: ").split(",")
    b = revert(a)
    print(("The input list is {}").format(a))
    print(("The reverted list is {}").format(b))

    print("\nSecond function to be tested: \"is_positive(int)\"")
    n = int(input("Insert a number: "))
    if is_positive(n):
        print(("The number {} is positive").format(n))
    else: print("The number is negative")

    print("\nThird function to be tested: \"no_duplicates(list)\"")
    a = input("Insert the elements of a list divided by commas: ").split(",")
    b = no_duplicates(a)
    print(("The input list is {}").format(a))
    print(("The list with no duplicates is {}").format(b))

    print("\nFourth function to be tested: \"is_palindrome(list)\"")
    a = input("Insert the elements of a list divided by commas: ").split(",")
    print(("The input list is {}").format(a))
    if is_palindrome(a):
        print("The list is palindrome")
    else: print("The list is not palindrome")

    print("\nFifth function to be tested: \"factorial(int)\"")
    n = int(input("Insert a number: "))
    print(("The factorial of {} is {}.").format(n, factorial(n)))

# Execute `main()` function 
if __name__ == '__main__':
    main()