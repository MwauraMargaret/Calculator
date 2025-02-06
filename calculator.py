from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("357x420+0+0")  
        master.config(bg='pink')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#Ffc0cb', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        buttons = [
            {'text': '(', 'x': 0, 'y': 50}, {'text': ')', 'x': 90, 'y': 50}, {'text': '%', 'x': 180, 'y': 50}, {'text': '/', 'x': 270, 'y': 50},
            {'text': '1', 'x': 0, 'y': 125}, {'text': '2', 'x': 90, 'y': 125}, {'text': '3', 'x': 180, 'y': 125}, {'text': '*', 'x': 270, 'y': 125},
            {'text': '4', 'x': 0, 'y': 200}, {'text': '5', 'x': 90, 'y': 200}, {'text': '6', 'x': 180, 'y': 200}, {'text': '-', 'x': 270, 'y': 200},
            {'text': '7', 'x': 0, 'y': 275}, {'text': '8', 'x': 90, 'y': 275}, {'text': '9', 'x': 180, 'y': 275}, {'text': '+', 'x': 270, 'y': 275},
            {'text': 'C', 'x': 0, 'y': 350, 'bg': 'white', 'command': self.clear}, 
            {'text': '0', 'x': 90, 'y': 350}, {'text': '.', 'x': 180, 'y': 350}, {'text': '=', 'x': 270, 'y': 350, 'bg': 'pink', 'command': self.solve}
        ]

        for btn in buttons:
            Button(
             width=11,
             height=4,
             text=btn['text'],
             relief="flat",
             bg=btn.get('bg', 'white'),  # Default to white if bg not specified
             command=btn.get('command', lambda t=btn['text']: self.show(t))   
            ).place(x=btn['x'], y=btn['y'])

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
    
    def clear(self):
        self.entry_value =''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except:
            self.equation.set("Error")

root = Tk()
Calculator(root)  
root.mainloop()
