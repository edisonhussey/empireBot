# from tkinter import *
import time
import tkinter as tk
import pyautogui
from PIL import Image, ImageStat,ImageGrab
import time
import random
import multiprocessing
import cv2
import pytesseract
import csv
import numpy as np
from pynput.mouse import Controller, Button
import multiprocessing


print(pyautogui.position())
def epoch_to_gmt_hhmmss(epoch_time):
    gmt_time = time.gmtime(epoch_time)
    hhmmss = time.strftime('%H:%M:%S', gmt_time)
    return hhmmss

gamestate='attack'

adCheck=False
shared_var = multiprocessing.Value('i', 0)



def worker(queue):
    local_var = 0
    while True:
        # Check if there is a message in the queue
        if not queue.empty():
            message = queue.get()
            if message == 'one':
                local_var = 1
            elif message == 'zero':
                local_var = 0
            elif message == 'stop':
                break
        print("Local variable:", local_var)
        if local_var==1:
            x=pyautogui.locateOnScreen('x.png',confidence=0.6)
            if x is not None:
                print(x)
                xnew=x[0]/2
                
                ynew=x[1]/2
                pyautogui.click(pyautogui.moveTo(xnew+15,ynew+15))
            else:
                print('none')

        time.sleep(1)
    print('ok')


def check():
    print('check')
    global adCheck
    while True:
        time.sleep(1)
        print(shared_var)
        if shared_var.value==1:
            x=pyautogui.locateOnScreen('x.png',confidence=0.6)
            if x is not None:
                print(x)
                xnew=x[0]/2
                
                ynew=x[1]/2
                pyautogui.click(pyautogui.moveTo(xnew+15,ynew+15))
            else:
                print('none')

        else:
            print('off')


def attackConfirm():
    x=pyautogui.locateOnScreen('confirmAttack.png')
    if x is not None:
        print('Attack')
        return 1
    else:
        print('Error attacking')
        return 0
sqrt3 = np.sqrt(3)
sqrt5 = np.sqrt(5)
mouse = Controller()
def wind_mouse(start_x, start_y, dest_x, dest_y, G_0=9, W_0=7.9, M_0=15, D_0=12, move_mouse=lambda x,y: None):
    '''
    WindMouse algorithm. Calls the move_mouse kwarg with each new step.
    Released under the terms of the GPLv3 license.
    G_0 - magnitude of the gravitational fornce
    W_0 - magnitude of the wind force fluctuations
    M_0 - maximum step size (velocity clip threshold)
    D_0 - distance where wind behavior changes from random to damped
    '''
    current_x,current_y = start_x,start_y
    v_x = v_y = W_x = W_y = 0
    while (dist:=np.hypot(dest_x-start_x,dest_y-start_y)) >= 1:
        W_mag = min(W_0, dist)
        if dist >= D_0:
            W_x = W_x/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
            W_y = W_y/sqrt3 + (2*np.random.random()-1)*W_mag/sqrt5
        else:
            W_x /= sqrt3
            W_y /= sqrt3
            if M_0 < 3:
                M_0 = np.random.random()*3 + 3
            else:
                M_0 /= sqrt5
        v_x += W_x + G_0*(dest_x-start_x)/dist
        v_y += W_y + G_0*(dest_y-start_y)/dist
        v_mag = np.hypot(v_x, v_y)
        if v_mag > M_0:
            v_clip = M_0/2 + np.random.random()*M_0/2
            v_x = (v_x/v_mag) * v_clip
            v_y = (v_y/v_mag) * v_clip
        start_x += v_x
        start_y += v_y
        move_x = int(np.round(start_x))
        move_y = int(np.round(start_y))
        if current_x != move_x or current_y != move_y:
            move_mouse(current_x:=move_x,current_y:=move_y)
    return current_x,current_y
def move_mouse(x, y):
    mouse.position=(x,y)
    time.sleep(0.01)

