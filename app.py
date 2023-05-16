import streamlit as st
import joblib


def main():
   
    st.title("Immobili")

    file = "Nuovomodel.pkl"
    model = joblib.load(file)

    crim= st.number_input('crim',0,10,5)
    indus= st.number_input('indus',0,10,5)
    nox= st.number_input('nox',0,10,5)
    rm= st.number_input('rm',0,10,5)
    age= st.number_input('age',0,10,5)
    dis= st.number_input('dis',0,10,5)
    rad= st.number_input('rad',0,10,5)
    tax= st.number_input('tax',0,10,5)
    ptratio= st.number_input('ptratio',0,10,5)
    b= st.number_input('b',0,10,5)
    Istat= st.number_input('Istat',0,10,5)


    res= model.predict([[crim,indus,nox,rm,age,dis,rad,tax,ptratio,b,Istat]])
    st.write(f"il risultato è {res[0]}")


if __name__ == "__main__":
    main()