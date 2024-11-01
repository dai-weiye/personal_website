import streamlit as st

# 设置页面标题和布局
st.set_page_config(page_title="个人网页 - 吉他改编教学与乐理分享", layout="centered")

# 自定义页面样式，包含音乐元素和渐变背景
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #c2e9fb, #a1c4fd);
            font-family: Arial, sans-serif;
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
            font-size: 2.5em;
            margin-bottom: 0.2em;
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
    </style>
    """, unsafe_allow_html=True
)

# 页面头部信息，加入音乐图标
st.markdown('<div class="header"><h1>🎶 欢迎来到我的个人音乐天地 🎶</h1><p>吉他改编教学 | 乐理知识分享 | 即兴实战</p></div>', unsafe_allow_html=True)

# 我的作品展示部分，带有音乐图标
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎸 我的作品")
st.markdown('<div class="music-icon">🎵</div>', unsafe_allow_html=True)

# 视频展示
st.subheader("APT.")
st.video(r"D:\个人文件\music_video\WeChat_20241101195742.mp4")  # 请确认路径正确

# 教学文档展示
st.markdown('</div>', unsafe_allow_html=True)

# 教学内容简介，加入乐谱符号图标
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎼 吉他教学与乐理分享")
st.markdown('<div class="music-icon">🎶</div>', unsafe_allow_html=True)
st.write(
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
