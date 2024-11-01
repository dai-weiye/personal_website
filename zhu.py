import streamlit as st
import os

# 设置页面标题和布局
st.set_page_config(page_title="个人网页 - 吉他改编教学与乐理分享", layout="centered")

# 自定义页面样式，包含更华丽的背景和字体
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Noto+Sans+SC:wght@400;700&display=swap');

        body {
            background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            font-family: 'Noto Sans SC', sans-serif;
            overflow: hidden; /* 防止出现滚动条 */
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .header, .footer {
            background-color: rgba(112, 161, 255, 0.8);
            color: white;
            padding: 20px;
            text-align: center;
            font-family: 'Great Vibes', cursive;
        }

        .section {
            background: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.2);
            margin-bottom: 30px;
            text-align: center;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .section:hover {
            transform: scale(1.03);
            box-shadow: 0px 12px 40px rgba(0, 0, 0, 0.3);
        }

        h1 {
            font-size: 4em;
            margin-bottom: 0.2em;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        h2 {
            font-family: 'Great Vibes', cursive;
            color: #70a1ff;
            font-size: 2.5em;
        }

        .music-icon {
            font-size: 2em;
            color: #3867d6;
            margin-bottom: 20px;
        }

        .content-text {
            color: #555;
            font-size: 1.3em;
            line-height: 1.8em;
        }

        .footer-text {
            font-size: 1.2em;
            color: #ffffff;
            font-family: 'Noto Sans SC', sans-serif;
        }

        /* 添加动态音符的样式 */
        .music-note {
            position: absolute;
            bottom: -50px;
            font-size: 25px;
            color: rgba(255, 255, 255, 0.8);
            animation: floatUp 10s infinite;
            opacity: 0;
        }

        @keyframes floatUp {
            0% {
                transform: translateY(0);
                opacity: 0;
            }
            50% {
                opacity: 1;
            }
            100% {
                transform: translateY(-110vh);
                opacity: 0;
            }
        }

        /* 创建多个音符，使用不同的动画延迟、位置和大小 */
        .music-note:nth-child(1) {
            left: 10%;
            animation-delay: 0s;
            font-size: 25px;
        }
        .music-note:nth-child(2) {
            left: 20%;
            animation-delay: 2s;
            font-size: 30px;
        }
        .music-note:nth-child(3) {
            left: 30%;
            animation-delay: 4s;
            font-size: 20px;
        }
        .music-note:nth-child(4) {
            left: 40%;
            animation-delay: 1s;
            font-size: 35px;
        }
        .music-note:nth-child(5) {
            left: 50%;
            animation-delay: 3s;
            font-size: 22px;
        }
        .music-note:nth-child(6) {
            left: 60%;
            animation-delay: 5s;
            font-size: 28px;
        }
        .music-note:nth-child(7) {
            left: 70%;
            animation-delay: 4s;
            font-size: 32px;
        }
        .music-note:nth-child(8) {
            left: 80%;
            animation-delay: 6s;
            font-size: 24px;
        }
        .music-note:nth-child(9) {
            left: 90%;
            animation-delay: 2s;
            font-size: 29px;
        }
        .music-note:nth-child(10) {
            left: 95%;
            animation-delay: 8s;
            font-size: 26px;
        }

        /* 视频花边样式 */
        .video-container {
            position: relative;
            display: inline-block;
            margin-bottom: 30px;
        }

        .video-frame {
            border: 10px solid transparent;
            padding: 10px;
            border-image-source: url('https://i.imgur.com/your_border_image.png'); /* 替换为您的花边图片URL */
            border-image-slice: 30;
            border-image-repeat: round;
        }
    </style>
    """, unsafe_allow_html=True
)

# 添加动态音符的HTML代码
st.markdown(
    """
    <div class="music-note">🎵</div>
    <div class="music-note">🎶</div>
    <div class="music-note">🎵</div>
    <div class="music-note">🎶</div>
    <div class="music-note">🎵</div>
    <div class="music-note">🎶</div>
    <div class="music-note">🎵</div>
    <div class="music-note">🎶</div>
    <div class="music-note">🎵</div>
    <div class="music-note">🎶</div>
    """, unsafe_allow_html=True
)

# 页面头部信息，加入音乐图标
st.markdown('<div class="header"><h1>🎶 欢迎来到我的个人音乐网站 🎶</h1><p style="font-family: \'Noto Sans SC\', sans-serif; font-size: 1.5em;">吉他改编教学 | 乐理知识分享 | 即兴实战</p></div>', unsafe_allow_html=True)

# 我的作品展示部分，带有音乐图标
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎸 我的作品")
st.markdown('<div class="music-icon">🎵</div>', unsafe_allow_html=True)

# 视频展示
def display_video(title, video_file):
    st.subheader(title)
    video_bytes = open(video_file, 'rb').read()
    st.markdown(
        f"""
        <div class="video-container">
            <div class="video-frame">
                <video controls width="700">
                    <source src="data:video/mp4;base64,{video_bytes.decode('utf-8')}" type="video/mp4">
                </video>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

display_video("APT.", "WeChat_20241101195742.mp4")
display_video("穿越时空的思念", "cyskdsn.mp4")
display_video("春泥", "cn.mp4")

# 结束作品展示部分
st.markdown('</div>', unsafe_allow_html=True)

# 教学内容简介，加入乐谱符号图标
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

# 页面底部联系方式，带有音乐符号
st.markdown('<div class="footer"><p class="footer-text">微信: D3300741176 🎶 期待与你的交流！</p></div>', unsafe_allow_html=True)
