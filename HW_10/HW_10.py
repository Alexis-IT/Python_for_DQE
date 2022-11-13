import sqlite3
import HW_6


def is_table_exists(table_name):
    cursor.execute(f"SELECT count(1) FROM pragma_table_info('{table_name}')")
    return int(cursor.fetchone()[0]) > 0


def is_duplicate(table_name, datadict):
    query = f"SELECT COUNT(*) FROM {table_name} WHERE text = '{datadict['publication_text']}' AND additional_info = '{datadict['additional_info']}'"
    print(query)
    cursor.execute(query)
    return int(cursor.fetchone()[0]) > 0


connection = sqlite3.connect('newsfeed.db')
cursor = connection.cursor()


def create_table(table_name):
    if not is_table_exists(table_name):
        query = f"""CREATE TABLE {table_name}
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
          text string,
          additional_info string);"""
        cursor.execute(query)


path_name = HW_6.user_option_for_path()
try:
    my_text = open(path_name + "NewPublicationInfo.txt")
except Exception as e:
    print(f"Such file path {path_name} doesn't contain correspond file. {e}")

try:
    a = my_text.read()
    prepare_list_of_dict = HW_6.get_article_info(a)
    print(prepare_list_of_dict)
except Exception as e:
    print(f"Something went wrong. {e}")


for article in prepare_list_of_dict:
    table_name = article['news_type']
    print(table_name)
    create_table(table_name)
    if not is_duplicate(table_name, article):
        cursor.execute(f"INSERT into {table_name} ('text','additional_info') Values('{article['publication_text']}', '{article['additional_info']}')")
    cursor.execute(f"Select * From {table_name}")
    result = cursor.fetchall()
    print(result)
    connection.commit()
