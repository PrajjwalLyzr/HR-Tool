import streamlit as st
from st_social_media_links import SocialMediaIcons
import os
import shutil



def remove_existing_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            st.error(f"Error while removing existing files: {e}")


def get_files_in_directory(directory):
    # This function help us to get the file path along with filename.
    files_list = []

    if os.path.exists(directory) and os.path.isdir(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            if os.path.isfile(file_path):
                files_list.append(file_path)

    return files_list

def save_uploaded_file(directory, uploaded_file):
    remove_existing_files(directory=directory)
    file_path = os.path.join(directory, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.read())
    st.success("File uploaded successfully")

def get_file_name(directory):
    try:
        files = os.listdir(directory)
        file_names = [file for file in files if os.path.isfile(os.path.join(directory, file))]
        
        return file_names[0]
    
    except FileNotFoundError:
        return f"The directory '{directory}' does not exist."
    
    except Exception as e:
        return f"An error occurred: {e}"


def delete_keys_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def social_media():
    # This function will help you to render socila media icons with link on the app
    social_media_links = [
    "https://github.com/LyzrCore/lyzr",
    "https://www.youtube.com/@LyzrAI",
    "https://www.instagram.com/lyzr.ai/",
    "https://www.linkedin.com/company/lyzr-platform/posts/?feedView=all",
                        ]   

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render(sidebar=True) # will render in the sidebar


def social_media_page():
    # This function will help you to render socila media icons with link on the app
    social_media_links = [
    "https://github.com/LyzrCore/lyzr",
    "https://www.youtube.com/@LyzrAI",
    "https://www.instagram.com/lyzr.ai/",
    "https://www.linkedin.com/company/lyzr-platform/posts/?feedView=all",
                        ]   

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render(sidebar=False, justify_content="space-evenly")

def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
       }
    </style>
    """, unsafe_allow_html=True)

def page_config(layout = "centered"):
    st.set_page_config(
        page_title="HR Tool",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )

def footer():
    footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        color: #6c757d;
    }
    </style>
    <div class="footer">
        <p>© 2024 HR Management by Lyzr.ai | All rights reserved.</p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

def template_end():
    with st.sidebar.expander("ℹ️ - About this App"):
        st.sidebar.markdown("This app uses Lyzr's Agent API to streamline and enhance human resource processes using advanced AI capabilities.")
        st.sidebar.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.sidebar.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.sidebar.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.sidebar.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)



if __name__ == "__main__":
    filname = get_file_name(directory='ResumeData')
    print(filname)