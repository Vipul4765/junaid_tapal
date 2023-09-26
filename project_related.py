import streamlit as st
import requests
import pandas as pd




def fetch_github_directory(repo_name):
    try:
        base_url = f"https://api.github.com/repos/{repo_name}/contents/"
        response = requests.get(base_url)
        response.raise_for_status()  # Check for HTTP request errors
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching repository contents: {e}")
        return None


def get_file_type(file_name):
    # Extract the file extension
    file_extension = file_name.split('.')[-1]

    # If the extension is empty, return 'Other'
    if not file_extension:
        return 'Other'

    # Otherwise, return the extension with .dot
    return f".{file_extension}"


def main():
    st.subheader("GitHub Directory Viewer")
    st.write('Github link of Ipl Api')
    st.markdown('https://github.com/tapal123/ipl-api')
    # Input fields
    repo_name = st.text_input("GitHub Repository Name", "tapal123/ipl-api")
    st.write('Click on Load Repository if want to load here ')
    if st.button("Load Repository"):

        if repo_name:
            contents = fetch_github_directory(repo_name)
            if isinstance(contents, list):
                st.write(f"Contents of '{repo_name}' repository:")

                # Create a list of clickable links
                URL = [f"https://raw.githubusercontent.com/{repo_name}/master/{item['name']}" for item in contents]

                # Create a new DataFrame with file details, types, and links
                df = pd.DataFrame({
                    "File Name": [item['name'] for item in contents],
                    "File Type": [get_file_type(item['name']) for item in contents]
                })
                df['URL'] = URL

                st.data_editor(
                    df,
                    column_config={
                        "URL": st.column_config.LinkColumn("File Link")
                    },
                    hide_index=True,
                )

                #df['Link'] = [create_link(url) for url in URL]

                # Dataframe as a plotly table

                '''fig = go.Figure(
                    data=[
                        go.Table(
                            columnwidth=[1, 0.3, 1],
                            header=dict(
                                values=[f"<b>{i}</b>" for i in df.columns.to_list()],
                                fill_color='pink'
                            ),
                            cells=dict(
                                values=df.transpose()
                            )
                        )
                    ]
                )
                st.plotly_chart(fig, use_container_width=True)'''





            else:
                st.error(f"Failed to fetch repository contents for '{repo_name}'. Check your repository name.")
        else:
            st.warning("Please enter a valid GitHub repository name.")

if __name__ == "__main__":
    main()













'''import streamlit as st
import requests
import base64

repo_name = "Vipul4765/ipl-api-service"
file_name = "bowler_related.py"

url = f"https://api.github.com/repos/{repo_name}/contents/{file_name}"

response = requests.get(url)

if response.status_code == 200:
    content = response.json()['content']
    decoded_content = base64.b64decode(content).decode('utf-8')
    st.code(decoded_content)
else:
    print(f"Failed to fetch content for {file_name}")'''