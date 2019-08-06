import item
dessertList = {"McShakes dessert": 70,"Soft Serve dessert":55,"Brownie Soft Serve dessert":65,"McFlurry dessert":69}
class dessert(item.item):
   
    def __init__(self,name,qty):
        super().__init__(name,qty)
        
    @property
    def showPrice(self):
        if self.name not in dessertList:
            return("Select some other item on menu or spell your item correctly.")
        else:
            for x in dessertList:
                if x == self.name:
                    y = dessertList.get(self.name)
         
            return (y*(self.qty) )

"""d1 = dessert("McShakes dessert",2) 
print(d1.showPrice)"""
    