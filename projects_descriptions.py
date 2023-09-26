import streamlit as st


def display_project_description( project_overview, challenges, key_takeaways, keywords,
                                skills_and_expertise,benfits):
    """
    Display a project description using st.write in Streamlit.

    Args:
    project_name (str): The name of the project.
    project_overview (str): An overview of the project.
    challenges (str): Challenges faced during the project.
    key_takeaways (str): Key takeaways or lessons learned.
    keywords (str): Keywords related to the project.
    skills_and_expertise (str): Skills and expertise gained during the project.
    """
    # Apply blue color to subheadings
    subheading_style = "color: #0074D9;"
    st.markdown(f"<h5 style='{subheading_style}'>Project Overview:</h5>", unsafe_allow_html=True)
    st.write(project_overview)

    st.markdown(f"<h5 style='{subheading_style}'>Challenges:</h5>", unsafe_allow_html=True)
    st.write(challenges)

    st.markdown(f"<h5 style='{subheading_style}'>Key Takeaways:</h5>", unsafe_allow_html=True)
    st.write(key_takeaways)

    st.markdown(f"<h5 style='{subheading_style}'>Keywords:</h5>", unsafe_allow_html=True)
    st.write(keywords)

    st.markdown(f"<h5 style='{subheading_style}'>Skills and Expertise:</h5>", unsafe_allow_html=True)
    st.write(skills_and_expertise)

    st.markdown(f"<h5 style='{subheading_style}'>Benefits:</h5>", unsafe_allow_html=True)
    st.write(benfits)





def ipl_api():
    display_project_description(

        project_overview="I built an IPL API that provides real data about the Indian Premier League.",
        challenges="The biggest challenge was Manipulating the data .",
        key_takeaways="I learned a lot about Python, Flask, Numpy and Pandas during this project.",
        keywords="IPL, API, Python, Flask, Pandas, Numpy, cricket, data science",
        skills_and_expertise="Data engineering, data science, API development",


        benfits = """• The benefits of using your API, such as its accuracy, reliability, and ease of use.    
             • The potential applications of your API, such as for fantasy cricket games, betting  apps, or news websites.                            
             • The future plans for your API, such as adding new features or expanding its coverage"""
    )