def newClick(x,y):
    startingPosition=mouse.position
    wind_mouse(startingPosition[0], startingPosition[1], x, y, move_mouse=move_mouse)
    mouse.press(Button.left)
    time.sleep(random.randint(1,100)/1000)
    mouse.release(Button.left)

def newMoveTo(x,y):
    startingPosition=mouse.position
    wind_mouse(startingPosition[0], startingPosition[1], x, y, move_mouse=move_mouse)
    # mouse.press(Button.left)
    time.sleep(random.randint(1,100)/1000)
    # mouse.release(Button.left)

pyautogui.FAILSAFE = False
def move_to_sand():
    global state
    state=0
    pyautogui.click(pyautogui.moveTo(1343,836,1))
    time.sleep(0.7)
    pyautogui.click(pyautogui.moveTo(1362,687,1))  #668  661
    time.sleep(2)

def move_to_fire():
    global state
    state=1
    pyautogui.click(pyautogui.moveTo(1343,836,0.5))
    time.sleep(0.7)
    pyautogui.click(pyautogui.moveTo(1368,664,0.5))    #667 643
    time.sleep(2)
coordinates=[[630,631],[624,630],[626,626],[626,638],[621,640],[624,643],[621,646],[615,646],[616,640],[618,636],[614,635],[621,633],[617,631],[620,628],[622,624],[617,625],[620,620],[615,620],[613,624],[610,628],[608,633],[609,637],[603,632],[602,637],[604,643],[598,642],[594,643],[590,642],[589,646],[585,643],[593,637],[597,638],[596,632],[605,628],[602,625],[606,624],[602,620],[604,615],[611,616],[616,612],[603,611],[599,613],[609,609],[601,607],[604,604],[594,604],[598,603],[590,603],[589,607],[585,604],[582,607],[584,611],[588,612],[581,614],[577,612],[572,616],[565,615],[564,611],[560,613],[570,609],[562,607],[565,604],[569,602],[559,603],[556,610],[555,614],[558,617],[551,617],[547,619],[548,626],[544,624],[542,628],[546,630],[552,631],[557,632],[554,637],[551,642],[546,643],[555,643],[550,646],[559,642],[556,649],[545,650],[549,651],[555,653],[560,652],[558,656],[551,656],[558,661],[563,659],[565,654],[572,655]]

for i in range(len(coordinates)):
    coordinates[i].append(0)


def brightness( im_file ):
    im = Image.open(im_file).convert('L')
    stat = ImageStat.Stat(im)   
    return stat.rms[0]

time.sleep(2)
# print(brightness('finder.png'))
def check_brightness_and_click():
    while True:
        # Capture the screen brightness using ImageGrab 
        im2 = ImageGrab.grab(bbox =(753,304,998,409))
        im2.save('prime.png')
        im2=Image.open('prime.png').convert('L')
        im2.save('prime.png')

        # Check the brightness condition (replace 100 with your desired threshold)
        if brightness('prime.png')==215.55975300065322: 
            # Perform the click action
            time.sleep(0.1)
            pyautogui.click(1035,540)

        time.sleep(0.1)
        im2 = ImageGrab.grab(bbox =(726,293,777,338))
        im2.save('low_prime.png')
        im2=Image.open('low_prime.png').convert('L')
        im2.save('low_prime.png')

        if brightness('low_prime.png')==162.92712593676066:
            time.sleep(0.1)
            pyautogui.click(pyautogui.moveTo(875,327))

        im2 = ImageGrab.grab(bbox =(478,285,533,317))
        im2.save('exclusive.png')
        im2=Image.open('exclusive.png').convert('L')
        im2.save('exclusive.png')
        if brightness('exclusive.png')==193.40427218652644:
            time.sleep(0.1)
            pyautogui.click(999,280)
        
        im3 = ImageGrab.grab(bbox =(631,325,784,363))
        im3.save('renegade.png')
        im3=Image.open('renegade.png').convert('L')
        im3.save('renegade.png')
        if brightness('renegade.png')==187.2406377246902:
            pyautogui.click(pyautogui.moveTo(738,678,0.1))
        if brightness('renegade.png')==199.41365201400612:
            pyautogui.click(712,715)

        im4 = ImageGrab.grab(bbox =(628,231,830,280))
        im4.save('tickets.png')
        im4=Image.open('tickets.png').convert('L')
        im4.save('tickets.png')

        if brightness('tickets.png')==197.74126964074844:
            pyautogui.click(pyautogui.moveTo(1075,249,0.3))
