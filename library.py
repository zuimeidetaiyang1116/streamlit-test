# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-10-02 13:13
# @File :library.py
# @Software: PyCharm

import library_info
import streamlit as st

def get_library_info(token):
    st.write("正在爬图书馆信息。。")
    library_info.token = token
    for date in date_list:
        msg += library_info.find_date_seats(date, '')
        res += library_info.taskdate(date,res)
    send_msg("图书馆有效座位号> 459", msg, "txt")
    send_msg("预约座位", res, "txt")
    


if __name__ == '__main__':
    token = st.text_input("请输入token")
    if token and st.button("点击爬取"):
        get_library_info(token)
        st.text(token)







