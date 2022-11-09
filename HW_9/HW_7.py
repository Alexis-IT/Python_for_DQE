import re
import csv


def counter_of_words_in_text(some_text):
    """Calculate number of words in text.
        Return dictionary where key - word
        value - counter of this word in text """

    my_text = re.findall(r'([A-Za-z]+)', some_text)
    cnt_words = {}
    for word in my_text:
        if word.lower() not in cnt_words.keys():
            cnt_words[word.lower()] = 1
        else:
            cnt_words[word.lower()] += 1
    return cnt_words


def counter_of_letters_from_text(some_text):
    """Calculate number of letters in text.
        Return dictionary where key - letter
        value - list [counter of this letter in text, count upper case of this letter in text,
                        percentage of this letter in text] """

    my_text = re.findall(r'([A-Za-z]+)', some_text)
    text_letters = ''.join(my_text)
    cnt_all_letters = {}
    cnt_uppercase = {}
    for letter in text_letters:
        if letter.lower() not in cnt_all_letters.keys():
            cnt_all_letters[letter.lower()] = 1
            if letter.isupper():
                cnt_uppercase[letter.lower()] = 1
        else:
            cnt_all_letters[letter.lower()] += 1
            if letter.isupper():
                cnt_uppercase[letter.lower()] = 1
    for key, values in cnt_all_letters.items():    # generate final result about letter info
        if key in cnt_uppercase:
            cnt_all_letters[key] = [values, cnt_uppercase[key], round(values / len(text_letters) * 100, 2)]
        else:
            cnt_all_letters[key] = [values, 0, round(values / len(text_letters) * 100, 2)]
    return cnt_all_letters


def run():
    """ The main function."""

    my_file = open("MyPublications.txt", 'r').read()
    csv.register_dialect('my_dialect', delimiter='-', lineterminator='\n', quoting=csv.QUOTE_NONE)

    with open("Words_info.csv", 'w') as file:
        writer = csv.writer(file, 'my_dialect')
        words_info = counter_of_words_in_text(my_file)
        for key in words_info.keys():
            writer.writerow([key, str(words_info[key])])

    with open("Letters_info.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['letter', 'count_all', 'count_uppercase', 'percentage'])
        letters_info = counter_of_letters_from_text(my_file)
        for key in letters_info.keys():
            writer.writerow([key, letters_info[key][0], letters_info[key][1], letters_info[key][2]])


if __name__ == '__main__':
    run()
