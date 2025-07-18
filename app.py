import streamlit as st
from chains.review_chain import review_chain
from chains.improvement_chain import post_improvement_chain
from utils.response_formatter import format_review_for_prompt
from streamlit.components.v1 import html

# ------------------ Page Settings ------------------
st.set_page_config(
    page_title="PostPilot",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        background-color: #f9f9f9;
    }
    .block-container {
        padding: 2rem 1rem 1rem 1rem;
    }
    .stTextInput>div>div>input {
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# ------------------ Title & Instructions ------------------
st.title("🧠 PostPilot")
st.caption("Generate, review, and improve multi-platform posts from a single topic.")

st.markdown("---")
st.subheader("📌 Enter a Topic")
topic = st.text_input("What would you like to post about?", placeholder="e.g., Why AI is essential for developers")

# ------------------ Button and Step-by-step Generation ------------------
if st.button("🚀 Generate Strategy", disabled=not topic.strip()):
    with st.spinner("Generating your AI-powered content strategy..."):

        progress = st.empty()
        progress.info("🔧 Step 1: Generating and reviewing posts...")

        # STEP 1: Generate & Review
        review_result = review_chain.invoke({"topic": topic})

        progress.success("✅ Step 1 Complete: Posts Reviewed")

        # STEP 2: Format Review
        progress.info("📝 Step 2: Preparing improvement prompt...")
        formatted_review = format_review_for_prompt(review_result)
        progress.success("✅ Step 2 Complete: Review ready")

        # STEP 3: Improve Posts
        progress.info("🚀 Step 3: Improving posts based on feedback...")
        final_post = post_improvement_chain.invoke({"formatted_review": formatted_review})
        progress.success("✅ Step 3 Complete: Posts Improved!")

    st.markdown("---")
    st.subheader("📊 Review Summary")
    with st.expander("Click to view full editorial review"):
        st.code(formatted_review, language="text")

    st.markdown("---")
    st.subheader("📢 Improved Platform-Specific Posts")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🐦 Twitter")
        with st.expander("Click to view full Twitter Post"):
            st.success(final_post.twitter_post)

        st.markdown("### 👥 LinkedIn")
        with st.expander("Click to view full Linkedin Post"):
            st.info(final_post.linkedin_post)

    with col2:
        st.markdown("### 📘 Facebook")
        with st.expander("Click to view full Facebook Post"):
            st.warning(final_post.facebook_post)

        st.markdown("### 📝 Blog")
        with st.expander("Click to view full Blog Post"):
            st.markdown(final_post.blog_post)

            copy_code = f"""
            <script>
            function copyToClipboard(text) {{
                navigator.clipboard.writeText(text).then(function() {{
                    alert('✅ Blog post copied to clipboard!');
                }});
            }}
            </script>
            <button onclick="copyToClipboard(`{final_post.blog_post}`)" style="margin-top:10px;">📋 Copy Blog Post</button>
            """
            html(copy_code)
            

    st.markdown("---")
    st.success("🎉 All content is ready to publish!")

# ------------------ Footer ------------------
st.markdown(
    "<hr><center>Made with ❤️ using LangChain + Gemini + Streamlit</center>",
    unsafe_allow_html=True
)
