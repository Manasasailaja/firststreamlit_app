import streamlit

streamlit.title(' 🥣 My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥑🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

fruits_selected= streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
streamlit.header('FruityVice Fruit Advice!!')

try:
  fruit_choice=streamlit.text_input('what fruit would you like to information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
    
  else:
  fruitvice_response=requests.get("https://www.fruityvice.com/api/fruit/watermelon")

  fruitvice_normalized=pandas.json_normalize(fruitvice_response.json())
  streamlit.dataframe(fruitvice_normalized)
  
except URLError as e:
  streamlit.error()

streamlit.stop()

import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()

streamlit.dataframe(my_data_rows)

fruit_choice=streamlit.text_input('what fruit would you like to add?')
streamlit.write('Thanks for adding',fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")




