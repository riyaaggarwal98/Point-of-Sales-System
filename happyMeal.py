import item
mealList = {"McAloo Tikki meal":105,"McEgg meal":108,"Chicken McGrill":118,"McChicken meal":120,"McVeggie meal":130}
class meal(item.item):
   
    def __init__(self,name,qty):
        super().__init__(name,qty)
        
    @property
    def showPrice(self):
        if self.name not in mealList:
            return("Select some other item on menu or spell your item correctly.")
        else:
            for x in mealList:
                if x == self.name:
                    y = mealList.get(self.name)
         
            return (y*(self.qty) )

"""m1 = meal("McAloo Tikki meal",2) 
print(m1.showPrice)"""
    