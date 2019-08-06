import item
sidesList = {"Dips sides": 20,"Veg Pizza Mcpuff sides":40,"Masala wedges sides":85}
class sides(item.item):
   
    def __init__(self,name,qty):
        super().__init__(name,qty)
        
    @property
    def showPrice(self):
        if self.name not in sidesList:
            return("Select some other item on menu or spell your item correctly.")
        else:
            for x in sidesList:
                if x == self.name:
                    y = sidesList.get(self.name)
         
            return (y*(self.qty) )

"""d1 = sides("Dips sides",2) 
print(d1.showPrice)"""
    