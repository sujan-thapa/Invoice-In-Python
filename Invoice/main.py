import first
sujan = first.dict1()
# print(sujan)
sss = sujan.items()
customerName = input("What is your name?: \n")
customer = input("Which prodcut do you want to buy from available products???: ")
# print(customer)
amount = 0
def inside():   
    for gadgets, prQty in sss:  #for loop for nested dictionary
        if customer in gadgets: #check if product is available
            print("\nProduct: ", gadgets)
            priceQty = []    #empty list
            for vg in prQty: #adding stock amount and price of product in list
                print(vg + ":", prQty[vg])  #displays the nested dictionary keys and values
                priceQty.append(prQty[vg])  #add the information at the end of list

            else:
                desire = int(input("How many piece do your want??: "))  #user input for desired piece
                strInt = int(priceQty[0])
                avail = int(priceQty[1])
                if avail >= desire:
                    global amount
                    amount = strInt * desire
                    # print(f"The total price is {amount}")
                    avail -= desire
                    # print(avail)
                    return avail
                    # rough = ""
                    # reading = open("vg.txt","r")
                    # for line in reading:
                    #     stripLine = line.strip()
                    #     newLine = stripLine.replace(sujan[customer]["stock"],str(avail))
                    #     rough += newLine +"\n"
                    # reading.close()
                    # print(rough)
                    # writing = open("vg.txt","w")
                    # writing.write(rough)
                    # writing.close()
                else:
                    # print("The stock of product is limited.")  
                    return "The stock of product is limited."
            break
        else:
            continue
    else:
        # print("Sorry! The product is not available")
        return "The product is not available"  #returns the sorry message

# print(inside())   
# inside()
# print("The total amount is " + amount)    #This ways is wrong because print can only concatenate str (not "int") to str
# print(amount)              #This gives the result

#Displays the message with proper message
# amt = str(amount)     #Convert integer to string
# print("The total amount of product is "+ amt)    #prints the message in appropriate way

# print(type(amount))

