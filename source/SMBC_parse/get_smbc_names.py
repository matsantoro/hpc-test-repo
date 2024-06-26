import urllib.request
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()

def parse_smbc(month, year):
    """
    Function that parses SMBC website for comic names with specific month and year
    :param month: string with month name
    :param year: string with year

    :return: returns an iterable with all the comic names, while printing them
    """
    data = urllib.request.urlopen('https://www.smbc-comics.com/comic/archive')
    strings = data.read().decode('utf8')
    soup = BeautifulSoup(strings, 'html.parser')
    comics = soup.find_all("option")
    for comic in comics:
        if year in str(comic) and month in str(comic):
            print(comic.text)
            yield(comic.text)


if __name__ == '__main__':
    parser.add_argument("-y", "--year", default='2023')
    parser.add_argument("-m", "--month", default='September')
    args = parser.parse_args()
    parse_smbc(args.month, args.year)
