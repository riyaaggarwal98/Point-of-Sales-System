#Wraps

import item
wrapList = {"Big Spicy Paneer wrap":149,"Big Spicy Chicken Wrap":155,"Big Spicy Paneer wrap Meal":239,"Big Spicy Chicken Meal Wrap":244 }
class wrap(item.item):
   
    def __init__(self,name,qty):
        super().__init__(name,qty)
        
    @property
    def showPrice(self):
        if self.name not in wrapList:
            return("Select some other item on menu or spell your item correctly.")
        else:
            for x in wrapList:
                if x == self.name:
                    y = wrapList.get(self.name)
         
            return (y*(self.qty) )

"""w1 = wrap("Big Spicy Paneer wrap",2) 
print(w1.showPrice)"""
    