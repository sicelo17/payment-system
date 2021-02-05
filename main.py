from tkinter import *
import random
import time
import tkinter.messagebox

root = Tk()
root.geometry('1600x800+0+0')
root.title("Payments Service")

text_input = StringVar()
operator = ''

Tops = Frame(root, width = 1600, height = 50, bg = "powder blue", relief = SUNKEN)
Tops.pack(side = TOP) 

f1 = Frame(root, width = 700, height = 700, relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 300, height = 700, relief = SUNKEN)
f2.pack(side = RIGHT)
# ========================time================
localtime = time.asctime(time.localtime(time.time()))
# ====================Info=====================
lblInfo = Label(Tops, font = ('arial', 50, 'bold'), text = "Payment Service App", fg = "Steel Blue", bd=10, anchor = 'w')
lblInfo.grid(row = 0, column = 0)

lblInfo = Label(Tops, font = ('arial', 20, 'bold'), text = localtime, fg = "Steel Blue", bd=10, anchor = 'w')
lblInfo.grid(row = 1, column = 0)

# ===================================================Calculator===================================================================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDsiplay():
    global operator
    operator = ""
    text_input.set("")


def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_input.set(sumup)
    operator = ''


def Ref():
    x = random.randint(12908, 500876)
    randomRef= str(x)
    rand.set(randomRef)

    CoMJ = float(Male_Jeans.get())
    CoT = float(T_Shirt.get())
    CoMFS = float(Male_Formal_Shoe.get())
    CoS = float(Sandals.get())
    CoFJ= float(Female_Jeans.get())
    CoC = float(Cap.get())

    CostofMale_Jeans = CoMJ * 19.50
    CostofT_Shirt = CoT * 8.00
    CostofMale_Formal_Shoe = CoMFS * 29.99
    CostofSandals = CoS * 12.87
    CostofFemale_Jeans = CoFJ * 21.89
    CostofCap = CoC * 4.69

    CostofMeal = '$', str('%.2f' % (CostofMale_Jeans + CostofT_Shirt + CostofMale_Formal_Shoe + CostofSandals + CostofFemale_Jeans + CostofCap))

    PayTax = ((CostofMale_Jeans + CostofT_Shirt + CostofMale_Formal_Shoe + CostofSandals + CostofFemale_Jeans + CostofCap) * 0.2)

    TotalCost = (CostofMale_Jeans + CostofT_Shirt + CostofMale_Formal_Shoe + CostofSandals + CostofFemale_Jeans + CostofCap)

    Ser_Charge = ((CostofMale_Jeans + CostofT_Shirt + CostofMale_Formal_Shoe + CostofSandals + CostofFemale_Jeans + CostofCap)/99)

    Service = '$', str('%.2f' % Ser_Charge)

    OverAllCost = '$', str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax = '$', str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    iExit = tkinter.messagebox.askyesno("Payment Service App", "Are you sure you want to exit")
    if iExit > 0:
        root.destroy()
    return


def Reset():
    rand.set("")
    Male_Jeans.set("")
    T_Shirt.set("")
    Male_Formal_Shoe.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Cap.set("")
    Tax.set("")
    Cost.set("")
    Sandals.set("")
    Female_Jeans.set("")


txtDisplay = Entry(f2, font = ('arial', 20, 'bold'), textvariable = text_input, bd = 30, insertwidth = 4, bg = "powder blue", justify = 'right')
txtDisplay.grid(columnspan = 4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='7', bg = 'powder blue', command=lambda: btnClick(7)).grid(row=2,column=0)

btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='8', bg = 'powder blue', command=lambda: btnClick(8)).grid(row=2,column=1)

btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='9', bg = 'powder blue', command=lambda: btnClick(9)).grid(row=2,column=2)

Addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='+', bg = 'powder blue', command=lambda: btnClick('+')).grid(row=2,column=3)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='6', bg = 'powder blue', command=lambda: btnClick(6)).grid(row=3,column=0)

btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='5', bg = 'powder blue', command=lambda: btnClick(5)).grid(row=3,column=1)

btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='4', bg = 'powder blue', command=lambda: btnClick(4)).grid(row=3,column=2)

Subtract = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='-', bg = 'powder blue', command=lambda: btnClick('-')).grid(row=3,column=3)

# ----------------------------------------------------------------------------------------------------------------------------------

btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='3', bg = 'powder blue', command=lambda: btnClick(3)).grid(row=4,column=0)

btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='2', bg = 'powder blue', command=lambda: btnClick(2)).grid(row=4,column=1)

btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='1', bg = 'powder blue', command=lambda: btnClick(1)).grid(row=4,column=2)

Multiplication = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='*', bg = 'powder blue', command=lambda: btnClick('*')).grid(row=4,column=3)

# --------------------------------------------------------------------------------------------------------------------------------

btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='0', bg = 'powder blue', command=lambda: btnClick(0)).grid(row=5,column=0)
btnclear = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='CE', bg = 'powder blue', command= btnClearDsiplay).grid(row=5,column=1)
btnequal = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='=', bg = 'powder blue', command = btnEqualsInput).grid(row=5,column=2)
Division = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text='/', bg = 'powder blue', command=lambda: btnClick('/')).grid(row=5,column=3)

