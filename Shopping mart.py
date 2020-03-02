import pandas as pd
from os import system, name
import time

def clear():
    if name == 'nt': 
        _ = system('cls')


#Prices Dictionary...
prices_Mens = {'M-Jeans':700,'M-T-Shirt':400,'Formal Shirt':1100,'M-Ethnic':3000,'M-Accessories':300}
prices_Womens = {'Kurti':500,'W-T-Shirt':500,'One-Piece':1500,'W-Accessories':300}
prices_Kids = {'K-Jeans':700,'K-T-Shirt':400,'Night Suits':800,'K-Ethnic':2000,'K-Accessories':300}

#Inventory Management...
'''
inventory_mens = {'mJeans':20,'mT-Shirt':20,'Formal Shirt':20,'Ethnic':20,'mAccessories':20}
inventory_womens = {'Kurti':20,'wT-shirt':20,'One-Piece':20,'wAccessories':20}
inventory_kids = {'K-Jeans':20,'K-T-Shirt':20,'Night Suits':20,'K-Ethnic':20,'K-Accessories':20}
'''


cart = {}

cart_price = []

#Main Menu....
def main_menu():
	print("\tWelcome to Fashion Mart.")
	print("----------------------------------------")
	print("1.| Mens Section.")
	print("2.| Womens Section.")
	print("3.| Kids Section.")
	print("4.| Show Cart.")
	print("5.| Print Bill")
	print("6.| EXIT.")

main_menu()
ch = int(input("\n\nSelect section:\t"))

