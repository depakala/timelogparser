import os
import sys
from datetime import *
import math
import streamlit as st
from datetime import datetime
import time

def parser(folder):

    infolist=[]
    extra = []
    doc = open(folder,"r")
    si=0
    for i in doc:
        infolist.append(i)
        #print(i)

    if "time log" in infolist[0].lower():

        pair=[]

        for i in infolist:
            a=[]
            b=[]
            c=[]
            s=''
            s1=''
            first=''
            second=''
            k=folder


            for j in range(len(i)-9):
                if(i[j] == '1')and(i[j+1] == '0' or i[j+1] == '1' or i[j+1] == '2' ) and (i[j+2] == ':') and (i[j+8] == '-'):
                    s=i[j]+i[j+1]
                    a.append(s)
                    j=j+1

                elif(i[j] == '0' or i[j] == '1' or i[j] == '2' or i[j] == '3' or i[j] == '4' or i[j] == '5' or i[j] == '6' or i[j] == '7' or i[j] == '8' or i[j] == '9') and (i[j+1] == ':') and (i[j+7]=='-') and(i[j-1]!='0' or i[j-1]!='1' or i[j-1]!='2'):
                    s=i[j]
                    a.append(s)

                if(i[j] == ':') and ((i[j+4]=='M') or (i[j+4]=='m')) and (i[j+6]=='-'):
                    s=i[j+1]+i[j+2]
                    s1=i[j+3]+i[j+4]
                    a.append(s)
                    a.append(s1)
                    j=j+4

                if(i[j] == '0' or i[j] == '1' or i[j] == '2' or i[j] == '3' or i[j] == '4' or i[j] == '5' or i[j] == '6' or i[j] == '7' or i[j] == '8' or i[j] == '9') and (i[j+1] == ':') and (i[j+7]!='-'):
                    s=i[j]
                    b.append(s)

                elif(i[j] == '1')and(i[j+1] == '0' or i[j+1] == '1' or i[j+1] == '2' ) and (i[j+2] == ':') and (i[j+8] != '-'):
                    s=i[j]+i[j+1]
                    b.append(s)
                    j=j+1



                if(i[j] == ':') and ((i[j+4]=='M') or (i[j+4]=='m')) and (i[j+6]!='-'):
                    s=i[j+1]+i[j+2]
                    s1=i[j+3]+i[j+4]
                    b.append(s)
                    b.append(s1)
                    j=j+4


                #if len(a)== 3 and len(b)==3:
                if j == len(i)-10:
                    if len(a)>2 and len(b)>2:
                        c.append(a)
                        c.append(b)
                        pair.append(c)

                        #print(a,b)

            for j in range(len(i)-8):
                if len(i) <= 27:
                    #print("hui")
                    #print(i,j,i[j])
                    extra.append(i)


        #extra.pop(0)
        #extra.pop(0)
        if k[-7] == 'b':
            si = 0.25
        elif k[-7] == 'g':
            si = -9.23
        elif k[-7] == 'r':
            si = -0.85
        elif k[-7] == 't':
            si =-12.63
        elif k[-7] == 'h':
            si = -21.39
        for i in range(len(extra)):
            for j in range(i+1,len(extra)-1):
                if extra[i] == extra[j]:
                    extra[i]=0

        extra = [i for i in extra if i != 0]
        #print(extra)
        for i in extra:
            a=[]
            b=[]
            c=[]
            s=''
            s1=''
            for j in range(len(i)):
                if j>=7:
                    if j==8:
                        if(i[j] == '2' or i[j] == '3' or i[j] == '4' or i[j] == '5' or i[j] == '6' or i[j] == '7' or i[j] == '8' or i[j] == '9'):
                            s=i[j]
                            a.append(s)
                        elif(i[j] == '1') and (i[9]=='0' or i[9]=='1' or i[9]=='2'):
                            s=i[8]+i[9]
                            a.append(s)
                        elif(i[j]=='1'):
                            s=i[8]
                            a.append(s)
                    if j==9:
                        if(i[j] == '2' or i[j] == '3' or i[j] == '4' or i[j] == '5' or i[j] == '6' or i[j] == '7' or i[j] == '8' or i[j] == '9'):
                            s=i[j]
                            a.append(s)
                        elif(i[j] == '1') and (i[10]=='0' or i[10]=='1' or i[10]=='2'):
                            s=i[9]+i[10]
                            a.append(s)
                        elif(i[j]=='1'):
                            s=i[9]
                            a.append(s)
                    if j==10:
                        if(i[j] == '2' or i[j] == '3' or i[j] == '4' or i[j] == '5' or i[j] == '6' or i[j] == '7' or i[j] == '8' or i[j] == '9'):
                            s=i[j]
                            a.append(s)
                        elif(i[j] == '1') and (i[10]=='0' or i[10]=='1' or i[10]=='2'):
                            s=i[10]+i[11]
                            a.append(s)
                        elif(i[j]=='1'):
                            s=i[10]
                            a.append(s)
                    if j==9:
                        if i[j]==':':
                            s=i[j+1]+i[j+2]
                            s1=i[j+3]+i[j+4]
                            a.append(s)
                            a.append(s1)
                    if j==10:
                        if i[j]==':':
                            s=i[j+1]+i[j+2]
                            s1=i[j+3]+i[j+4]
                            a.append(s)
                            a.append(s1)
                    if j==11:
                        if i[j]==':':
                            s=i[j+1]+i[j+2]
                            s1=i[j+3]+i[j+4]
                            a.append(s)
                            a.append(s1)
                    if j==15:
                        if i[j]=='-':
                            if(i[j+2] == '2' or i[j+2] == '3' or i[j+2] == '4' or i[j+2] == '5' or i[j+2] == '6' or i[j+2] == '7' or i[j+2] == '8' or i[j+2] == '9'):
                                s=i[j+2]
                                b.append(s)
                                s=i[j+4]+i[j+5]
                                b.append(s)
                                s=i[j+6]+i[j+7]
                                b.append(s)
                            elif(i[j+2] =='1') and (i[j+3]!='0' or i[j+3]!='1' or i[j+3]!='2'):
                                s=i[j+2]+i[j+3]
                                b.append(s)
                                s=i[j+5]+i[j+6]
                                b.append(s)
                                s=i[j+7]+i[j+8]
                                b.append(s)
                            elif(i[j+2] =='1'):
                                s=i[j+2]
                                b.append(s)
                                s=i[j+4]+i[j+5]
                                b.append(s)
                                s=i[j+6]+i[j+7]
                                b.append(s)
                    if j==16:
                        if i[j]=='-':
                            if(i[j+2] == '2' or i[j+2] == '3' or i[j+2] == '4' or i[j+2] == '5' or i[j+2] == '6' or i[j+2] == '7' or i[j+2] == '8' or i[j+2] == '9'):
                                s=i[j+2]
                                b.append(s)
                                s=i[j+4]+i[j+5]
                                b.append(s)
                                s=i[j+6]+i[j+7]
                                b.append(s)
                            elif(i[j+2] =='1') and (i[j+3]=='0' or i[j+3]=='1' or i[j+3]=='2'):
                                s=i[j+2]+i[j+3]
                                b.append(s)
                                s=i[j+5]+i[j+6]
                                b.append(s)
                                s=i[j+7]+i[j+8]
                                b.append(s)
                            elif(i[j+2] =='1'):
                                s=i[j+2]
                                b.append(s)
                                s=i[j+4]+i[j+5]
                                b.append(s)
                                s=i[j+6]+i[j+7]
                                b.append(s)
                    if j==17:
                        if i[j]=='-':
                            if(i[j+2] == '2' or i[j+2] == '3' or i[j+2] == '4' or i[j+2] == '5' or i[j+2] == '6' or i[j+2] == '7' or i[j+2] == '8' or i[j+2] == '9'):
                                s=i[j+2]
                                b.append(s)
                                s=i[j+4]+i[j+5]
                                b.append(s)
                                s=i[j+6]+i[j+7]
                                b.append(s)
                            elif(i[j+2] =='1') and (i[j+3]!='0' or i[j+3]!='1' or i[j+3]!='2'):
                                s=i[j+2]+i[j+3]
                                b.append(s)
                                s=i[j+5]+i[j+6]
                                b.append(s)
                                s=i[j+7]+i[j+8]
                                b.append(s)
                            elif(i[j+2] =='1'):
                                s=i[j+2]
                                b.append(s)
                                s=i[j+4]+i[j+5]
                                b.append(s)
                                s=i[j+6]+i[j+7]
                                b.append(s)
                        c.append(a)
                        c.append(b)
                        if(len(a)>=3 and len(b)>=3):
                            pair.append(c)
                        #print(c)





        for i in pair:
            for j in i:
                if len(j) == 4 and (j[-1]=='5' or j[-1]=='15'):
                    j.pop(-1)
                    #if j[0] == 12 and j[1] == 2:
                    #print("h")
                if len(j) == 4:
                    j.pop(1)

                elif len(j) == 5 :#and j[0] == 12 and j[1] == 2:
                    #print("hie")
                    j.pop(0)
                    j.pop(0)
                elif len(j) == 6 :#and j[0] ==12 and j[1] ==2 and j[2] == 11 and j[3] ==1:
                    #print("h")
                    j.pop(0)
                    j.pop(0)
                    j.pop(1)
            #print(i)



        add=[]
        #print(pair)
        for i in pair:
            time=0
            if not i:
                continue
            else:

                x=list(i);
                hour0=int(x[0][0])
                min0=int(x[0][1])
                hour1=int(x[1][0])
                min1=int(x[1][1])


                if x[0][2] == 'pm' or x[0][2] == 'pM' or x[0][2]=='Pm' or x[0][2]=='PM':
                    if x[1][2] == 'am' or x[1][2] == 'aM' or x[1][2]=='Am' or x[1][2]=='AM':
                        if(hour1!=12):
                            hour1=hour1+12
                        if(hour0==12):
                            hour0=hour0-12
                        if(hour0 < hour1):
                            time=time+(hour1-hour0)*60
                        elif(hour0==hour1):
                            time=0
                        else:
                            time=time+(hour0-hour1)*60


                        if(min1 > min0):
                            time=time+(min1-min0)
                        else:
                            time=time-(min0-min1)




                if x[0][2] == 'am' or x[0][2] == 'aM' or x[0][2]=='Am' or x[0][2]=='AM':
                    if x[1][2] == 'pm' or x[1][2] == 'pM' or x[1][2]=='Pm' or x[1][2]=='PM':
                        if(hour0==12):
                            hour1=hour1-12
                        if(hour1!=12):
                            hour1=hour1+12
                        if(hour0 < hour1):
                            time=time+(hour1-hour0)*60
                        elif(hour0==hour1):
                            time=0
                        else:
                            time=time+(hour0-hour1)*60

                        if(min1 > min0):
                            time=time+(min1-min0)
                        else:
                            time=time-(min0-min1)

                if x[0][2] == 'pm' or x[0][2] == 'pM' or x[0][2]=='Pm' or x[0][2]=='PM':
                    if x[1][2] == 'pm' or x[1][2] == 'pM' or x[1][2]=='Pm' or x[1][2]=='PM':
                        if(hour0==12 and hour1!=12):
                            hour1=hour1+12
                        if(hour0 < hour1):
                            time=time+(hour1-hour0)*60
                        elif(hour0==hour1):
                            time=0
                        else:
                            time=time+(hour0-hour1)*60


                        if(min1 > min0):
                            time=time+(min1-min0)
                        else:
                            time=time-(min0-min1)


                if x[0][2] == 'am' or x[0][2] == 'aM' or x[0][2]=='Am' or x[0][2]=='AM':
                    if x[1][2] == 'am' or x[1][2] == 'aM' or x[1][2]=='Am' or x[1][2]=='AM':

                        if(hour0==12 and hour1!=12):
                            hour1=hour1+12
                        if(hour0 < hour1):
                            time=time+(hour1-hour0)*60

                        elif(hour0==hour1):
                            time=0
                        else:
                            time=time+(hour0-hour1)*60



                        if(min1 > min0):
                            time=time+(min1-min0)
                        else:
                            time=time-(min0-min1)






                add.append(time)
        tt=0

        for i in add:
            tt=tt+i

        h = tt/60 + si
        rh = math.floor(h)
        rt = math.ceil((h-rh)*60)
        d = math.floor(h/24)
        dh=(((tt/60)/24)-d)*24
        dm =   math.ceil((dh-math.floor(dh))*60)
        if(math.floor(dh)==0):
            print("{}hours {}minutes -- {} minutes -- {}days     {}minutes -- {}hours".format(rh,rt,tt,d,dm,round(h,6)))
            output = str(rh)+" hours "+str(rt)+" minutes --"+str(tt)+" minutes -- "+str(d)+" days "+str(dm)+" minutes -- "+str(round(h,6))+" hours"
        else:
            print("{}hours {}minutes -- {} minutes -- {}days {}hours {}minutes -- {}hours".format(rh,rt,tt,d,math.floor(dh),dm,round(h,6)))
            output =  str(rh)+" hours "+str(rt)+" minutes --"+str(tt)+" minutes -- "+str(d)+" days "+str(math.floor(dh))+" hours "+str(dm)+" minutes -- "+str(round(h,6))+" hours"
        return output


