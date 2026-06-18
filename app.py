import streamlit as st
from src.pipeline.pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

.main-title{
    text-align:center;
    font-size:52px;
    font-weight:700;
}

.sub-title{
    text-align:center;
    color:#9ca3af;
    margin-bottom:2rem;
}

.stButton > button{
    width:100%;
    height:3rem;
    border-radius:12px;
    font-weight:600;
}

.agent-card{
    background-color:#111827;
    padding:15px;
    border-radius:15px;
    text-align:center;
    border:1px solid #374151;
}

.report-container{
    background-color:#111827;
    padding:25px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Header ---------------- #
st.markdown(
"""
<div class='main-title'>
🔬 Multi-Agent Research System
</div>

<div class='sub-title'>
Search • Read • Analyze • Critique
</div>
""",
unsafe_allow_html=True
)

st.divider()

# ---------------- Input ---------------- #
topic = st.text_input(
    "Research Topic",
    placeholder="Example: Latest developments in AI"
)

run = st.button("🚀 Start Research")

if run and topic:

    progress_bar = st.progress(0)
    status = st.empty()

    # Search
    status.info("🔍 Search Agent")
    progress_bar.progress(25)

    result = run_research_pipeline(topic)

    # Since pipeline already runs everything,
    # we just animate status updates.
    status.info("📖 Reader Agent")
    progress_bar.progress(50)

    status.info("✍ Writer Agent")
    progress_bar.progress(75)

    status.info("🧐 Critic Agent")
    progress_bar.progress(100)

    status.success("Research Completed")

    st.divider()

    # ---------- Agent Status ----------
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric("🔍 Search Agent","✓")

    with col2:
        st.metric("📖 Reader Agent","✓")

    with col3:
        st.metric("✍ Writer Agent","✓")

    with col4:
        st.metric("🧐 Critic Agent","✓")

    st.divider()

    # ---------- Main Report ----------
    st.subheader("📑 Final Research Report")

    with st.container(border=True):
        st.markdown(result["report"])

    st.download_button(
        "📥 Download Report",
        result["report"],
        file_name="research_report.md"
    )

    st.divider()

    # ---------- Tabs ----------
    tab1, tab2, tab3 = st.tabs(
        [
            "🌐 Search Results",
            "📚 Extracted Content",
            "🧐 Critique"
        ]
    )

    with tab1:

        st.subheader("Search Results")

        with st.expander("View Raw Search Output"):
            st.code(result["search_results"])

    with tab2:

        st.subheader("Scraped Content")

        with st.expander("View Extracted Content"):
            st.write(result["scraped_content"])

    with tab3:

        st.subheader("Evaluation")

        st.markdown(result["Evaluation"])

# ---------- Sidebar ----------
with st.sidebar:

    st.title("⚙ Pipeline")

    st.success("🔍 Search Agent")

    st.success("📖 Reader Agent")

    st.success("✍ Writer Agent")

    st.success("🧐 Critic Agent")

    st.divider()

    st.caption(
        """
Built with

• LangChain

• Groq

• Tavily

• Streamlit
"""
    )