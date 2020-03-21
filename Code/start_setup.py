##------------------FROM: Arrival_Fingerprint_Lite_Scan.py--------------
##---------------------------TO: Folder_Search.py-----------------------
##-----------------------------Importing Section------------------------

import setup
import Departure_Window
import Arrival_Window

##-----------------------------Code Section----------------------------

def main():
    f = open("setup_needed.txt","r")
    flag = f.read()
    f.close()
    print("Setup needed: " + flag)
    if(flag == "Y"):
        setup.main()
    elif(flag == "N"):
        f = open("Config.txt","r")
        config = f.read()
        f.close()

        if (config == "Departure"):
            Departure_Window.main()
        elif (config == "Arrival"):
            Arrival_Window.main()

if __name__ == "__main__":
    main()
