import streamlit as st
import joblib

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
    Annual_Salary = st.number_input('연봉을 입력하세요', 0)
    Credit_Card_Debt = st.number_input('카드빚을 입력하세요', 0)
    Net_Worth = st.number_input('자산을 입력하세요', 0)

    new_data = np.array([gender, age, Annual_Salary, Credit_Card_Debt, Net_Worth])
    # new_data = new_data.reshape(1, 5)
    # new_data = X_scaler.transform(new_data)
    # y_pred = regressor.predict(new_data)
    # y_scaler.inverse_transform(y_pred)





if __name__ == '__main__':
    main()
    