import datetime
import HW_3
from random import randrange


def user_choice(items_list):
    """ Return which value user chooses from input list.
    Ask user choose value from list. Ask until user choose value from input list.
        """

    print("Please choose:")
    for idx, element in enumerate(items_list):  # print available values
        print(f"{idx + 1}. {element}")

    res = None
    while res is None:
        res = input("Enter number: ")  # read user input
        try:  # check if input is available
            result = int(res) - 1
            if 0 < int(res) <= len(items_list):
                return items_list[result]
            else:
                print("Choose from existing types")
                res = None
        except ValueError:
            print("Input is not a number, please enter a number only")
            res = None
    return None


def article(news, publication_text):
    """Gather requirement data for correspond type of publication.
    Prepare article for publication"""

    match news:
        case "News":
            city_news = input("Please write city: ")
            obj = News('News', publication_text, city_news)
            ready = obj.for_publish()
        case "Privat Ad":
            exp_date = input('Enter a date in YYYY-MM-DD format: ')
            obj = PrivatAd('Privat Ad', publication_text, exp_date)
            ready = obj.for_publish()
        case "Weather":
            obj = Weather('Weather', publication_text)
            ready = obj.for_publish()
    return ready


class Publication:
    """General publication.
    Requirement argument: name - name of publication,
    text - main text of publication."""

    def __init__(self, name, text):
        """Define object from class Publication"""
        self.name = name
        self.text = text

    def for_publish(self):
        """Preparation for publication"""
        return self.name + '-------------------------' + '\n' + self.text


class News(Publication):
    """Extend class Publication.
    Requirement argument: name - name of publication,
    text - main text of publication,
    city - city to which News is related"""

    def __init__(self, name, text, city):
        """Define object from class News"""
        Publication.__init__(self, name=name, text=text)
        self.city = city

    def for_publish(self):
        """Overwrite method for_publish(). Add city and date info"""
        now = datetime.datetime.now()
        return super(News, self).for_publish() + "\n" + self.city + ', ' + now.strftime("%Y-%m-%d %H.%M") \
               + "\n" + "------------------------------" + "\n" + "\n"


class PrivatAd(Publication):
    """Extend class Publication.
    Requirement argument: name - name of publication,
    text - main text of publication,
    actual_date - expiration date of publication"""

    def __init__(self, name, text, actual_date):
        """Define object from class PrivatAd"""
        Publication.__init__(self, name=name, text=text)
        self.actual_date = actual_date

    def __left_days(self, date_entry):
        """Calculate how long publication will be active"""
        today = datetime.date.today()
        year, month, day = map(int, date_entry.split('-'))
        date1 = datetime.date(year, month, day)
        diff = date1 - today
        return diff.days

    def for_publish(self):
        """Overwrite method for_publish(). Add expiration date and long publication will be active"""
        return super(PrivatAd, self).for_publish() + "\n" \
               + 'Actual until: ' + self.actual_date + ', ' + str(self.__left_days(self.actual_date)) \
               + ' days left' + "\n" + "------------------------------" + "\n" + "\n"


class Weather(Publication):
    """Extend class Publication.
    Requirement argument: name - name of publication,
    text - main text of publication"""

    def __init__(self, name, text):
        """Define object from class Weather"""
        Publication.__init__(self, name=name, text=text)

    def for_publish(self):
        """Overwrite method for_publish(). Add probability of rain and date"""
        now = datetime.datetime.now()
        return super(Weather, self).for_publish() + "\n" + "Probability of rain: " + str(randrange(101)) \
               + '%, ' + now.strftime("%Y-%m-%d %H.%M") + "\n" + "------------------------------" + "\n" + "\n"


def run():
    """ The main function."""
    options = ["News", "Privat Ad", "Weather"]
    news_type = user_choice(options)
    publication_text = HW_3.normalize_letter_cases(input("Please write text of publication: "))

    with open('MyPublications.txt', 'a') as f:  # write publication into .txt file
        f.write(article(news_type, publication_text))


if __name__ == '__main__':
    run()
