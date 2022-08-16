
<p align="center"> <img src="https://user-images.githubusercontent.com/101704557/184862313-efae0fff-a916-4d3a-8696-093acf6c45c9.png" alt="Descripción de la imagen"  height="200" /> </p>


<h1 style='text-align: center; color:#FF7F00 ;'></h1>

<p align="center"> <img src="https://user-images.githubusercontent.com/101704557/184918236-12d57e4d-aa56-4d34-ad0e-15458a90988e.gif"  height="350"//> </p>

<h1 style='text-align: center; color:#FF7F00 ;'></h1>


The TasterAI is a neural network model for food categorization. It consists of a database of 15 types of food with an accuracy of 85%. A database with calories and recipes of the foods predicted by the model has also been implemented.

At any time you can train the model with more food types. But at the same time they have to update the calorie data etc. of the foods that are not originally implemented.

The model predicts the following foods: Carrot Cake, Chocolate Cake, Cheesecake, Hamburger, Hot Dog, Cup Cake, Guacamole, Nachos, Gyoza, Ice Cream, Paella, Donuts, Sushi, Macarons and Pizza. 

<h1 style='text-align: center; color:#FF7F00 ;'></h1>

<h2 align="center">Contents of this file</h2>

- Requeriments
- Instructions
- API Reference

<h1 style='text-align: center; color:#FF7F00 ;'></h1>

<h2 align="center">Requeriments</h2>

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


