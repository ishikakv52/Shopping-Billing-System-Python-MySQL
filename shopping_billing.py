import mysql.connector
import datetime
#  connection 
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaat@2010",
    database="da"
)

cursor = con.cursor() 
sum=0

while True:
    n=int(input("Press 1 to continue shopping,0 to exit : "))
    if n==1:
        k=int(input("Press 1 for Laptop,2 for Mobile,3 for Earbuds : "))
        if k==1:
            product_id=10123
            product_name="Laptop"
            price=100000
            quantity=int(input("Enter quantity : "))
            amount=price*quantity
            rem_quantity=int(input("Enter number of items to remove : "))
            if rem_quantity>quantity:
                print("Invalid (because item are more than selected ones)")
                x=0
            else:    
              x=rem_quantity*price
            exact_amount=amount-x
            # print("Total Amount : ",amount)
        elif k==2:
            product_id=14322
            product_name="Mobile"
            price=15000   
            quantity=int(input("Enter quantity : "))
            amount=price*quantity
            rem_quantity=int(input("Enter number of items to remove : "))
            if rem_quantity>quantity:
                print("Invalid (because item are more than selected ones)")
                x=0
            else:    
              x=rem_quantity*price
            exact_amount=amount-x
            # print("Total Amount : ",amount)     
        elif k==3:
            product_id=12345
            product_name="Earbuds"
            price=5000
            quantity=int(input("Enter quantity : "))
            amount=price*quantity
            rem_quantity=int(input("Enter number of items to remove : "))
            if rem_quantity>quantity:
                print("Invalid (because item are more than selected ones)")
                x=0
            else:    
              x=rem_quantity*price
            exact_amount=amount-x
            # print("Total Amount : ",amount)
        else:
            print("Invalid input")    
        
        sum=sum+exact_amount
    elif   n==0:
        break
    else:
        print("Invalid input") 

user_name=input("Enter name of customer : ") 
id=int(input("Enter customer's order id : "))
totalamount=sum
print("Total amount before applying discount : ",sum)
if totalamount>10000:
    u=totalamount*0.20
    total_amount=totalamount-u
elif totalamount>5000:
    u=totalamount*0.10
    total_amount=totalamount-u
else:    
    u=0
    total_amount=totalamount-u

print("Total amount after applying discount : ",total_amount)


#to insert in file
file=user_name
f=open(file+".txt","w")
a=str(id)
b=str(totalamount)
c=str(u)
p=str(total_amount)
it=datetime.datetime.now()      
t=str(it)
f.write("Order Id : "+a+"\nCustomer name : "+user_name+"\nTotal Amount : "+b+"\nDiscount : "+c+"\nPayable Amount : "+p+"\nTime : "+t)
f.close()

# to insert in sql
sql='''insert into orders 
values (%s,%s,%s,%s,%s,%s)'''
values=(id,user_name,totalamount,u,total_amount,t)
cursor.execute(sql,values)
con.commit()

print("Data inserted successfully")
con.close()
