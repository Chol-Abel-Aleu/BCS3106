from tkinter import *
from tkinter import ttk, messagebox
import random
import time
import datetime

root = Tk()
root.geometry("1350x650+0+0")
root.title("Restaurant Cancelling Order System")


CustomerRef= StringVar()
Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofRiceChicken=StringVar()
CostofRiceBeef=StringVar()
CostofRiceFish=StringVar()
CostofDelivery=StringVar()
CustomerName=StringVar()
CustomerPhone=StringVar()
CustomerEmail=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
CostofRiceFish=StringVar()
CostofRiceBeef=StringVar()
CostofRiceChicken=StringVar()
UnitPriceRiceFish=StringVar()
UnitPriceRiceBeef=StringVar()
UnitPriceRiceChicken=StringVar()
UnitPriceRiceBeef=StringVar()
QtyRiceFish=StringVar()
QtyRiceBeef=StringVar()
QtyRiceChicken=StringVar()
Discount=StringVar()
Qty1=float()
Qty2=float()
Qty3=float()
SubTotalp=float()
#==========================init component==========
CostofRiceChicken.set(0)
CostofRiceBeef.set(0)
CostofRiceFish.set(0)
CostofDelivery.set(0)
CostofRiceFish.set(0)
CostofRiceBeef.set(0)
CostofRiceChicken.set(0)
UnitPriceRiceFish.set(0)
UnitPriceRiceBeef.set(0)
UnitPriceRiceChicken.set(0)
UnitPriceRiceBeef.set(0)
QtyRiceFish.set(0)
QtyRiceBeef.set(0)
QtyRiceChicken.set(0)
Discount.set(0)

TimeOfOrder.set(time.strftime("%H:%M:%S"))
DateOfOrder.set(time.strftime("%d/%m/%Y"))


def Exit():
    qExit= messagebox.askyesno("You are about to cancel your order", "Do you want to cancel your order")
    if qExit > 0:
        root.destroy()
        return

def Reset():
        CustomerRef.set("")
        Tax.set("")
        SubTotal.set("")
        TotalCost.set("")
        CustomerName.set("")
        CustomerPhone.set("")
        CustomerEmail.set("")

def OrderRef():
    Refpay = random.randint(20000, 709467)
    Refpaid = ("PR" + str(Refpay) )
    CustomerRef.set (Refpaid)

def CostofOrder():
      Qty1=float(QtyRiceChicken.get())
      Qty2 = float(QtyRiceBeef.get())
      Qty3 = float(QtyRiceFish.get())

UnitPrice1 =float (UnitPriceRiceChicken.get())
UnitPrice2 =float(UnitPriceRiceBeef.get())
UnitPrice3 =float(UnitPriceRiceFish.get())

CostofRice1="€", str('%.2f'% (Qty1 * UnitPrice1))
CostofRice2="€", str('%.2f'% (Qty2 * UnitPrice2))
CostofRice3="€", str('%.2f'% (Qty3 * UnitPrice3))

CostofRiceChicken.set(CostofRice1)
CostofRiceBeef.set(CostofRice2)
CostofRiceFish.set(CostofRice3)

CostRice1=(Qty1 * UnitPrice1)
CostRice2=(Qty2 * UnitPrice2)
CostRice3=(Qty3 * UnitPrice3)

AllCost = ((Qty1 * UnitPrice1)+(Qty2 * UnitPrice2)+(Qty3 * UnitPrice3))
TaxAll= "€", str('%.2f'% (AllCost)*2)
Tax.set(TaxAll)

SubTotalp= "€", str('%.2f'% (AllCost))
SubTotal.set(SubTotalp)

TotalCostp="€", str('%.2f'% (AllCost+ ((AllCost) *0.02)))

TotalCost.set(TotalCostp)


#=================== =============================


#===================Frame=======================

Tops = Frame(root, width=1350, height=50, bd=16, relief="raise")
Tops.pack(side=TOP)

LF = Frame(root, width=700, height=650, bd=16, relief="raise")
LF.pack(side=LEFT)

RF = Frame(root, width=600, height=650, bd=16, relief="raise")
RF.pack(side=RIGHT)

Tops.configure(background='blue')
LF.configure(background='blue')
RF.configure(background='blue')