def attack():
    pyautogui.click(pyautogui.moveTo(727,522,1))    
    pyautogui.click(pyautogui.moveTo(712,532,0.2))
    time.sleep(0.3)
    pyautogui.moveRel(90,20,0.5)    
    pyautogui.click()
    time.sleep(0.4)
    pyautogui.click(pyautogui.moveTo(813,629,0.3))
    time.sleep(1)
    pyautogui.click(pyautogui.moveTo(1145,754,0.3))
    pyautogui.click(pyautogui.moveTo(1099,863,0.2))
    pyautogui.click(pyautogui.moveTo(916,453,0.2))
    pyautogui.click(pyautogui.moveTo(848,711,0.2))
    time.sleep(0.2)
def attack_fire_tower(x,y):
    pyautogui.click(pyautogui.moveTo(872,361,0.4)) 
    pyautogui.press('tab')                              
    pyautogui.typewrite(str(x))
    pyautogui.press('tab')          
    pyautogui.typewrite(str(y))
    pyautogui.press('enter')     
    pyautogui.click(872,361)        
    time.sleep(0.2)  #1.5 works  
    pyautogui.click(pyautogui.moveTo(727,522,1.4))
    pyautogui.click(pyautogui.moveTo(810,535,0.5))
    time.sleep(0.5)
    pyautogui.click(pyautogui.moveTo(818,635,0.5)) 
    time.sleep(1.4)

    pyautogui.click(pyautogui.moveTo(1078,719,0.5))
    time.sleep(0.5)
    pyautogui.click(pyautogui.moveTo(1078,631,0.5))
    time.sleep(0.5)
    pyautogui.click(pyautogui.moveTo(1137,757,0.5))
    time.sleep(0.5)

    pyautogui.click(pyautogui.moveTo(1079,724,0.5))
    time.sleep(0.5)
    pyautogui.click(pyautogui.moveTo(1078,657,0.5))
    time.sleep(0.5)
    pyautogui.click(pyautogui.moveTo(1163,864,0.5))
    time.sleep(0.5)
    pyautogui.click(pyautogui.moveTo(538,491,0.5))
    time.sleep(0.5)
    pyautogui.click(pyautogui.moveTo(842,712,0.5))
    time.sleep(0.5)
def attack_tower():
    for i in range(len(coordinates)):
        if coordinates[i][2]<time.time():
            coordinates[i][2]=time.time()+11700
            move_to_fire()
            attack_fire_tower(coordinates[i][0],coordinates[i][1])
            return 0 
def read_numbers_from_image(image_path):
    # Load the image using OpenCV
    print(image_path)
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to extract the text (numbers) from the image
    custom_config = r'--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'
    numbers = pytesseract.image_to_string(gray_image, config=custom_config)
    return numbers
def extract_numbers_from_string(input_string, l):
    return_string = ''
    for i in range(l):
        if input_string[i].isdigit():
            return_string += input_string[i]
    return return_string

def get_time_after():
    image= ImageGrab.grab(bbox=(851,474,924,494))
    image.save('image.png')
    image=Image.open('image.png').convert('L')
    image.save('image.png')
    image_path= '/img.png'
    numbers = read_numbers_from_image(image_path)
    extracted_number = ''.join(filter(str.isdigit, numbers))

    # Validate the extracted number
    if not extracted_number:
        return None

    # Calculate the cooldown time in seconds based on the extracted number
    if len(extracted_number) == 6:
        return (
            3600 * 10 * int(extracted_number[0])
            + 3600 * int(extracted_number[1])
            + 60 * 10 * int(extracted_number[2])
            + 60 * int(extracted_number[3])
            + 10 * int(extracted_number[4])
            + int(extracted_number[5])
        )
    elif len(extracted_number) == 4:
        return (
            60 * 10 * int(extracted_number[0])
            + 60 * int(extracted_number[1])
            + 10 * int(extracted_number[2])
            + int(extracted_number[3])
        )
    else:
        return None

