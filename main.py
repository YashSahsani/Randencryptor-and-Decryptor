import Gatherer
import Shredder
import os
import sys
import platform
def Main():
       if(platform.system() != 'Linux'):
              print("\n Run on Linux")
       else:
            if os.getuid() != 0:
                  print("This program is not running as sudo or elevated this it will not work")
                  print("Usage sudo python3 main.py")
                  sys.exit(0)
            print("1. To Shred the File ")
            print("2. To Gather the Shredded File")
            print("3 Exit")
            choice = int(input("Enter your choice : "))
            if(choice == 1):
                   shred = Shredder.Shredder()
                   shred.Shredder()
            elif(choice == 2):
                    gather = Gatherer.Gatherer()
                    gather.gatherer()
            elif(choice == 3):
                    sys.exit(0)
            else:
                    print("Invalid Input")

if __name__ == "__main__":
           Main()
