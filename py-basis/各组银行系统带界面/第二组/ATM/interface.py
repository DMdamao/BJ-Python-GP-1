#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tkinter
import tkinter.messagebox
from tkinter import ttk
import time
from PIL import Image, ImageTk
"""
界面
类名：View
属性：
行为：管理员界面    管理员登陆   系统功能界面
open_count
check_deposit
withdrawal
deposit
transfer_accounts
change_password
freeze_card
unfreeze_card
card_reissue
account_cancellation
refund_card
"""


class TerminalGui(object):
    pass


class ATMGui(object):
    widget_list = []
    color_name = []
    color_dict = {"浅粉红": "#FFB6C1", "粉红": "#FFC0CB", "猩红": "#DC143C", "淡紫红": "#FFF0F5",
                  "弱紫罗兰红": "#DB7093", "热情的粉红": "#FF69B4", "深粉红": "#FF1493", "中紫罗兰红": "#C71585",
                  "兰花紫": "#DA70D6", "蓟色": "#D8BFD8", "洋李色紫": "#DDA0DD", "紫罗兰": "#EE82EE",
                  "洋红/玫瑰红": "#FF00FF", "灯笼海棠": "#FF00FF", "深洋红": "#8B008B", "紫色": "#800080",
                  "暗紫罗兰": "#9400D3", "暗兰花紫": "#9932CC", "靛青": "#4B0082",
                  "蓝紫罗兰": "#8A2BE2", "中紫色": "#9370DB", "中暗蓝色": "#7B68EE", "石蓝色": "#6A5ACD",
                  "暗板岩蓝": "#483D8B", "熏衣草淡紫": "#E6E6FA", "幽灵白": "#F8F8FF", "纯蓝": "#0000FF",
                  "中蓝色": "#0000CD", "午夜蓝": "#191970", "暗蓝色": "#00008B", "海军蓝": "#000080",
                  "皇家蓝": "#4169E1", "矢车菊蓝": "#6495ED", "亮钢蓝": "#B0C4DE", "亮蓝灰": "#778899",
                  "灰石色": "#708090", "闪兰色": "#1E90FF", "爱丽丝蓝": "#F0F8FF", "钢蓝": "#4682B4", "亮天蓝色": "#87CEFA",
                  "天蓝色": "#87CEEB", "深天蓝": "#00BFFF", "亮蓝": "#ADD8E6", "火药青": "#B0E0E6", "军兰色": "#5F9EA0",
                  "蔚蓝色": "#F0FFFF", "淡青色": "#E0FFFF", "弱绿宝石": "#AFEEEE", "青色": "#00FFFF", "浅绿色": "#00FFFF",
                  "暗绿宝石": "#00CED1", "暗瓦灰色": "#2F4F4F", "暗青色": "#008B8B", "水鸭色": "#008080", "中绿宝石": "#48D1CC",
                  "浅海洋绿": "#20B2AA", "绿宝石": "#40E0D0", "宝石碧绿": "#7FFFD4", "中宝石碧绿": "#66CDAA", "中春绿色": "#00FA9A",
                  "薄荷奶油": "#F5FFFA", "春绿色": "#00FF7F", "中海洋绿": "#3CB371", "海洋绿": "#2E8B57", "蜜色": "#F0FFF0",
                  "淡绿色": "#90EE90", "弱绿色": "#98FB98", "暗海洋绿": "#8FBC8F", "闪光深绿": "#32CD32", "闪光绿": "#00FF00",
                  "森林绿": "#228B22", "纯绿": "#008000", "暗绿色": "#006400", "查特酒绿": "#7FFF00", "草坪绿": "#7CFC00",
                  "绿黄色": "#ADFF2F", "暗橄榄绿": "#556B2F", "黄绿色": "#9ACD32", "橄榄褐色": "#6B8E23", "米色": "#F5F5DC",
                  "亮菊黄": "#FAFAD2", "象牙色": "#FFFFF0", "浅黄色": "#FFFFE0", "纯黄": "#FFFF00", "橄榄": "#808000",
                  "深卡叽布": "#BDB76B", "柠檬绸": "#FFFACD", "苍麒麟色": "#EEE8AA", "卡叽布": "#F0E68C", "金色": "#FFD700",
                  "玉米丝色": "#FFF8DC", "金菊黄": "#DAA520", "暗金菊黄": "#B8860B", "花的白色": "#FFFAF0", "旧蕾丝": "#FDF5E6",
                  "小麦色": "#F5DEB3", "鹿皮色": "#FFE4B5", "橙色": "#FFA500", "番木瓜": "#FFEFD5", "白杏色": "#FFEBCD",
                  "纳瓦白": "#FFDEAD", "古董白": "#FAEBD7", "茶色": "#D2B48C", "硬木色": "#DEB887", "陶坯黄": "#FFE4C4",
                  "深橙色": "#FF8C00", "亚麻布": "#FAF0E6", "秘鲁色": "#CD853F", "桃肉色": "#FFDAB9", "沙棕色": "#F4A460",
                  "巧克力色": "#D2691E", "重褐色": "#8B4513", "海贝壳": "#FFF5EE", "黄土赭色": "#A0522D", "浅鲑鱼肉色": "#FFA07A",
                  "珊瑚": "#FF7F50", "橙红色": "#FF4500", "深鲜肉": "#E9967A", "番茄红": "#FF6347", "浅玫瑰色": "#FFE4E1",
                  "鲑鱼色": "#FA8072", "雪白色": "#FFFAFA", "淡珊瑚色": "#F08080", "玫瑰棕色": "#BC8F8F", "印度红": "#CD5C5C",
                  "纯红": "#FF0000", "棕色": "#A52A2A", "火砖色": "#B22222", "深红色": "#8B0000", "栗色": "#800000", "纯白": "#FFFFFF",
                  "白烟": "#F5F5F5", "淡灰色": "#DCDCDC", "浅灰色": "#D3D3D3", "银灰色": "#C0C0C0", "深灰色": "#A9A9A9",
                  "灰色": "#808080", "暗淡灰": "#696969", "纯黑": "#000000"}
    for name in color_dict.keys():
        color_name.append(name)

    def __init__(self, fnc_open_count,
                 fnc_withdrawal,
                 fnc_deposit,
                 fnc_transfer_accounts,
                 fnc_change_password,
                 fnc_freeze_card,
                 fnc_unfreeze_card,
                 fnc_card_reissue,
                 fnc_account_cancellation,
                 fnc_refund_card,
                 fnc_read_cord,
                 fnc_login):
        self.fnc_open_count = fnc_open_count
        self.fnc_withdrawal = fnc_withdrawal
        self.fnc_deposit = fnc_deposit
        self.fnc_transfer_accounts = fnc_transfer_accounts
        self.fnc_change_password = fnc_change_password
        self.fnc_freeze_card = fnc_freeze_card
        self.fnc_unfreeze_card = fnc_unfreeze_card
        self.fnc_card_reissue = fnc_card_reissue
        self.fnc_account_cancellation = fnc_account_cancellation
        self.fnc_refund_card = fnc_refund_card
        self.fnc_read_cord = fnc_read_cord
        self.fnc_login = fnc_login
        self.font_color = "#DEB887"
        self.background_color = "#696969"
        # self.screen_col = self.background_color

        self.main_window = tkinter.Tk()
        self.main_window.title("ATM终端")
        self.main_window.geometry("940x700+500+200")

        self.screen_t = tkinter.StringVar()
        self.bt_l1_t = tkinter.StringVar()

        self.bt_l2_t = tkinter.StringVar()
        self.bt_l3_t = tkinter.StringVar()
        self.bt_l4_t = tkinter.StringVar()
        self.bt_r1_t = tkinter.StringVar()
        self.bt_r2_t = tkinter.StringVar()
        self.bt_r3_t = tkinter.StringVar()
        self.bt_r4_t = tkinter.StringVar()
        self.bt_b1_t = tkinter.StringVar()

        frm = tkinter.Frame(self.main_window, bg="silver")
        frm.pack()

        self.screen_b = tkinter.Frame(frm, bg="silver", height=100, width=1000)
        self.screen_b.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        frm_l = tkinter.Frame(frm, bg="silver", height=500, width=150)
        frm_l.pack(side=tkinter.LEFT, fill=tkinter.Y)
        frm_r = tkinter.Frame(frm, bg="silver", height=500, width=150)
        frm_r.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        frm_bg = tkinter.Frame(frm, bg="black", height=600, width=700)
        frm_bg.pack(side=tkinter.TOP, pady=10)

        # image = Image.open("screen_m_bg.jpg")
        # im = ImageTk.PhotoImage(image)
        # frm_m = tkinter.Frame(frm_bg, bg="green", height=580, width=680)
        # frm_m.pack(padx=10, pady=10)

        # image = Image.open(r"image\bg1.jpg")  # screen_m_bg.jpg img.gif
        # bg1 = ImageTk.PhotoImage(image)
        # self.screen_m = tkinter.Canvas(frm_m, height=580, width=680, bg='cyan')
        # self.screen_m.create_image((0, 0), image=bg1)  # 1440, 1280  1024, 768
        # self.screen_m.place(x=-2, y=-2)
        self.screen_m = tkinter.Frame(frm_bg, bg=self.background_color, height=580, width=680)  # , image=im
        self.screen_m.pack(padx=10, pady=10)  # self.screen_col

        # image = Image.open(r"image\button1.png")  # screen_m_bg.jpg img.gif
        # button1 = ImageTk.PhotoImage(image)
        # button1 = tkinter.PhotoImage(file=r"image\img.gif")
        self.bt_l1 = tkinter.Button(frm_l, textvariable=self.bt_l1_t, width=10, height=2)  # , image=button1
        self.bt_l1.pack(padx=20, pady=40)
        self.bt_l2 = tkinter.Button(frm_l, textvariable=self.bt_l2_t, width=10, height=2)
        self.bt_l2.pack(padx=20, pady=40)
        self.bt_l3 = tkinter.Button(frm_l, textvariable=self.bt_l3_t, width=10, height=2)
        self.bt_l3.pack(padx=20, pady=40)
        self.bt_l4 = tkinter.Button(frm_l, textvariable=self.bt_l4_t, width=10, height=2)
        self.bt_l4.pack(padx=20, pady=40)

        self.bt_r1 = tkinter.Button(frm_r, textvariable=self.bt_r1_t, width=10, height=2)
        self.bt_r1.pack(padx=20, pady=40)
        self.bt_r2 = tkinter.Button(frm_r, textvariable=self.bt_r2_t, width=10, height=2)
        self.bt_r2.pack(padx=20, pady=40)
        self.bt_r3 = tkinter.Button(frm_r, textvariable=self.bt_r3_t, width=10, height=2)
        self.bt_r3.pack(padx=20, pady=40)
        self.bt_r4 = tkinter.Button(frm_r, textvariable=self.bt_r4_t, width=10, height=2)
        self.bt_r4.pack(padx=20, pady=40)

        self.bt_b1 = tkinter.Button(self.screen_b, textvariable=self.bt_b1_t, width=20, height=2)  #
        self.bt_b1.pack(side=tkinter.RIGHT, padx=20, pady=20)
        self.page_home()

    def set_fnc(self, bt, fnc):
        if bt is "l1":
            self.bt_l1.bind("<Button-1>", fnc)
        elif bt is "l2":
            self.bt_l2.bind("<Button-1>", fnc)
        elif bt is "l3":
            self.bt_l3.bind("<Button-1>", fnc)
        elif bt is "l4":
            self.bt_l4.bind("<Button-1>", fnc)
        elif bt is "r1":
            self.bt_r1.bind("<Button-1>", fnc)
        elif bt is "r2":
            self.bt_r2.bind("<Button-1>", fnc)
        elif bt is "r3":
            self.bt_r3.bind("<Button-1>", fnc)
        elif bt is "r4":
            self.bt_r4.bind("<Button-1>", fnc)
        else:
            self.bt_b1.bind("<Button-1>", fnc)

    @staticmethod
    def message_box(title: str, info: str):
        tkinter.messagebox.showinfo(title, info)

    def clear_page(self):
        for w in self.widget_list:
            w.destroy()
        self.widget_list = []
        self.bt_l1.unbind_all("<Button-1>")
        self.bt_l1_t.set("")
        self.bt_l2.unbind_all("<Button-1>")
        self.bt_l2_t.set("")
        self.bt_l3.unbind_all("<Button-1>")
        self.bt_l3_t.set("")
        self.bt_l4.unbind_all("<Button-1>")
        self.bt_l4_t.set("")
        self.bt_r1.unbind_all("<Button-1>")
        self.bt_r1_t.set("")
        self.bt_r2.unbind_all("<Button-1>")
        self.bt_r2_t.set("")
        self.bt_r3.unbind_all("<Button-1>")
        self.bt_r3_t.set("")
        self.bt_r4.unbind_all("<Button-1>")
        self.bt_r4_t.set("")
        self.bt_b1.unbind_all("<Button-1>")
        self.bt_b1_t.set("")

    def set_color(self, card_number, balance, bg_col_name=None, font_col_name=None):
        if bg_col_name is not None:
            bg_col = self.color_dict[bg_col_name]
            self.background_color = bg_col
            self.screen_m.config(bg=self.background_color)
        else:
            font_col = self.color_dict[font_col_name]
            self.font_color = font_col
        self.page_count(card_number, balance)

    def page_building(self):
        self.clear_page()
        self.bt_r4_t.set("返回")
        self.set_fnc("r4", lambda event: self.page_home())
        lb1 = tkinter.Label(self.screen_m,
                            text="功能即将到来，敬请期待",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb1.place(x=250, y=10)
        self.widget_list.append(lb1)

    def page_home(self):
        self.clear_page()
        self.bt_l1_t.set("开户")
        self.set_fnc("l1", lambda event: self.page_open_count())
        self.bt_l2_t.set("解锁")
        self.set_fnc("l2", lambda event: self.page_unfreeze_card())
        self.bt_l3_t.set("补卡")
        self.set_fnc("l3", lambda event: self.page_building())
        s = """
                *************************************
                *                                   *
                *        欢迎使用神马银行ATM机       *
                *                                   *
                *                                   *
                *************************************
                """
        self.screen_t.set(s)
        lb1 = tkinter.Label(self.screen_m,
                            textvariable=self.screen_t,
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="center")
        lb1.place(y=200)
        self.widget_list.append(lb1)

        e1 = tkinter.Entry(self.screen_b, font=("黑体", 12))
        e1.place(x=550, y=35)
        self.widget_list.append(e1)

        self.bt_b1_t.set("请放入你的银行卡")
        self.set_fnc("b1",
                     lambda event: self.fnc_read_cord(eval(e1.get()) if e1.get().isdigit() else None))

    def page_open_count(self):
        self.clear_page()
        self.bt_r4_t.set("返回")
        self.set_fnc("r4", lambda event: self.page_home())
        lb1 = tkinter.Label(self.screen_m,
                            text="请输入您的个人信息",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb1.place(x=250, y=10)
        self.widget_list.append(lb1)

        lb2 = tkinter.Label(self.screen_m,
                            text="姓名：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb2.place(x=240, y=100)
        self.widget_list.append(lb2)
        e1 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e1.place(x=300, y=105)
        self.widget_list.append(e1)

        lb3 = tkinter.Label(self.screen_m,
                            text="身份证号：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb3.place(x=200, y=130)
        self.widget_list.append(lb3)
        e2 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e2.place(x=300, y=135)
        self.widget_list.append(e2)

        lb4 = tkinter.Label(self.screen_m,
                            text="联系方式：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb4.place(x=200, y=160)
        self.widget_list.append(lb4)
        e3 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e3.place(x=300, y=165)
        self.widget_list.append(e3)

        lb5 = tkinter.Label(self.screen_m,
                            text="住址：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb5.place(x=240, y=190)
        self.widget_list.append(lb5)
        # **************
        e4 = ttk.Combobox(self.screen_m)
        e4["value"] = ("北京", "天津", "河北", "内蒙古",
                       "辽宁", "吉林", "黑龙江", "上海",
                       "江苏", "浙江", "安徽", "福建", "江西",
                       "山东", "河南", "湖北", "湖南", "广东",
                       "广西", "海南", "重庆", "四川", "贵州",
                       "云南", "西藏", "陕西", "甘肃", "青海",
                       "宁夏", "新疆", "香港", "澳门", "台湾",
                       "具体的我就不写了。。。")
        e4.current(0)
        e4.place(x=300, y=195)
        self.widget_list.append(e4)
        # **************
        # e4 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        # e4.place(x=300, y=195)
        # self.widget_list.append(e4)

        lb6 = tkinter.Label(self.screen_m,
                            text="设置密码：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb6.place(x=200, y=220)
        self.widget_list.append(lb6)
        e5 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e5.place(x=300, y=225)
        self.widget_list.append(e5)

        bt1 = tkinter.Button(self.screen_m, text="提交", width=10, height=1, font=("黑体", 15))
        bt1.place(x=290, y=255)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_open_count(e1.get(), e2.get(), e3.get(), e4.get(), eval(e5.get()) if e5.get().isdigit() else None))
        self.widget_list.append(bt1)

        lb7 = tkinter.Label(self.screen_m,
                            text="请及时向前台提交纸质资料！",
                            bg=self.background_color, fg="red",
                            font=("黑体", 15),
                            anchor="n")
        lb7.place(x=220, y=290)
        self.widget_list.append(lb7)

    def page_login(self, card_number: int):
        self.clear_page()
        self.bt_b1_t.set("退卡")
        self.set_fnc("b1", lambda event: self.fnc_refund_card())

        lb1 = tkinter.Label(self.screen_m,
                            text="读取成功",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=20, y=20)
        self.widget_list.append(lb1)

        lb2 = tkinter.Label(self.screen_m,
                            text="请输入密码：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb2.place(x=200, y=260)
        self.widget_list.append(lb2)
        e1 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e1.place(x=330, y=265)
        self.widget_list.append(e1)

        bt1 = tkinter.Button(self.screen_m,
                             text="确认",
                             font=("黑体", 12),
                             width=10, height=2)
        bt1.place(x=320, y=330)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_login(card_number, e1.get()))
        self.widget_list.append(bt1)

    def page_count(self, card_number: int, balance: float):
        self.clear_page()
        self.bt_b1_t.set("退卡")
        self.set_fnc("b1", lambda event: self.fnc_refund_card())

        self.bt_l1_t.set("取款")
        self.bt_l1.bind("<Button-1>",
                        lambda event: self.page_withdrawal(card_number, balance))
        self.bt_l2_t.set("存款")
        self.bt_l2.bind("<Button-1>",
                        lambda event: self.page_deposit(card_number, balance))
        self.bt_l3_t.set("转账")
        self.bt_l3.bind("<Button-1>",
                        lambda event: self.page_transfer_accounts(card_number, balance))
        self.bt_l4_t.set("改密")
        self.bt_l4.bind("<Button-1>",
                        lambda event: self.page_change_password(card_number, balance))
        self.bt_r1_t.set("锁定")
        self.bt_r1.bind("<Button-1>",
                        lambda event: self.page_freeze_card(card_number, balance))
        self.bt_r2_t.set("销户")
        self.bt_r2.bind("<Button-1>",
                        lambda event: self.page_account_cancellation(card_number, balance))

        lb1 = tkinter.Label(self.screen_m,
                            text="卡号：%d  账户余额：%.2f" % (card_number, balance),
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=20, y=20)
        self.widget_list.append(lb1)

        lb2 = tkinter.Label(self.screen_m,
                            text="请选择功能",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="center")
        lb2.place(x=290, y=270)
        self.widget_list.append(lb2)

        lb2 = tkinter.Label(self.screen_m,
                            text="设置背景颜色：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb2.place(x=200, y=350)
        self.widget_list.append(lb2)
        e2 = ttk.Combobox(self.screen_m)
        e2["value"] = self.color_name
        for index, s in enumerate(self.color_name):
            if self.color_dict[s] == self.background_color:
                e2.current(index)
        e2.place(x=340, y=350)
        e2.bind("<<ComboboxSelected>>", lambda event: self.set_color(card_number, balance, bg_col_name=e2.get()))
        self.widget_list.append(e2)

        lb3 = tkinter.Label(self.screen_m,
                            text="设置字体颜色：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="n")
        lb3.place(x=200, y=380)
        self.widget_list.append(lb3)
        e3 = ttk.Combobox(self.screen_m)
        e3["value"] = self.color_name
        for index, s in enumerate(self.color_name):
            if self.color_dict[s] == self.font_color:
                e3.current(index)
        e3.place(x=340, y=380)
        e3.bind("<<ComboboxSelected>>", lambda event: self.set_color(card_number, balance, font_col_name=e3.get()))
        self.widget_list.append(e3)

    def page_withdrawal(self, card_number, balance):
        self.clear_page()
        self.bt_b1_t.set("退卡")
        self.set_fnc("b1", lambda event: self.fnc_refund_card())
        self.bt_r4_t.set("返回")
        self.set_fnc("r4", lambda event: self.page_count(card_number, balance))

        lb1 = tkinter.Label(self.screen_m,
                            text="卡号：%d  账户余额：%.2f" % (card_number, balance),
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=20, y=20)
        self.widget_list.append(lb1)

        lb2 = tkinter.Label(self.screen_m,
                            text="请输入取款金额：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb2.place(x=180, y=260)
        self.widget_list.append(lb2)
        e1 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e1.place(x=350, y=263)
        self.widget_list.append(e1)
        bt1 = tkinter.Button(self.screen_m,
                             text="确认",
                             font=("黑体", 12),
                             width=10, height=2)
        bt1.place(x=320, y=330)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_withdrawal(event, eval(e1.get())))
        self.widget_list.append(bt1)

    def page_deposit(self, card_number, balance):
        self.clear_page()
        self.bt_b1_t.set("退卡")
        self.set_fnc("b1", lambda event: self.fnc_refund_card())
        self.bt_r4_t.set("返回")
        self.bt_r4.bind("<Button-1>",
                        lambda event: self.page_count(card_number, balance))

        lb1 = tkinter.Label(self.screen_m,
                            text="卡号：%d  账户余额：%.2f" % (card_number, balance),
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=20, y=20)
        self.widget_list.append(lb1)

        lb2 = tkinter.Label(self.screen_m,
                            text="请将现金放入下边现金槽中。",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="center")
        lb2.place(x=210, y=260)
        self.widget_list.append(lb2)
        e1 = tkinter.Entry(self.screen_b, font=("黑体", 12))
        e1.place(x=250, y=35)
        self.widget_list.append(e1)
        bt1 = tkinter.Button(self.screen_b,
                             text="确认",
                             font=("黑体", 12),
                             width=10, height=2)
        bt1.place(x=450, y=25)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_deposit(eval(e1.get())))
        self.widget_list.append(bt1)

    def page_transfer_accounts(self, card_number: int, balance: float):
        self.clear_page()
        self.bt_b1_t.set("退卡")
        self.set_fnc("b1", lambda event: self.fnc_refund_card())
        self.bt_r4_t.set("返回")
        self.bt_r4.bind("<Button-1>",
                        lambda event: self.page_count(card_number, balance))

        lb1 = tkinter.Label(self.screen_m,
                            text="卡号：%d  账户余额：%.2f" % (card_number, balance),
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=20, y=20)
        self.widget_list.append(lb1)

        lb2 = tkinter.Label(self.screen_m,
                            text="请输入对方卡号：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb2.place(x=180, y=240)
        self.widget_list.append(lb2)
        e1 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e1.place(x=350, y=243)
        self.widget_list.append(e1)

        lb3 = tkinter.Label(self.screen_m,
                            text="请输入转账金额：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb3.place(x=180, y=270)
        self.widget_list.append(lb3)
        e2 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e2.place(x=350, y=273)
        self.widget_list.append(e2)

        bt1 = tkinter.Button(self.screen_m,
                             text="确认",
                             font=("黑体", 12),
                             width=10, height=2)
        bt1.place(x=300, y=310)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_transfer_accounts(eval(e1.get()), eval(e2.get())))
        self.widget_list.append(bt1)

    def page_change_password(self, card_number, balance):
        self.clear_page()
        self.bt_b1_t.set("退卡")
        self.set_fnc("b1", lambda event: self.fnc_refund_card())
        self.bt_r4_t.set("返回")
        self.set_fnc("r4", lambda event: self.page_count(card_number, balance))

        lb1 = tkinter.Label(self.screen_m,
                            text="卡号：%d  账户余额：%.2f" % (card_number, balance),
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=20, y=20)
        self.widget_list.append(lb1)

        lb2 = tkinter.Label(self.screen_m,
                            text=" 请输入旧密码：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb2.place(x=180, y=240)
        self.widget_list.append(lb2)
        e1 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e1.place(x=350, y=243)
        self.widget_list.append(e1)

        lb3 = tkinter.Label(self.screen_m,
                            text=" 请输入新密码：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb3.place(x=180, y=270)
        self.widget_list.append(lb3)
        e2 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e2.place(x=350, y=273)
        self.widget_list.append(e2)

        bt1 = tkinter.Button(self.screen_m,
                             text="确认",
                             font=("黑体", 12),
                             width=10, height=2)
        bt1.place(x=300, y=310)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_change_password( eval(e1.get()), eval(e2.get()) ))
        self.widget_list.append(bt1)

    def page_freeze_card(self, card_number, balance):
        self.clear_page()
        self.bt_b1_t.set("退卡")
        self.set_fnc("b1", lambda event: self.fnc_refund_card())
        self.bt_r4_t.set("返回")
        self.set_fnc("r4", lambda event: self.page_count(card_number, balance))

        lb1 = tkinter.Label(self.screen_m,
                            text="卡号：%d  账户余额：%.2f" % (card_number, balance),
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=20, y=20)
        self.widget_list.append(lb1)
        lb2 = tkinter.Label(self.screen_m,
                            text="点击“确定”冻结银行卡",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="center")
        lb2.place(x=230, y=270)
        self.widget_list.append(lb2)

        bt1 = tkinter.Button(self.screen_m,
                             text="确认",
                             font=("黑体", 12),
                             width=10, height=2)
        bt1.place(x=300, y=310)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_freeze_card())
        self.widget_list.append(bt1)

    def page_account_cancellation(self, card_number, balance):
        self.clear_page()
        self.bt_b1_t.set("退卡")
        self.set_fnc("b1", lambda event: self.fnc_refund_card())
        self.bt_r4_t.set("返回")
        self.set_fnc("r4", lambda event: self.page_count(card_number, balance))

        lb1 = tkinter.Label(self.screen_m,
                            text="卡号：%d  账户余额：%.2f" % (card_number, balance),
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=20, y=20)
        self.widget_list.append(lb1)

        lb2 = tkinter.Label(self.screen_m,
                            text="点击“确定”进行销户",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="center")
        lb2.place(x=230, y=270)
        self.widget_list.append(lb2)
        bt1 = tkinter.Button(self.screen_m,
                             text="确认",
                             font=("黑体", 12),
                             width=10, height=2)
        bt1.place(x=300, y=310)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_account_cancellation())
        self.widget_list.append(bt1)

    def page_unfreeze_card(self):
        self.clear_page()
        self.bt_r4_t.set("返回")
        self.set_fnc("r4", lambda event: self.page_home())

        lb1 = tkinter.Label(self.screen_m,
                            text="请输入解冻卡号：",
                            bg=self.background_color, fg=self.font_color,
                            font=("黑体", 15),
                            anchor="ne")
        lb1.place(x=180, y=260)
        self.widget_list.append(lb1)
        e1 = tkinter.Entry(self.screen_m, font=("黑体", 12))
        e1.place(x=350, y=263)
        self.widget_list.append(e1)
        bt1 = tkinter.Button(self.screen_m,
                             text="确认",
                             font=("黑体", 12),
                             width=10, height=2)
        bt1.place(x=320, y=330)
        bt1.bind("<Button-1>",
                 lambda event: self.fnc_unfreeze_card(eval(e1.get())))
        self.widget_list.append(bt1)

    def page_card_reissue(self):
        self.clear_page()
        pass

    def loop(self):
        self.main_window.mainloop()
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(ATMGui, cls).__new__(cls)
        return cls.instance


class OPGui(object):
    pass


# 测试用
def dfnc():
    pass


if __name__ == '__main__':
    gui = ATMGui(dfnc, dfnc, dfnc, dfnc, dfnc, dfnc, dfnc, dfnc, dfnc, dfnc, dfnc, dfnc)
    # gui.page_home()
    # gui.page_open_count()
    gui.page_count(10000000, 15)
    # gui.page_withdrawal(10000000, 15)
    # gui.page_deposit(10000000, 15)
    # gui.page_change_password(10000000, 15)
    # gui.page_transfer_accounts(10000000, 15)
    # gui.page_freeze_card(10000000, 15)
    gui.loop()
    pass