if __name__ == "__main__":

    st.title("Time log parser")
    background = "background.jpg"
    background_ext = "jpg"

    st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #FFC0CB;
        color:black;
    }
    div.stButton > button:hover {
        background-color: white;
        color:black;
        border: 2px solid #87ceeb;
        }
    </style>""", unsafe_allow_html=True)

    st.markdown("""
     ### please select a log file
    """, unsafe_allow_html=True)
    
    one = st.button('Carbon log file')
    two = st.button('TimeLogEnergy file')
    three = st.button('TimeLogNitrogen file')
    four = st.button('TimeLogWater file')
    five = st.button('TimeLogWatershed file')
    six = st.button('TimeParser log file')
    seven = st.button('correctcases log file')
    eight = st.button('errorcase log file')

    if one:
        st.write(parser('Carbon.txt'))
    elif two:
        st.write(parser('TimeLogEnergy.txt'))
    elif three:
        st.write(parser('TimeLogNitrogen.txt'))
    elif four:
        st.write(parser('TimeLogWater.txt'))
    elif five:
        st.write(parser('TimeLogWatershed.txt'))
    elif six:
        st.write(parser('TimeParser.txt'))
    elif seven:
        st.write(parser('correctcases.txt'))
    elif eight:
        st.write(parser('errorcase.txt'))  
