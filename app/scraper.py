"""This file was written by GPT3 Chatbot! Has not been verified/tested."""


if __name__ == '__main__':

    # Import the BeautifulSoup library
    from bs4 import BeautifulSoup

    # Open the Pocket Mortys .apk file and read its contents
    with open("PocketMortys.apk", "r") as file:
        data = file.read()

    # Parse the file's HTML or XML code using BeautifulSoup
    soup = BeautifulSoup(data, "html.parser")

    # Use BeautifulSoup to find all the elements you want to extract
    elements = soup.find_all("div", class_="morty")

    # Loop through the elements and print their data
    for element in elements:
        print(element.text)
