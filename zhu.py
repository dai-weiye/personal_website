import streamlit as st
import os

# Set page title and layout
st.set_page_config(page_title="个人网页 - 吉他改编教学与乐理分享", layout="centered")

# Enhanced styles with a starry, animated background
st.markdown(
    """
    <style>
        /* Multi-layered animated starry sky */
        body {
            background: radial-gradient(circle at bottom, #1b2735, #090a0f);
            font-family: Arial, sans-serif;
            overflow-x: hidden;
            color: #FFFFFF;
        }

        /* Add star layers */
        .stars, .stars2, .stars3 {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            background-repeat: repeat;
            background-size: cover;
            opacity: 0.6;
        }
        .stars {
            background-image: url('https://www.transparenttextures.com/patterns/stardust.png');
            animation: moveStars 200s linear infinite;
        }
        .stars2 {
            background-image: url('https://www.transparenttextures.com/patterns/stardust.png');
            animation: moveStars 150s linear infinite;
            opacity: 0.4;
        }
        .stars3 {
            background-image: url('https://www.transparenttextures.com/patterns/stardust.png');
            animation: moveStars 100s linear infinite;
            opacity: 0.2;
        }

        /* Star animations for parallax effect */
        @keyframes moveStars {
            from { transform: translateY(0); }
            to { transform: translateY(-1000px); }
        }

        /* Pulsing header */
        .header h1 {
            font-family: 'Courier New', Courier, monospace;
            font-size: 2em;
            color: #70a1ff;
            margin-bottom: 0.2em;
            animation: pulse 2s infinite;
        }

        /* Pulse effect */
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        /* Section styling with glow effect */
        .section {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
            text-align: center;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: fadeIn 1.5s ease forwards;
        }

        /* Section glow */
        .section:hover {
            border-color: #70a1ff;
            box-shadow: 0 0 20px rgba(112, 161, 255, 0.8);
        }

        /* Fade-in effect for sections */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Music icon floating effect */
        .music-icon {
            font-size: 1.5em;
            color: #70a1ff;
            animation: float 3s ease-in-out infinite;
        }

        /* Floating music icon animation */
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        /* Content text styling */
        .content-text {
            color: #FFFFFF;
            font-size: 1.1em;
        }

        /* Footer text styling */
        .footer-text {
            font-size: 0.9em;
            color: #ffffff;
        }
    </style>
    """, unsafe_allow_html=True
)

# Adding star layers for parallax background
st.markdown(
    """
    <div class="stars"></div>
    <div class="stars2"></div>
    <div class="stars3"></div>
    """, unsafe_allow_html=True
)

# Header section with pulsing effect
st.markdown('<div class="header"><h1>🎶 欢迎来到我的个人音乐网站 🎶</h1><p>吉他改编教学 | 乐理知识分享 | 即兴实战</p></div>', unsafe_allow_html=True)

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
