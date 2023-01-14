import pyshorteners
import streamlit as st

s = pyshorteners.Shortener()
long_url = st.text_input("Input link")
if long_url:
    short_url = s.tinyurl.short(long_url)
    st.success(f"Short link : {short_url}")

st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
