from tkinter import *
from tkinter import filedialog as fd


def selectedRB():
    if r_var.get() == 0:
        return 'Плановое ТО'
    if r_var.get() == 1:
        return 'Шиномонтаж'
    if r_var.get() == 2:
        return 'Диагностика автомобиля'
    if r_var.get() == 3:
        return 'Мелко-срочный ремонт'
    if r_var.get() == 4:
        return 'Кузовой ремонт'
    if r_var.get() == 5:
        return 'Ремонт узлов и агрегатов'

def check():
    lst=[]
    if cb1.get() ==1:
        lst.append(ch1['text'])
    if cb2.get() ==1:
        lst.append(ch2['text'])
    if cb3.get() ==1:
        lst.append(ch3['text'])
    if cb4.get() ==1:
        lst.append(ch4['text'])
    if cb5.get() ==1:
        lst.append(ch5['text'])
    return lst
    
def selected_item():
    for i in enListBox.curselection():
        return(enListBox.get(i))

def addItem():
    title = ' '*round((orderFinal.winfo_width()/8))+'ЗАКАЗ'+' '*round((orderFinal.winfo_width()/8))
    orderFinal.insert(END,title)
    titleD = '_'*round((orderFinal.winfo_width()/6))
    orderFinal.insert(END,titleD)  
    orderFinal.insert(END,'')   
    nameO=f"Клиент:"
    nameO=nameO+" "*round((orderFinal.winfo_width()/10)-3)+entryFIO.get()
    orderFinal.insert(END,nameO)
    nameA=f"Автомобиль:"
    nameA=nameA+" "*round((orderFinal.winfo_width()/10)-13)
    nameA=nameA+entryC.get()+' '+entryDateC.get()+" года"
    orderFinal.insert(END,nameA)
    nameA=f"Основная услуга:      {selectedRB()}"
    orderFinal.insert(END,nameA)
    l=check()
    try:
        l[0]=" "*round((orderFinal.winfo_width()/8)-18)+l[0]
    except IndexError:
        l.append(' ')
    nameA=f"Доп.услуги:"+l[0]
    orderFinal.insert(END,nameA)  
    for ch in range(1,len(l)):
        l[ch]=" "*round((orderFinal.winfo_width()/7)-1)+l[ch]
        orderFinal.insert(END,l[ch])
    try:
        select = selected_item()
        select=" "*round((orderFinal.winfo_width()/10)-12)+select
    except TypeError:
        select=''
    spec=f"Специалист:{select}"
    orderFinal.insert(END,spec)
   
def delList():
        orderFinal.delete(0,END)
        entryC.delete(0, END)
        entryFIO.delete(0, END)
        entryDateC.delete(0, END)
        entryP.delete(0, END)
        cb1.set(0)
        cb2.set(0)
        cb3.set(0)
        cb4.set(0)
        cb5.set(0)
        enListBox.select_clear(0,END)

def extract_text():
    file_name = fd.asksaveasfilename()+".txt"
    with open (file_name,'w+') as f:
        s = orderFinal.get(0, END)
        for  line in s:
            f.write(line + '\n')

  

root = Tk()
root.title("Сервисный центр")
root.geometry("900x800")


#Верхний фрейм
frametopBig= Frame(root)
#Серединный фрейм
frameMid = Frame(root)

#Нижний фрейм
frameBot = Frame(root)

#Фреймы, которые находятся в верхнем фрейме
frameBL = Frame(frametopBig)
frameBR = Frame(frametopBig)
frameName = Frame(frameBL,padx=30) 
frame2 = Frame(frameBL,padx=125) 
frame3 = Frame(frameBL,padx=51) 
frame4 = Frame(frameBL,padx=7)
frameRadioBut = Frame(frameBR, padx=20)

#Фреймы, которые находятся в среднем фрейме
framelServ=LabelFrame(frameMid,text= "Услуги:")
framelServA=LabelFrame(frameMid,text= "Дополнительные услуги:")
framelServSp= LabelFrame(frameMid,text="Инженер сервиса-центра:")

#Фреймы, которые находятся в среднем фрейме
frameFinal=Frame(frameBot)

#Виджеты верхнего фрейма
lableTop = Label (root, text='Сервисный центр "Шараш-Монтаж',justify='center',fg='black',font="Arial 18 bold")

lalelE = Label(frameName, text='Фамилия Имя клиента:', font='Arial 12 normal')
entryFIO = Entry(frameName, width=40)

labelP = Label(frame2, text='Телефон:', font='Arial 12 normal')
entryP = Entry(frame2, width=10)

labelC = Label(frame3, text='Марка автомобиля:', font='Arial 12 normal')
entryC = Entry(frame3, width=10)

