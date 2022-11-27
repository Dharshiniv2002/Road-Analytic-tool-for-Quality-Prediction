import streamlit as st
from streamlit_option_menu import option_menu
from  PIL import Image
import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import plotly.express as px
from sklearn.linear_model import LogisticRegression
import joblib
from tkinter import HORIZONTAL

##img = Image.open('SIH_2018_logo.png')

##st.set_page_config(page_title="Road Analytics",page_icon=img)

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            body {
            background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
            background-size: cover;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



##st.sidebar.image(img, use_column_width=False,width=None)     #-----------> For icon on the side (Note: Kindly change the size of the image)

with st.sidebar:
    selected = option_menu(
        menu_title="Dashboard",
        options=["Home","Analytics","Visualization","Prediction"],
        icons=["house","activity","clipboard-data","graph-up-arrow"],
        menu_icon=None,
        
        styles={
                "container": {"padding": "0!important", "background-color": "DBF0F9"},  #background color for the Website
                "icon": {"color": "black", "font-size": "20px"},   # icon color for the tabs
                "nav-link": {
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "DBF0F9", # icon color after hover
                },
                "nav-link-selected": {"background-color": "#ADD8E6"},   # Colour when tab is selected  #ADD8E6
                "icon": {"color": "black", "font-size": "20px"},   # icon color
            },
        )


if selected=="Home":
        st.title("Analytics tool for Road data Analysis")
        st.header('Pradhan Mantri Gram Sadak Yojana (PMGSY)')
        st.write('The Pradhan Mantri Gram Sadak Yojana (PMGSY), was launched by the Govt. of India to provide connectivity to unconnected Habitations as part of a poverty reduction strategy. Govt. of India is endeavoring to set high and uniform technical and management standards and facilitating policy development and planning at State level in order to ensure sustainable management of the rural roads network.')
        st.write('According to latest figures made available by the State Governments under a survey to identify Core Network as part of the PMGSY programme, about 1.67 lakh Unconnected Habitations are eligible for coverage under the programme. This involves construction of about 3.71 lakh km of roads for New Connectivity and 3.68 lakh km. under upgradation.')
        PMGSY = Image.open('pmgsy.jpeg')
        st.image(PMGSY)
        st.header("NQM and SQM")
        font="serif"
        st.write("The primary functions of transportation include mobility, connectivity and accessibility.Road transport in general and rural transport in essential for it.")
        font="serif"
        st.header('Problem Statement')
        st.write('Analytics tool to provide detail reports on the grading between NQM and SQM.')
        st.header('Brief Explanation of the Problem Statement')
        st.write('In this problem statement we have to analyze the data and provide the detailed reports based on the grading between NQM and SQM.')
        st.header('NQM [National Quality Monitors] :')
        st.write('Under the third tier, independent National Quality Monitors (NQM) are deployed by National Rural Roads Developing Agency (NRRDA) for inspection of road works at random not only to monitor quality but also to provide guidance of senior professionals to the field functionaries.')
        NQM = Image.open('Collage.jpeg')
        st.image(NQM)
        st.header('SQM [State Quality Monitors]:')
        st.write('The State Quality Monitors (SQM) shall inspect every road work including CD works and all other related works at 3 stages as prescribed.')
        SQM = Image.open('sqm.jpeg')
        st.image(SQM)
        st.header('Idea/Solution: ')
        st.write('Our idea is to collect and analyze the data, given by the NQM and SQM and to find out the quality of the road using the Machine Learning concept. Here we can provide the analyzed data on the graphical manner, so that we can interpret the correctness of the grading provided by the NQM and SQM. In this we need to acquire the different set of inputs, so that we can provide the exact difference between their grading. Our main goal is to analyze the data and to present the quality of the road in the graphical representation and to find out the variance with the given parameters.')
        st.write("Note: Before running the script we have used the following packages each of it has its own features and conditions to run the  code succesfully.")
        st.write("Program by: Loads of Logic")


if selected=="Visualization":
    st.header("Visualization")
    st.write("Now its time for us to visualize the dataset that we have uploaded. When speaking about visualization, We should als understand there are many types. Some of which are as follows: \n  1) Bar chart \n 2) Scatter Plot \n 3) Line plot \n 4) Histogram")
    st.write("In the side bar use the drop down menu to visualize the dataset that we have uploaded.")
    st.set_option('deprecation.showfileUploaderEncoding', False)

# Add a sidebar
    st.sidebar.subheader("Visualization Settings")
    st.write("For this project since we aren't sure on what dataset to use we used dataset from the following websites: \n\t[Dataset 1](http://omms.nic.in/),\n[Dataset 2](https://data.gov.in/catalog/total-road-length-and-percentage-share-each-category-road-total-road-length)")
    st.write("Based on our discussion with Civil Department students we have got a [pdf](https://github.com/Aristophanes26/SIH/blob/main/Basic%20Road%20Statics%20of%20India%20CTCcompressed1.pdf) file containing the values required")
    st.write("Note: If you cann't view the Pdf file try to downoad it instead.")
# Setup file upload
    uploaded_file = st.sidebar.file_uploader(
        label="Upload your CSV or Excel file. (200MB max)",
        type=['csv', 'xlsx'])

    global da 
    if uploaded_file is None:
        st.header("Your file is not uploaded....")
    if uploaded_file is not None:
        print("The dataset is being displayed")
        try:
            da = pd.read_csv(uploaded_file)
            da.fillna(da.iloc[:,:].median(), inplace = True)                   #------------------>  Add
            print(da)
        except Exception as e:
            print(e)
            da = pd.read_excel(uploaded_file)
            da.fillna(da.iloc[:,:].median(), inplace = True) 
            print(da)                          # ------------------>  Add
    global numeric_columns
    global non_numeric_columns
    try:
        st.write(da)
        numeric_columns = list(da.select_dtypes(['float', 'int']).columns)
        non_numeric_columns = list(da.select_dtypes(['object']).columns)
        non_numeric_columns.append(None)
        print(non_numeric_columns)
    except Exception as e:
        print(e)
        st.write("Please upload file to the application.")
# add a select widget to the side bar
    chart_select = st.sidebar.selectbox(
        label="Select the chart type",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
    )

    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Scatterplot Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
            plot = px.scatter(data_frame=da, x=x_values, y=y_values, color=color_value)
        # display the chart
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Lineplots':
        st.sidebar.subheader("Line Plot Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
            plot = px.line(data_frame=da, x=x_values, y=y_values, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Histogram':
        st.sidebar.subheader("Histogram Settings")
        try:
            x = st.sidebar.selectbox('Feature', options=numeric_columns)
            bin_size = st.sidebar.slider("Number of Bins", min_value=10,
            max_value=100, value=40)
            color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
            plot = px.histogram(x=x, data_frame=da, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Boxplot':
        st.sidebar.subheader("Boxplot Settings")
        try:
            y = st.sidebar.selectbox("Y axis", options=numeric_columns)
            x = st.sidebar.selectbox("X axis", options=non_numeric_columns)
            color_value = st.sidebar.selectbox("Color", options=non_numeric_columns)
            plot = px.box(data_frame=da, y=y, x=x, color=color_value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
if selected=="Analytics":
    st.header('Upload your CSV data')
    st.write("Now it's time for you to uplod your CSV files with the drag and drop functionality")
    st.write("Follow the given steps below to upload your CSV files with the drag and drop functionality")
    st.write("\t 1) Use the drag and drop icon to upload your CSV files")
    st.write("2) Now the model tries to perform analytics based on the given data. This may vary based on the size of the data uploaded.")
    st.write("3) You can now view the analytics that is been performed on the dataset. Some on the common analytics funvtion include: ")
    st.write("a) Mean ")
    st.write("b) Median")  
    st.write("c) Mode and many more...")
    uploaded_file = st.file_uploader("Note: Only CSV files are allowed", type=["csv"])
# Pandas Profiling Report
    if uploaded_file is not None:
        @st.cache
        def load_csv():
            csv = pd.read_csv(uploaded_file)                 # ------------------>  Add
            csv.fillna(csv.iloc[:,:].median(), inplace = True)
            return csv
            
        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**The following is the Data frame that you have uploaded..**')
        st.write(df)
        st.write('---')
        st.header('**Please wait your report is being generated...**')
        st_profile_report(pr)
    else:
        st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        @st.cache
        def load_data():
            a = pd.read_csv('https://raw.githubusercontent.com/Aristophanes26/SIH/main/State%20wise%20Road%20datasets.csv')
            a.fillna(a[:].median(),inplace=True)
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Example Dataset is being loaded..**')
        st.write(df)
        st.write('---')
        st.header('**Please wait your report is being generated...**')
        st_profile_report(pr)

if selected == 'Prediction':
    st.title('Machine Learning Model predictor for the road datset')
    st.header('Road Quality')
    st.write("When taking road Quality, Some other parameters must also be taken into account for bringing suitable conclusion. It's not always necessary that all the data will be given for carrying out the analysis. In such cases relying on the given data won't be sufficient enough.")
    st.write("So, We must use Machine Learning concepts instead to make accurate and absolute decisions about the data we are handling.")
    st.header("Approach towards reaching the solution")
    st.write("One of the most popular algorithm that is used for doing this job is Logistic Regression which provides the output in two classes: ")
    st.write('❄️ Good (1)') 
    st.write('❄️ Bad (0)')
    st.write()
    st.write("For the road dataset that we are handling add the values of suitable parameters. You can either type it or use the '+' icon to increase the value of the parameters ")

    df = pd.read_csv("Road Quality.csv")
    X = df[["Resource Access Roads (in km)", "Low traffic Roads(1 or 0)", " Low Speed Roads(m/s)", "Speed Range Roads(m/s)", "Land use Roads(in Km)", "Special Functional Roads (in km)", "Vehicle type Roads(in cm)", "Other PGMSY Roads (in Km)", "Special Section Roads (in Km)", "Weather Roads(in C)", "Junction Links(in Km)", "Streets(in Km)", "Path Holes (in Binary)"]]
    y = df["Road Quality (G/B)"]
    clf = LogisticRegression() 
    clf.fit(X, y)
    joblib.dump(clf, "clf.pkl")
    a = st.number_input("Enter the Resource Access Road (in Km)")
    b = st.number_input("Enter the Low Traffic Roads (1 or 0)")
    c = st.number_input("Enter the Low Speed Roads (in m/s) ")
    d = st.number_input("Enter the Speed Range Roads (in m/s)")
    e = st.number_input("Enter the Land Use Roads (in Km)")
    f = st.number_input("Enter the Special Functional Roads (in Km) ")
    g = st.number_input("Enter the Vehicle Type Roads (in cm) ")
    h = st.number_input("Enter the Other PGMSY Roads (in Km)")
    i = st.number_input("Enter the Special Section Roads (in Km)")
    j = st.number_input("Enter the Weather Roads (in Celcius)")
    k = st.number_input("Enter the Junction Links (in Km)")
    l = st.number_input("Enter the Streets (in Km)")
    m = st.number_input("Enter the Path Holes (0 or 1) ")
    if st.button("Submit"):
        clf = joblib.load("clf.pkl")
        X = pd.DataFrame([[a, b, c, d, e, f, g, h, i, j, k, l, m]], 
                     columns = ["Resource Access Roads (in km)", "Low traffic Roads(1 or 0)", " Low Speed Roads(m/s)", "Speed Range Roads(m/s)", "Land use Roads(in Km)", "Special Functional Roads (in km)", "Vehicle type Roads(in cm)", "Other PGMSY Roads (in Km)", "Special Section Roads (in Km)", "Weather Roads(in C)", "Junction Links(in Km)", "Streets(in Km)", "Path Holes (in Binary)"])
        prediction = clf.predict(X)[0]
        st.write("Based on the data you have uploaded the model has trained itself to come to conclusion.")
        st.info(f"The road quality is a {prediction}") 
        