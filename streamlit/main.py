import time
from streamlit_option_menu import option_menu
from func_aux.func_aux import *
from keras.models import load_model
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import  webrtc_streamer, RTCConfiguration, WebRtcMode, VideoTransformerBase
from get_data.get_data import *
from PIL import Image



st.set_page_config(page_title='TasterAI', page_icon='https://cdn-icons-png.flaticon.com/512/1548/1548988.png',
                   layout='centered', initial_sidebar_state='expanded')

# Clases
dir_classes = "classes/classes.txt"
read_classes = open(dir_classes, "r")
with read_classes as archivo:
    names = list(map(str.rstrip, archivo))


MODEL_PATH = "model/tasteria_model_fit.h5"


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark">
  <ul  style="list-style: none;">
  <div class="container-fluid">
    <a class="navbar-brand" href="https://github.com/Nachosori" target="_blank">Nachosori
     <li><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="" width="50" class="d-inline-block align-text-top">Nachosori</li></a>
    </a>
  </div>
  </ul>
</nav>""", unsafe_allow_html=True)


# Logo y encabezado


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("https://i.ibb.co/hXzrg03/Logo-Taster-AI.png", width=250)

with col3:
    st.write(' ')


selected = option_menu(
    menu_title= None,
    options=["Home", "Upload photo","Video", "Adm. menu" ],
    icons=["house", "upload","camera", "lock"],
    menu_icon="cast",
    orientation= "horizontal",
    default_index=0,
    styles={
    "container": {"padding": "0!important", "background-color": "#f3f3f3"},
    "icon": {"color": "grey", "font-size": "20px"}, 
    "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#F7DC6F"},
    "nav-link-selected": {"background-color": "#F7DC6F"},
}

    ) 


if selected == "Home":
    
    st.markdown(f"<h3 style='text-align: center;color: black;'><u>Food Detector Neural Network</u></h3", unsafe_allow_html=True)    
    st.markdown(f"<h5 class='justify: left; color: #566573;'>The following project consists of the realization of a neural network model for food categorization. It consists of a database of 15 types of food with an accuracy of 85%. A database with calories and recipes of the foods predicted by the model has also been implemented. </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 class='justify: left; color: #566573;'>At any time you can train the model with more food types. But at the same time they have to update the calorie data etc. of the foods that are not originally implemented. </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 class='justify: left; color: #566573;'>The model predicts the following foods: Carrot Cake, Chocolate Cake, Cheesecake, Hamburger, Hot Dog, Cup Cake, Guacamole, Nachos, Gyoza, Ice Cream, Paella, Donuts, Sushi, Macarons and Pizza. </h5>", unsafe_allow_html=True)

    st.markdown(f"<p style='text-align: center;color: grey ;'></p", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;color: grey ;'></p", unsafe_allow_html=True)

    st.image("https://i.ibb.co/1LRMHrK/My-project-1.png", width=700)



if selected == "Upload photo":

    lista = ["Grease", "Saturat.", "Carbohy.", "Sugar", "Fiber", "Protein", "Sal" ]

    def main():
        
        model=''


        # Se carga el modelo
        if model=='':
            model = load_model(MODEL_PATH)
        
        check = st.checkbox("Take a picture")

        if check:
            image = photo()

            if st.button("Prediction", key="2"):
                predictS = model_prediction(image, model)
                print(predictS)
                food = names[np.argmax(predictS)]
                kilocalories,grease,saturated,carbohy,sugar,fiber,protein,sal = calls_nutritional(food)
                transform_letters(food)
                st.markdown(f"<h2 style='text-align: center;color: #A93226 ;'><b>{food} | {kilocalories[0]} kcal.</b></h2>", unsafe_allow_html=True)
                columns(grease,saturated,carbohy,sugar,fiber,protein,sal)
                preparing_bar(lista,grease,saturated,carbohy,sugar,fiber,protein,sal)
                    

        img_file_buffer = st.file_uploader("Carga una imagen", type=["png", "jpg", "jpeg"], key= "infinity" )
            
        # El usuario carga una imagen
        if img_file_buffer is not None:
            image = np.array(Image.open(img_file_buffer))    
            st.image(image, caption="Imagen", use_column_width=False, width=700)
            
        
        # El botón predicción se usa para iniciar el procesamiento
        if st.button("Prediction", key="1"):
            predictS = model_prediction(image, model)
            
            food = names[np.argmax(predictS)]

            aux(food)

        try: 
            predictS = model_prediction(image, model)

            food = names[np.argmax(predictS)]

            name_recipes = calls_recipes(food)

            print(name_recipes)

            list_names = ["No",]

            for i in name_recipes:
                list_names.append(i)

            option = st.selectbox(label="May I suggest a recipe?", options = list_names)
            
            time_preparation, time_cooking, ingredients, elaboration = call_recipes_name(option)

            if option == "No":
                st.markdown(f"<h3 style='text-align: center;color: #D4AC0D ;'></h3>", unsafe_allow_html=True)
            else:

                st.markdown(f"<h2 style='text-align: center;color: #A93226 ;'><b>{option}</b></h2>", unsafe_allow_html=True)
                st.markdown(f"<hr style='text-align: center;color: #A93226;'></hr>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align: center;color: #A93226 ;'>Time preparation {time_preparation[0]} m | Time cooking {time_cooking[0]} m | Total time {time_preparation[0] + time_cooking[0]} m</h3>", unsafe_allow_html=True)
                st.markdown(f"<hr style='text-align: center;color: #A93226 ;'></hr>", unsafe_allow_html=True)
                st.markdown(f"<h4 style='text-align: center;color: #A93226 ;'><b>Ingredients</b></h4>", unsafe_allow_html=True)
                for ingredient in ingredients:
                    st.markdown(f"<h4 style='text-align: left;color: #A93226  ;'>  - {ingredient} </h4>", unsafe_allow_html=True)
                st.markdown(f"<hr style='text-align: center;color: #A93226 ;'></hr>", unsafe_allow_html=True)
                st.markdown(f"<h4 style='text-align: center;color: #A93226 ;'><b>Elaboration</b></h4>", unsafe_allow_html=True)
                for e in elaboration:
                    st.markdown(f"<h4 style='text-align: left;color: #A93226  ;'> {e} </h4>", unsafe_allow_html=True)
        except(UnboundLocalError):
            print("")


    if __name__ == '__main__':
        main()


if selected == "Video":

    model = load_model(MODEL_PATH)

    def process(image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = model_prediction(image, model)
        return results
        
        
    RTC_CONFIGURATION = RTCConfiguration(
         {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
     )

    class VideoTransformerBase(VideoTransformerBase):
        def _annotate_image(self,image,detections):
            labels = []
            color_ = (0, 255, 0)
            pred = process(image)
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB )
            pred = process(img)
            gray = cv2.cvtColor(image.copy(),cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(gray, 125, 255, 0)
            contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
            prediction = names[np.argmax(pred)]
            print(prediction)

            for area in contours:
                (x, y, w, h) = cv2.boundingRect(area)
                print(x,y,w,h)

            img = cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 1)
            cv2.putText(img, prediction, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

            return img, prediction

        def transform(self,frame):
            image = frame.to_ndarray(format="bgr24")
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pred = process(img)
            prediction = names[np.argmax(pred)]
            annotated_image, labels = self._annotate_image(img, prediction)

            return annotated_image


    webrtc_ctx = webrtc_streamer(
        key="object-detection",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoTransformerBase,
        async_processing=True,
    )

if selected == "Adm. menu":

    if check_password():
        name_food = get_names()
        
        food_list = []

        for name in name_food:
            name = transform_letters(name)
            food_list.append(name)

        type = st.selectbox("Choose type of food", food_list)
        name = st.text_input('Name of recipe:')
        preparation = st.text_input('Time of preparation:')
        cooking = st.text_input('Time of cooking:')
        ingredients = st.text_input("Ingredients:")
        elaboration = st.text_area("Elaboration:")
        type = type.replace(" ", "_").lower()

        dic_recipe = {"type": type,
        "name": name,
        "preparation": preparation,
        "cooking": cooking,
        "ingredients" : [ingredients],
        "elaboration": [elaboration]
        }

        if st.button("Send"):
            post_add_recipes(dic_recipe)
            with st.spinner('Wait for it...'):
                time.sleep(3)
                st.success('The recipe has been added to the database.')

