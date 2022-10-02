# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-10-02 13:13
# @Author : 张杰
# @File :library.py
# @Software: PyCharm

import streamlit as st

def get_library_info():
    st.write("正在爬图书馆信息。。")
    pass


if __name__ == '__main__':
    token = st.text_input("请输入token")
    if token and st.button("点击爬取"):
        get_library_info()
        st.text(token)







