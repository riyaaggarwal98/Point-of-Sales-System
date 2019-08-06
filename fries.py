import item
friesList = {"Small fries":60,"Medium fries":75,"Large fries":95,"Cheesy Mexican fries":111}
class fries(item.item):
   
    def __init__(self,name,qty):
        super().__init__(name,qty)
        
    @property
    def showPrice(self):
        if self.name not in friesList:
            return("Select some other item on menu or spell your item correctly.")
        else:
            for x in friesList:
                if x == self.name:
                    y = friesList.get(self.name)
         
            return (y*(self.qty) )

"""f1 = fries("Medium fries",2) 
print(f1.showPrice)"""
    