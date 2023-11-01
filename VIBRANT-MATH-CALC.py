from tkinter import *


#APP CREATION , APP TITLE , APP BACKGROUND COLOR:
    
app=Tk()

app.title("VIBRANT-MATH-CALC")

app.configure(bg="#D3D3D3")


#CREATION AND POSITION OF HEADING USING LABEL:
    
heading = Label(app, text="VIBRANT - MATH - CALC", font=("Helvetica", 20, "bold"), bg="#D3D3D3")

heading.grid(row=8, column=0, columnspan=4, padx=10, pady=10)


#ENTRY-INPUTBOX-CREATION AND POSITIONING:
    
inputBox=Entry(app,width=40,borderwidth=5, bg="black" , fg="green",font=(20))

inputBox.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


#INPUT-BOX-FUNCTION:
    
def buttonClick(number):
    
    current=inputBox.get()
    
    inputBox.delete(0,END)
    
    inputBox.insert(0,str(current)+str(number))
    
    
#CLEAR-BUTTON-FUNCTION: 
    
def buttonClear():
    
    inputBox.delete(0,END)
    
    
#ADD-BUTTON-FUNCTION:
    
def buttonAdd():
    
    firstNumber=inputBox.get()
    
    global fNum
    
    global math
    
    math="ADD"
    
    fNum=int(firstNumber)
    
    inputBox.delete(0,END)
    
    
#SUB-BUTTON-FUNCTION:
    
def buttonSub():

    firstNumber=inputBox.get()
    
    global fNum
    
    global math
    
    math="SUB"
    
    fNum=int(firstNumber)
    
    inputBox.delete(0,END) 


#MULTI-BUTTON-FUNCTION:
    
def buttonMul():

    firstNumber=inputBox.get()
    
    global fNum
    
    global math
    
    math="MULTI"
    
    fNum=int(firstNumber)
    
    inputBox.delete(0,END)
    
    
#DIV-BUTTON-FUNCTION:
    
def buttonDiv():

    firstNumber=inputBox.get()
    
    global fNum
    
    global math
    
    math="DIV"
    
    fNum=int(firstNumber)
    
    inputBox.delete(0,END)
    
    
#EQUAL-BUTTON-FUNCTION:
     
def buttonEqual():

     secondNumber=inputBox.get()
     
     inputBox.delete(0,END)
     
     if math=="ADD":
     
        inputBox.insert(0,fNum + int(secondNumber))
        
     if math=="SUB":
        
         inputBox.insert(0,fNum - int(secondNumber))
           
     if math=="MULTI":
           
         inputBox.insert(0,fNum * int(secondNumber))
              
     if math=="DIV":
              
         inputBox.insert(0,fNum / int(secondNumber))
         
         
    
    
#BUTTON-CREATION: 

button1=Button(app,text="1",padx=60,pady=30,command=lambda:buttonClick(1))

button2=Button(app,text="2",padx=60,pady=30,command=lambda:buttonClick(2))

button3=Button(app,text="3",padx=58,pady=30,command=lambda:buttonClick(3))

button4=Button(app,text="4",padx=60,pady=30,command=lambda:buttonClick(4))

button5=Button(app,text="5",padx=60,pady=30,command=lambda:buttonClick(5))

button6=Button(app,text="6",padx=58,pady=30,command=lambda:buttonClick(6))

button7=Button(app,text="7",padx=60,pady=30,command=lambda:buttonClick(7))

button8=Button(app,text="8",padx=60,pady=30,command=lambda:buttonClick(8))

button9=Button(app,text="9",padx=58,pady=30,command=lambda:buttonClick(9))

button0=Button(app,text="0",padx=60,pady=30,command=lambda:buttonClick(0))



buttonadd=Button(app,text="+",padx=60,pady=30,command=buttonAdd)

buttonsub=Button(app,text="-",padx=62,pady=30,command=buttonSub)

buttonmul=Button(app,text="*",padx=62,pady=30,command=buttonMul)

buttondiv=Button(app,text="/",padx=60,pady=30,command=buttonDiv)




buttonequal=Button(app,text="=",padx=137,pady=30,command=buttonEqual)

buttonclear=Button(app,text="C",padx=137,pady=30,command=lambda:buttonClear())





#BUTTONS-ARRANGEMENTS:
    
button1.grid(row=3,column=0)

button2.grid(row=3,column=1)

button3.grid(row=3,column=2)


button4.grid(row=2,column=0)

button5.grid(row=2,column=1)

button6.grid(row=2,column=2)



button7.grid(row=1,column=0)

button8.grid(row=1,column=1)

button9.grid(row=1,column=2)


button0.grid(row=4,column=0)



buttonclear.grid(row=4,column=1,columnspan=2)

buttonequal.grid(row=5,column=1,columnspan=2)


buttonadd.grid(row=5,column=0)

buttonsub.grid(row=6,column=0)

buttonmul.grid(row=6,column=1)

buttondiv.grid(row=6,column=2)







#VIBRANTS-COLORS:
    
button1.config(bg="lightblue", fg="black",font=(50))

button2.config(bg="lightblue", fg="black",font=(50))

button3.config(bg="lightblue", fg="black",font=(50))

button4.config(bg="lightblue", fg="black",font=(50))

button5.config(bg="lightblue", fg="black",font=(50))

button6.config(bg="lightblue", fg="black",font=(50))

button7.config(bg="lightblue", fg="black",font=(50))

button8.config(bg="lightblue", fg="black",font=(50))

button9.config(bg="lightblue", fg="black",font=(50))

button0.config(bg="lightblue", fg="black",font=(50))



buttonadd.config(bg="lightgreen", fg="black",font=(50))

buttonsub.config(bg="lightgreen", fg="black",font=(50))

buttonmul.config(bg="lightgreen", fg="black",font=(50))

buttondiv.config(bg="lightgreen", fg="black",font=(50))


buttonequal.config(bg="lightcoral", fg="black",font=(50))

buttonclear.config(bg="lightcoral", fg="black",font=(50))



#RUNS THE APP:
    
app.mainloop()