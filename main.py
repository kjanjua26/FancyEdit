from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import os
import cv2
import cv2
import matplotlib.pyplot as plt
import numpy as np
import editor 

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.button = tk.Button(self, text="Load Image", command=self.openImage)
        self.refreshButton = tk.Button(self, text="Refresh", command=self.refreshCanvas)
        self.saveButton = tk.Button(self, text="Save", command=self.saveImage)
        self.recolor = tk.Button(self, text="ReColor Image", command=self.reColorEditImageCaller)
        self.edgeDetect = tk.Button(self, text="Edge Detection", command=self.reColorEditImageCaller)
        self.spatialFiltering = tk.Button(self, text="Spatial Filtering", command=self.reColorEditImageCaller)
        self.title_text = tk.StringVar()
        self.display_text = tk.StringVar()
        self.holder_text = tk.StringVar()
        self.editOptions = tk.Label(self, textvariable=self.display_text)
        self.image_holder_name = tk.Label(self, textvariable=self.holder_text)
        self.title_name = tk.Label(self, textvariable=self.title_text)
        self.title_name.config(font=("Courier", 44))
        self.editOptions.config(font=("Courier", 24))
        self.image_holder_name.config(font=("Courier", 24))
        self.title_text.set("FancyEdit")
        self.display_text.set("Edit Options")
        self.holder_text.set("Image Holder")
        self.frame = tk.Frame(self)
        self.frame.place(x=10, y=120)
        self.recolor.place(x=650, y=120)
        self.edgeDetect.place(x=650, y=170)
        self.spatialFiltering.place(x=650, y=220)
        self.editOptions.place(x=610, y=80)
        self.title_name.place(x=400, y=10)
        self.image_holder_name.place(x=200, y=80)
        self.create_canvas()
        self.button.place(x=200, y=600)
        self.refreshButton.place(x=300, y=600)
        self.saveButton.place(x=400, y=600)
        self.choiceValue = ""

    def reColorEditImageCaller(self):
        self.reColorEditWindow = tk.Toplevel(self)
        self.buttonValue = tk.StringVar(self.reColorEditWindow)
        tk.Label(self.reColorEditWindow, text="""Choose a Recoloring Method: """, justify=tk.LEFT, padx=20).pack()
        tk.Radiobutton(self.reColorEditWindow, text="Grayscale", padx=20, variable=self.buttonValue, value="grayscale", command=self.setValueOfChoice, tristatevalue=0).pack(anchor=tk.W)
        tk.Radiobutton(self.reColorEditWindow, text="Red", padx=20, variable=self.buttonValue, value="redrecolor", command=self.setValueOfChoice,tristatevalue=0).pack(anchor=tk.W)
        tk.Radiobutton(self.reColorEditWindow, text="Blue", padx=20, variable=self.buttonValue, value="bluerecolor", command=self.setValueOfChoice,tristatevalue=0).pack(anchor=tk.W)
        tk.Radiobutton(self.reColorEditWindow, text="Green", padx=20, variable=self.buttonValue, value="greenrecolor", command=self.setValueOfChoice,tristatevalue=0).pack(anchor=tk.W)
        tk.Radiobutton(self.reColorEditWindow, text="Binarize", padx=20, variable=self.buttonValue, value="binarize", command=self.setValueOfChoice,tristatevalue=0).pack(anchor=tk.W)
        tk.Radiobutton(self.reColorEditWindow, text="Invert", padx=20, variable=self.buttonValue, value="invert", command=self.setValueOfChoice,tristatevalue=0).pack(anchor=tk.W)
        
    def setValueOfChoice(self):
        self.choiceValue = self.buttonValue.get()
        self.commonEditor()

    def refreshCanvas(self):
        refreshedImg = self.img
        self.ax1.imshow(refreshedImg, cmap="gray")
        self.canvas.draw()

    def saveImage(self):
        
        cv2.imwrite("C:\\Users\\Syed Waleed Hyder\\Pictures\\edited.png", cv2.cvtColor(self.edited_img.copy(), cv2.COLOR_BGR2RGB))
        tk.messagebox.showinfo("Info","Image saved")
        
    def commonEditor(self):
        self.reColorEditWindow.destroy()
        self.edited_img = editor.recolor(self.choiceValue, self.img.copy())
        self.ax1.imshow(self.edited_img, cmap="gray")
        self.canvas.draw()

    def openImage(self):
        self.filePath = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              filetypes=(("JPEG", ".jpg"), ("PNG", ".png"), ("TIFF", ".tif"),
                                                         ("All Files", "*.*")),
                                              title="Open Image")
        self.img = cv2.imread(self.filePath)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.ax1.imshow(self.img, cmap="gray")
        self.canvas.draw()

    def create_canvas(self):
        ''' Add a canvas to plot images '''
        self.fig1 = Figure(frameon=False, figsize=(6, 4.5))
        self.canvas = FigureCanvasTkAgg(self.fig1, master=self.frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        self.canvas.set_window_title("AutoEdit")
        self.ax1 = self.fig1.add_axes([0, 0, 1, 1])
        self.ax1.axis('off')

# Run program
app = GUI()
app.config()
app.title("FancyEdit")
app.geometry("900x650")
app.mainloop()