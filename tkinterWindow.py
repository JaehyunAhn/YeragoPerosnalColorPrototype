# -*- coding: utf-8 -*-
"""
    Sogang University Datamining Laboratory
    FileName: tkinterWindow, window view
    Author: Sogo
    Start Date: 15/02/08
    Copyright (c) Sogang University Datamining Lab All right Reserved
"""
import tkinter as tk

# Instance and call the run method to run
class MainWindow(tk.Frame):
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=500,
                          height=200)
        # Set the title
        self.master.title('Yerago Personal Color Extraction - Prototype')

        # This allows the size specification to take effect
        self.pack_propagate(0)

        # We will use the flexible pack layout manager
        self.pack()

        # The greeting selector
        # Use a StringVar to access the selector's value
        self.greeting_var = tk.StringVar()
        self.greeting = tk.OptionMenu(self,
                                      self.greeting_var,
                                      'hello',
                                      'goodbye',
                                      'heyo')
        self.greeting_var.set('hello')

        # The recipient text entry control and its String Var
        self.recipient_var = tk.StringVar()
        self.recipient = tk.Entry(self,
                                  textvariable=self.recipient_var)
        self.recipient_var.set('world')

        # The go button
        self.go_button = tk.Button(self,
                                   text='Go',
                                   command=self.print_out)
        # Put the controls on the form
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.greeting.pack(fill=tk.X, side=tk.TOP)
        self.recipient.pack(fill=tk.X, side=tk.TOP)

    def print_out(self):
        '''
        :return Print a greeting constructed from the selections
        made by the user
        '''
        print('%s, %s!' % (self.greeting_var.get().title(),
                            self.recipient_var.get()))
    def run(self):
        '''
        :return: run the app
        '''
        self.mainloop()