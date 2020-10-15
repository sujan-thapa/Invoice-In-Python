import main


# print(type(price))
name = main.customerName
# print(name)
# print(sujan)
suj = main.sujan   # access nested dictionary of products details
# print(suj)
available = main.inside()
amt = main.amount
print(amt)
# print(available)    #print the remaining stock after the transaction
cust = main.customer
# print(cust)


def update():
    rough = ""   #empty string
    reading = open("vg.txt","r")   #read the file
    for line in reading:
        stripLine = line.strip()
        # print(stripLine)
        newLine = stripLine.replace(suj[cust]["stock"],str(available))
        # print(newLine)
        rough += newLine +"\n"
    
    reading.close()
    print(rough)
    writing = open("vg.txt","w")
    writing.write(rough)
    writing.close()
update()