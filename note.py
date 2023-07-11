import argparse
from data import getItems, createItem, findItem, deleteItem, updateItem, search
from ui import createTable
import datetime
import os

def main_note ():
    data = getItems(2)
    header = ["No", "Title", "Date"]
    table = createTable(data, header)

    print(table) 
    user_input = input("\nMasukkan argumen: ")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--read', type=int, help='')
    parser.add_argument('-c', '--create', type=int, help='lol')
    parser.add_argument('-u', '--update', type=int, help='lol')
    parser.add_argument('-d', '--delete', type=int, help='lol')
    parser.add_argument('-s', '--search', type=str, help='Lol')
    
    try:
        args = parser.parse_args(user_input.split())
        if(args.read):
            item = findItem(args.read,2);
            if (item):
                print("\n")
                print("Title:", item['title'])
                print("Date:", item['date'])
                print("\nMessage:\"", item['message'],'"')
            else:
                print("Data not found")

        elif (args.create):
            title = str(input("Title : "))
            message = str(input("Message : "))
            now = datetime.datetime.now()
            date = now.strftime("%d-%B-%Y")

            newDiary = {
                "id": len(data) + 1, 
                "title": title, 
                "message": message, 
                "date": date
            }
            createItem(newDiary, 2)

        elif (args.update):
            title = str(input("New title : "))
            message = str(input("New message : "))
            now = datetime.datetime.now()
            date = now.strftime("%d-%B-%Y")

            updateData = {
                "id": args.update, 
                "title": title, 
                "message": message, 
                "date": date
            }
            updateItem (updateData,2)

        elif (args.delete):
            deleteItem(args.delete, 2)

        elif (args.search):
            search(args.search)
    except argparse.ArgumentError:
        print("Argumen tidak valid.")
 
