import tkinter as tk

result = ""

#Input String
def calculation(symbol):
    global result
    result += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, result)

#Evalution of String
def evaluate():
    global result
    try:
        result = str(eval(result))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear()
        text_result.insert(1.0, "Math Error")

#Clear-AC
def clear():
    global result
    result = ""
    text_result.delete(1.0, "end")


#Clear one string from back-C
def xclear():
    global result
    result = result[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, result)

#Alternative sign
def negative():
    global result
    if result and result[-1].isdigit():
        result = "-" + result
    text_result.delete(1.0, "end")
    text_result.insert(1.0, result)

window = tk.Tk()
window.geometry("358x330")

text_result = tk.Text(window, width=20, height=2, font=("Arial", 24), fg="#000", bg="#fff", padx=10, pady=5)
text_result.grid(columnspan=30)



calculator_data = [
    "AC", "C", "+/-", "/",
    "7", "8", "9", "x",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "%", "0", ".", "="
]

row_num = 3
col_num = 1



#Looping Buttons from list and config button with color and method

for item in calculator_data:
    btn = tk.Button(window, text=item, width=5, font=("Arial", 14, "bold"), padx=10, pady=5)
    if item in ("AC", "C", "=", "/", "-", "+","+/-","x"):
        btn.config(bg="#FE9100", fg="#fff")
    if item in ("AC", "X", "="):
        btn.config(command=clear if item == "AC" else (xclear if item == "X" else evaluate))
    elif item == "+/-":
        btn.config(command=negative)
    else:
        btn.config(command=lambda s=item: calculation(s))
    btn.grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 4:
        col_num = 1
        row_num += 1


window.mainloop()
