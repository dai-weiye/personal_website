import streamlit as st
import os

# Set page title and layout
st.set_page_config(page_title="个人网页 - 吉他改编教学与乐理分享", layout="centered")

# Enhanced styles with neon background and floating music notes
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

        /* Floating music notes across the screen */
        .music-note {
            position: fixed;
            font-size: 1.8em;
            color: rgba(255, 255, 255, 0.6);
            animation: floatNote 8s infinite linear;
        }

        /* Floating music note animation */
        @keyframes floatNote {
            0% { transform: translateY(0) translateX(0); }
            100% { transform: translateY(-100vh) translateX(10vw); }
        }

        /* Place music notes in different locations with unique delays */
        .note1 { top: 90vh; left: 5vw; animation-delay: 0s; }
        .note2 { top: 85vh; left: 15vw; animation-delay: 1s; }
        .note3 { top: 95vh; left: 25vw; animation-delay: 2s; }
        .note4 { top: 88vh; left: 35vw; animation-delay: 3s; }
        .note5 { top: 93vh; left: 45vw; animation-delay: 4s; }
        .note6 { top: 87vh; left: 55vw; animation-delay: 5s; }
        .note7 { top: 92vh; left: 65vw; animation-delay: 6s; }
        .note8 { top: 89vh; left: 75vw; animation-delay: 7s; }
        .note9 { top: 94vh; left: 85vw; animation-delay: 8s; }
        .note10 { top: 91vh; left: 95vw; animation-delay: 9s; }

        /* Glowing text effects */
        .header h1, .section h1, .section h2 {
            color: #FFFFFF;
            text-shadow: 0 0 10px #70a1ff, 0 0 20px #70a1ff;
            font-family: 'Courier New', Courier, monospace;
        }

        /* Glowing sections */
        .section {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 15px rgba(112, 161, 255, 0.8);
            margin-bottom: 20px;
            text-align: center;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            border: 1px solid rgba(255, 255, 255, 0.3);
            animation: fadeIn 1.5s ease forwards;
        }

        /* Fade-in effect for sections */
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        /* Floating music icon effect */
        .music-icon {
            font-size: 1.5em;
            color: #70a1ff;
            animation: float 3s ease-in-out infinite;
        }

        /* Floating icon animation */
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

# Adding floating music notes across the page
st.markdown(
    """
    <div class="music-note note1">🎶</div>
    <div class="music-note note2">🎵</div>
    <div class="music-note note3">🎶</div>
    <div class="music-note note4">🎵</div>
    <div class="music-note note5">🎶</div>
    <div class="music-note note6">🎵</div>
    <div class="music-note note7">🎶</div>
    <div class="music-note note8">🎵</div>
    <div class="music-note note9">🎶</div>
    <div class="music-note note10">🎵</div>
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
