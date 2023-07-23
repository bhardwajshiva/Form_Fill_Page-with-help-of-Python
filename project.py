# importing only those functions which are needed
from tkinter import*
  
# creating tkinter window
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

# Heading
Label(root,text="Python Regestration Form", font="ar 15 bold").grid(row=0,column=3)

# Field Name
name=Label(root,text="Name")
Phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency")
paymentmood=Label(root,text="Payment Mood")

# Packing Field
name.grid(row=1 ,column=2)
Phone.grid(row=2 ,column=2)
gender.grid(row=3 ,column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# Variable for storing data
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmoodvalue=StringVar
emergencyvalue=StringVar

checkvalue=IntVar
# Create entry field
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)

genderentry=Entry(root,textvariable=gendervalue)
paymentmoodentry=Entry(root,textvariable=paymentmoodvalue)
emergencypayentry=Entry(root,textvariable=emergencyvalue)
# Packing entry field
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
paymentmoodentry.grid(row=4,column=3)
emergencypayentry.grid(row=5,column=3)



# creating checkbox
checkbtn=Checkbutton(text="rember me?",variable=checkvalue)
checkbtn.grid(row=6,column=3)

# Submit Button
Button(text="Submit",command=getvals).grid(row=7,column=3)
root.mainloop()
