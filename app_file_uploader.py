"""
基于streamlit完成web网页上传服务
Develop a web-based file upload service using Streamlit.
"""
import streamlit as st

#网页标题，Webpage Title
st.title("请Tom老师审批")

#file_uploader
uploader_file = st.file_uploader(
    "请上传txt文件",
    type=["txt"],
    accept_multiple_files=False,  #False表示只接收一个文件上传
)

if uploader_file is not None:
    #提取信息
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024  #kb

    #页面显示文件内容
    st.subheader(f"文件名{file_name}")
    st.write(f"格式：{file_type} |大小：{file_size:.2f} KB")

    #获取内容是bytes转变成中文
    text = uploader_file.getvalue().decode("utf-8")
    st.write(text)


