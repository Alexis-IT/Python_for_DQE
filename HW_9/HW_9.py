import os
import xml.etree.ElementTree as ET
import HW_5
import HW_6
import HW_7
import HW_8


def user_choose_how_get_input():
    """ Ask user how get input information.
     Ask until user choose value from input list.
        """

    print("Please choose how get input information:")
    print("1. From file")
    print("2. Manual write")
    print("3. From JSON file")
    print("4. From XML file")

    res = None
    while res is None:
        res = input("Enter number: ")  # read user input
        try:  # check if input is available
            if int(res) == 1:
                return "File"
            elif int(res) == 2:
                return "Manual"
            elif int(res) == 3:
                return "JSON"
            elif int(res) == 4:
                return "XML"
            else:
                print("Choose from existing options")
                res = None
        except ValueError:
            print("Input is not a number, please enter a number only")
            res = None
    return None


def get_article_info_from_xml(path_name):
    """ Divide xml by articles.
    Return list of dictionaries.
    Element of list is dictionary which contains necessary information for one article."""

    xml_file = ET.parse(path_name)
    xml_data = []
    xml_root = xml_file.getroot()
    cnt = len(xml_root.tag)
    for elements in xml_root:
        xml_dict_info = {}
        for tag in elements:
            xml_dict_info[tag.tag] = tag.text
        xml_data.append(xml_dict_info)
        cnt -= 1
        if cnt == 0:
            break
    return xml_data


def publication_from_xml_file():
    """ Publicate text from XML file. Remove input file if it was successfully processed """
    path = HW_6.user_option_for_path()
    path_name = path + "PublicationInfo.xml"
    prepare_list_of_dict = get_article_info_from_xml(path_name)
    oo = HW_6.generate_text(prepare_list_of_dict)
    with open(path + 'MyPublications.txt', 'a') as f:  # write publication into .txt file
        f.write(oo)
    os.remove(path_name)
    print(f"File info file has been deleted")
    return None


def run():
    """ The main function."""

    input_type = user_choose_how_get_input()
    if input_type == "File":
        HW_6.publication_from_file()
        HW_7.run()
    elif input_type == "Manual":
        HW_5.run()
        HW_7.run()
    elif input_type == "JSON":
        HW_8.publication_from_json_file()
        HW_7.run()
    elif input_type == "XML":
        publication_from_xml_file()
        HW_7.run()
    else:
        print("Something went wrong")


if __name__ == '__main__':
    run()