LeftInsideLF=Frame(LF, width=700, height=100, bd=8, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=700, height=400, bd=8, relief="raise")
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF=Frame(RF, width=604, height=200, bd=8, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=306, height=400, bd=8, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300, height=400, bd=8, relief="raise")
RightInsideRFRF.pack(side=RIGHT)

#===============================Title======================
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Order Cancelling System", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

# ======================== Top left Frame==========================
lblCustomerName= Label(LeftInsideLF, font=('arial', 14, 'bold'), text="Customer Name",
                        fg="black", bd=10, anchor="w")
lblCustomerName.grid(row=0, column=0)
txtCustomerName = Entry(LeftInsideLF, font=('arial', 14, 'bold'), bd=20, width=43,
                        justify='left', textvariable=CustomerName)
txtCustomerName.grid(row=0, column=1)

lblCustomerPhone= Label(LeftInsideLF, font=('arial', 14, 'bold'), text="Customer Phone",
                        fg="black", bd=10, anchor="w")
lblCustomerPhone.grid(row=1, column=0)
txtCustomerPhone = Entry(LeftInsideLF, font=('arial', 14, 'bold'), bd=20, width=43,
                         justify='left', textvariable=CustomerPhone)
txtCustomerPhone.grid(row=1, column=1)

lblCustomerEmail= Label(LeftInsideLF, font=('arial', 14, 'bold'), text="Customer Email",
                        fg="black", bd=10, anchor="w")
lblCustomerEmail.grid(row=2, column=0)
txtCustomerEmail = Entry(LeftInsideLF, font=('arial', 14, 'bold'), bd=20, width=43,
                        justify='left', textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2, column=1)

# ======================== Top Right Frame=======================
lblDateOfOrder= Label(RightInsideLF, font=('arial', 12, 'bold'), text="Date of Order",
                        fg="black", bd=10, anchor="w")
lblDateOfOrder.grid(row=0, column=0)
txtDateOfOrder = Entry(RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=43,
                       justify='left', textvariable=DateOfOrder)
txtDateOfOrder.grid(row=0, column=1)

lblTimeOfOrder= Label(RightInsideLF, font=('arial', 12, 'bold'), text="Time of Order",
                        fg="black", bd=10, anchor="w")
lblTimeOfOrder.grid(row=1, column=0)
txtTimeOfOrder = Entry(RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=43,
                        justify='left', textvariable=TimeOfOrder)
txtTimeOfOrder.grid(row=1, column=1)

lblCustomerRef= Label(RightInsideLF, font=('arial', 12, 'bold'), text="Customer Ref",
                        fg="black", bd=10, anchor="w")
lblCustomerRef.grid(row=2, column=0)
txtCustomerRef = Entry(RightInsideLF, font=('arial', 12, 'bold'), bd=20, width=43,
                         justify='left', textvariable=CustomerRef)
txtCustomerRef.grid(row=2, column=1)
# ======================== Right Frame=======================================================
lblMethodOfPayment=Label(RightInsideLFLF, font=('arial', 12, 'bold'), text="Method of Payment",
                        fg="black" , bd=16, anchor="w")
lblMethodOfPayment.grid(row=0, column=0)
cmdMethodOfPayment=ttk.Combobox(RightInsideLFLF, font=('arial', 12, 'bold'))
cmdMethodOfPayment['value']=('', 'Cash', 'Debit Card', 'Master')
cmdMethodOfPayment.grid(row=0, column=1)

lblDiscount=Label(RightInsideLFLF, font=('arial', 12, 'bold'), text="Discount",
                        fg="black",  bd=16, anchor="w")
lblDiscount.grid(row=1, column=0)
txtDiscount = Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=16, width=18,
                         justify='left', textvariable=Discount)
txtDiscount.grid(row=1, column=1)

lblTax=Label(RightInsideLFLF, font=('arial', 12, 'bold'), text="Tax",
                        fg="black" ,  bd=16, anchor="w")
lblTax.grid(row=2, column=0)
txtTax = Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=16, width=18,
                        justify='left', textvariable=Tax)
txtTax.grid(row=2, column=1)

lblSubTotal=Label(RightInsideLFLF, font=('arial', 12, 'bold'), text="SubTotal",
                        fg="black" , bd=16, anchor="w")
lblSubTotal.grid(row=3, column=0)
txtSubTotal = Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=16, width=18,
                        justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=3, column=1)

