import streamlit as st
import os

def app():
    st.title("Taxonomy: 'Early Turn'")

    why_selection = st.selectbox(
        'Please select which "WHY" examples you would like to see:',
        ('Oncoming Lane', 'Towards Kerb')
    )

    video_folder = "media/early_turn"

    if why_selection == 'Oncoming Lane':
        video_dir = os.path.join(video_folder, 'oncoming_lane')

    elif why_selection == 'Towards Kerb':
        video_dir = os.path.join(video_folder, 'towards_kerb')

    # Get all video files in the selected directory
    video_files = os.listdir(video_dir)
    video_files = [os.path.join(video_dir, f) for f in video_files]

    if video_files:
        # Display each video in the directory
        for video_path in video_files:
            st.video(video_path)
    else:
        st.warning("No videos found in the selected directory.")
