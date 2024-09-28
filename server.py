import streamlit as st
import util
import base64

st.title("Celebrity Face Recognition App")
st.write("Hello World")
img = st.file_uploader("Please upload an Image file", type=["jpg", "png"])
if img:
    img_data = img.getvalue()
    print(img_data)
    b64 = base64.b64encode(img_data).decode("utf-8")
    class_data = util.classify_image(b64)
    if len(class_data) == 0:
        st.write("Not recognised")
    else:
        for i in class_data:
            st.metric(
                value=" ".join(i["class"].split("_")).title(), label="Celebrity Name:"
            )
            st.image(img_data)
