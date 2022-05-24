import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title(' 🥣 My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥑🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

fruits_selected= streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show= my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

def get_fruitvice_data(this_fruit_choice):
  fruitvice_response= requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
  fruitvice_normalized=pandas.json_normalize(fruitvice_response.json())
  return fruitvice_normalized

streamlit.header('FruityVice Fruit Advice!!')

try:
  fruit_choice=streamlit.text_input('what fruit would you like to information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
    
  else:
    back_from_function= get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()


streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM fruit_load_list")
    return my_cur.fetchall()
  
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows= get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
    

fruit_choice=streamlit.text_input('what fruit would you like to add?')
streamlit.write('Thanks for adding',fruit_choice)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