# ============================================================ Labels and buttons =============================================
rand = StringVar()
Male_Jeans = StringVar()
T_Shirt = StringVar()
Male_Formal_Shoe = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Cap = StringVar()
Tax = StringVar()
Cost = StringVar()
Sandals = StringVar()
Female_Jeans = StringVar()


lblReference = Label(f1, font=('arial', 16, 'bold'), text = 'Reference', bd=16, anchor = 'w').grid(row=0, column=0)
txtReference = Entry(f1, font =('arial', 16, 'bold'), textvariable = rand, bd =10, insertwidth= 4, bg='powder blue', justify = "right").grid(row=0, column=1)

lblMale_Jeans = Label(f1, font=('arial', 16, 'bold'), text = 'Male Jeans', bd=16, anchor = 'w').grid(row=1, column=0)
txtMale_Jeans= Entry(f1, font =('arial', 16, 'bold'), textvariable = Male_Jeans, bd =10, insertwidth= 4, bg='powder blue', justify = "right").grid(row=1, column=1)

lblT_Shirt = Label(f1, font=('arial', 16, 'bold'), text = 'T-shirt', bd=16, anchor = 'w').grid(row=2, column=0)
txtT_Shirt = Entry(f1, font =('arial', 16, 'bold'), textvariable = T_Shirt, bd =10, insertwidth= 4, bg='powder blue', justify = "right").grid(row=2, column=1)

lblMale_Formal_Shoe = Label(f1, font=('arial', 16, 'bold'), text = 'Male Formal Shoe', bd=16, anchor = 'w').grid(row=3, column=0)
txtMale_Formal_Shoe = Entry(f1, font =('arial', 16, 'bold'), textvariable = Male_Formal_Shoe, bd =10, insertwidth= 4, bg = 'powder blue', justify = 'right').grid(row=3, column=1)

lblSandals = Label(f1, font=('arial', 16, 'bold'), text = 'Sandals', bd=16, anchor = 'w').grid(row=4, column=0)
txtSandals = Entry(f1, font =('arial', 16, 'bold'), textvariable = Sandals, bd =10, insertwidth= 4, bg = 'powder blue', justify = 'right').grid(row=4, column=1)

lblCheese = Label(f1, font=('arial', 16, 'bold'), text = 'Female Jeans', bd=16, anchor = 'w').grid(row=5, column=0)
txtCheese = Entry(f1, font =('arial', 16, 'bold'), textvariable = Female_Jeans, bd =10, insertwidth= 4, bg = 'powder blue', justify = 'right').grid(row=5, column=1)

# ========================================== Restaurant Info 2 =================================================================
lblCap = Label(f1, font=('arial', 16, 'bold'), text = 'Cap', bd=16, anchor = 'w').grid(row=0, column=2)
txtCap = Entry(f1, font =('arial', 16, 'bold'), textvariable = Cap, bd=10, insertwidth=4, bg='#ffffff', justify = "right").grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text = 'Cost of meal', bd=16, anchor = 'w').grid(row=1, column=2)
txtCost= Entry(f1, font =('arial', 16, 'bold'), textvariable = Cost, bd =10, insertwidth= 4, bg='#ffffff', justify = "right").grid(row=1, column=3)

lblService = Label(f1, font=('arial', 16, 'bold'), text = 'Service Charge', bd=16, anchor = 'w').grid(row=2, column=2)
txtService = Entry(f1, font =('arial', 16, 'bold'), textvariable = Service_Charge, bd =10, insertwidth= 4, bg='#ffffff', justify = "right").grid(row=2, column=3)

lblStateTax = Label(f1, font=('arial', 16, 'bold'), text = 'State Tax', bd=16, anchor = 'w').grid(row=3, column=2)
txtStateTax = Entry(f1, font =('arial', 16, 'bold'), textvariable = Tax, bd =10, insertwidth= 4, bg = '#ffffff', justify = 'right').grid(row=3, column=3)

lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text = 'Sub Total', bd=16, anchor = 'w').grid(row=4, column=2)
txtSubTotal = Entry(f1, font =('arial', 16, 'bold'), textvariable = SubTotal, bd =10, insertwidth= 4, bg = '#ffffff', justify = 'right').grid(row=4, column=3)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text = 'Total Cost', bd=16, anchor = 'w').grid(row=5, column=2)
txtTotalCost = Entry(f1, font =('arial', 16, 'bold'), textvariable = Total, bd =10, insertwidth= 4, bg = '#ffffff', justify = 'right').grid(row=5, column=3)

# ============================================================ Buttons ======================================================================

btnTotal = Button(f1, padx=16, pady=8, bd=16, fg='black',font=('arial', 16, 'bold'), width=20, text='Total', bg='powder blue', command = Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg='black',font=('arial', 16, 'bold'), width=10, text='Reset', bg='powder blue', command = Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg='black',font=('arial', 16, 'bold'), width=10, text='Exit', bg='powder blue', command = qExit).grid(row=7, column=3)

root.mainloop()
