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

    car_df_col_list          # 위에서 뽑은 숫자들만 있는 컬럼

    selected_list = st.multiselect('서로 상관관계를 보고 싶은 컬럼들을 2개 이상 선택하세요.',car_df_col_list)
    
    if len(selected_list) >= 2 :        # 상관관계는 1개일 땐 의미가 없으므로  >= 2 를 설정
        fig_01 = sb.pairplot(data = car_df[selected_list])
        st.pyplot(fig_01)

        st.text('선택하신 컬럼들의 상관계수입니다.')
        corr_list = car_df[selected_list].corr()
        st.dataframe(corr_list)

        # 히트맵을 웹 대시보드에 만들어보자.
        fig_02 = plt.figure()
        sb.heatmap( data = car_df[selected_list].corr(), annot = True, fmt = '.2f', vmin = -1 , vmax = 1 , cmap = 'coolwarm', linewidths=0.5)
        st.pyplot(fig_02)


    ### 고객 이름 컬럼을 검색할 수 있도록 만듭니다.
    ### he 라고 넣으면, he가 이름에 들어있는 고객들의 데이터를 가져옵니다.
    # 1. 유저한테 검색어를 입력받는다.
    word = st.text_input('이름 검색')

    # 2. 검색어가 고객이름 컬럼에 들어있는 데이터를 가져온다.
    search_name= car_df.loc[car_df['Customer Name'].str.lower().str.contains(word.lower()),]

    # 3. 화면에 보여준다.
    st.dataframe(search_name)

    
 
    
        