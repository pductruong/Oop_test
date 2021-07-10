from tkinter import *
import PIL
from PIL import Image, ImageTk

class TextureManager:


    def load_image(file_path,_canvas,_root):
        

        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)
        _canvas.create_image(0, 0, anchor=NW, image=img) 
        root.mainloop()

if __name__=='__main__':
    root = Tk()
    canvas = Canvas(root, width=400,height=800)
    
    canvas.pack()
    TextureManager.load_image('/home/tucuman/FlappyBird-JavaScript/images/new_bg.png',canvas)
    TextureManager.load_image('/home/tucuman/FlappyBird-JavaScript/images/anh/bird.png',canvas)