while ch!=6:
    
    
    #*******************************
    #Mens Section
    #*******************************
    
    if ch==1:
        print("\n\tWelcome to Mens Section.")
        print("----------------------------------------")
        print('1.| Jeans - {}'.format(prices_Mens['M-Jeans']))
        print('2.| T-Shirt - {}'.format(prices_Mens['M-T-Shirt']))
        print('3.| Formal Shirts  - {}'.format(prices_Mens['Formal Shirt']))
        print('4.| Ethnic  - {}'.format(prices_Mens['M-Ethnic']))
        print('5.| Accessories  - {}'.format(prices_Mens['M-Accessories']))
        print("6.| Back to main menu.")
        
        ch1 = int(input("Choice:\t"))
        
        while ch1 != 6:
            if ch1 == 1:
                qty = int(input("Enter Quantity of Jeans:\t"))
                total = qty * prices_Mens['M-Jeans']
                print("\nYou have successfully bought {} jeans for Rs.{}".format(qty,total))
                
                cart['M-Jeans'] = cart.get("M-Jeans",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
                
            
            elif ch1 == 2:
                qty = int(input("Enter Quantity of T-shirt:\t"))
                total = qty * prices_Mens['mT-Shirt']
                print("You have successfully bought {} T-Shirt for Rs.{}".format(qty,total))
                
                cart['M-T-Shirt'] = cart.get("M-T-Shirt",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
                
            
            elif ch1 == 3:
                qty = int(input("Enter Quantity of Formal Shirts:\t"))
                total = qty * prices_Mens['Formal Shirt']
                print("You have successfully bought {} Formal Shirts for Rs.{}".format(qty,total))
                
                cart['Formal Shirt'] = cart.get("Formal Shirt",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
                
        
            elif ch1 == 4:
                qty = int(input("Enter Quantity of Ethnic:\t"))
                total = qty * prices_Mens['M-Ethnic']
                print("You have successfully bought {} Ethnic for Rs.{}".format(qty,total))
                
                cart['M-Ethnic'] = cart.get("M-Ethnic",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
                
                
            elif ch1 == 5:
                qty = int(input("Enter Quantity of Accessories:\t"))
                total = qty * prices_Mens['M-Accessories']
                print("You have successfully bought {} Accessories for Rs.{}".format(qty,total))
                
                cart['M-Accessories'] = cart.get("M-Accessories",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
                
        clear()
        main_menu()
        ch = int(input("Select Section:\t"))
        

    #*******************************
    #Womens Section
    #*******************************
    
    elif ch==2:
        print("\n\nWelcome to Womens Section.")
        print("----------------------------------------")
        print('1.| Kurti  - {}'.format(prices_Womens['Kurti']))
        print('2.| T-Shirt  - {}'.format(prices_Womens['W-T-Shirt']))
        print('3.| One-Piece  - {}'.format(prices_Womens['One-Piece']))
        print('4.| Accessories  - {}'.format(prices_Womens['W-Accessories']))
        print("5.| Back to main menu.")
        
        ch1 = int(input("Choice:\t"))
        
        while ch1 != 5:
            if ch1 == 1:
                qty = int(input("Enter Quantity of Kurti you want:\t"))
                total = qty * prices_Womens['Kurti']
                print("You have successfully bought {} Kurti for Rs.{}".format(qty,total))
                
                cart['Kurti'] = cart.get("Kurti",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
                
            
            elif ch1 == 2:
                qty = int(input("Enter Quantity of T-shirts:\t"))
                total = qty * prices_Womens['W-T-Shirt']
                print("You have successfully bought {} T-Shirt for Rs.{}".format(qty,total))
                
                cart['W-T-Shirt'] = cart.get("W-T-Shirt",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
            
            elif ch1 == 3:
                qty = int(input("Enter Quantity of one-piece:\t"))
                total = qty * prices_Womens['One-Piece']
                print("You have successfully bought {} One-Piece for Rs.{}".format(qty,total))
                
                cart['One-Piece'] = cart.get("One-Piece",qty)   
                
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
        
                
            elif ch1 == 4:
                qty = int(input("Enter Quantity of accessories:\t"))
                total = qty * prices_Womens['W-Accessories']
                print("You have successfully bought {} Accessories for Rs.{}".format(qty,total))
                
                cart['W-Accessories'] = cart.get("W-Accessories",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
        
        
        clear()
        main_menu()
        ch = int(input("Select Section:\t"))
        
    #*******************************
    #Kids Section
    #*******************************
    
    elif ch==3:
        print("Welcome to kids section.")
        print("----------------------------------------")
        print('1.| Jeans  - {}'.format(prices_Kids['K-Jeans']))
        print('2.| T-Shirt  - {}'.format(prices_Kids['K-T-Shirt']))
        print('3.| Night Suits  - {}'.format(prices_Kids['Night Suits']))
        print('4.| Ethnic  - {}'.format(prices_Kids['K-Ethnic']))
        print('5.| Accessories  - {}'.format(prices_Kids['K-Accessories']))
        print("6.| Back to main section.")
        
        ch1 = int(input("Choice:\t"))
        
        while ch1 != 6:
            if ch1 == 1:
                qty = int(input("Enter Quantity of Jeans:\t"))
                total = qty * prices_Kids['K-Jeans']
                print("You have successfully bought {} jeans for Rs.{}".format(qty,total))
                
                cart['K-Jeans'] = cart.get("K-Jeans",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
            
            elif ch1 == 2:
                qty = int(input("Enter Quantity of T-shirts:\t"))
                total = qty * prices_Kids['K-T-Shirt']
                print("You have successfully bought {} T-Shirt for Rs.{}".format(qty,total))
                
                cart['K-T-Shirt'] = cart.get("K-T-Shirt",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
            
            elif ch1 == 3:
                qty = int(input("Enter Quantity of Night Suits:\t"))
                total = qty * prices_Kids['Night Suits']
                print("You have successfully bought {} Night Suits for Rs.{}".format(qty,total))
                
                cart['Night Suits'] = cart.get("Night Suits",qty)  
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
        
            elif ch1 == 4:
                qty = int(input("Enter Quantity of Ethnic:\t"))
                total = qty * prices_Kids['K-Ethnic']
                print("You have successfully bought {} Ethnic for Rs.{}".format(qty,total))
                
                cart['K-Ethnic'] = cart.get("K-Ethnic",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
                
            elif ch1 == 5:
                qty = int(input("Enter Quantity of Accessories:\t"))
                total = qty * prices_Kids['K-Accessories']
                print("You have successfully bought {} Accessories for Rs.{}".format(qty,total))
                
                cart['K-Accessories'] = cart.get("K-Accessories",qty)
                cart_price.append(total)
                ch1 = int(input("Choice:\t"))
        
        clear()
        main_menu()
        ch = int(input("Select Section:\t"))
        
    #Cart Display
    #****************
    elif ch == 4:
        cart_items = list(cart.keys())
        cart_qty = list(cart.values())
        data_cart = {'Particulars':cart_items,'Quantity':cart_qty}
        
        
        df_cart = pd.DataFrame(data_cart)
        print("\n\n")
        print("-"*12,"CART","-"*12) 
        print(df_cart)
        print("-"*30)
        
        main_menu()
        ch = int(input("Select Section:\t"))
    
        
    #Printing bill
    #*****************
    elif ch ==5:
        #calculating Taxes
        total_amount = sum(cart_price)
        
        CGST = 0.09 * total_amount
        SGST = 0.09 * total_amount
        
        total_tax = CGST + SGST
        
        bill = total_amount + total_tax
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        print("-"*12,"BILL","-"*12)
        print("\n")
        
        cart_items = list(cart.keys())
        cart_qty = list(cart.values())
        
        data_bill = {'Particulars':cart_items,'Quantity':cart_qty,'Amount':cart_price}
        
        df_bill = pd.DataFrame(data_bill)
        print(df_bill)
        print("-"*30)
        print("CGST is 9% = Rs. {} ".format(CGST))
        print("SGST is 9% = Rs. {}".format(SGST))
        print("Total Taxes = Rs. {}".format(total_tax))
        print("-"*30)
        print("TOTAL AMOUNT TO BE PAID : Rs. {}".format(bill))
        print("\n\n")
        print("Press 1 to continue shopping:\t")
        print("Press 0 to Exit")
        
        choicee = int(input("Enter:\t"))
        
        if choicee == 1:
            main_menu()
            ch = int(input("Select Section:\t"))
        else:
            print("EXITING in 10 seconds...")
            time.sleep(10)
        

