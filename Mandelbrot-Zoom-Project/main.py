import MandelbrotMain
import tkinter as tk

root = tk.Tk()
root.title("Mandelbrot Visualizer")
root.geometry("560x350")

def create_clickbutton():
        global size
        size = int(text.get())
        if size > 512:
                errorSize()
        else: 
            MandelbrotMain.make_image((-0.75, 0), 3, size)

def errorSize():
        sizeerror = tk.Label(root, text= "This size is quite large, this could take a while. Do you still want to continue?")
        sizeerror.place(x=44, y = 275)
        sizeerror.configure(background="wheat2")
        confirm = tk.Button(root, text="Yes", command=createImage)
        confirm.place(x=250, y = 300)
        confirm.configure(highlightbackground="wheat2")

def createImage():
       MandelbrotMain.make_image((-0.75, 0), 3, size)
       

text = tk.Entry(root)
text.place(x=180, y=130)

button = tk.Button(root, text="Render", command=create_clickbutton)
button.place(x=240, y=165)

label = tk.Label(root, text="Please give the square pixel size of the image you would like generated")
label.place(x=60, y=100)
#label2 = tk.Label(root, text="(Please do not generate anything above 1024 square pixels)")
#label2.place(x=85, y = 120)

root.configure(bg="wheat2")
label.configure(background="wheat2")
button.configure(background="wheat2")
button.configure(highlightbackground="wheat2")
text.configure(highlightbackground="wheat2")
#label2.configure(background="wheat2") 

root.mainloop()
