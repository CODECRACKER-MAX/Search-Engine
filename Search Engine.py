# Using Web Browser Model In Python!
import webbrowser
import socket
import time
import os
def Welcome():
    Clear_Screen_In_Windows()
    print("\t\t\t\t\t\t\t\t\t\t\tWelcome To QuickSearch!") #Set_The Welcome Screen According to your choice!
    print("List Of Available Search Engines")
    print("1.YouTube")
    print("2.Google")
    print("Choose any of these search engines and search from them: ")
    search_engine = int(input("Enter the search engine number 1/2: "))
    if search_engine == 1:
        YouTube()
    elif search_engine == 2:
        Google()
    else:
        Try_Again()

def YouTube():
    Clear_Screen_In_Windows()
    YouTube_URL = "www.youtube.com/results?search_query="
    print("Youtube Search Engine!")
    print("Press 0 and Hit Enter To Search!")
    print("Press 1 and Hit Enter To Go Back!")
    print("Press Q and Hit Enter To Quit!")
    key = input("Enter your choice:  ")
    if key == "0":
        search_keyword = input("What Do You Want To Search For?: ")
        webbrowser.open(YouTube_URL+search_keyword)
    elif key == "1":
        Welcome()
    elif key == "Q" or key == "q":
        time.sleep(2)
        print("Thank You For Using Our Application Hope To See Yah Soon ;)")
        time.sleep(2)
        print("Exiting.........")
        time.sleep(2)
        print("Press Any To Exit!")
def Google():
    Clear_Screen_In_Windows()
    Google_URL = "https://www.google.com/search?q="
    print("Google Search Engine! ")
    print("Press 0 and Hit Enter To Search!")
    print("Press 1 and Hit Enter To Go Back!")
    print("Press Q and Hit Enter To Quit!")
    key = input("Enter your choice:  ")
    if key == "0":
        search_keyword = input("What Do You Want To Search For?: ")
        webbrowser.open(Google_URL + search_keyword)
    elif key == "1":
        Welcome()
    elif key == "Q" or key == "q":
        time.sleep(2)
        print("Thank You For Using Our Application Hope To See Yah Soon ;)")
        time.sleep(2)
        print("Exiting.........")
        time.sleep(2)
        print("Press Any To Exit!")
    else:
        os.system('cls')
        print("Sorry, We couldn't understood you!")
        Try_Again()

def Try_Again():
    Clear_Screen_In_Windows()
    print("Do you want try again y/n ?")
    Y_N = input("Enter your choice: ")
    if (Y_N == "Y" or Y_N == "y"): 
        Clear_Screen_In_Windows()
        Welcome()

    elif (Y_N == "N" or Y_N == "n"): 
        Clear_Screen_In_Windows()
        print("Thank you for using the application, See you soon ;) ")
        print("Exiting..........!")
        time.sleep(2)
        os.system(exit(0))
    else:
        Clear_Screen_In_Windows()
        print("Sorry, I cannot understand you again!, Try Again!")
        time.sleep(2)
        Try_Again()


def Clear_Screen_In_Windows():
    os.system('cls')

Welcome()
