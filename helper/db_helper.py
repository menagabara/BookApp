#this file is used for one time only.

from library.models import *


def ini_countries():
    with open("Countries.txt") as lines:
        for line in lines:
            status = Country(name=line)
            try:
                status.save()
            except:
                print("there was a problem with line")

# def ini_users():
#
# def ini_authors():
#
# def ini_books():
