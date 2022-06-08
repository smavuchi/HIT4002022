import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
#import selecting
# obtain audio from the microphone
def func():
        r = sr.Recognizer()
        isl_gif=['Accountant', 'alcohol', 'are you okay', 'basketball', 'black history month', 'boxing day', 'bread', 'brother', 'chicken', 'christmas eve', 'cow', 
		'drunk', 'easter day', 'engineer', 'every week', 'excuse me', 'facebook', 'fall in love', 'family', 'football', 'go', 'good afternoon', 'good evening', 
		'good friday', 'good morning', 'good night', 'hello', 'hockey', 'honored', 'how are you doing', 'i do not know', 'i do not understand', 'i enjoy this', 
		'i know', 'i like it', 'i understand', 'i want', 'i will help you', 'i am excited', 'i am fine', 'i am impressed', 'i am shocked', 'i am touched', 'instagram', 
		'is it far', 'it is clear', 'it is very hard', 'last week', 'maybe', 'monkey', 'mosquito', 'movie', 'new year eve', 'next year', 'nothing', 'passover', 
		'pizza', 'please help me', 'please repeat', 'please', 'president', 'shark', 'social media', 'spider', 'spoon', 'stop', 'swimming', 'therapist', 'today', 
		'twitter', 'volleyball', 'what are you doing', 'what happened', 'what is for lunch', 'what is the weather like', 'what time is it', 'what', 'where are you from', 
		'where is the next class', 'aggressive', 'banana', 'best friends', 'boxing', 'competition', 'dance', 'delete', 'fishing', 'funny', 'golf', 'grapes', 'gymnastics', 
		'i am confused', 'i am embarassed', 'i am jealous', 'i am sad', 'love', 'mountain climbing', 'practice', 'rolling on the floor', 'shoes', 'soccer', 'sports', 
		'strawberry', 'watermelon', 'wrestling', 'no']
        
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']
        with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source) 
                i=0
                while True:
                        print('Say something')
                        audio = r.listen(source)

                                                        # recognize speech using Sphinx
                        try:
                                a=r.recognize_google(audio)
                                print("you said " + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='goodbye'):
                                        print("oops!Time To say good bye")
                                        break
                                
                                elif(a.lower() in isl_gif):
                                    
                                    class ImageLabel(tk.Label):
                                            """a label that displays images, and plays them if they are gifs"""
                                            def load(self, im):
                                                if isinstance(im, str):
                                                    im = Image.open(im)
                                                self.loc = 0
                                                self.frames = []

                                                try:
                                                    for i in count(1):
                                                        self.frames.append(ImageTk.PhotoImage(im.copy()))
                                                        im.seek(i)
                                                except EOFError:
                                                    pass

                                                try:
                                                    self.delay = im.info['duration']
                                                except:
                                                    self.delay = 100

                                                if len(self.frames) == 1:
                                                    self.config(image=self.frames[0])
                                                else:
                                                    self.next_frame()

                                            def unload(self):
                                                self.config(image=None)
                                                self.frames = None

                                            def next_frame(self):
                                                if self.frames:
                                                    self.loc += 1
                                                    self.loc %= len(self.frames)
                                                    self.config(image=self.frames[self.loc])
                                                    self.after(self.delay, self.next_frame)

                                    root = tk.Tk()
                                    lbl = ImageLabel(root)
                                    lbl.pack()
                                    lbl.load(r'C:\Users\panashemanyonganise\Desktop\HIT400SLR\isl_gif\{0}.gif'.format(a.lower()))
                                    root.mainloop()
                                else:

                                    for i in range(len(a)):
                                                    #a[i]=a[i].lower()
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'letters/'+a[i]+'.jpg'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(0.8) # pause how many seconds
                                                            #plt.close()
                                                    else:
                                                            continue

                        except:
                               print("Could not listen")
                        plt.close()

#func()
while 1:
  image   = "signlang.png"
  msg="SIGN LANGUAGE RECOGNITION"
  choices = ["Live Voice","All Done!","Recorded Audio","Hand Gesture"]
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
  if reply==choices[2]:
        os.system("selecting.py")
  if reply== choices[3]:
        os.system("Dashboard.py")