labelDateC = Label(frame4, text='Год выпуска автомобиля:', font='Arial 12 normal')
entryDateC = Entry(frame4, width=10)

r_var = BooleanVar()
r_var.set(0)
r1 = Radiobutton(frameRadioBut,text='первичное обращение',variable=r_var, value=0)
r2 = Radiobutton(frameRadioBut,text='повторное обращение',variable=r_var, value=1)

#Виджеты серединного фрейма
r_varServ = BooleanVar()
r_varServ.set(0)
rs1 = Radiobutton(framelServ,text='Плановое ТО',variable=r_varServ, value=0)
rs2 = Radiobutton(framelServ,text='Шиномонтаж',variable=r_varServ, value=1)
rs3 = Radiobutton(framelServ,text='Диагностика автомобиля',variable=r_varServ, value=2)
rs4 = Radiobutton(framelServ,text='Мелко-срочный ремонт',variable=r_varServ, value=3)
rs5 = Radiobutton(framelServ,text='Кузовой ремонт',variable=r_varServ, value=4)
rs6 = Radiobutton(framelServ,text='Ремонт узлов и агрегатов',variable=r_varServ, value=5)

cb1=IntVar()
cb2=IntVar()
cb3=IntVar()
cb4=IntVar()
cb5=IntVar()
ch1 = Checkbutton(framelServA,text="Мойка",variable=cb1,onvalue=1, offvalue=0,)
ch2 = Checkbutton(framelServA,text="Химчистка",variable=cb2,onvalue=1, offvalue=0,)
ch3 = Checkbutton(framelServA,text="Антикоррозийная обработка",variable=cb3,onvalue=1, offvalue=0,)
ch4 = Checkbutton(framelServA,text="Тонировка",variable=cb4,onvalue=1, offvalue=0,)
ch5 = Checkbutton(framelServA,text="Установка сигнализации",variable=cb5,onvalue=1, offvalue=0,)

specialists_var=Variable(value=["Орлов И.С.","Ильин. О.П.","Сорокин К.М.","Сидоров В.В.", "Зверев Р.Д."])

enListBox=Listbox(framelServSp,listvariable=specialists_var,height=6,selectmode=EXTENDED)

lableTop.pack(pady=[2, 15],)

#Виджеты нижнего фрейма
buttonSave=Button(frameFinal,text="Сформировать заказ",command=lambda:[selected_item(), addItem()],activebackground='lightblue')
buttonDel=Button(frameFinal,text="Очистить",command=delList, activebackground='lightblue')
orderFinal= Listbox(frameBot,width=45)
buttonInFile=Button(frameBot,text="Сохранить в файл",command=extract_text, activebackground='lightblue')

#Верхний большой фрейм
frametopBig.pack(anchor="nw")
frameBL.pack(anchor="nw",side=LEFT)
frameBR.pack(anchor="ne",side=LEFT)

frameName.pack(anchor="nw")
lalelE.pack(side=LEFT)
entryFIO.pack(side=RIGHT)


frameRadioBut.pack()
r1.pack()
r2.pack()

frame2.pack(anchor="nw")
labelP.pack(side=LEFT)
entryP.pack(side=RIGHT)

frame3.pack(anchor="nw")
labelC.pack(side=LEFT)
entryC.pack(side=RIGHT)

frame4.pack(anchor="nw")
labelDateC.pack(side=LEFT)
entryDateC.pack(side=RIGHT)

#Серединный фрейм
frameMid.pack(anchor="nw", pady=7)
framelServ.pack(anchor="nw",padx=[15,30], side=LEFT)
rs1.pack(anchor="nw")
rs2.pack(anchor="nw")
rs3.pack(anchor="nw")
rs4.pack(anchor="nw")
rs5.pack(anchor="nw")
rs6.pack(anchor="nw")

framelServA.pack(anchor="nw",padx=[15,30], side=LEFT)
ch1.pack(anchor="nw")
ch2.pack(anchor="nw")
ch3.pack(anchor="nw")
ch4.pack(anchor="nw")
ch5.pack(anchor="nw")

framelServSp.pack(anchor="nw",padx=[15,30], side=LEFT)
enListBox.pack(anchor="nw")

#Нижний фрейм
frameBot.pack(anchor="nw", pady=[7,10],padx=8)
frameFinal.pack(anchor="nw",pady=[0,15])
buttonSave.pack(anchor="nw",side=LEFT,padx=[0,15],ipadx=10,ipady=3)
buttonDel.pack(anchor="nw",side=LEFT,ipadx=10,ipady=3)
orderFinal.pack(anchor="nw") 
buttonInFile.pack(anchor="nw",side=LEFT,ipadx=10,ipady=3)
root.mainloop()

