# Tkinter Library in Python

Tkinter is Python's standard GUI (Graphical User Interface) package. It is one of the easiest ways to develop graphical applications in Python, as it comes pre-installed with Python.

## Getting Started

### Importing Tkinter

```python
import tkinter as tk
```

### Creating a Basic Window

```python
root = tk.Tk()
root.title("Basic Window")
root.geometry("400x300")  # Width x Height
root.mainloop()
```

## Tkinter Widgets

### 1. Labels

Displays text or images in the window.

```python
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
```

### 2. Buttons

Allows user interaction.

```python
def on_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()
```

### 3. Entry

For single-line text input.

```python
entry = tk.Entry(root)
entry.pack()
```

### 4. Text

For multi-line text input.

```python
text = tk.Text(root, height=5, width=30)
text.pack()
```

### 5. Frames

Used to group other widgets.

```python
frame = tk.Frame(root, bg="blue", width=100, height=100)
frame.pack()
```

## Layout Managers

### 1. Pack

Places widgets in a top-down manner.

```python
label.pack(side="top")
```

### 2. Grid

Places widgets in a table-like structure.

```python
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
```

### 3. Place

Places widgets at specific x, y coordinates.

```python
button.place(x=50, y=50)
```

## Event Handling

Bind events to widgets.

```python
def on_keypress(event):
    print(f"Key pressed: {event.char}")

root.bind("<Key>", on_keypress)
```

## Example: Basic Calculator

```python
import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        label_result.config(text=f"Result: {result}")
    except Exception as e:
        label_result.config(text="Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20)
entry.pack()

button = tk.Button(root, text="Calculate", command=calculate)
button.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()
```

## Resources

- [Official Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Tkinter Tutorial](https://realpython.com/python-gui-tkinter/)

## Conclusion

Tkinter is a versatile and easy-to-learn library for creating GUI applications in Python. With its wide range of widgets and layout options, you can create both simple and complex applications effortlessly.
