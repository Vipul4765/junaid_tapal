
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


lottie_coder = load_lottie1('https://lottie.host/dcb96a6c-63df-40de-94ab-fdf386d34d71/fpVA71rpTV.json')

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

            st_lottie(lottie_coder,height=277 )
                # Adjust width and alignment
            st.write('---')
            st.header("👨‍💻Coding Profile")
            st.markdown("- [Leetcode](https://leetcode.com/tapal_junaid/)")
            st.markdown("- [Hackerrank](https://www.hackerrank.com/tj6130)")

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
            options=['IPL API', 'Workshop platform - DOM and Mysql', 'VIRTUAL MOUSE - virtual mouse using ARTIFICIAL INTELLIGENCE and ML', 'Driver Drowsiness Detection - software - PYTHON', 'Full-Stack Web Project - Java and ReactJS'],
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

    if selected == 'Workshop platform - DOM and Mysql':
        st.title('Project - Workshop platform - DOM and MySQL')
        #st.image('workshop_image.jpg', use_column_width=True)  # You can add an image for illustration
        st.markdown(
            """
            This platform provides students with an effortless way to discover and participate in workshops. It also empowers club leaders
            to organize workshops that align with student interests, ultimately increasing workshop attendance.

            **Key Features**:
            - **Workshop Discovery**: Easily find workshops based on your interests and preferences.
            - **Club Heads**: Club leaders can gauge student interest and organize relevant workshops.
            - **Efficient Registration**: Streamlined registration process for hassle-free participation.
            - **Feedback**: Provide feedback on workshops to help improve future events.

            Whether you're a student eager to learn or a club leader looking to engage your peers, our Workshop platform - DOM and MySQL
            has you covered!
            """
        )

    if selected == 'VIRTUAL MOUSE - virtual mouse using ARTIFICIAL INTELLIGENCE and ML':
        st.title('Virtual Mouse Control')
        # st.image('virtual_mouse_image.jpg', use_column_width=True)  # Add an image for illustration

        st.markdown(
            """
            **Experience a Revolution in Mouse Control!**

            Our Virtual Mouse Control system brings the future to your fingertips. Imagine harnessing the power of hand gestures to navigate your computer seamlessly. With this cutting-edge technology, you can perform all your mouse functions effortlessly:

            - **Intuitive Gestures**: Left-click, right-click, and perform settings changes with simple hand movements.
            - **Drag and Drop**: Effortlessly move and organize files and folders.
            - **Precision Control**: Fine-tune your actions with pinpoint accuracy.
            - **No Hardware Required**: No need for additional equipment – just your hands and our software.

            Whether you're a professional looking for a more efficient workflow or simply seeking an innovative way to interact with your computer, our Virtual Mouse Control system empowers you to take control like never before.


            Get ready to revolutionize your computing experience with the future of mouse control!
            """,
            unsafe_allow_html=True
        )

    if selected == 'Driver Drowsiness Detection - software - PYTHON':
        st.title('Driver Drowsiness Detection - Python Software')
        # st.image('drowsiness_detection_image.jpg', use_column_width=True)  # Add an image for illustration

        st.markdown(
            """
            **Stay Awake, Stay Safe!**

            Presenting our Driver Drowsiness Detection system, powered by Python. This software provides a comprehensive solution to ensure road safety by preventing drowsy driving incidents. It incorporates advanced techniques to monitor driver behavior and alert in real-time.

            **Key Features**:
            - **Face Detection**: Utilizing state-of-the-art algorithms to detect the driver's face accurately.
            - **Eye Position Tracking**: Real-time monitoring of eyelid movements and gaze direction.
            - **AI-Based Eye Tracking**: Continuous analysis of eye behavior to detect signs of drowsiness.
            - **Instant Alerts**: Immediate alerts to prevent accidents caused by drowsiness.
            - **Seamless Integration**: Easily integrates with your vehicle's safety system.
            - **Python-Powered**: Developed using Python for flexibility and reliability.

            Whether you're a professional driver or a safety-conscious individual, our Driver Drowsiness Detection software is your vigilant co-pilot on the road.


            Say goodbye to drowsy driving—prioritize safety with our Python-powered solution.
            """,
            unsafe_allow_html=True
        )

    if selected == 'Full-Stack Web Project - Java and ReactJS':
        st.title('Full-Stack Web Project - Java and ReactJS')
        # st.image('fullstack_web_project_image.jpg', use_column_width=True)  # Add an image for illustration

        st.markdown(
            """
            **Empowering the Web with Java and ReactJS!**

            Our Full-Stack Web Project is a testament to the synergy of technology, bridging the gap between front-end and back-end development. With Java powering the backend and ReactJS driving the frontend, we've created a comprehensive web solution that covers every aspect of modern web development.

            **Key Highlights**:
            - **Security**: Robust security measures ensure your data is protected.
            - **CRUD Operations**: Seamlessly Create, Read, Update, and Delete data with ease.
            - **Databases**: Efficiently manage data using state-of-the-art databases.
            - **Frontend Frameworks**: ReactJS forms the foundation for a responsive and dynamic user interface.
            - **State Management**: Utilize advanced state management techniques for a seamless user experience.
            - **APIs**: Power your application with flexible and well-documented APIs.
            - **Version Control**: Implement version control systems for code management and collaboration.

            Our full-stack web project is a testament to the power of technology, offering a secure, efficient, and user-friendly web experience. Whether you're a developer, business owner, or user, our project brings the best of both worlds to the web.


            Join us on a journey of innovation and excellence in web development!
            """,
            unsafe_allow_html=True
        )

if selected == 'Contact':
    contact_info.create_streamlit_content()