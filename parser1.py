import os
import sys
from datetime import *
import math
import streamlit as st
from datetime import datetime
import time
import re

def parser(folder):

    infolist=[]
    extra = []
    doc = open(folder,"r")
    formatted = expression(doc)
    number_mins = number_of_mins(formatted)
    output(number_mins)
    
def amorpm(temp):
    log_0_h = int(temp[0][0])
    log_0_m = int(temp[0][1])
    log_1_h = int(temp[1][0])
    log_1_m = int(temp[1][1])
    m=0
    if(log_0_h == 12):
        if(log_1_h != 12):
            log_1_h = log_1_h + 12
    if(log_0_h < log_1_h):
        m = m + (log_1_h - log_0_h)*60
    else:
        if(log_0_h == log_1_h):
            m = 0
        else:
            m = m + (log_0_h - log_1_h)*60
                            
    if(log_1_m > log_0_m):
        m = m + (log_1_m - log_0_m)
    else:
        m = m - (log_0_m - log_1_m)
            
    return m

def ampm(temp):
    log_0_h = int(temp[0][0])
    log_0_m = int(temp[0][1])
    log_1_h = int(temp[1][0])
    log_1_m = int(temp[1][1])
    m=0
    if(log_0_h == 12):
        log_1_h = log_1_h - 12
    if(log_1_h != 12):
        log_1_h = log_1_h + 12
    if(log_0_h < log_1_h):
        m = m + (log_1_h - log_0_h)*60
    else:
        if(log_0_h == log_1_h):
            m = 0
        else:
            m = m + (log_0_h - log_1_h)*60
                            
    if(log_1_m > log_0_m):
        m = m + (log_1_m - log_0_m)
    else:
        m = m - (log_0_m - log_1_m)
            
    return m    
    
    
def pmam(temp):
    log_0_h = int(temp[0][0])
    log_0_m = int(temp[0][1])
    log_1_h = int(temp[1][0])
    log_1_m = int(temp[1][1])
    m=0
    if(log_0_h == 12):
        log_1_h = log_1_h - 12
    if(log_1_h != 12):
            log_1_h = log_1_h + 12
    if(log_0_h < log_1_h):
        m = m + (log_1_h - log_0_h)*60
    else:
        if(log_0_h == log_1_h):
            m = 0
        else:
            m = m + (log_0_h - log_1_h)*60
                            
    if(log_1_m > log_0_m):
        m = m + (log_1_m - log_0_m)
    else:
        m = m - (log_0_m - log_1_m)
            
    return m 

def expression(data):
    log_data = []
    for variable in data:
        log = re.findall(r'([01][0-9]|[0-9]):([0-5][0-9]|[0-9])([apAP][mM])',variable) 
        log_data.append(log)
    return log_data    
    
 
def output(m):
    raw_h = m/60
    floor_h = math.floor(raw_h)
    ceil_m = math.ceil((raw_h - floor_h)*60)
    raw_d = math.floor(raw_h/24)
    hour = math.floor((((m/60)/24)-raw_d)*24)
    mi = math.ceil((((((m/60)/24)-raw_d)*24)-hour)*60)
    if(hour == 0):
        st.write(f"{floor_h}hours {ceil_m}minutes -- {m} minutes -- {raw_d}days     {mi}minutes -- {raw_h}hours")
    else:
        st.write(f"{floor_h}hours {ceil_m}minutes -- {m} minutes -- {raw_d}days {hour}hours {mi}minutes -- {raw_h}hours")


 
def number_of_mins(data):
    tot = []
    for variable in data:
        m = 0
        if len(variable)!= 0:
            temp=list(variable)
            if variable[0][2] == 'am' or variable[0][2] == 'aM' or variable[0][2] == 'Am' or variable[0][2] == 'AM' :
                if variable[1][2] == 'am' or variable[1][2] == 'aM' or variable[1][2] == 'Am' or variable[1][2] == 'AM' :
                    m = amorpm(temp)
                    
            if variable[0][2] == 'pm' or variable[0][2] == 'pM' or variable[0][2] == 'Pm' or variable[0][2] == 'PM' :
                if variable[1][2] == 'pm' or variable[1][2] == 'pM' or variable[1][2] == 'Pm' or variable[1][2] == 'PM' :
                    m = amorpm(temp)            
                
            if variable[0][2] == 'am' or variable[0][2] == 'aM' or variable[0][2] == 'Am' or variable[0][2] == 'AM' :
                if variable[1][2] == 'pm' or variable[1][2] == 'pM' or variable[1][2] == 'Pm' or variable[1][2] == 'PM' :
                    m = ampm(temp)
                    
            if variable[0][2] == 'pm' or variable[0][2] == 'pM' or variable[0][2] == 'Pm' or variable[0][2] == 'PM' :
                if variable[1][2] == 'am' or variable[1][2] == 'aM' or variable[1][2] == 'Am' or variable[1][2] == 'AM' :
                    m = pmam(temp)           
            
            
            tot.append(m)
    tot_min = 0
    for variable in tot:
        tot_min = tot_min + variable
    return tot_min

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
        parser('Carbon.txt')
    elif two:
        parser('TimeLogEnergy.txt')
    elif three:
        parser('TimeLogNitrogen.txt')
    elif four:
        parser('TimeLogWater.txt')
    elif five:
        parser('TimeLogWatershed.txt')
    elif six:
        parser('TimeParser.txt')
    elif seven:
        parser('correctcases.txt')
    elif eight:
        parser('errorcase.txt')  
