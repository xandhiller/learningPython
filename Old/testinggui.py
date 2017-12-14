from tkinter import *

def main():
    root = Tk()
    
    root.minsize(width=300, height=100)
    root.title("Hello GUI!")
  

    button = Button(root, text = "Is this thing on?", height = 10, width = 30)
    button.pack()



    root.mainloop()
    # Have to have this mainloop at the bottom in order for everything above it to happen.

if __name__ == "__main__":
    main()
