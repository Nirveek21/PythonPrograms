class bill:
    
    def __init__(self):
       self.data = { }
       self.data2 = { }
       self.item=0
    
             
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
             
         while True:
            f = open('bill.txt', 'a' )
            self.item=input('''
                Enter PP for Pepsi
                ER for Eggroll
                CR for Chicken roll
                FR for Fried rice
                BR for Biriyani : ''') 
            self.quantity= int(input('Enter quantity : '))
            f.write( (data2[self.item] ) + '     ' + str(self.quantity) + '     ' + str(data[data2[self.item]]*self.quantity) + '\n' )
            f.close()
            self.Temp=input('Want more ? Enter  Y for yes , N for no : ')
            if self.Temp=='N':
                break

    
if __name__== "__main__":
    obj= bill()
    obj.getdata()
    
    
    
       
