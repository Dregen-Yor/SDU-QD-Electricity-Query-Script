# -*- coding: utf-8 -*-
import streamlit as st
from QueryScript import query, TIMESTAMPS

st.title("青岛校区宿舍电量查询系统")

st.write("请修改根目录 config.yaml 文件后再运行本程序")

option = st.selectbox("选择宿舍楼", [building for building in TIMESTAMPS])

room_number = st.text_input("输入宿舍号")


if st.button("查询"):
    buildingid = option
    st.write(f"您的宿舍剩余电量为：{query(buildingid, room_number)}")
