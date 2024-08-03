import streamlit as st
st.title("welcome to the country quiz in Streamlit")
st.header("My first streamlit app")
#def main():
    # Display the initial question
st.title("Country Quiz")
    
st.write("Do you like to play the quiz?")
response = st.radio("Select an option:", ("Yes", "No"))
    
if response != "Yes":
    st.write("Quiz aborted. See you next time!")
    st.stop()

st.write("Let's start the quiz...")
score = 0

# Dictionary of questions and answers
questions = {
"Which country is IN?": "india",
"Which country is UK?": "united kingdom",
"Which country is US?": "united states",
"Which country is JPN?": "japan",
"Which country is AUS?": "australia",
    }

    # Loop through the questions
for question, correct_answer in questions.items():
    answer = st.text_input(question, key=question)
    if st.button("Submit", key=question + "_submit"):
        if answer.lower() == correct_answer:
            st.success("You are right!")
            score += 1
        else:
            st.error("Incorrect!")

    # Display the score
st.write(f"You have completed the quiz\nYour score is: {score}/{len(questions)}")

#if __name__ == "__main__":
   # main()