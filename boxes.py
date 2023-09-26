import streamlit as st


def create_skill_buttons(skills, buttons_per_row=3):
    # Calculate the number of rows
    st.subheader('🔥Stack')
    num_rows = len(skills) // buttons_per_row
    if len(skills) % buttons_per_row != 0:
        num_rows += 1

    # Create columns for each row
    columns = [st.columns(buttons_per_row) for _ in range(num_rows)]

    # Define the button style with the desired background color and fixed size
    button_style = (
        "background-color: orange; "
        "border: 2px solid black; "
        "color: white; "
        "width: 160px; "
        "height: 40px; "
        "margin: 5px; "
        "cursor: pointer;"
    )

    # Iterate through the skills and create buttons with the specified style
    for idx, skill in enumerate(skills):
        row_index = idx // buttons_per_row
        column_index = idx % buttons_per_row
        with columns[row_index][column_index]:
            st.markdown(f'<button style="{button_style}">{skill}</button>', unsafe_allow_html=True)



