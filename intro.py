import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


def play_gif(root, file_path):
    root.lift()
    root.attributes("-topmost", True)

    img = Image.open(file_path)
    lbl = tk.Label(root)
    lbl.place(x=0, y=0)

    for img_frame in ImageSequence.Iterator(img):
        img_frame = img_frame.resize((1200, 750))
        img_tk = ImageTk.PhotoImage(img_frame)
        lbl.config(image=img_tk)
        lbl.image = img_tk  # keep a reference to the image
        root.update_idletasks()
        root.after(50)  # schedule the next frame after 50ms

    #root.destroy()
    k = 0
    while True:
        if k==1:
            break
        else:
            k=1
            root.destroy()
           

root = tk.Tk()
root.geometry("1200x750")

file_path = r"C:\Users\swift\Desktop\python_prjects\openAi\iron-man.gif"
play_gif(root, file_path)

root.mainloop()
