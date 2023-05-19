import streamlit as st
import requests
from streamlit_lottie import st_lottie
import locale
import pickle
locale.setlocale(locale.LC_ALL, 'en_IN')
model = pickle.load(open('./rf_pickle.pkl','rb'))

def formatINR(number):
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    return "".join([r] + d)


def main():
    Fuel_Type=0
    Seller_Type=0
    Transmission_Type=0
    lcol,rcol = st.columns(2)
    with lcol:
        st.title("Car Bechoo")
        st.markdown("##### Are you planning to sell your car ?\n##### Evaluate the price for free! ")
    with rcol:
        st_lottie(car_logo,height=300)
    Model_Name = st.text_input("Enter the name of the model: ","Wagon R",key='model')
    Year = st.number_input('In which year car was purchased ?',2005, 2020, step=1, key ='year')
    Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 1000.00, 500000.00, step=500.00, key ='driven')
    Fuel_Type_Form = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
    if(Fuel_Type_Form=='Petrol'):
        Fuel_Type=3
    elif(Fuel_Type_Form=='Diesel'):
        Fuel_Type=1
    else:
        Fuel_Type=2
    Seller_Type_Form = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'), key='dealer')
    if(Seller_Type_Form=='Individual'):
        Seller_Type=1
    else:
        Seller_Type=0	
    Transmission_Type_Form = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(Transmission_Type_Form=='Manual'):
        Transmission_Type=1
    else:
        Transmission_Type=0
    Owner = st.number_input("The number of owners the car had previously ?",1,4,step=1, key='owner')
    Mileage = st.number_input("The current mileage of the car(in km/L) ?",8,50,step=5, key='mileage')
    Engine_Capacity = st.number_input("What is the engine capacity(in CC) ?",800,5000,step=100, key='capacity')
    Max_Power = st.number_input("What is the maximum power(in bhp) ?",37,step=10,key='max_power')
    Seats = st.number_input("How many seats ?",2,10,step=1,key='seats')
    if st.button("Estimate Price", key='predict'):
        try:
            Model = model  #get_model()
            user_input = [[1249,Year,Kms_Driven,Transmission_Type,Mileage,Engine_Capacity,Max_Power,Seats]]
            prediction = Model.predict(user_input)
            output = round(prediction[0])
            print(output)
            if output<0:
                st.warning("You will be not able to sell this car !")
            else:
                print(output)
                lcol,rcol = st.columns(2)
                with lcol:
                    st.header("You can sell the car for {} rupees !".format(formatINR(output)))
                with rcol:
                    st_lottie(tick_symbol,height=50,loop=False)
                
        except:
            st.warning("Error Encountered!")
            
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()


if __name__ == "__main__":
    st.set_page_config("Car Bechoo",page_icon='🚗')
    car_logo = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ztrluajh.json")
    tick_symbol =load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_UbUJUM.json")
    main()
