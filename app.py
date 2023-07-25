import streamlit as st
import random
import string

random.seed(42)

nb_columns = 4
nb_rows = 4

correct_answers = ['A9b', 'C3f', 'K2z','R8q','T3m']

# add random elements to list 
answers = list(correct_answers)
while len(answers) < nb_columns*nb_rows:
    random_answer = random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.ascii_lowercase)    
    answers.append( random_answer )

random.shuffle(answers)

cols = st.columns(nb_columns)

correct_boxes = list()
wrong_boxes = list()

for col in cols:
    with col:
        for i in range(nb_rows):
            answer = answers.pop()
            box = st.checkbox(answer)
            if answer in correct_answers:
                correct_boxes.append(box)
            else:
                wrong_boxes.append(box)

if all(correct_boxes) and not any(wrong_boxes):
    st.balloons()