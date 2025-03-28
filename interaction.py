import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageFont, ImageDraw
import ctypes  # 用于加载系统字体
from function.process import data_process  # 导入 data_process 函数

# 加载Windows系统自带的高质量字体（示例使用微软雅黑）
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # 启用高DPI支持
    DEFAULT_FONT = ("Microsoft YaHei", 12, "bold")
except:
    DEFAULT_FONT = ("Helvetica", 12, "bold")


class LuxuryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("行稳致远")
        self.root.geometry("1000x600")  # 适中尺寸界面

        # 加载背景图
        self.bg_image = Image.open("background.jpg")  # 替换为你的背景图路径
        self.bg_image = self.bg_image.resize((1000, 600), Image.Resampling.LANCZOS)  # 使用 LANCZOS 替代 ANTIALIAS
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # 创建主画布
        self.canvas = tk.Canvas(root, width=1000, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # 设置背景图（铺满窗口）
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)

        # 绘制艺术标题
        self.draw_title()

        # 主功能按钮框架
        self.button_frame = ttk.Frame(self.canvas, style="Luxury.TFrame")
        self.button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # 自定义样式
        self.style = ttk.Style()
        self.configure_styles()

        # 创建功能按钮
        self.create_buttons()

    def draw_title(self):
        """绘制艺术化标题"""
        # 主标题
        self.canvas.create_text(500, 100,
                                text="行稳致远",
                                font=("Microsoft YaHei", 36, "bold"),
                                fill="#ffffff",  # 白色文字
                                anchor=tk.CENTER)

        # 副标题
        self.canvas.create_text(500, 150,
                                text="基于国产大算力芯片的危险驾驶行为检测系统",
                                font=("Microsoft YaHei", 14),
                                fill="#cccccc",  # 浅灰色文字
                                anchor=tk.CENTER)

        # 装饰性渐变线
        self.canvas.create_line(350, 130, 650, 130,
                                fill="#3498db",
                                width=3,
                                capstyle=tk.ROUND)

    def configure_styles(self):
        """配置高级样式"""
        # 背景样式
        self.style.configure("Luxury.TFrame",
                             background="",
                             borderwidth=0)

        # 现代按钮样式
        self.style.map("Luxury.TButton",
                       foreground=[('active', '#ffffff'), ('!active', '#000000')],
                       background=[('active', '#2980b9'), ('!active', '#3498db')],
                       bordercolor=[('active', '#2980b9')],
                       lightcolor=[('active', '#3498db')],
                       darkcolor=[('active', '#2980b9')])

        self.style.configure("Luxury.TButton",
                             font=DEFAULT_FONT,
                             padding=15,
                             width=15,
                             borderwidth=3,
                             relief="raised",
                             anchor=tk.CENTER)

    def create_buttons(self):
        """创建三大功能按钮"""
        # 图片检测按钮
        self.btn_image = ttk.Button(self.button_frame,
                                    text="📷 图片智能检测",
                                    command=self.open_image,
                                    style="Luxury.TButton")
        self.btn_image.grid(row=0, column=0, padx=20, pady=20, ipadx=10, ipady=10)

        # 视频分析按钮
        self.btn_video = ttk.Button(self.button_frame,
                                    text="🎥 视频行为分析",
                                    command=self.open_video,
                                    style="Luxury.TButton")
        self.btn_video.grid(row=0, column=1, padx=20, pady=20, ipadx=10, ipady=10)

        # 实时监测按钮
        self.btn_realtime = ttk.Button(self.button_frame,
                                       text="🚨 实时安全监测",
                                       command=self.realtime_monitor,
                                       style="Luxury.TButton")
        self.btn_realtime.grid(row=0, column=2, padx=20, pady=20, ipadx=10, ipady=10)

    # 以下是功能实现部分（示例）
    def open_image(self):
        filetypes = [("图像文件", "*.jpg *.jpeg *.png")]
        path = filedialog.askopenfilename(title="选择待检测图片", filetypes=filetypes)
        if path:
            data_process('image', path)
            # messagebox.showinfo("AI分析中", f"正在分析图片:\n{path}")

    def open_video(self):
        filetypes = [("视频文件", "*.mp4 *.avi")]
        path = filedialog.askopenfilename(title="选择待分析视频", filetypes=filetypes)
        if path:
            data_process('video', path)
            # messagebox.showinfo("行为分析", f"正在解析视频:\n{path}")

    def realtime_monitor(self):
        messagebox.showwarning("设备状态", "⛔ 未检测到安全监测设备\n请连接专用硬件后重试")


if __name__ == "__main__":
    root = tk.Tk()
    app = LuxuryApp(root)

    # 添加窗口图标
    try:
        root.iconbitmap("system_icon.ico")  # 准备一个高质量的ICO图标
    except:
        pass

    root.mainloop()



