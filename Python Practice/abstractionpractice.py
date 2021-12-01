



from abc import ABC, abstractmethod




class computer(ABC):
    @abstractmethod #importing abstract method
    def task(self): #defining function
        pass

class laptop(computer):
    def task(self): #child class utilizing function but changing it
        print('open')


#com = computer()
#com.task()

        
com1 = laptop()
com1.task()
