import tkinter as tk

class myProgram:
    global container
    global colors
    global i

    def __init__(self, root):
        self.container = root
        self.colors = ["blue", "yellow", "red", "black", "purple", "white"]
        self.i = 0
        self.createView()

    def createView(self):
        self.container.title("JProgram - Events Clicks")
        self.container.geometry("640x480+250+100")
        self.container["bg"] = self.colors[0]

        self.button = tk.Button(self.container, text="Click", background="green", command = self.changeBackground)
        self.button.place(x=100, y=90)

        self.container.mainloop()

    def changeBackground(self):
        if(self.container["bg"] == "white"):
            self.i = -1

        self.i = self.i + 1
        self.container["bg"] = self.colors[self.i]

if __name__ == '__main__':
    window = tk.Tk()
    ap = myProgram(window)