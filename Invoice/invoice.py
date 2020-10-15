import datetime
import remove
# #import main
# #price = main.amt
# #print(price)

amountt = remove.amt
# print(type(amountt))

Name = remove.name
# print(Name)
product = remove.cust


gadi = datetime.datetime.now()
# print(gadi)
bill = open("bill.txt","w")
bill.write("----------------------Welcome to the VG Store----------------------\n")
bill.write("Name: " + Name +                         "Date and Time: "+str(gadi)+ "\n")
bill.write("Products: "+product +"\n")
bill.write("Total Amount: " + str(amountt) + "\n")
bill.write("-------------------Thanks fo visitng us!!!----------------------")
bill.close()

