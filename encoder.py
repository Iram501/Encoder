def encoding(event):
    text=e.get("1.0","end-1c")
    n=3
    '''we are splitting the list using insert method instead of split as we want to count white
    spaces also split function will not count white spaces by default.'''
    #*************************making list of three for spaces in end ***************
    b=[]     #if we want to take all 3 3 letters in the list
    for i in range (0,len(text),n):
        if (len(text[i:i+n])==3):
            b.insert(i,text[i:i+n])        #if we want to take all 3 3 letters in the list
        elif (len(text[i:i+n])<3):
            if (len(text[i:i+n])==1):
                b.insert(i,text[i:i+n]+"  ")
            else:
                b.insert(i,text[i:i+n]+" ")
        #a=(text[i:i+n])  #if we dont want to tke letters in the list
    #print(b)
    #*******************************joining the list*********************************
    #c=''.join(b)
    #print('c=',c)
    #*************************converting into ascii**************************
    lis=[]
    x=0
    y=0
    for i in b:
        for j in i: 
            if ((x==len(b)-1) and (y==len(i)-1) and (j==' ')):
                a=0
                lis.append(a)
            elif ((x==len(b)-1) and (i[1]==' ') and (i[2]==' ') and (j==' ')):
                a=0
                lis.append(a)
            else:
                a=ord(j)
                lis.append(a)
            if (y!=2):
                y+=1
        x+=1
    #print(lis)
    #************converting to binary*****************
    val1=''
    for i in lis:
        val=''    
        while (i!=0):
            val=val + str(i%2)
            i=i//2
        if i==0:
            if(len(val)<8):
                for j in range(len(val),8):
                    val=val+str(0)
                val1=val+val1
    val2=(val1[::-1])
    #print(val2)
    #***********splitting string of binary no. in 6 digits using list comprehension***********
    m=6
    val3=[(val2[i:i+m]) for i in range(0,len(val2),m)]    
    #print(val3)
    #*******************converting 6y digits into decimal number******************************
    x=0
    for i in val3:
        z=0
        m=6-1
        for j in i:
            z+=int(int(j)*(2**m))
            m-=1
        val3[x]=z
        x+=1
    #print(val3)
    
    #******************************mapping through index***********************************
    encode=''
    for i in val3:
        encode=str(encode)+str(l[i]) 
    if (encode[len(encode)-1]=='A'):
        en=list(encode)
        en[len(en)-1]='='
        encode=''.join(en)
    if (encode[len(encode)-2]=='A'):
        en=list(encode)
        en[len(en)-2]='='
        encode=''.join(en)
    #lab2=tkinter.Label(scrn,text='Encoded data...',bg='pink',fg='black',font=('normal',15))
    #lab2.pack()
    #lab2.place(x=600,y=20)
    lab2.configure(text="Encoded data...")
    tab.configure(state='normal')
    tab.delete(0.0,'end')
    tab.insert(0.0,encode)
    tab.configure(state='disabled')
   #*******************************encoding done:)************************************
#***********************************indexing***********************************************
capital=65
small=97
numbers=0
l=[]
for i in range (0,62):
    if (i<26):
        l.append(chr(capital))
        capital+=1
    if (i>=26 and i<52):
        l.append(chr(small))
        small+=1
    if (i>=52 and i<62):
        l.append(str(numbers))
        numbers+=1
l.append(chr(43))
l.append(chr(47))
#**************************indexing done*********************************
def decoding(event):
    Dtext=e.get("1.0","end-1c")
    #****************************mapping***********************************************
    dtext=list(Dtext)
    for i in range(len(dtext)):
        for j in range(len(l)):
            if (dtext[i]==l[j]):
                dtext[i]=j

    if (dtext[len(dtext)-1]=='='):
        dtext[len(dtext)-1]=0
    if (dtext[len(dtext)-2]=='='):
        dtext[len(dtext)-2]=0
    #print(dtext)   
    #******************converting mapped decimal no. into binary no.********************
    temp1=''                                                   
    for i in dtext:
        temp=''    
        while (i!=0):
            temp=temp + str(i%2)
            i=i//2
        if i==0:
            if(len(temp)<6):
                for j in range(len(temp),6):
                    temp=temp+str(0)
            temp1=temp+temp1
    temp2=(temp1[::-1])
    #print(temp2)
    #***********splitting string of binary no. in 8 digits using list comprehension***********
    q=8
    temp3=[(temp2[i:i+q]) for i in range(0,len(temp2),q)]    
    #print(temp3)
    #*******************converting 8 digits into decimal number******************************
    w=0
    for i in temp3:
        r=0
        q=8-1
        for j in i:
            r+=int(int(j)*(2**q))
            q-=1
        temp3[w]=r
        w+=1
    #print(temp3)
    #*************************converting into character**************************
    lis1=[]
    x1=0
    for i in temp3:
        if ((x1==len(temp3)-1) and (i==0)):
            temp3.remove(0)
        elif ((x1==len(temp3)-2) and (i==0)):
            temp3.remove(0)
        else:
            a=chr(i)
            lis1.append(a)
        x1+=1
    #print(lis1)
    #*******************combining list*************************
    decode=''.join(lis1)
    #lab2=tkinter.Label(scrn,text='Decoded data...',bg='pink',fg='black',font=('normal',15))
    #lab2.pack()
    #lab2.place(x=600,y=20)
    lab2.configure(text="Decoded data...")
    tab.configure(state='normal')
    tab.delete(0.0,'end')
    tab.insert(0.0,decode)
    tab.configure(state='disabled')
    #*******************decoding done:)*****************************************

   
#**********************making window using tkinter**************************
import tkinter
scrn=tkinter.Tk()                           #making object of class Tk
scrn.title("ENCODING AND DECODING")
scrn.geometry('1000x700+300+40')   #size and position of o/p scrn
scrn.resizable(height=False,width=False)#making o/p scrn unchngable
scrn.configure(bg='pink')

 #***************text boxes and buttons**********************
e=tkinter.Text(scrn,bg="white",font=12)
e.pack()
e.place(x=60,y=50,width=350,height=600)

tab=tkinter.Text(scrn,bg="white",font=12,state='disabled')
tab.pack()
tab.place(x=600,y=50,width=350,height=600)

btt=tkinter.Button(scrn,text="  ENCODE  ",bg="white",fg="dark grey",font=("normal",20,"bold"),command='show_data')
btt.pack()
btt.bind("<Button>",encoding)
btt.place(x=417,y=250)

btt1=tkinter.Button(scrn,text="  DECODE  ",bg="white",fg="dark grey",font=("normal",20,"bold"))
btt1.pack()
btt1.bind('<Button>',decoding)
btt1.place(x=417,y=350)

lab1=tkinter.Label(scrn,bg='pink',fg='black',text='Enter the message here...',font=('normal',15))
lab1.pack()
lab1.place(x=60,y=20)

lab2=tkinter.Label(scrn,bg='pink',fg='black',font=('normal',15))
lab2.pack()
lab2.place(x=600,y=20)

scrn.mainloop()  #it give window it is a infinite loop hold the scrn untill we close
