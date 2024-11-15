import streamlit as st
from PIL import Image

 # Define the home page content
def home_page():
    image = Image.open(r'C:\Users\nanay\Desktop\tc.png')
    st.image(image)

    st.title("Embedded a ML model in GUI's --Used Streamlit")

    st.markdown("""
    This app uses machine learning to classify whether a customer is likely to be churned or not.
    """)

    st.subheader("Instructions")
    st.markdown("""
    - Upload a CSV file
    - Select the features for classification
    - Choose a machine learning model from the dropdown
    - Click on 'Classify' to get the predicted results
    - The app gives you a report on the performance of the model
    - Expect it to give metrics like f1 score, recall, precision, and accuracy
    """)

    st.header("App Features")
    st.markdown("""
    - **Data View**: Access the customer data.
    - **Predict View**: Shows the various models & predictions you will make.
    - **Dashboard**: Shows data visualizations for insights.
    """)

    st.subheader("User Benefits")
    st.markdown("""
    - **Data Driven Decisions**: You make an informed decision backed by data.
    - **Access Machine Learning**: Utilize machine learning algorithms.
    """)

    st.write("#### How to Run the application")
    with st.container(border=True):
        st.code("""
        # Activate the virtual environment
        env/scripts/activate
                
        # Run the App
        streamlit run p.py
                """)

    # Adding the embedded link
    # st.video("https://www.youtube.com/watch?v=fMM54UG4a8A&list=PPSV", autoplay=True)

    # Adding a clickable link
    st.markdown("[Watch a Demo](https://www.youtube.com/watch?v=fMM54UG4a8A&list=PPSV)")

    #st.divider()
    st.write("+++" * 15)

    st.write("Need Help?")
    st.write("Contact me on:")

    # Add an image
    # st.image(r"C:\Users\nanay\Desktop\Screenshot 2024-10-24 133032.png")
    st.markdown("[Visit LinkedIn Profile](https://www.linkedin.com/in/portiabentum/)")

# Display the home page
if __name__ == "__main__":
    home_page()