lblTotalCost=Label(RightInsideLFLF, font=('arial', 12, 'bold'), text="TotalCost",
                        fg="black" ,  bd=16, anchor="w")
lblTotalCost.grid(row=4, column=0)
txtTotalCost = Entry(RightInsideLFLF, font=('arial', 12, 'bold'), bd=16, width=18,
                         justify='left', textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1)

# ========================Buttons left Frame=====================
lblItemOrder = Label(LeftInsideLFLF, font=('arial', 14, 'bold'), text="Item Order", fg="black", bd=20)
lblItemOrder.grid(row=0, column=0)

lblQty = Label(LeftInsideLFLF, font=('arial', 14, 'bold'), text="Qty", fg="black", bd=10)
lblQty.grid(row=0, column=1)

lblUnitPrice = Label(LeftInsideLFLF, font=('arial', 14, 'bold'), text="Unit Price", fg="black", bd=20)
lblUnitPrice.grid(row=0, column=2)

lblCostofItem = Label(LeftInsideLFLF, font=('arial', 14, 'bold'), text="Cost of Item", fg="black", bd=20)
lblCostofItem.grid(row=0, column=3)

#=====================#
lblRiceChicken = Label(LeftInsideLFLF, font=('arial', 14, 'bold'), text="Rice Chicken", fg="blue", bd=20)
lblRiceChicken.grid(row=1, column=0)

lblRiceBeef= Label(LeftInsideLFLF, font=('arial', 14, 'bold'), text="Rice Beef", fg="blue", bd=20)
lblRiceBeef.grid(row=2, column=0)

lblRiceFish = Label(LeftInsideLFLF, font=('arial', 14, 'bold'), text="Rice Fish", fg="blue", bd=20)
lblRiceFish.grid(row=3, column=0)

#=========================

txtQtyRiceChicken = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                        fg="black", justify='left', textvariable=QtyRiceChicken)
txtQtyRiceChicken.grid(row=1, column=1)

txtQtyRiceBeef = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                         justify='left', textvariable=QtyRiceBeef)
txtQtyRiceBeef.grid(row=2, column=1)

txtQtyRiceFish = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                         justify='left', textvariable=QtyRiceFish)
txtQtyRiceFish.grid(row=3, column=1)

#============

txtUnitPriceRiceChicken= Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                        justify='left', textvariable=UnitPriceRiceChicken)
txtUnitPriceRiceChicken.grid(row=1, column=2)

txtUnitPriceRiceBeef = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                         justify='left', textvariable=UnitPriceRiceBeef)
txtUnitPriceRiceBeef.grid(row=2, column=2)

txtUnitPriceRiceFish = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                        justify='left', textvariable=UnitPriceRiceFish)
txtUnitPriceRiceFish.grid(row=3, column=2)

#=====================

txtCostofRiceChicken = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                      justify='left', textvariable=CostofRiceChicken)
txtCostofRiceChicken.grid(row=1, column=3)


txtCostofRiceBeef = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                        justify='left', textvariable=CostofRiceBeef)
txtCostofRiceBeef.grid(row=2, column=3)


txtCostofRiceFish = Entry(LeftInsideLFLF, font=('arial', 12, 'bold'), bd=20, width=16,
                         justify='left', textvariable=CostofRiceFish)
txtCostofRiceFish.grid(row=3, column=3)

# ========================Buttons Right Frame=======================================================
btnTotalCost= Button(RightInsideRFRF, pady=8, fg="black", font=('arial', 16, 'bold'),width=11,
                    text="Total Cost", bg="blue", command=CostofOrder).grid(row=0, column=0)
btnReset= Button(RightInsideRFRF, pady=8, fg="black", font=('arial', 16, 'bold'),width=11,
                    text="Reset", bg="blue", command=Reset).grid(row=1, column=0)
btnOderRef= Button(RightInsideRFRF, pady=8, fg="black", font=('arial', 16, 'bold'),width=11,
                    text="Order Ref", bg="blue",command=OrderRef).grid(row=2, column=0)
btnExit= Button(RightInsideRFRF, pady=8, fg="white", font=('arial', 16, 'bold'),width=11,
                    text="Cancel Order", bg="red", command=Exit).grid(row=3, column=0)



root.mainloop()