def Is_There():
    im2 = ImageGrab.grab(bbox =(716,495,736,525))
    im2.save('holding.png')
    im2=Image.open('holding.png').convert('L')
    im2.save('holding.png')
    if brightness('holding.png')==102.43875405984463:   
        attack()
        return 1
    if brightness('holding.png')==134.42936187207516:
        attack()
        return 1
    else:
        return 0

def new_attack(x,y,z):
    if z==1:
        pyautogui.click(pyautogui.moveTo(872,361,0.4)) 
        pyautogui.press('tab')                              
        pyautogui.typewrite(str(x))
        pyautogui.press('tab')          
        pyautogui.typewrite(str(y))
        pyautogui.press('enter')     
        pyautogui.click(872,361)        
        time.sleep(0.2)  #1.5 works  
        
        pyautogui.click(pyautogui.moveTo(715,544,0.5))
        pyautogui.click(pyautogui.moveTo(808,536,0.5))
        time.sleep(0.3) 
        pyautogui.click(pyautogui.moveTo(813,629,0.3))  
        time.sleep(1.4)
        pyautogui.click(pyautogui.moveTo(1145,754,0.3))
        pyautogui.click(pyautogui.moveTo(1099,863,0.3))
        pyautogui.click(pyautogui.moveTo(916,453,0.3))
        pyautogui.click(pyautogui.moveTo(848,711,0.3))
        pyautogui.moveTo(1285,780,0.2)
        time.sleep(0.2)
    else:
        newMoveTo(872,361)
        pyautogui.press('tab')                              
        pyautogui.typewrite(str(x))
        pyautogui.press('tab')          
        pyautogui.typewrite(str(y))
        pyautogui.press('enter')     
        # pyautogui.click(872,361)
        newClick(872,361)        
        time.sleep(0.2)  #1.5 works  

        newClick(715+random.randint(-2,2),544+random.randint(-2,2))
        newClick(808+random.randint(-5,5),536+random.randint(-5,5))
        time.sleep(0.3+(random.randint(1,2)/10))
        newClick(813+random.randint(-5,6),629+random.randint(-5,6))
        time.sleep(1.4+(random.randint(1,2)/10))
        newClick(1145+random.randint(-5,6),761+random.randint(-5,6))
        newClick(1136+random.randint(-5,6),867+random.randint(-5,6))
        newClick(902+random.randint(-5,6),477+random.randint(-5,6))
        confirmValue=attackConfirm()
        if confirmValue==1:
            newClick(834+random.randint(-5,6),714+random.randint(-5,6))



