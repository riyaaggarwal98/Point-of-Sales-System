import item
beverageList = {"Soft drink": 35,"Mineral Water drink":20,"Ice Tea drink":45,"Cold Coffee drink":49,"Tea drink":35,"Black Tea drink":30,"McFloat drink":30}
class beverage(item.item):
   
    def __init__(self,name,qty):
        super().__init__(name,qty)
        
    @property
    def showPrice(self):
        if self.name not in beverageList:
            return("Select some other item on menu or spell your item correctly.")
        else:
            for x in beverageList:
                if x == self.name:
                    y = beverageList.get(self.name)
         
            return (y*(self.qty) )

"""d1 = beverage("Soft Drink",2) 
print(d1.showPrice)"""
    