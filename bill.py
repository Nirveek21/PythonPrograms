class bill:
    
    def __init__(self):
       self.data = { }
       self.data2 = { }
       self.item=0
       self.quantity=0
       self.total=0  
    def getdata(self):
         data={
             "Pepsi       ":10,
             "Eggroll     ":30,
             "Chicken Roll":50,
             "Fried Rice  ":100,
             "Biriyani    ":150
            }
         data2={
             "PP":"Pepsi       ",
             "ER":"Eggroll     ",
             "CR":"Chicken Roll",
             "FR":"Fried Rice  ",
             "BR":"Biriyani    "
            }
         f = open('bill.txt', 'w+' )
         f.write('ITEM       QUANTITY     PRICE(RS) '+'\n')
         f.write('--------------------------------------'+'\n')
         while True:
            self.item=input('''
                Enter PP for Pepsi
                ER for Eggroll
                CR for Chicken roll
                FR for Fried rice
                BR for Biriyani : ''') 
            self.quantity= int(input('Enter quantity : '))
            f.write( (data2[self.item] ) + '     ' + str(self.quantity) + '     ' + str(data[data2[self.item]]*self.quantity) + '\n' )
            self.total += (data[data2[self.item]]*self.quantity)
            self.Temp=input('Want more ? Enter  Y for yes , N for no : ')
            if self.Temp=='N':
                f.write('--------------------------------------'+'\n')
                f.write('TOTAL IS                '+str(self.total))
                f.close()
                break
         f= open('bill.txt', 'r')
         print (f.read())
         f.close()    

if __name__== "__main__":
    obj= bill()
    obj.getdata()
    
    
    
       
