
from tkinter import *
from typing import Dict, List
import PIL
from PIL import Image, ImageTk


class TextureManager:

    def __init__(self):
        self.__image_list = dict()

        
    #Thêm ảnh vào Dictionary image_list
    def LoadImage(self, file_path, image_name):
            img = Image.open(file_path)
            img = ImageTk.PhotoImage(img)
            self.__image_list[image_name]=img
        

    #Hiển thị ảnh trong Dictionary image_list
    def Draw(self, image_name, canvas, pos_x, pos_y):
        img = self.__image_list.get(image_name)
        canvas.create_image(pos_x, pos_y, anchor=NW, image=img)
        
        

    
  

