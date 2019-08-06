import burgers as bg
import tax
import wraps as wr
import happyMeal as hm
import fries as fr
import beverages as bv
import desserts as ds
import sides as sd
import string

class bill(bg.burger,wr.wrap, hm.meal ,fr.fries,bv.beverage,ds.dessert,sd.sides):
    def __init__(self,name,qty):
        self.name = name
        self.qty = qty
       
    
    @property
    def objects(self):
        x = self.name
        
        if x.endswith("burger"):
           y = (bg.burger(self.name,self.qty).showPrice)
        elif x.endswith("wrap"):
           y = (wr.wrap(self.name,self.qty).showPrice)
        elif x.endswith("meal"):
           y = (hm.meal(self.name,self.qty).showPrice)
        elif x.endswith("fries"):
           y = (fr.fries(self.name,self.qty).showPrice)
        elif x.endswith("drink"):
           y = (bv.beverage(self.name,self.qty).showPrice)
        elif x.endswith("dessert"):
           y = (ds.dessert(self.name,self.qty).showPrice)
        elif x.endswith("sides"):
           y = (sd.sides(self.name,self.qty).showPrice)
        else:
            y = "Select some other item on menu or spell your item correctly."
        
        return y

    #def total(self):
i = []
k = []
s = 0.0
l = []
q = 0

d = " "
while d != "end":
    d = input()
    if d == "remove":
        rem = input("Enter the item:")
        #qt = int(input("how much less?"))
        if rem in i:
            index1 = int(i.index(rem))
            i.remove(rem)
            k.pop(index1)
             
        else:
            print("No such order exists.")
    elif(d=="end"):
        break

    else:    
        name = input("enter the item:")
        quantity = int(input("enter the quantity:"))
    
        i.append(name.strip())
        k.append(quantity)
for j in range(len(i)):
    w = bill(i[j],k[j]).objects
    if w != "Select some other item on menu or spell your item correctly.":
        s = s + w
        q = q + k[j]
    else:
        l.append(i[j])
    
print("================================================================")
for j in range(len(i)):
    print(i[j],":",k[j])
if len(l)!=0:
    print("Sorry due to some technical problems these items couldnt be included:" )
    print(l)
else:
    pass
print("Total collectable items:",q)

print("Total bill:",s)
t = tax.tax(s).amount
print("tax included:",t)
print("payable amount:",s + float(t))
print("================================================================")
