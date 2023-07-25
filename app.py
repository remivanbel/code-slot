import streamlit as st
import random
import string

random.seed(42)

# can be adapted
nb_columns = 4
nb_rows = 6

# should be adapted
correct_answers = ['A9b', 'C3f', 'K2z','R8q','T3m']

# add random elements to list 
answers = list(correct_answers)
while len(answers) < nb_columns*nb_rows:
    random_answer = random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.ascii_lowercase)    
    if random_answer not in answers:
        answers.append(random_answer)

#shuffle answers to make it less obvious
random.shuffle(answers)

#greate streamlit app
cols = st.columns(nb_columns)

# keep list of which boxes are from correct answers and which from wrong
# you will need this later for checking
correct_boxes = list()
wrong_boxes = list()

# fill grid, keep track of correct_boxes and wrong_boxes
for col in cols:
    with col:
        for i in range(nb_rows):

            # create box with possible answer
            answer = answers.pop()
            box = st.checkbox(answer)
            
            # keep track if the answer is correct or wrong
            if answer in correct_answers:
                correct_boxes.append(box)
            else:
                wrong_boxes.append(box)

# check if all the correct boxes, and none of the wrong boxes are checked
if all(correct_boxes) and not any(wrong_boxes):
    st.balloons()