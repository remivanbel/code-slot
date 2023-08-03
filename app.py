import streamlit as st
import random
import string
import numpy as np
from matplotlib import pyplot as plt
from numpy import sin, cos, pi, linspace
random.seed(42)

def deg2rad(deg):
    return deg * pi / 180

st.title('cos + + - - +')
st.title('sin - + - + +')

your_angles = [0,0,0,0,0]
cosinus = [0, 0, 0, 0, 0]
sinus = [0, 0, 0, 0, 0]

check = [1, 1, -1, -1, 1]
check_sinus = [-1, 1, -1, 1, 1]

for i, col in enumerate(st.columns(5)):
    with col:
        plt.figure(i)
        plt.plot(0,0, color = 'red', marker = 'o')
        #draw circle
        r = 1
        angles = linspace(0 * pi, 2 * pi, 100) 
        xs = cos(angles)
        ys = sin(angles)
        plt.plot(xs, ys, color = 'green')

        plt.xlim(-r, r)
        plt.ylim(-r, r)
        plt.gca().set_aspect('equal')

        your_angles[i] = st.slider('How many degrees?',0, 360, 30, step=30, key=i)
        angle = your_angles[i]
        x = cos(deg2rad(angle))
        y = sin(deg2rad(angle))
        plt.plot([0, x], [0, y], color = "red")
        cosinus[i] = x
        sinus[i] = y
        st.pyplot(plt.gcf())

if np.all(np.sign(cosinus) == np.sign(check)) and np.all(np.all(np.sign(sinus) == np.sign(check_sinus))):

    #st.components.v1.iframe('https://www.geogebra.org/geometry/qukckzbk', height=800)
    st.write('[help](https://www.geogebra.org/geometry/qukckzbk)')
    # can be adapted
    nb_columns = 4
    nb_rows = 6

    # should be adapted
    correct_answers = ['Wp', 'Am', 'Kq','Jf','Bu']

    # add random elements to list 
    answers = list(correct_answers)
    while len(answers) < nb_columns*nb_rows:
        random_answer = random.choice(string.ascii_uppercase) + random.choice(string.digits)   
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

    boxes_ok = all(correct_boxes) and not any(wrong_boxes)
    degrees_ok = np.all(np.sign(cosinus) == np.sign(check))

    # check if all the correct boxes, and none of the wrong boxes are checked
    if boxes_ok and degrees_ok:
        st.balloons()
        st.title(':tada: Proficiat :tada:')