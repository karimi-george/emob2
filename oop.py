class Cars:
    #constructor
    def __init__(self,type,color,model):
        self.type = type
        self.color = color
        self.model=model

        #method
    def onyesha(self):
        print(f"l love {self.model} cars which is a {self.type} being {self.color}")
#create an object
myobj = Cars("Salon","White","Toyota")
myobj.onyesha()
myobj2 = Cars("subaru", "black", "toyota")
myobj2.onyesha()
myobj3=Cars("corolla","white", "toyota")
myobj3.onyesha()