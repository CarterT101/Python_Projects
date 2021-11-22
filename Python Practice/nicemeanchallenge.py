#
#
#
#   Python: 3.9.9
#
#   Author: Carter T.
#
#   Purpose: The Tech Academy Python Course, creating first program together
#
#            How to pass variables from function to function while producing functional game
#





def start():
    print("Hello {}!".format(get_name()))


def get_name():
    name = input("What is your name? ")
    return name






if __name__ == "__main__":          #python will look at this line, python knows  
    start()                         #you're running this as a script and will go
                                    #down and run the next function in order




































