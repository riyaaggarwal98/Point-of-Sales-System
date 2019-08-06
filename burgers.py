#BURGERS
import item as it
burgersList = { "McAloo Tikki burger":30,"McVeggie burger" : 69,"McChicken burger": 85,"Filet-O-Fish burger":105,"Chicken Maharaja Mac burger":109,
                        "McSpicy Paneer burger":119,"McSpicy Paneer Supreme burger":125,"McSpicy Chicken burger":125,
                        "McSpicy Chicken Supreme burger":135,"Double McSpicy Chicken burger":200,"McAloo Tikki Meal burger":109,"McVeggie Meal burger": 155,
                        "McChicken Meal burger" : 165,"Filet-O-Fish Meal burger":189,"Chicken Maharaja Mac Meal burger":204,
                        "McSpicy Paneer Meal burger":209,"McSpicy Paneer Supreme Meal burger":215,"McSpicy Chicken Meal burger":214,
                        "McSpicy Chicken Supreme Meal burger":220,"Double McSpicy Chicken Meal burger":280}
class burger(it.item):
    
    def __init__(self,name,qty):
        super().__init__(name,qty)
        
    @property
    def showPrice(self):
        if self.name not in burgersList:
            return("Select some other item on menu or spell your item correctly.")
        else:
            for x in burgersList:
                if x == self.name:
                    y = burgersList.get(self.name)
                    
            return (y*(self.qty) )

"""b1 = burger("McSpicy Chicken Supreme Meal ",2) 
print(b1.showPrice)"""
    