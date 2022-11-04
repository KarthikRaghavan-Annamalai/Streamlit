#import necessary libraries
import streamlit as st

#Set title for the Streamlit App
st.title('Our First Streamlit App')

#Set subheader
st.subheader('Streamlit')

#To add image in the Streamlit App
st.image('streamlit.png')
st.success('Image Loaded successfully')

#Add Text
st.write('Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science')

#Add Markdown
st.markdown('This is a markdown cell')
st.info('INFO - Streamlit Test App')

#Add Warning
st.warning('Be Cautious')

#Add Error
st.error('Error Message')

#Add Help with package
st.help(range)


import numpy as np
import pandas as pd

dataframe = np.random.rand(10,20)

st.dataframe(dataframe)
st.success('DataFrame Loaded')

st.text('---'*100)

df = pd.DataFrame(np.random.rand(10,20),columns=('col %d' % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=1))

st.text('---'*100)

#Display Chart
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.line_chart(chart_data)


st.text('---'*100)

st.area_chart(chart_data)

st.text('---'*100)

chart_data = pd.DataFrame(np.random.randn(50,3),columns=['A','B','C'])
st.bar_chart(chart_data)

st.text('---'*100)

import matplotlib.pyplot as plt

arr = np.random.normal(1,1,size=100)
plt.hist(arr,bins=20)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

st.text('---'*100)

import plotly
import plotly.figure_factory as ff
import scipy

#Adding Distplot
x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)-2

hist_data = [x1, x2, x3]
group_labels = ['Grp1', 'Grp2', 'Grp3']

fig = ff.create_distplot(hist_data,group_labels,bin_size=[0.2,0.25,0.5])
st.plotly_chart(fig,use_container_width=True)

st.text('---'*100)

df = pd.DataFrame(np.random.randn(100,2)/[50,50]*[37.76,-122.4],columns=['lat','lon'])
st.map(df)

#Create Button
if st.button('Click Here to Say Hello'):
    st.write('Hello')
else:
    st.write('Why are you here ??')

st.text('---'*100)

genre = st.radio('What is your fav genre?', ('Comedy','Action','Supernatural'))

if genre == 'Comedy':
    st.write('You like Comedy')
elif genre == 'Action':
    st.write('You like Action')
else :
    st.write('You like Supernatural')

st.text('---'*100)

#Select Button
option = st.selectbox('How was your day?', ('Good', 'Bad'))
st.write(f'Your day was {option}')

st.text('---'*100)

#Select Multiple Buttons
option = st.multiselect('How was your day?', ('Good', 'Bad'))
st.write(f'Your day was {option}')

st.text('---'*100)

#Slider
age = st.slider('How old are you?',0,150,20)
st.write(f'your age is {age}')

st.text('---'*100)

values = st.slider('Select of range of values',0,200,(15,80))
st.write(f'you selected a range between {values}')

number = st.number_input('Enter the number')
st.write(f'The number is {number}')

st.text('---'*100)
st.text('---'*100)

#Allow user to upload file from their end
#upload = st.file_uploader('Browse to upload files')
upload_csv = st.file_uploader('Browse to upload files',type='csv')

if upload_csv is not None:
    data = pd.read_csv(upload_csv)
    st.dataframe(data)
    st.success('Dataframe uploaded')
else:
    st.info('File is empty, Upload a file')

st.text('---'*100)

#Add Color Picker
color = st.color_picker('Pick your preferred color','#00FFAA')
st.write(f'The color is {color}')

st.text('---'*100)

#Side bar
#Using object notation
add_selectbox = st.sidebar.selectbox("What is your fav course?",("ML", "DL", "CV","NLP"))

#Using "with" notation
with st.sidebar:
    add_radio = st.radio("What is your fav course?",("ML", "DL", "CV","NLP"))

#Color Picker as Sidebar
st.sidebar.color_picker('Color Picker',"#00FFAA")

#Progress Bar
import time

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete+1)

st.text('---'*100)

with st.spinner('wait for it...'):
    time.sleep(5)
st.success('Successful')

st.balloons()

