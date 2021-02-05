class Singleton:
    instance = None
    def __init__(self):
       self._data = 12 
       if not Singleton.instance:
           Singleton.instance = self
    
    @staticmethod
    def getInstance():
        if Singleton.instance is None:
            Singleton()
        else:
            raise Exception("Singleton class already defined")
        return Singleton.instance

    @property
    def Data(self):
        return self._data
    
    @Data.setter
    def Data(self,a):
        self._data = a



print(Singleton.getInstance().Data)
Singleton.getInstance().Data = 16
print(Singleton.getInstance().Data)
