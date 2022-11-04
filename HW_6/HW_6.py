import os
import HW_5
import HW_3


def find_between(some_string, first, last=False):
    """ Return substring between first and last substrings.
        Requirement argument: some_string - input text (type string),
        first - from where start get necessary substring
        last - end point get necessary substring, by default take by the end of input text."""
    try:
        start = some_string.index(first) + len(first)
        if last:
            end = some_string.index(last, start)
        else:
            end = len(some_string)
        return some_string[start:end]
    except ValueError:
        return ""


def get_article_info(input_text):
    """ Divide input_text by articles.
    Return list of dictionaries.
    Element of list is dictionary which contains necessary information for one article."""

    text = input_text.split("\n--------------------")
    info = []
    for i in text:
        article = {}
        news_type_i = find_between(i, "news_type: ", "\npublication_text:")
        article["news_type"] = news_type_i
        publication_text_i = find_between(i, "publication_text: ", "\nadditional_info:")
        article["publication_text"] = publication_text_i
        additional_info_i = (find_between(i, "additional_info: "))
        article["additional_info"] = additional_info_i
        info.append(article)
    return info


def generate_text(some_list_of_dict):
    """ Transform list of dictionary into text for publishing.
    Each dictionary convert into corespondent article view according to class: News, Privat Ad, Weather.
    Text for publication fixes by using function normalize_letter_cases(text)"""

    fin = ''
    for article_item in some_list_of_dict:
        #print(article_item)
        news_type = article_item["news_type"]
        publication_text = HW_3.normalize_letter_cases(article_item["publication_text"])
        additional_info = article_item["additional_info"]

        match news_type:
            case "News":
                city_news = additional_info
                obj = HW_5.News('News', publication_text, city_news)
                ready_text = obj.for_publish()
            case "Privat Ad":
                exp_date = additional_info
                obj = HW_5.PrivatAd('Privat Ad', publication_text, exp_date)
                ready_text = obj.for_publish()
            case "Weather":
                obj = HW_5.Weather('Weather', publication_text)
                ready_text = obj.for_publish()
        fin = fin + ready_text
    return fin


def user_option_for_path():
    """ Return path info: user choose it will be default folder or user provided file path"""

    user_path = None
    while user_path is None:
        user_info = input('Would you like provided file path? \n'
                          'Yes \n'
                          'No (If you said "No" will be used default path) \n')
        if user_info == "Yes":
            user_path = input('Write file path: \n')
            user_path = user_path + "\\"
        elif user_info == "No":
            user_path = ''
        else:
            print("Input is not correct, please write 'Yes' or 'No'")

    return user_path


def user_choose_how_get_input():
    """ Ask user how get input information: from file or from manual write.
     Ask until user choose value from input list.
        """

    print("Please choose how get input information:")
    print("1. From file")
    print("2. Manual write")

    res = None
    while res is None:
        res = input("Enter number: ")  # read user input
        try:  # check if input is available
            if int(res) == 1:
                return "File"
            elif int(res) == 2:
                return "Manual"
            else:
                print("Choose from existing options")
                res = None
        except ValueError:
            print("Input is not a number, please enter a number only")
            res = None
    return None


def publication_from_file():
    """ Publicate text from file. Remove input file if it was successfully processed """
    path_name = user_option_for_path()
    try:
        my_text = open(path_name + "PublicationInfo.txt")
    except Exception as e:
        print(f"Such file path {path_name} doesn't contain correspond file. {e}")

    try:
        a = my_text.read()
        prepare_list_of_dict = get_article_info(a)

        oo = generate_text(prepare_list_of_dict)
        with open(path_name + 'MyPublications.txt', 'a') as f:  # write publication into .txt file
            f.write(oo)
        my_text.close()
        os.remove(path_name + "PublicationInfo.txt")
        print(f"File info file has been deleted")
    except Exception as e:
        print(f"Something went wrong. {e}")


def run():
    """ The main function."""

    input_type = user_choose_how_get_input()
    if input_type == "File":
        publication_from_file()
    elif input_type == "Manual":
        HW_5.run()
    else:
        print("Something went wrong")


if __name__ == '__main__':
    run()
