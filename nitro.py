import random, string
import webbrowser
import time
import requests
nitro= input("enter link")
with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("nitro")

        url = nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))
input("The end! Press Enter 5 times to close the program.")
input("4")
input("3")
input("2")
input("1")
© 2021 GitHub, Inc.
