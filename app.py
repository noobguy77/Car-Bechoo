import streamlit as st
import pickle
model = pickle.load(open('actual.pkl','rb'))


def main():
    Fuel_Type=0
    Seller_Type=0
    Transmission_Type=0
    st.title("Car Bechoo 🚗")
    st.markdown("##### Are you planning to sell your car !?\n##### Evaluate the price for free! ")
    st.write('')
    st.write('')
    Model_Name = st.text_input("Enter the name of the model: ","Wagon R",key='model')
    Year = st.number_input('In which year car was purchased ?',1990, 2020, step=1, key ='year')
    Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=500.00, key ='driven')
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
    Owner = st.number_input("The number of owners the car had previously ?",0,4,step=1, key='owner')
    Mileage = st.number_input("The current mileage of the car ?",5,50,step=5, key='mileage')
    Engine_Capacity = st.number_input("What is the engine capacity ?",800,5000,step=100, key='capacity')
    Max_Power = st.number_input("What is the maximum power(in bhp) ?",37,step=10,key='max_power')
    Seats = st.number_input("How many seats ?",4,10,step=1,key='seats')


    if st.button("Estimate Price", key='predict'):
        try:
            Model = model  #get_model()
            user_input = [[1249,Year,Kms_Driven,Fuel_Type,Seller_Type,Transmission_Type,Owner,Mileage,Engine_Capacity,Max_Power,Seats]]
            prediction = Model.predict(user_input)
            output = round(prediction[0])
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} rupees ! 🙌".format(output))
        except:
            st.warning("Error Encountered!")
            



if __name__ == "__main__":
    st.set_page_config("Car Bechoo")
    main()