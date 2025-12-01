import streamlit as sl

sl.markdown("<h1 style = 'text-align: center;'><b style='color: White;'>Finance.Ai</b></h1><hr>", unsafe_allow_html=True)
sl.sidebar.markdown("<h2 style='color: White;'><b>Finance.Ai</b></h2>",unsafe_allow_html=True)
sl.sidebar.markdown("<h4 style='color: White;'> New Chat</h4>",unsafe_allow_html=True)

with sl.sidebar.expander("About"):
    sl.markdown("This is a simple AI app that can help you with your finance related queries.", unsafe_allow_html=True)
    # sl.markdown("## Contact")
    # sl.markdown("If you have any questions, feel free to reach out to me at [your email address].")

sl.sidebar.markdown("<hr>This is a simple AI app that can help you with your finance related queries.", unsafe_allow_html=True)
sl.sidebar.markdown("## Contact")
sl.sidebar.markdown("If you have any questions, feel free to reach out to me at [your email address].")
sl.markdown("<br><br><br>",unsafe_allow_html=True)
sl.markdown("<h3 style = 'text-align: center;'><b>Ask Your Questions</b></h3>", unsafe_allow_html=True)
sl.markdown("<input type='text' placeholder='Enter Your Question' style='width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 10px;'>", unsafe_allow_html=True)

# sl.text("I hope you like it")
# df = pd.DataFrame()

# sl.map(df)

sl.markdown("<br><button style = 'display: block; margin: 0 auto;'>Search</button>", unsafe_allow_html=True)
