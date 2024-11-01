import streamlit as st
import os

# Set page title and layout
st.set_page_config(page_title="个人网页 - 吉他改编教学与乐理分享", layout="centered")

# Custom styles with dynamic background and adjusted title font size
st.markdown(
    """
    <style>
        /* Animated gradient background */
        body {
            background: linear-gradient(90deg, #c2e9fb, #a1c4fd, #c2e9fb);
            background-size: 200% 200%;
            animation: gradientBackground 15s ease infinite;
            font-family: Arial, sans-serif;
        }

        /* Gradient animation */
        @keyframes gradientBackground {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Header and footer styling */
        .header, .footer {
            background-color: #70a1ff;
            color: white;
            padding: 20px;
            text-align: center;
        }

        /* Section styling */
        .section {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            text-align: center;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Adjusted title font size */
        h1 {
            font-family: 'Courier New', Courier, monospace;
            font-size: 2em;
            color: #3867d6;
            margin-bottom: 0.2em;
        }

        h2 {
            color: #70a1ff;
        }

        /* Music icon styling */
        .music-icon {
            font-size: 1.5em;
            color: #3867d6;
        }

        /* Content text styling */
        .content-text {
            color: #555;
            font-size: 1.1em;
        }

        /* Footer text styling */
        .footer-text {
            font-size: 0.9em;
            color: #ffffff;
        }

        /* Animated floating music notes */
        .music-note {
            position: absolute;
            bottom: -50px;
            font-size: 30px;
            color: #ffffff;
            animation: floatUp 10s infinite;
            opacity: 0;
        }

        @keyframes floatUp {
            0% { transform: translateY(0); opacity: 0; }
            50% { opacity: 1; }
            100% { transform: translateY(-110vh); opacity: 0; }
        }

        /* Different music notes positions and delays */
        .music-note:nth-child(1) { left: 10%; animation-delay: 0s; }
        .music-note:nth-child(2) { left: 30%; animation-delay: 2s; }
        .music-note:nth-child(3) { left: 50%; animation-delay: 4s; }
        .music-note:nth-child(4) { left: 70%; animation-delay: 6s; }
        .music-note:nth-child(5) { left: 90%; animation-delay: 8s; }
    </style>
    """, unsafe_allow_html=True
)

# Adding floating music notes
st.markdown(
    """
    <div class="music-note">🎵</div>
    <div class="music-note">🎶</div>
    <div class="music-note">🎵</div>
    <div class="music-note">🎶</div>
    <div class="music-note">🎵</div>
    """, unsafe_allow_html=True
)

# Header section with adjusted title font size
st.markdown('<div class="header"><h1>欢迎来到我的个人音乐网站</h1><p>吉他改编教学 | 乐理知识分享 | 即兴实战</p></div>', unsafe_allow_html=True)

# Video selection interface
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎸 我的作品")
st.markdown('<div class="music-icon">🎵</div>', unsafe_allow_html=True)

# List of videos
videos = {
    "APT.": "WeChat_20241101195742.mp4",
    "穿越时空的思念": "cyskdsn.mp4",
    "春泥": "cn.mp4",
    "海阔天空": "hktk.mp4"
}

# Dropdown for video selection
selected_video = st.selectbox("选择一个视频播放：", options=list(videos.keys()))

# Display the selected video
st.video(videos[selected_video])

st.markdown('</div>', unsafe_allow_html=True)

# Teaching content section
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
