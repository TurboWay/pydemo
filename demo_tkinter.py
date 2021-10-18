#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/18 10:59
# @Author : way
# @Site : 
# @Describe: tkinter 制作可视化小工具


import tkinter


class FindLocation(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("小工具")
        self.input = tkinter.Text(self.root, width=50, height=25)
        self.rep_button = tkinter.Button(self.root, command=self.rep, text="替换")
        self.copy_button = tkinter.Button(self.root, command=self.copy, text="复制")
        self.display = tkinter.Text(self.root, width=50, height=25, state='disabled')
        self.input.pack()
        self.display.pack(expand=True, fill="both", side="bottom")
        self.rep_button.pack(expand=True, fill="both", padx=5, pady=10, side="left")
        self.copy_button.pack(expand=True, fill="both", padx=5, pady=10, side="right")
        # self.rep_button.pack()
        # self.copy_button.pack()

    def udf(self, str):
        return str + '没什么好替换的'

    def rep(self):
        input = self.input.get('0.0', 'end')
        output = self.udf(input)
        # 展示
        self.display.config(state='normal')
        self.display.delete('1.0', 'end')
        self.display.insert('end', output)
        self.display.config(state='disabled')

    def copy(self):
        # 复制到剪切板
        output = self.display.get('0.0', 'end')
        self.root.clipboard_clear()
        self.root.clipboard_append(output)


if __name__ == "__main__":
    FL = FindLocation()
    tkinter.mainloop()
