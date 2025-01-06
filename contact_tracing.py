import csv
from datetime import datetime


def load_csv(filename):
    data = []
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def find_contacts(visits, infected_person, test_date, addresses):
    contacts = []
    for visit in visits:
        if (
            visit["User"] != infected_person
            and visit["Date"] == test_date
            and visit["Address"] in addresses
        ):
            contacts.append(
                {
                    "name": visit["User"],
                    "address": visit["Address"],
                    "date": visit["Date"],
                }
            )
    return contacts


def find_address(data, infected_person, test_date):
    addresses = []
    for i in data:
        if i["User"] == infected_person and i["Date"] == test_date:
            addresses.append(i["Address"])
    return addresses


def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    return date_obj.strftime("%d, %b %Y")


def generate_report(contacts):
    for contact in contacts:
        formatted_date = format_date(contact["date"])
        print(
            f"{contact['name']} should stay at home for next 10 days due to the trip to {contact['address']} on {formatted_date}"
        )


infected_person = input("The person who was tested positive: ")
test_date = input("When was the test? ")
test_date = datetime.strptime(test_date, "%m/%d/%Y").strftime("%m/%d/%Y")
data = load_csv("contacts.csv")
addresses = find_address(data, infected_person, test_date)
contacts = find_contacts(data, infected_person, test_date, addresses)
generate_report(contacts)
