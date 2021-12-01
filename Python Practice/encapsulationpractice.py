



class Protected:
    def __init__(self):
        self._protected = 'Hello, this is protected.' #created protected variable
        
    def __init__(self):
        self.__private = 'And this is private.' #private variable
         


protect = Protected() #assigned variable to class
protect._protected = 'Changed' #changed _protected 
print(protect._protected)

private = Protected()
private.__private = 'Changed this too' #changed __private 
print(private.__private)


    
