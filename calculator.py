from tkinter import Tk, Entry, Button, StringVar
import math

class ScientificCalculator:
    def __init__(self, master):
        master.title("Scientific Calculator")
        master.geometry("400x600+0+0")
        master.config(bg='pink')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#Ffc0cb', font=('Arial Bold', 24), textvariable=self.equation).place(x=0, y=0)

        #Standard buttons
        buttons = [
           {'text': 'C', 'x': 0, 'y': 60, 'bg': 'red', 'command': self.clear},
            {'text': '(', 'x': 80, 'y': 60}, {'text': ')', 'x': 160, 'y': 60}, {'text': '/', 'x': 240, 'y': 60},
            {'text': '7', 'x': 0, 'y': 120}, {'text': '8', 'x': 80, 'y': 120}, {'text': '9', 'x': 160, 'y': 120}, {'text': '*', 'x': 240, 'y': 120},
            {'text': '4', 'x': 0, 'y': 180}, {'text': '5', 'x': 80, 'y': 180}, {'text': '6', 'x': 160, 'y': 180}, {'text': '-', 'x': 240, 'y': 180},
            {'text': '1', 'x': 0, 'y': 240}, {'text': '2', 'x': 80, 'y': 240}, {'text': '3', 'x': 160, 'y': 240}, {'text': '+', 'x': 240, 'y': 240},
            {'text': '0', 'x': 80, 'y': 300}, {'text': '.', 'x': 160, 'y': 300}, {'text': '=', 'x': 240, 'y': 300, 'bg': 'green', 'command': self.solve}
        ]

        #Scientific buttons
        scientific_buttons = [
            {'text': 'π', 'x': 0, 'y': 360, 'command': lambda: self.show('math.pi')},
            {'text': 'e', 'x': 80, 'y': 360, 'command': lambda: self.show('math.e')},
            {'text': 'sin', 'x': 160, 'y': 360, 'command': lambda: self.show('math.sin(')},
            {'text': 'cos', 'x': 240, 'y': 360, 'command': lambda: self.show('math.cos(')},
            {'text': 'tan', 'x': 0, 'y': 420, 'command': lambda: self.show('math.tan(')},
            {'text': 'log', 'x': 80, 'y': 420, 'command': lambda: self.show('math.log10(')},
            {'text': 'ln', 'x': 160, 'y': 420, 'command': lambda: self.show('math.log(')},
            {'text': '√', 'x': 240, 'y': 420, 'command': lambda: self.show('math.sqrt(')},
            {'text': 'x²', 'x': 0, 'y': 480, 'command': lambda: self.show('**2')},
            {'text': 'xʸ', 'x': 80, 'y': 480, 'command': lambda: self.show('**')},
        ]

        #Create standard buttons
        for btn in buttons + scientific_buttons:
            Button(
             width=10,
             height=2,
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
ScientificCalculator(root)  
root.mainloop()