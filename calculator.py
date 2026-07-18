import tkinter as tk

def calculator():
    root = tk.Tk()
    root.title("计算器")
    root.geometry("300x400")
    root.resizable(False, False)

    # 显示屏（可手动输入）
    display = tk.StringVar(value="0")
    entry = tk.Entry(root, textvariable=display, font=("Arial", 24),
                     justify="right", bd=10)
    entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

    def press(ch):
        if ch == "C":
            display.set("")
        elif ch == "=":
            try:
                result = str(eval(display.get()))
                display.set(result)
            except:
                display.set("错误")
        elif ch == "←":
            display.set(display.get()[:-1])
        else:
            # 如果当前是0，替换掉
            if display.get() == "0" and ch not in "+-*/.%":
                display.set(ch)
            else:
                display.set(display.get() + ch)

    # 按钮布局
    buttons = [
        ["C", "←", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "=", "="]
    ]

    for i, row in enumerate(buttons):
        for j, txt in enumerate(row):
            # = 按钮占两列
            if txt == "=" and i == 4:
                btn = tk.Button(root, text=txt, font=("Arial", 18),
                                command=lambda t=txt: press(t))
                btn.grid(row=i+1, column=j, columnspan=2, sticky="nsew")
                break
            else:
                color = "#f0a030" if txt in ["=","+","-","*","/","%"] else \
                        "#ff6b6b" if txt == "C" else "#e0e0e0"
                fg = "white" if txt in ["=","+","-","*","/","%","C"] else "black"
                btn = tk.Button(root, text=txt, font=("Arial", 18),
                                bg=color, fg=fg,
                                command=lambda t=txt: press(t))
                btn.grid(row=i+1, column=j, sticky="nsew")

    # 行列权重，让按钮自动撑满
    for i in range(6):
        root.rowconfigure(i, weight=1)
    for j in range(4):
        root.columnconfigure(j, weight=1)

    root.mainloop()

if __name__ == "__main__":
    calculator()
