import tkinter as tk
from tkinter import messagebox
import random

# 登录窗口
def login_window():
    root = tk.Tk()
    root.title("贪吃蛇登录")
    root.geometry("300x200")
    root.resizable(False, False)

    tk.Label(root, text="贪吃蛇游戏", font=("Arial", 18, "bold")).pack(pady=10)

    tk.Label(root, text="用户名:").pack()
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="密码:").pack()
    entry_pwd = tk.Entry(root, show="*")
    entry_pwd.pack(pady=5)

    # 登录按钮功能
    def login():
        name = entry_user.get().strip()
        if name == "":
            messagebox.showwarning("提示", "请输入用户名")
            return
        root.destroy()
        start_window(name)  # 登录后打开开始界面

    tk.Button(root, text="登录", width=15, command=login).pack(pady=10)
    root.mainloop()

# 新增：点击开始游戏界面
def start_window(name):
    win = tk.Tk()
    win.title("游戏准备")
    win.geometry("300x180")
    win.resizable(False, False)

    tk.Label(win, text="欢迎玩家：" + name, font=("Arial", 15)).pack(pady=30)
    tk.Label(win, text="使用上下左右方向键控制蛇").pack()

    # 点击按钮进入游戏
    def begin():
        win.destroy()
        snake_game(name)

    tk.Button(win, text="点击开始游戏", command=begin, font=("Arial",12)).pack(pady=20)
    win.mainloop()

# 贪吃蛇主游戏
def snake_game(username):
    width = 400
    height = 400
    size = 20
    root = tk.Tk()
    root.title("贪吃蛇")
    root.resizable(False, False)

    score = 0
    snake = [[5,5]]
    direction = [1,0]
    food = [random.randint(0,19), random.randint(0,19)]
    game_run = True

    # 顶部得分栏
    frame = tk.Frame(root)
    frame.pack()
    tk.Label(frame, text="玩家："+username).pack(side="left", padx=10)
    score_label = tk.Label(frame, text="得分：0")
    score_label.pack(side="right", padx=10)

    canvas = tk.Canvas(root, bg="black", width=width, height=height)
    canvas.pack()

    # 刷新画面
    def draw():
        canvas.delete("all")
        # 画食物
        canvas.create_rectangle(food[0]*size, food[1]*size, food[0]*size+size, food[1]*size+size, fill="red")
        # 画蛇
        for index, pos in enumerate(snake):
            if index == 0:
                canvas.create_rectangle(pos[0]*size, pos[1]*size, pos[0]*size+size, pos[1]*size+size, fill="lime")
            else:
                canvas.create_rectangle(pos[0]*size, pos[1]*size, pos[0]*size+size, pos[1]*size+size, fill="green")

    # 游戏循环
    def game_loop():
        nonlocal score, game_run
        if game_run == False:
            canvas.create_text(200,200,text="游戏结束\n得分："+str(score),fill="white",font=("Arial",20))
            return

        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]

        # 撞墙、撞到自己判断
        if head_x<0 or head_x>=20 or head_y<0 or head_y>=20 or [head_x,head_y] in snake:
            game_run = False
            game_loop()
            return

        snake.insert(0,[head_x,head_y])

        # 吃到食物
        if head_x == food[0] and head_y == food[1]:
            score += 10
            score_label.config(text="得分："+str(score))
            food[0] = random.randint(0,19)
            food[1] = random.randint(0,19)
        else:
            snake.pop()

        draw()
        root.after(200, game_loop)  # 200毫秒走一次，速度偏慢

    # 键盘控制方向
    def key_control(event):
        if event.keysym == "Up" and direction != [0,1]:
            direction = [0,-1]
        if event.keysym == "Down" and direction != [0,-1]:
            direction = [0,1]
        if event.keysym == "Left" and direction != [1,0]:
            direction = [-1,0]
        if event.keysym == "Right" and direction != [-1,0]:
            direction = [1,0]

    root.bind("<Key>", key_control)
    draw()
    game_loop()
    root.mainloop()

# 程序入口
if __name__ == "__main__":
    login_window()
