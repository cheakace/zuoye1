import tkinter as tk
import time

def show_love():
    root = tk.Tk()
    root.title("对你的思念")
    root.geometry("600x400")
    
    # 表白文字标签
    love_label = tk.Label(root, text="", font=("微软雅黑", 16), fg="red")
    love_label.pack(expand=True)
    
    # 逐字显示表白内容
    content = "代码只有100多行，对你的思念不止于此"
    for char in content:
        love_label.config(text=love_label["text"] + char)
        root.update()
        time.sleep(0.5)
    
    root.mainloop()

if __name__ == "__main__":
    show_love()