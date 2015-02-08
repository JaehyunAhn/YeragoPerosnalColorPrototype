# -*- coding: utf-8 -*-
"""
    Sogang University Datamining Laboratory
    FileName: tkinterWindow, window view
    Author: Sogo
    Start Date: 15/02/08
    Copyright (c) Sogang University Datamining Lab All right Reserved
"""
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from faceDetection import *

# Instance and call the run method to run
class MainWindow(tk.Frame):
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=400,
                          height=100)
        # Set the title
        self.master.title('예라고 퍼스널 컬러 추출 - Prototype')
        # This allows the size specification to take effect
        self.pack_propagate(0)
        # We will use the flexible pack layout manager
        self.pack()
        # Filedialog
        self.open_button = tk.Button(self,
                                     text='이미지 파일 열기 (jpg, jpeg, png 형식만 가능)',
                                     command=self.open_file)
        # The go button
        self.analyze_button = tk.Button(self,
                                        text='분석하기',
                                        command=self.analyze)
        # Put the controls on the form
        self.open_button.pack(fill=tk.X, side=tk.TOP)
        self.analyze_button.pack(fill=tk.X, side=tk.TOP)
        # Open Image's filename
        self.file_name = None
        self.loaded_image = None

    def open_file(self):
        '''
        :return: Get an absolute image file string from FileOpen Dialog
        '''
        self.file_name = filedialog.askopenfilename(filetypes=(("Jpg images", "*.jpg"),
                                                              ("PNG files", "*.png"),
                                                                ("Jpeg images", "*.jpeg")))
        print(self.file_name, 'is loaded.')
        # load image and resize (PIL side), output: (resize)image
        image = Image.open(self.file_name)
        basewidth = 380
        wpercent = (basewidth/float(image.size[0]))
        hsize = int((float(image.size[1])*float(wpercent)))
        image = image.resize((basewidth, hsize), Image.ANTIALIAS)

        # load image for Tkinter
        photo = ImageTk.PhotoImage(image)
        if self.loaded_image:
            # 한 번에 하나씩만 이미지가 올라오도록 (Garbage Collection)
            self.loaded_image.destroy()
        self.loaded_image = Label(image=photo)
        self.loaded_image.image = photo
        self.loaded_image.pack()

    def analyze(self):
        '''
        :return Print a greeting constructed from the selections
        made by the user
        '''
        try:
            self.file_name
        except:
            print("Exception Error Occurred! Please contact Manager (jaehyunahn@sogang.ac.kr).")
        else:
            if self.file_name is not None:
                # Do analyze!
                print('%s will be analyzed.' % self.file_name)
                (weather, personal_color_array) = face_detect(self.file_name)
                print('weather is %s' % weather)
                print('weather matrix ', personal_color_array)
            else:
                print("There's no exception occurred.")
    def run(self):
        '''
        :return: run the app
        '''
        self.mainloop()