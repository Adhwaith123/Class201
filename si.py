from tkinter import *
window=Tk()

# add widgets here


window.title('Simple Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="Simple Interest Calculator", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle=Label(window,text="Enter principle",fg="black",bg="lightcyan",font=("Calibri",12),bd=1)
principle.place(x=20,y=130)

principle1=Entry(window,text="",bd=2,width=22)
principle1.place(x=155,y=132)

rate=Label(window,text="Enter rate",fg="black",bg="lightcyan",font=("Calibri",12),bd=1)
rate.place(x=20,y=170)

rate1=Entry(window,text="",bd=2,width=22)
rate1.place(x=155,y=172)

time=Label(window,text="Enter time",fg="black",bg="lightcyan",font=("Calibri",12),bd=1)
time.place(x=20,y=200)

time1=Entry(window,text="",bd=2,width=22)
time1.place(x=155,y=202)

def calculate_bmi():
    principleValue=float(principle1.get())
    rateValue=float(rate1.get())
    timeValue=float(time1.get())
    si=(principle*rate*time)/100
    si=round(si,1)
    

button=Button(window, text="Submit",fg="black",bg="lightcyan",font=("Calibri",12),bd=1,command=calculate_bmi)
button.place(x=200, y=260)


    
result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

result_label.destroy()

            

window.mainloop()
