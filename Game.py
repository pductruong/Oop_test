
from tkinter import *
from typing import TextIO
import PIL
from PIL import Image, ImageTk
from InputHandle import *
from TextureManager import TextureManager

class Game:

    
    def __init__(self):
        # Khởi tạo của sổ
            #__root phạm vi private; _root phạm vi protect; root phạm vi public 
        self.__root = Tk()
        self.__canvas = Canvas(self.__root, width=500,height=950)
        self.__canvas.pack()
        self.__root.eval('tk::PlaceWindow . center')
        ###################################################
        self.__input_handle = InputHandle()
        # Tải ảnh vào texture
        self.__texture = TextureManager()
        self.__texture.LoadImage("/home/tucuman/FlappyBird-JavaScript/Oop_test/anh/new_bg.png", "background")
        self.__texture.LoadImage("/home/tucuman/FlappyBird-JavaScript/Oop_test/anh/new_fg.png", "footground")
        self.__texture.LoadImage("/home/tucuman/FlappyBird-JavaScript/Oop_test/anh/bird.png", "bird")
        ###################################################
        
    def handle_event(self):
        InputHandle.get_Key()

    def Update(self):

        #Cập nhật trạng thái các đối tượng trong gamme
        print("update")



        ##############################################
    def Draw(self):
        # Hiển thị ảnh lên canvas
        self.__texture.Draw("background", self.__canvas, 0, 0)
        self.__texture.Draw("footground", self.__canvas, 0, 800)
        self.__texture.Draw("bird",self.__canvas, 200, 350)
        print("draw")

    def GetCanvas(self):
        return self.__canvas
        
        

