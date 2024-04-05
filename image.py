from PIL import ImageTk, Image
from tkinter import Tk, Label
window = Tk()
image = Image.open("C:\\Users\\URK23AI1112\\Downloads\\im.jpg")

# Create a PhotoImage object
photo = ImageTk.PhotoImage(image)


# Display the image
label = Label(image=photo)
label.pack()

# Start the Tkinter event loop
window.mainloop()

