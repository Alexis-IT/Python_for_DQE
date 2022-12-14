from string import ascii_lowercase  # give the lowercase letters
from random import randint, choice  # choice() - returns a randomly selected element from the specified sequence
                                    # randint() - method returns an integer number selected element from the specified range

def generate_random_dict():
    """ Generate dictionary with random number of pairs.

        Key: random lowercase latin letter
        Value: random integer number in range from 0 to 100
    """

    numb_pairs = randint(1, 26)  # As exist 26 letter, we can have from 1 to 26 keys in dict.

    # # Alternative way for generate list of dict
    # key_values = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # inner_dict = { key_values[randint(0, 25)]: randint(0, 100) for i in range(numb_pairs)}

    inner_dict = {}

    while len(inner_dict) < numb_pairs:  # Generated keys for dict should be unique.
        inner_dict.update({choice(ascii_lowercase): randint(0, 100)})

    return inner_dict


def list_of_dict():
    """ Create list of dict.

    Elements of list are generated by outer function generate_random_dict().
    """

    n = randint(2, 10)                      # how much list elements will be created
    list_of_random_dict = [generate_random_dict() for i in range(n)]

    return list_of_random_dict


# Part2

def count_keys(some_dict_list):
    """ Return dict which count keys entry in list of dicts
    Key: key from dict from list of dicts
    Value: count how much times key appears in different dictionaries from list.
    """
    dict_key = {}
    for dict in some_dict_list:
        for key in dict:
            if key in dict_key.keys():
                dict_key[key] = dict_key[key] + 1
            else:
                dict_key[key] = 1

    return dict_key


def max_keys(some_dict_list):
    """ Return dict which count max value of keys entry in list of dicts
    Key: key from dict from list of dicts
    Value: max value of key in list of dicts
    """
    dict_key_result_max = {}
    for dict in some_dict_list:
        for key, value in dict.items():
            if key in dict_key_result_max.keys():
                dict_key_result_max[key] = max(dict_key_result_max[key], value)
            else:
                dict_key_result_max[key] = value

    return dict_key_result_max


def index_max_keys(some_dict_list):
    """ Return dict which count index of max value of keys entry in list of dicts
    Key: key from dict from list of dicts
    Value: index of max value of key in list of dicts
    """
    dict_key_result_index = {}
    for dict in some_dict_list:
        for key, value in dict.items():
            if value == max_keys(some_dict_list)[key]:
                dict_key_result_index[key] = some_dict_list.index(dict) + 1

    return dict_key_result_index


def dict_key_info(some_dict_list):
    """ Return dictionary with information about keys entry in list of dicts

    Key: key from dict from list of dicts
    Value: list [count of key, max value for correspond key, in which dict (index of dict) exist max value for
    correspond key]
    """
    dict_info = {}
    for dict in some_dict_list:
        for key in dict:
            dict_info[key] = [count_keys(some_dict_list)[key], max_keys(some_dict_list)[key],
                              index_max_keys(some_dict_list)[key]]
    return dict_info


def result_function(some_dict_list):
    """ Return one common dict from input list of dicts:

    if dicts have same key, we will take max value, and rename key with dict number with max value
    if key is only in one dict - take it as is.
    """
    result_dict = {}
    dict_info = dict(sorted(dict_key_info(some_dict_list).items()))
    for key, value in dict_info.items():
        if value[0] == 1:
            result_dict[key] = value[1]
        else:
            result_dict[key + "_" + str(value[2])] = value[1]

    return result_dict


generated_list_of_dict = list_of_dict()

print(*generated_list_of_dict, sep='\n')
print('result: ', result_function(generated_list_of_dict))

