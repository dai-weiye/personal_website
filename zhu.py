import streamlit as st
import os

# Set page title and layout
st.set_page_config(page_title="个人网页 - 吉他改编教学与乐理分享", layout="centered")

# Enhanced styles with neon background and styled video thumbnails
st.markdown(
    """
    <style>
        /* Animated neon gradient background */
        body {
            background: linear-gradient(135deg, #2a2a72, #009ffd, #2a2a72, #004e92);
            background-size: 400% 400%;
            animation: neonBackground 10s infinite alternate;
            font-family: Arial, sans-serif;
            overflow-x: hidden;
            color: #FFFFFF;
        }

        /* Neon gradient animation */
        @keyframes neonBackground {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }

        /* Video thumbnails styling */
        .video-thumbnail {
            position: relative;
            width: 100%;
            max-width: 250px;
            margin: 10px;
            border-radius: 10px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .video-thumbnail:hover {
            transform: scale(1.05);
            box-shadow: 0px 4px 15px rgba(112, 161, 255, 0.8);
        }
        .video-overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2em;
            font-weight: bold;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .video-thumbnail:hover .video-overlay {
            opacity: 1;
        }

        /* Thumbnail container */
        .video-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }

        /* Modal for video playback */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            color: white;
        }
        .modal-content {
            position: relative;
            max-width: 800px;
            width: 100%;
            padding: 20px;
            background-color: #1b1b32;
            border-radius: 8px;
        }
        .close-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            color: white;
            font-size: 1.5em;
            cursor: pointer;
        }
    </style>
    """, unsafe_allow_html=True
)

# JavaScript for modal functionality
st.markdown(
    """
    <script>
        function openModal(videoSrc) {
            var modal = document.getElementById("videoModal");
            var video = document.getElementById("modalVideo");
            video.src = videoSrc;
            modal.style.display = "flex";
        }

        function closeModal() {
            var modal = document.getElementById("videoModal");
            var video = document.getElementById("modalVideo");
            video.src = "";
            modal.style.display = "none";
        }
    </script>
    """, unsafe_allow_html=True
)

# Display video thumbnails
st.markdown('<div class="video-container">', unsafe_allow_html=True)

# Video thumbnails with overlay titles
videos = {
    "APT.": "WeChat_20241101195742.mp4",
    "穿越时空的思念": "cyskdsn.mp4",
    "春泥": "cn.mp4",
    "海阔天空": "hktk.mp4"
}

for title, src in videos.items():
    st.markdown(
        f"""
        <div class="video-thumbnail" onclick="openModal('{src}')">
            <img src="https://via.placeholder.com/250x150.png?text=Thumbnail" alt="{title}" width="100%">
            <div class="video-overlay">{title}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# Modal HTML structure for video playback
st.markdown(
    """
    <div id="videoModal" class="modal" onclick="closeModal()">
        <div class="modal-content">
            <span class="close-btn" onclick="closeModal()">×</span>
            <video id="modalVideo" controls autoplay style="width: 100%; border-radius: 8px;"></video>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Rest of the page content (e.g., teaching section)
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎼 吉他教学与乐理分享")
st.markdown('<div class="music-icon">🎶</div>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="content-text">
    在这里，我会分享吉他改编的技巧、基础乐理知识以及即兴演奏的实战经验，帮助你更深入理解音乐创作。
    无论你是初学者还是进阶者，我的教程会帮助你在音乐的世界中找到自信与乐趣。
    </p>
    """, unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# Footer with contact info
st.markdown('<div class="footer"><p class="footer-text">微信: D3300741176 🎶 期待与你的交流！</p></div>', unsafe_allow_html=True)
