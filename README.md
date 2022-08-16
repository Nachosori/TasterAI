
<p align="center"> <img src="https://user-images.githubusercontent.com/101704557/184862313-efae0fff-a916-4d3a-8696-093acf6c45c9.png" alt="Descripción de la imagen"  height="200" /> </p>


<h1 style='text-align: center; color:#FF7F00 ;'></h1>

<p align="center"> <img src="https://user-images.githubusercontent.com/101704557/184918236-12d57e4d-aa56-4d34-ad0e-15458a90988e.gif"  height="350"//> </p>

<h1 style='text-align: center; color:#FF7F00 ;'></h1>


The TasterAI is a neural network model for food categorization. It consists of a database of 15 types of food with an accuracy of 85%. A database with calories and recipes of the foods predicted by the model has also been implemented.

At any time you can train the model with more food types. But at the same time they have to update the calorie data etc. of the foods that are not originally implemented.

The model predicts the following foods: Carrot Cake, Chocolate Cake, Cheesecake, Hamburger, Hot Dog, Cup Cake, Guacamole, Nachos, Gyoza, Ice Cream, Paella, Donuts, Sushi, Macarons and Pizza. 

<h1 style='text-align: center; color:#FF7F00 ;'></h1>

# Contents of this file

<details>
<summary>Index</summary>
  <ol>
    <li>
      <a href="#Introduction">Introduction</a>
    </li>
    <li>
        <a href="#Requeriments">Requeriments</a>
    </li>
    <li><a href="#Objectives">Objectives</a></li>
    <li><a href="#Acknowledgments">Acknowledgments</a></li>
    <li><a href="#Autor">Autor</a></li>
  </ol>
</details>

<h1 style='text-align: center; color:#FF7F00 ;'></h1>

# Introduction

The database with which the model is trained is based on 15,000 photographs, 1,000 for each type of food.

The photographs were extracted from the food-101 database.

I attach a link below:

https://www.kaggle.com/datasets/dansbecker/food-101

The model has been trained after several tests with MobileNet v2.

The MobileNet v2 architecture is based on an inverted residual structure in which the input and output of the residual block are thin bottleneck layers, unlike traditional residual models that use expanded representations at the input. MobileNet v2 uses lightweight convolutions in depth to filter features in the intermediate expansion layer. In addition, nonlinearities in the narrow layers have been removed to maintain representational power.

The training with MobileNet gave good results from the very first moment, even though training food recognition is always a bit complicated since each type of food can be represented in very different ways.

<h1 style='text-align: center; color:#FF7F00 ;'></h1>

As can be seen in the image, the model leads to an accuracy of almost 85%.

After training, two different datasets have been created, the first one with nutritional data for each of the foods recognized by the model and the last one with recipes for each of the foods.

All this has been implemented in Streamlit so that when a food is recognized, the nutritional data is automatically displayed and a recipe is suggested.

<p align="center"> <img src=https://i.ibb.co/gR6RfpP/ejemplo.png" alt="Descripción de la imagen"  height="400" /> </p>


Within Streamlit the model has been implemented with opencv where we can see the model working with a live camera.

<p align="center"> <img src="https://i.ibb.co/8PYZKGS/Captura-de-pantalla-de-2022-08-16-18-49-04.png"alt="Descripción de la imagen"  height="400" /> </p>

Finally we have implemented an administration section with username and password where we can upload recipes directly to the database so that the model can suggest them.

<p align="center"> <img src="https://i.ibb.co/0cDDFjz/Captura-de-pantalla-de-2022-08-16-18-55-55.png" alt="Descripción de la imagen"  height="350" /> </p>

<h1 style='text-align: center; color:#FF7F00 ;'></h1>

# Requeriments

You need to have all the libraries from the requirements.txt file installed. Once everything is installed, you can start running the TasterAIdashboad.

To start, go to the Dashboard folder from the console and run the following command:

```
streamlit run main.py
```
To be able to use the administrator section from the Dashboard it is necessary to include a file with the users that are going to have these permissions, this file will be placed inside the .streamlit folder with the name secrets.toml and will have the following format:

```
#.streamlit/secrets.toml

[passwords]
# Follow the rule: username = "password"
username = "password"
```
<h1 style='text-align: center; color:#FF7F00 ;'></h1>

# Objectives

The objectives for improving the model in the short term are as follows:

- [x] Detecting live food through the camera
- [ ] Detect several meals at the same time
- [ ] Improve the accuracy of the model.
- [ ] Increase the number of foods recognized by the model.
- [ ] Implement its use on a Rasberry Pi and test the system on the street or in stores.

# Acknowledgments

  <ol>
    <li>
      <a href="https://www.corecode.school/">CORE Code School</a>
    </li>
    <li>
        <a href="https://github.com/boyander">Marc Pomar</a>
    </li>
    <li><a href="https://github.com/Alvaro-Lucas">Alvaro Lucas</a></li>
    <li><a href=https://github.com/DanielDls-exe>Daniel Alvarado</a></li>
    <li><a href=https://github.com/Luxor5k>Santino Lede</a></li>
  </ol>

# Autor


<a href=https://github.com>Nacho Soria</a>

<a >isoriadiez@gmail.com</a>

