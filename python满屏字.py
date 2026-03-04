import tkinter as tk
import random
import threading
import time
import math

def show_warn_tip(x, y):
    # 创建窗口
    window = tk.Tk()
    
    # 窗口尺寸
    window_width = 190
    window_height = 65
    
    # 设置窗口标题和位置
    window.title('提示')
    window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    
    # 关心生活健康的话语（30条）
    tips = [
        '好好吃饭', '好好休息', '早点休息', '天天开心',
        '记得喝水', '按时吃饭', '别熬夜了', '照顾好自己',
        '注意身体', '记得运动', '放松一下', '保持微笑',
        '劳逸结合', '别太劳累', '记得午休', '多吃水果',
        '出去走走', '呼吸新鲜空气', '保持好心情', '别久坐',
        '记得早餐', '保护眼睛', '注意保暖', '别着凉',
        '保持健康', '平安喜乐', '开心每一天', '一切顺利',
        '万事如意', '心想事成'
    ]
    
    tip = random.choice(tips)
    
    # 更多背景颜色选择
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow',
        'plum', 'coral', 'bisque', 'aquamarine', 'mistyrose', 'honeydew',
        'peachpuff', 'paleturquoise', 'lavenderblush', 'oldlace', 'lemonchiffon',
        'lightcyan', 'lightgray', 'lightpink', 'lightsalmon', 'lightseagreen',
        'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow'
    ]
    bg = random.choice(bg_colors)
    
    # 创建并显示Label
    label = tk.Label(
        window, 
        text=tip, 
        bg=bg, 
        font=('仿宋', 18),
        width=15,
        height=2
    )
    label.pack()
    
    # 立即更新窗口显示
    window.update()
    
    # 窗口置顶
    window.attributes('-topmost', True)
    
    # 3秒自动关闭
    window.after(9000, window.destroy)
    
    window.mainloop()

def generate_heart_positions(window_count):
    """生成爱心形状的坐标位置"""
    positions = []
    
    # 获取屏幕尺寸
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    
    # 爱心参数方程
    # 爱心方程: x = 16sin^3(t), y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)
    
    # 调整爱心大小以适应屏幕
    scale_x = screen_width / 64
    scale_y = screen_height / 44
    center_x = screen_width / 2
    center_y = screen_height / 2
    
    # 生成爱心上的点
    for i in range(window_count):
        t = 2 * math.pi * i / window_count
        # 爱心参数方程
        x = 16 * (math.sin(t) ** 3)
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        
        # 缩放和平移到屏幕中心
        screen_x = center_x + x * scale_x
        screen_y = center_y - y * scale_y  # 注意：屏幕坐标系y轴向下，所以取负
        
        positions.append((screen_x, screen_y))
    
    return positions

if __name__ == "__main__":
    # 窗口数量
    window_count = 100  # 减少数量以便看清爱心形状
    
    # 生成爱心形状的位置
    heart_positions = generate_heart_positions(window_count)
    
    # 按照爱心形状顺序创建窗口
    for i, (x, y) in enumerate(heart_positions):
        t = threading.Thread(target=show_warn_tip, args=(x, y))
        t.daemon = True
        t.start()
        time.sleep(0.05)  # 稍微延长间隔以便看清爱心形成过程
    
    # 保持主程序运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # 按Ctrl+C退出
        pass