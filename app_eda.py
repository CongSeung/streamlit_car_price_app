import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from validators import card_number


def run_eda():
    st.subheader('데이터 분석')

    car_df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')

    # 라디오 버튼을 이용해서, 데이터프레임과, 통계치를 선택해 보여줄 수 있게 한다.
    
    radio_menu = ['데이터프레임', '통계치']

    selected = st.radio('선택하세요', radio_menu)

    if selected == radio_menu[0]:
        st.dataframe(car_df)
    elif selected == radio_menu[1]:
        st.dataframe(car_df.describe())


    # 컬럼을 보여주고 , 컬럼을 선택하면
    # 해당 컬럼의 최대값 데이터와, 최솟값 데이터를 보여준다.

    car_df_col_list = car_df.columns[4:]

    selected_col = st.selectbox('최소, 최대값을 보고싶은 컬럼을 선택하세요',car_df_col_list)

    df_max = car_df.loc[car_df[selected_col]==car_df[selected_col].max(), ]
    df_min = car_df.loc[car_df[selected_col]==car_df[selected_col].min(), ]

    st.text('{}컬럼의 최댓값에 해당하는 데이터입니다.'.format(selected_col))
    st.dataframe(df_max)
    st.text('{}컬럼의 최솟값에 해당하는 데이터입니다.'.format(selected_col))
    st.dataframe(df_min)

    # 유저가 선택한 컬럼들만, pairplot 그리고 
    # 그 아래, 상관계수를 보여준다.

    car_df_col_list_2 = car_df.columns[4:]
    selected_col_list = st.multiselect('서로 상관관계를 보고 싶은 컬럼들을 선택하세요.',car_df_col_list_2)
    if selected_col_list is not None:
        fig_01 = plt.figure()
        sb.pairplot(data = car_df, vars = selected_col_list )
        st.pyplot(fig_01)

