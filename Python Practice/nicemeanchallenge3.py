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
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)

def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} year old {}.".format(f_name,l_name,age,gender))


if __name__ == "__main__":          #python will look at this line, python knows  
    start()                         #you're running this as a script and will go
                                    #down and run the next function in order




































