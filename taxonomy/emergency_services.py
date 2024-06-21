import streamlit as st
import os

def app():
    st.title("Taxonomy: 'Emergency Services'")

    # Video folder path
    video_folder = "media/emergency_services"

    # Get the list of folder names in video_folder
    folder_names = [name for name in os.listdir(video_folder) if os.path.isdir(os.path.join(video_folder, name))]

    # Display a select box for choosing the folder
    why_selection = st.selectbox(
        'Please select which "WHY" examples you would like to see:',
        folder_names
    )
    st.markdown("---")


    # Construct the directory path based on the selected option
    video_dir = os.path.join(video_folder, why_selection)

    # Get all video files in the selected directory
    video_files = os.listdir(video_dir)
    video_files = [os.path.join(video_dir, f) for f in video_files]

    if video_files:
        # Display each video in the directory
        for video_path in video_files:
            st.video(video_path)
    else:
        st.warning("No videos found in the selected directory.")

