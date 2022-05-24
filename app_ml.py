from tkinter import Y
from unittest import skip
import streamlit as st
import joblib
import numpy as np

import sklearn as sk


def run_ml():
    st.subheader('자동차 구매 가능 금액 예측')

    # pkl 파일 불러오기
    # 예측하기 위해서 필요한 파일들을 불러와야 한다.
    regressor = joblib.load('data/regressor.pkl')
    X_scaler = joblib.load('data/X_scaler.pkl')
    y_scaler = joblib.load('data/y_scaler.pkl')

    # 성별, 나이, 연봉, 카드빚, 자산을 입력받도록 만드세요.

    gender = st.radio('성별 입력',['남','여'])
    if gender == '남':
        gender = 1
    else :
        gender = 0

    age = st.number_input('나이를 입력하세요', 0 , 100)
    salary = st.number_input('연봉을 입력하세요', 0)
    debt = st.number_input('카드빚을 입력하세요', 0)
    worth = st.number_input('자산을 입력하세요', 0)

    if st.button('자동차 구매 금액 예측하기') :

        # 1. 신규고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([gender, age, salary, debt, worth])
        # 2. 머신러닝에 사용하기 위해 피터스케일링을 해야한다.
        # 그 전에, 2차원 데이터로 바꿔주기
        new_data = new_data.reshape(1, 5)
        # 3. 피처 스케일링 해준다.
        new_data = X_scaler.transform(new_data)
        # 4. 인공지능에게 예측해달라 한다.
        y_pred = regressor.predict(new_data)
        # 5. 피처스케일링된 예측값을 되돌린다.
        y_pred = y_scaler.inverse_transform(y_pred)
        # 6. 소수점이 너무 길게 나오므로
        result = round(y_pred[0,0])


        st.write('이 사용자의 자동차 구매 가능 금액은 ' + str(result) + '$ 입니다.')

        ### 버전확인하기 ###
        print(sk.__version__)



if __name__ == '__main__':
    main()
    