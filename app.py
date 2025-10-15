import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI setup
st.set_page_config(page_title="AI Fashion Design Studio", page_icon="👗", layout="wide")

st.title("👗 AI Fashion Design Studio")
st.markdown("### Generate AI-powered fashion designs instantly!")
st.write("Describe your outfit idea (e.g. *A futuristic evening gown made of silver silk with neon patterns*).")

# User input
prompt = st.text_area("🎨 Enter your fashion design idea:", height=100, placeholder="Example: A summer floral dress inspired by Indian traditional motifs")

# Button to generate
if st.button("Generate Fashion Design"):
    if prompt.strip() == "":
        st.warning("Please enter a design idea first!")
    else:
        with st.spinner("Creating your AI fashion design..."):
            try:
                # Generate image using DALL·E
                result = client.images.generate(
                    model="gpt-image-1",
                    prompt=prompt,
                    size="1024x1024"
                )

                image_url = result.data[0].url
                st.image(image_url, caption="Your AI Fashion Design", use_container_width=True)
                st.success("✨ Design generated successfully!")

            except Exception as e:
                st.error(f"Error generating design: {e}")

# Footer
st.markdown("---")
st.markdown("💡 *Powered by OpenAI & Streamlit | Created for AI Fashion Enthusiasts*")
streamlit 