import streamlit as st
import streamlit.components.v1 as components
import os

# 设置页面标题和布局
st.set_page_config(page_title="个人网页 - 吉他改编教学与乐理分享", layout="centered")

# 自定义页面样式，包含音乐元素和渐变背景
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #c2e9fb, #a1c4fd);
            font-family: Arial, sans-serif;
            overflow: hidden; /* 防止出现滚动条 */
        }
        .header, .footer {
            background-color: #70a1ff;
            color: white;
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
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
        h1, h2 {
            font-family: 'Courier New', Courier, monospace;
            color: #3867d6;
        }
        h1 {
            font-size: 2em; /* 将字体大小从2.5em调小到2em */
            margin-bottom: 0.2em;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }
        h2 {
            color: #70a1ff;
        }
        .music-icon {
            font-size: 1.5em;
            color: #3867d6;
        }
        .content-text {
            color: #555;
            font-size: 1.1em;
        }
        .footer-text {
            font-size: 0.9em;
            color: #ffffff;
        }
        /* 添加动态音符的样式 */
        .music-note {
            position: absolute;
            bottom: -50px;
            font-size: 30px;
            color: #ffffff;
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
        /* 创建多个音符，使用不同的动画延迟和位置 */
        .music-note:nth-child(1) {
            left: 10%;
            animation-delay: 0s;
        }
        .music-note:nth-child(2) {
            left: 30%;
            animation-delay: 2s;
        }
        .music-note:nth-child(3) {
            left: 50%;
            animation-delay: 4s;
        }
        .music-note:nth-child(4) {
            left: 70%;
            animation-delay: 6s;
        }
        .music-note:nth-child(5) {
            left: 90%;
            animation-delay: 8s;
        }
        /* 视频花边样式 */
        .video-container {
            position: relative;
            display: inline-block;
            margin-bottom: 30px;
        }

        .video-frame {
            border: 15px solid transparent;
            padding: 10px;
            border-image-source: url('https://i.imgur.com/FKJ1KcA.png'); /* 请替换为您的花边图片URL */
            border-image-slice: 30;
            border-image-repeat: round;
            border-image-width: 15px;
            display: inline-block;
        }

        .video-frame video {
            width: 100%;
            height: auto;
        }

        /* 调整视频容器的宽度以适应页面 */
        @media (max-width: 820px) {
            .video-frame video {
                width: 100%;
            }
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
    """, unsafe_allow_html=True
)

# 页面头部信息，加入音乐图标
st.markdown('<div class="header"><h1>🎶 欢迎来到我的个人音乐网站 🎶</h1><p>吉他改编教学 | 乐理知识分享 | 即兴实战</p></div>', unsafe_allow_html=True)

# 我的作品展示部分，带有音乐图标
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎸 我的作品")
st.markdown('<div class="music-icon">🎵</div>', unsafe_allow_html=True)

# 视频展示函数，包含互斥播放功能
def display_video(title, video_file, video_id):
    """
    显示视频，并确保播放一个视频时暂停其他视频。

    参数:
    - title: 视频标题
    - video_file: 视频文件路径或URL
    - video_id: 视频的唯一ID
    """
    # 构建视频HTML
    video_html = f"""
    <div class="video-container">
        <div class="video-frame">
            <video id="{video_id}" controls width="700">
                <source src="{video_file}" type="video/mp4">
                您的浏览器不支持视频标签。
            </video>
        </div>
    </div>
    <script>
        const currentVideo = document.getElementById("{video_id}");
        const videos = document.querySelectorAll('video');
        currentVideo.addEventListener('play', () => {{
            videos.forEach(video => {{
                if (video !== currentVideo) {{
                    video.pause();
                }}
            }});
        }});
    </script>
    """
    # 使用components.html嵌入视频
    components.html(video_html, height=450, scrolling=True)

# 请确保视频文件位于应用程序运行的目录中，或者提供正确的路径或URL
display_video("APT.", "WeChat_20241101195742.mp4", "video1")
display_video("穿越时空的思念", "cyskdsn.mp4", "video2")
display_video("春泥", "cn.mp4", "video3")
display_video("海阔天空", "hktk.mp4", "video4")  # 新增视频

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
