import streamlit as st
st.title("Hello world")
st.header("Header")
st.subheader("Sub-Header")

st.text("Hello world I m learning streamlit")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag 
:moon:<br>
:sunglasses:<br>
**bold**<br>
_italics_<br>
**_both_**                
~~Strike~~     
""",True)

st.latex(r''' x^2 + y^2 = z^2 ''')
st.write(" # ISHA SHAH")
st.write(sum)

d={
    "Name" : "Isha",
    "language" : "Python"
}
st.write(d)
