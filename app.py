import streamlit as st
import pandas as pd
import re

def main():
    st.title("日語華語句子範例")
    

    # data = get_data()
    # st.text(type(data))
    data = pd.read_csv('df.csv')
    data.set_axis(['日語','華語'],axis='columns',inplace = True)
    # st.dataframe(data)

    texts = st.sidebar.radio("請選擇關鍵詞查詢文字類別", options=['日語','華語'])

    text_box = st.sidebar.text_input('在下方輸入華語或日語，按下ENTER後便會自動更新查詢結果')

    t_filt = data[texts].str.contains(text_box, flags=re.IGNORECASE)
    filt_df = data[(t_filt)]

    st.dataframe(filt_df,800,400)
@st.cache
def get_data():
    pickle = pd.read_pickle('data.pickle')
    df = pd.DataFrame.from_dict(pickle,orient='index')
    # df = df.astype(str, errors='ignore')
    return df

if __name__ == '__main__':
    main() 