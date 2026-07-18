import tkinter as tk

def calculator():
    root = tk.Tk()
    root.title("计算器")
    root.geometry("300x400")
    root.resizable(False, False)
    display = tk.StringVar(value="0")
    entry = tk.Entry(root, textvariable=display, font=("Arial", 24),
                     justify="right", bd=10)
    entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

    def press(ch):
        cur = display.get()
        if ch == "C":
            display.set("0")
        elif ch == "←":
            v = cur[:-1]
            display.set(v if v else "0")
        elif ch == "=":
            try:
                display.set(str(eval(cur)))
            except:
                display.set("错误")
        elif ch in "+-*/.%":
            display.set(cur + ch)
        else:
            display.set(ch if cur == "0" else cur + ch)

    # 键盘绑定
    key_map = {"\r": "=", "\x08": "←", "c": "C"}
    root.bind("<Key>", lambda e: press(key_map.get(e.char, e.char)))
    entry.focus_set()

    rows = [
        ["C", "←", "%", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "="]
    ]
    colors = {"/": "#f0a030", "*": "#f0a030", "-": "#f0a030", "+": "#f0a030",
              "%": "#f0a030", "=": "#f0a030", "C": "#ff6b6b"}

    for i, row in enumerate(rows):
        for j, txt in enumerate(row):
            bg = colors.get(txt, "#e0e0e0")
            fg = "white" if bg != "#e0e0e0" else "black"
            cs = 2 if txt == "=" else 1
            btn = tk.Button(root, text=txt, font=("Arial", 18), bg=bg, fg=fg,
                            command=lambda t=txt: press(t))
            btn.grid(row=i+1, column=j, columnspan=cs, sticky="nsew")
            if cs == 2:
                break

    for i in range(6):
        root.rowconfigure(i, weight=1)
    for j in range(4):
        root.columnconfigure(j, weight=1)
    root.mainloop()

if __name__ == "__main__":
    calculator()