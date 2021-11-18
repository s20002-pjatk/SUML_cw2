import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

objawy_d = {0:"1",1:"2",2:"3",3:"4",4:"5"}
choroby_d = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5"}
#embarked_d = {0:"Cherbourg", 1:"Queenstown", 2:"Southampton"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy wyzdrowiejesz?")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	st.image("https://www.damian.pl/Data/Thumbs/storage_files/2021/2/3/be40e4e8-79d7-4e30-8a7f-78b025cf8598/koronawirus-376x2511.jpg?preset=1200x900")

	with overview:
		st.title("Czy wyzdrowiejesz?")

	with left:
		objawy_radio = st.radio( "Objawy", list(objawy_d.keys()), format_func=lambda x : objawy_d[x] )
		choroby_radio = st.radio( "Choroby", list(choroby_d.keys()), format_func=lambda x: choroby_d[x])
		#embarked_radio = st.radio( "Port zaokrętowania", list(embarked_d.keys()), index=2, format_func= lambda x: embarked_d[x] )

	with right:
		wiek_slider = st.slider("Wiek", value=50, min_value=1, max_value=100)
		wzrost_slider = st.slider( "Wzrost", min_value=40, max_value=220)
	#	parch_slider = st.slider( "# Liczba rodziców i/lub dzieci", min_value=0, max_value=6)
	#	fare_slider = st.slider( "Cena biletu", min_value=0, max_value=500, step=10)

	data = [[ objawy_radio,wiek_slider,choroby_radio, wzrost_slider ]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dana osoba przeżyje? {0}".format("Tak" if survival[0] == 0 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga
