import streamlit as st

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    return output_text

# ----- Streamlit UI -----

st.title("🔐 Caesar Cipher Web App")
st.markdown("Encrypt or decrypt messages using a simple Caesar shift cipher.")

mode = st.radio("Choose mode:", ["encode", "decode"])
text = st.text_area("Enter your message:", height=150)
shift = st.slider("Choose shift amount:", 1, 25, 3)

if st.button("Run Cipher"):
    result = caesar(original_text=text.lower(), shift_amount=shift, encode_or_decode=mode)
    st.success(f"Result ({mode}d): {result}")
