import random  # import module random (function randint) for possibility generate random numbers
from statistics import mean  # import function mean for calculate average for numbers


def random_numbers(start_numb, end_numb, count):
    """Return random list
    Create list of {count} random numbers from {start_numb} to {end_numb}
    """
     rand_lst = []  # initialise list for result
    [rand_lst.append(random.randint(start_numb, end_numb)) for x in range(count)]
    # for i in range(count):  # repeat cycle {count} times
    #     rand_lst.append(
    #         random.randint(start_numb, end_numb))  # add random int number from [start_numb, end_numb] to result list
    return rand_lst  # return result list

def insertion_sort(lst):
    """Sort list from min to max by using insertion method."""
    length = len(lst)  # get length of input list
    for i in range(1, length):  # begin from second till last element of list
        key = lst[i]  # mark element of list
        j = i  # use additional index
        while (j - 1 >= 0) and (lst[j - 1] > key):  # check conditions for comparing previous elements in list
            lst[j - 1], lst[j] = lst[j], lst[j - 1]  # swap the elements if the previous conditions are met
            j = j - 1  # decrease index for check previous elements
        lst[j] = key  # put {key} element in correct(sorted) position
    return lst  # return sorted list as result


def even_numb(lst):
    """ Get list of even numbers from input list of integer numbers."""
    even = []  # initialise list for result
    for i in range(len(lst)):  # the cycle passes on each item of list
        if lst[i] % 2 == 0:  # check condition if element is even
            even.append(lst[i])  # if condition is True, add element to result list
    return even  # return list of even numbers as result


def odd_numb(lst):
    """ Get list of odd numbers from input list of integer numbers."""
    odd = []  # initialise list for result
    for i in range(len(lst)):  # the cycle passes on each item of list
        if lst[i] % 2 != 0:  # check condition if element is odd
            odd.append(lst[i])  # if condition is True, add element to result list
    return odd  # return list of odd numbers as result


my_list = random_numbers(0, 1000, 100)  # generate list of 100 random numbers from 0 to 1000
# my_list = [1, 3, 5]         # uncomment for test only

insertion_sort(my_list)  # sort list from min to max

#  print result of calculation average of even numbers
try:
    print('Average of even numbers: ', mean(even_numb(my_list)))
except Exception as e:
    print(f'Something went wrong (even_numb): {e}')  # print exception reason

#  print result of calculation of odd numbers
try:
    print('Average of odd numbers: ', mean(odd_numb(my_list)))
except Exception as e:
    print(f'Something went wrong (even_numb): {e}')  # print exception reason
