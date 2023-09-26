# Now you can import option_menu
from streamlit_option_menu import option_menu
import streamlit as st
import pandas as pd
from streamlit.runtime.state import widgets
import requests
from streamlit_lottie import st_lottie
import project_related
import projects_descriptions
import boxes
import contact_info

st.set_page_config(layout='wide', page_title="My Portfolio Website", page_icon="🚀")





def load_lottie1(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coder = load_lottie1('https://lottie.host/69aed16c-7cf5-46b9-beb6-50aee75e3535/1IH5t9bwIN.json')

st.write('##')
st.subheader('I am Junaid Tapal')
st.title('My portfolio Website')
st.write('-----')

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Certification', 'Contact'],
        icons=['person', 'code-slash', 'cc-square', 'chat-left-text-fill'],
        orientation='horizontal'

    )
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('🎓Undergraduate At SRM University')
            st.write(
                "My name is junaid I am a software engineer graduate from SRM in specialization of AIML,with  a passion of coding and problem solving skill.I am well acquainted im CPP, python and one of the script langauge which is js and especially in Dbms i usually use SQL which gives me privilege to work with and also gives strong encryption .I am a eager learner as well as an innovative thinker,i used to compare my solution with my group of frds and i will compare it.i have contributed some constant complexity solution in leetcode which i used to practice in my free  time.i have been constantly striving to improve new tech skills which makes me to move a head in my career in software development.")
            st.write("----------")
            skills = ['C++', 'MySql', 'Numpy', 'Pandas', 'SDLC', 'Networking Protocol', 'Python', 'DSA', 'OOPs', 'JavaScripts',
                      'Linux', 'Html', 'CSS', 'C Programming', ' Power BI']

            # Display the Skills section
            st.title('🔥Skills')

            # Display skills buttons in rows
            boxes.create_skill_buttons(skills)

        with col2:
            with col2:
                col1, col2 = st.columns(2)
                with col2:
                    st_lottie(lottie_coder, width=350, )  # Adjust width and alignment
                st.write('---')
                st.header("👨‍💻Coding Profile")
                st.markdown("- [GFG](https://auth.geeksforgeeks.org/user/vipuldhankar)")
                st.markdown("- [Leetcode](https://leetcode.com/coder_123_/)")
                st.markdown("- [CodeChef](https://www.codechef.com/users/vipuldhankar17)")
                st.markdown("- [Hackerrank](https://www.hackerrank.com/vipuldhankar1711)")
                st.markdown(
                    "- [Coding Ninja](https://www.codingninjas.com/studio/profile/a732a5a7-88e5-44ab-9eaf-4af8a4cb59ff)")

        st.write('-----')
        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.header("Education")
                education_df = pd.DataFrame({
                    'Education': ['B.Tech', 'XII', 'X'],
                    'Passing Year': [2024, 2020, 2018],
                    'Grade': ['9.1 CGPA', '92.8%', '95%'],
                    'Board': ['SRMIST', 'BIEAP', 'BIEAP']
                })
                st.table(education_df.style.set_properties(**{'text-align': 'center', 'width': 'auto'}))

            with col4:
                st.write('#')
                st.write('#')
                st.code("""
                #include <iostream>

                using namespace std;

                int main() {
                    string passion = "I find my passion in coding and problem-solving!";
                    cout << passion << endl;
                    return 0;
                }

""")
    st.write('##')
    with st.container():
        col5, col6 = st.columns(2)

        pass

if selected == 'Certification':
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            selected = option_menu(
                menu_title= 'Choose one to see the certificate',
                options=["Problem Solving", 'Hackathon', 'INTERNSHIP - Tathastu DSA Scholar', 'JavaScript', 'Python Programming', 'INTERNSHIP - Data Science with ML', 'Data Analysis'],
                icons=['code-square', 'code-square', 'code-square', 'code-square', 'code-square', 'code-square', 'code-square'],
            )

        if selected == 'Problem Solving':
            with col2:
                st.image('img.png', caption='Coding Ninjas Certificate',
                         use_column_width=True)

        if selected == 'Hackathon':
            with col2:
                st.image('img_1.png')
        if selected == 'INTERNSHIP - Tathastu DSA Scholar':
            with col2:
                st.image('INTERNSHIP_TATHASTU_TECH_page-0001.jpg')
        if selected == 'JavaScript':
            with col2:
                st.image('OPEN_WEAVER_JS_CERTIFICATION_page-0001.jpg')
        if selected == 'Python Programming':
            with col2:
                st.image('OPEN_WEAVER_PYTHON_CERTIFICATION_page-0001.jpg')
        if selected == 'INTERNSHIP - Data Science with ML':
            with col2:
                st.image('Skolar - Internship Completion Certificate _ Tapal Junaid_page-0001.jpg')

        if selected == 'Data Analysis':
            with col2:
                st.image('Image 2023-09-27 at 12.36.07 AM.jpeg')

st.write('----')
if selected == 'Projects':

    with st.container():
        selected = option_menu(
            menu_title=None,
            options=['IPL API', 'Workshop platform - DOM and Mysql', 'VIRTUAL MOUSE - virtual mouse using ARTIFICIAL INTELLIGENCE and ML ', 'Driver Drowsiness Detection - software - PYTHON ', 'RAILWAY TICKET BOOKING SYSTEM - USING C language Merge Sort '],
            icons=['rocket-takeoff', 'rocket-takeoff', 'rocket-takeoff', 'rocket-takeoff', 'rocket-takeoff'],
        )
    if selected == 'IPL API':

        project_name = 'Project : IPL API'
        st.title(project_name)


        col1, col2 = st.columns(2)
        with col1:

            # calling project description function
            subheading_style = "color: #000000; text-decoration: underline;"
            st.markdown(f"<h4 style='{subheading_style}'>Project Description:</h4>", unsafe_allow_html=True)
            projects_descriptions.ipl_api()




        with col2:
            stack = ['Flask', 'Python', 'Pandas', 'Numpy', 'Data Analysis', 'Kaggle']

            boxes.create_skill_buttons(stack)
            project_related.main()
if selected == 'Contact':
    contact_info.create_streamlit_content()