def create_numbers_spreadsheet(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write the data rows
        for row in data:
            writer.writerow(row)

def append_titles_to_spreadsheet(file_path, titles):
    # Append the titles to the existing CSV file
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(titles)

class Fortress:

    def __init__(self):
        self.win=tk.Tk()
        self.gameState='attacking'
        # self.win.attributes('-alpha', 0.7)  # Set transparency (optional)
        self.win.attributes('-topmost', True)  # Keep window on top
        self.win.lift()
        self.win.title('win')
        self.win.geometry('400x70+800+10')
        self.time=tk.StringVar()
        self.time.set('N/A')
        self.information=[]
        self.startTime=time.time()
        self.timeUntil=[]

    def attackMode(self):
        self.gameState='attack'
        global gamestate
        gamestate='attack'


    def updateClock(self, newValue):

        self.information.append(newValue)
        self.information=sorted(self.information, key=lambda x:x[2])

        self.timeUntil=self.information[0]

        coordinateX=self.timeUntil[0]
        coordinateY=self.timeUntil[1]

        secondsUntil=self.timeUntil[2]-time.time()
        gmtTime=epoch_to_gmt_hhmmss(self.information[0][2])

        global gamestate
        
        self.time.set(f"Next fortress at x={coordinateX}, y={coordinateY} in {int(secondsUntil)} seconds at {gmtTime}. {len(self.information)} fortresses scanned {gamestate}")
        self.win.update()

    def updateClockDone(self):
        self.information=sorted(self.information, key=lambda x:x[2])
        self.timeUntil=self.information[0]

        coordinateX=self.timeUntil[0]
        coordinateY=self.timeUntil[1]   
        gmtTime=epoch_to_gmt_hhmmss(self.information[0][2])
        secondsUntil=self.timeUntil[2]-time.time()  
        self.time.set(f"Next fortress at x={coordinateX}, y={coordinateY} in {int(secondsUntil)} seconds at {gmtTime}. {len(self.information)} fortresses scanned")
        self.win.update()
        
    def startScan(self):
      
        time.sleep(1)  

        for i in range(22): 
            for j in range(22): 
                pyautogui.press('tab')
                pyautogui.typewrite(str(243+i*39))
                pyautogui.press('tab')
                pyautogui.typewrite(str(243+39*j))
                pyautogui.press('enter')
                newClick(744,560)
                time.sleep(0.3)
                if Is_There()==1:
                    self.updateClock([243+39*i,243+39*j,time.time()+61000,0])

                    
                else:
                    pyautogui.click(pyautogui.moveTo(748,525,0.1))
                    newMoveTo(808,537)
                    time.sleep(0.2) 
                    hold=get_time_after()
                    print(type(hold),hold,self.information)
                    if type(hold) is int:
                        if hold<1200:
                            newClick(744,554)
                            time.sleep(0.1)
                            continue
                    if type(hold) is int:
                        self.updateClock([243+39*i,243+39*j,time.time()+hold,0])
                    newClick(744,544)

                    time.sleep(0.1)

                print(self.information)

        self.attackState()



    def attackState(self):

        queue = multiprocessing.Queue()
        process = multiprocessing.Process(target=worker, args=(queue,))
        process.start()


        queue.put('zero')


        while True:



            for i in range(len(self.information)):
                if time.time()>self.information[i][2]+1:

                    if self.information[i][3]==0:
                        queue.put('zero')
                        new_attack(self.information[i][0],self.information[i][1],0)
                        self.information[i][2]=61200+time.time()
                        queue.put('one')
                    else:
                        move_to_fire()
                        new_attack(self.information[i][0],self.information[i][1],1)
                        self.information[i][2]=61200+time.time()
            time.sleep(1) 

            self.updateClockDone()



    def initialClock(self):
        if self.information==[]:
            return
        else:
            self.information=sorted(self.information, key=lambda x:x[2])
            coordinateX=self.information[0][0]
            coordinateY=self.information[0][1]

            self.time.set(f"Next fortress at x={coordinateX}, y={coordinateY} in {int(self.information[0][2]-time.time())} seconds")

    def run(self):
        self.drawWidgets()
        self.win.mainloop()

    def clock(self):

        print(self.information)

        if self.information==[]:
            self.win.after(1000,self.clock)

        else:
            self.information=sorted(self.information, key=lambda x:x[2])
            coordinateX=self.information[0][0]
            coordinateY=self.information[0][1]

            self.time.set(f"Next fortress at x={coordinateX}, y={coordinateY} in {int(self.information[0][2]-time.time())} seconds")
            self.win.after(1000,self.clock)



    def drawWidgets(self):
        self.label=tk.Label(
            textvariable=self.time
        )
        self.label.grid(row=0, column=0)


        startBot=lambda :self.startScan()
        self.button=tk.Button(
            text='start',
            command=startBot
        )
        self.button.grid(row=0,column=1)


if __name__ == '__main__':

    app=Fortress()  
    app.run()
