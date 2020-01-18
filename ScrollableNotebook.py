# -*- coding: utf-8 -*-

# Copyright (c) Muhammet Emin TURGUT 2020
# For license see LICENSE
from tkinter import *
from tkinter import ttk
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
class ScrollableNotebook(ttk.Frame):
    def __init__(self,parent,*args):
        ttk.Frame.__init__(self, parent, *args)
        self.firstAdd=0
        self.xLocation = 0
        self.notebookContent = ttk.Notebook(self)
        self.notebookContent.pack(fill="both", expand=True)

        self.notebookTab = ttk.Notebook(self)
        self.notebookTab.bind("<<NotebookTabChanged>>",self.tabChanger)

        slideFrame = ttk.Frame(self)
        slideFrame.place(relx=1.0, x=0, y=1, anchor=NE)
        leftArrow = ttk.Label(slideFrame, text="\u25c0")
        leftArrow.bind("<1>",self.leftSlide)
        leftArrow.pack(side=LEFT)
        rightArrow = ttk.Label(slideFrame, text=" \u25b6")
        rightArrow.bind("<1>",self.rightSlide)
        rightArrow.pack(side=RIGHT)
        self.notebookContent.bind( "<Configure>", self.resetSlide)

    def tabChanger(self,event):
        self.notebookContent.select(self.notebookTab.index("current"))
        
    def rightSlide(self,event):
        if self.notebookTab.winfo_width()>self.notebookContent.winfo_width()-30:
            if (self.notebookContent.winfo_width()-(self.notebookTab.winfo_width()+self.notebookTab.winfo_x()))<=35:
                self.xLocation-=20
                self.notebookTab.place(x=self.xLocation,y=0)
    def leftSlide(self,event):
        if not self.notebookTab.winfo_x()== 0:
            self.xLocation+=20
            self.notebookTab.place(x=self.xLocation,y=0)

    def resetSlide(self,event):
        self.notebookTab.place(x=0,y=0)
        self.xLocation = 0

    def add(self,frame,state="normal",padding=0, text="",image=False,compound="left",underline=-1):
        if self.firstAdd!=0:
            self.notebookContent.add(frame, text="",state="hidden")
        else:
            self.notebookContent.add(frame, text="")
        self.notebookTab.add(ttk.Frame(self.notebookTab),state=state, padding=padding, text=text, image=image, compound=compound, underline=underline)

