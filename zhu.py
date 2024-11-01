import streamlit as st

# 设置页面标题和布局
st.set_page_config(page_title="个人网页 - 吉他改编教学与乐理分享", layout="centered")

# 添加标题和描述
st.markdown(
    """
    <style>
        .header, .footer {
            background-color: #86c1b9;
            color: white;
            padding: 20px;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        .section {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            text-align: center;
        }
        h2 {
            color: #86c1b9;
        }
    </style>
    """, unsafe_allow_html=True
)

# 页面头部信息
st.markdown('<div class="header"><h1>欢迎来到我的个人网页</h1><p>吉他改编教学 | 乐理知识分享 | 即兴实战</p></div>', unsafe_allow_html=True)

# 我的作品展示
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎸 我的作品")

# 视频展示
st.subheader("APT.")
st.video("D:\个人文件\music_video\WeChat_20241101195742.mp4")
  # 这里替换为视频文件路径

# 教学文档展示

st.markdown('</div>', unsafe_allow_html=True)

# 教学内容简介
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("🎼 吉他教学与乐理分享")
st.write(
    """
    在这里，我会分享吉他改编的技巧、基础乐理知识以及即兴演奏的实战经验，帮助你更深入理解音乐创作。
    """
)
st.markdown('</div>', unsafe_allow_html=True)

# 页面底部联系方式
st.markdown('<div class="footer"><p>微信: D3300741176</p></div>', unsafe_allow_html=True)
