import streamlit as st
import pandas as pd
import base64
import time


def main():
    # 파일 업로드
    layout = st.file_uploader('파일 업로드')
    if layout != None:
        df = pd.read_excel(layout)
        print(df)

    # 파일 다운로드
    # 파일열기 -> 읽기 -> b64인코딩 -> 디코딩
    with open('data/새마을금고_layout.xlsx', 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="연습파일.xlsx">파일 다운로드</a>', unsafe_allow_html=True)

    print("=================")

    # 버튼이 click 되면 전체가 다시 도는데 클릭 됐을 때만 True를 뱉는 듯
    # 버튼1
    btn1 = st.button("클릭1")
    print("before1")
    
    if btn1:
        while True:
            print("clicked1")
            time.sleep(1)
    print("after1")

    print("=================")

    # 버튼2
    btn2 = st.button("클릭2")
    print("before2")
    if btn2:
        while True:
            print("clicked2")
            time.sleep(1)
    print("after2")

if __name__ == '__main__':
    main()