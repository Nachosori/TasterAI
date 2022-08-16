import streamlit as st
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
from get_data.get_data import *
from keras.models import load_model

# Funcion para realizar las columnas

def columns(*data):
    lista = ["Grease", "Saturat.", "Carbohy.", "Sugar", "Fiber", "Protein", "Sal" ]
    colours = ["color: #A93226", "color: grey"]
    for i, col in enumerate(st.columns(7)):
        with col:
            st.markdown(f"<h5 style='text-align: center; {colours[0]};'><b>{lista[i]}</b></h5>", unsafe_allow_html=True)
            st.markdown(f"<P style='text-align: center; {colours[1]};'>{data[i][0]} gr.</P>", unsafe_allow_html=True)

    st.markdown(f"<p style='text-align: center;color: grey ;'></p", unsafe_allow_html=True)       
    st.markdown(f"<p style='text-align: center;color: grey ;'>The detailed information is approximate and corresponds to 100 gr. of food.</p", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;color: grey ;'></p", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;color: grey ;'></p", unsafe_allow_html=True)

# Se recibe la imagen y el modelo, devuelve la predicción

def model_prediction(img, model):
    X = []
    size = (160,160)
    img = Image.fromarray(img).resize(size).convert("RGB")
    img = np.array(img)
    img = img/255
    X.append(img)
    X = np.array(X)
    pred = model.predict(X)
    return pred

# Funcion para realizar una grafica pie

def covid_pie_graf(courses,values):
    sns.set_style("whitegrid")
    labels = courses
    sizes = values
    explode = (0, 0, 0.1,0,0,0,0)  
    fig1, ax1 = plt.subplots(figsize=(9, 5))
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, pctdistance=0.7)
    ax1.axis('equal')
    ax1.legend()
    plt.show()
    return plt


@st.cache
def calls_nutritional(food):
    kilocalories = get_kilocalories(food)
    grease = get_grease(food)
    saturated = get_saturated(food)
    carbohy = get_carbohydrates(food)
    sugar = get_sugar(food) 
    fiber = get_fiber(food)
    protein = get_protein(food)
    sal = get_sal(food)
    return kilocalories, grease,saturated,carbohy,sugar,fiber,protein,sal

@st.cache
def calls_recipes(food):
    name_recipes = get_name_recipes(food)
    return name_recipes

@st.cache   
def call_recipes_name(name):
    time_preparation = get_preparation_recipes(name)
    time_cooking = get_cooking_recipes(name)
    ingredients = get_ingredients_recipes(name)
    elaboration = get_elaboration_recipes(name)
    return time_preparation,time_cooking,ingredients,elaboration


def transform_letters(food):
    if "_" in food:
        food = food.replace("_", " ").capitalize()
    else:
        food = food.capitalize()
    return food



def photo():
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        image = np.array(Image.open(img_file_buffer))  
        p = st.image(image, caption="Imagen", use_column_width=False, width=700)
        return image

def preparing_bar(lista,grease,saturated,carbohy,sugar,fiber,protein,sal):

    dict_nutritional = {lista[0]: grease[0],
    lista[1]: saturated[0],
    lista[2]: carbohy[0],
    lista[3]: sugar[0],
    lista[4]: fiber[0],
    lista[5]: protein[0],
    lista[6]: sal[0]
    }

    courses_nutriti = list(dict_nutritional.keys())
    values_nutriti = list(dict_nutritional.values())


    return st.pyplot(covid_pie_graf(courses_nutriti,values_nutriti))


def aux(food):

    lista = ["Grease", "Saturat.", "Carbohy.", "Sugar", "Fiber", "Protein", "Sal" ]

    kilocalories,grease,saturated,carbohy,sugar,fiber,protein,sal = calls_nutritional(food)
    
    food_transform = transform_letters(food)

    st.markdown(f"<h2 style='text-align: center;color: #A93226 ;'><b>{food_transform} | {kilocalories[0]} kcal.</b></h2>", unsafe_allow_html=True)

    columns(grease,saturated,carbohy,sugar,fiber,protein,sal)

    return preparing_bar(lista,grease,saturated,carbohy,sugar,fiber,protein,sal)

def check_password():

    def password_entered():
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        return True
