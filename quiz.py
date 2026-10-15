# 欢迎使用 PythonIDE！如果觉得好用，请给个好评哦～
import streamlit as st
st.title("Year 8 Maths Quiz")
# Question 1
st.write("Question 1: Calculate (-6) × (-8) ÷ 4.")
opt1 = st.radio("Choose your answer:", ["A. -12", "B. 12", "C. -48", "D. 48"], key="q1")
if st.button("Submit Question 1", key="b1"):
    if opt1 == "B. 12":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 12.")
# Question 2
st.write("Question 2: What is the prime factorisation of 60?")
opt2 = st.radio("Choose your answer:", ["A. 2 × 3 × 10", "B. 2² × 3 × 5", "C. 2 × 30", "D. 3² × 5"], key="q2")
if st.button("Submit Question 2", key="b2"):
    if opt2 == "B. 2² × 3 × 5":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 2² × 3 × 5.")
# Question 3
st.write("Question 3: Calculate -14 + 9.")
opt3 = st.radio("Choose your answer:", ["A. -23", "B. 23", "C. -5", "D. 5"], key="q3")
if st.button("Submit Question 3", key="b3"):
    if opt3 == "C. -5":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. -5.")
# Question 4
st.write("Question 4: Round 58,746 to the nearest thousand.")
opt4 = st.radio("Choose your answer:", ["A. 58,000", "B. 58,700", "C. 59,000", "D. 60,000"], key="q4")
if st.button("Submit Question 4", key="b4"):
    if opt4 == "C. 59,000":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 59,000.")
# Question 5
st.write("Question 5: What is 0.006 × 1,000?")
opt5 = st.radio("Choose your answer:", ["A. 0.06", "B. 0.6", "C. 6", "D. 60"], key="q5")
if st.button("Submit Question 5", key="b5"):
    if opt5 == "C. 6":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 6.")
# Question 6
st.write("Question 6: Which is the smallest number?")
opt6 = st.radio("Choose your answer:", ["A. 0.505", "B. 0.55", "C. 0.5005", "D. 0.515"], key="q6")
if st.button("Submit Question 6", key="b6"):
    if opt6 == "C. 0.5005":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 0.5005.")
# Question 7
st.write("Question 7: Calculate 7.35 ÷ 0.1.")
opt7 = st.radio("Choose your answer:", ["A. 0.735", "B. 7.35", "C. 73.5", "D. 735"], key="q7")
if st.button("Submit Question 7", key="b7"):
    if opt7 == "C. 73.5":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 73.5.")
# Question 8
st.write("Question 8: Calculate 3.6 × 0.25.")
opt8 = st.radio("Choose your answer:", ["A. 0.09", "B. 0.9", "C. 9", "D. 1.44"], key="q8")
if st.button("Submit Question 8", key="b8"):
    if opt8 == "B. 0.9":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 0.9.")
# Question 9
st.write("Question 9: Calculate 4.32 ÷ 0.6.")
opt9 = st.radio("Choose your answer:", ["A. 0.72", "B. 7.2", "C. 72", "D. 2.592"], key="q9")
if st.button("Submit Question 9", key="b9"):
    if opt9 == "B. 7.2":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 7.2.")
# Question 10
st.write("Question 10: Calculate 2⅓ - ⅚.")
opt10 = st.radio("Choose your answer:", ["A. 1½", "B. 1⅔", "C. 1⅚", "D. 2⅙"], key="q10")
if st.button("Submit Question 10", key="b10"):
    if opt10 == "A. 1½":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is A. 1½.")
# Question 11
st.write("Question 11: Calculate 3 ÷ ⅖.")
opt11 = st.radio("Choose your answer:", ["A. 1⅕", "B. 1⅗", "C. 6/5", "D. 7½"], key="q11")
if st.button("Submit Question 11", key="b11"):
    if opt11 == "D. 7½":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is D. 7½.")
# Question 12
st.write("Question 12: What is ⅗ of 40?")
opt12 = st.radio("Choose your answer:", ["A. 8", "B. 15", "C. 24", "D. 25"], key="q12")
if st.button("Submit Question 12", key="b12"):
    if opt12 == "C. 24":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 24.")
# Question 13
st.write("Question 13: Calculate ⅔ + ¼.")
opt13 = st.radio("Choose your answer:", ["A. 3/7", "B. 5/7", "C. 11/12", "D. 1"], key="q13")
if st.button("Submit Question 13", key="b13"):
    if opt13 == "C. 11/12":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 11/12.")
# Question 14
st.write("Question 14: What is 15% of 80?")
opt14 = st.radio("Choose your answer:", ["A. 8", "B. 12", "C. 15", "D. 18"], key="q14")
if st.button("Submit Question 14", key="b14"):
    if opt14 == "B. 12":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 12.")
# Question 15
st.write("Question 15: A game costs RM120. It has a 25% discount. What is the sale price?")
opt15 = st.radio("Choose your answer:", ["A. RM30", "B. RM80", "C. RM90", "D. RM95"], key="q15")
if st.button("Submit Question 15", key="b15"):
    if opt15 == "C. RM90":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. RM90.")
# Question 16
st.write("Question 16: A value increases from 50 to 60. What is the percentage increase?")
opt16 = st.radio("Choose your answer:", ["A. 10%", "B. 15%", "C. 20%", "D. 25%"], key="q16")
if st.button("Submit Question 16", key="b16"):
    if opt16 == "C. 20%":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 20%.")
# Question 17
st.write("Question 17: A jacket costs RM200. Its price increases by 10%. What is the new price?")
opt17 = st.radio("Choose your answer:", ["A. RM180", "B. RM190", "C. RM210", "D. RM220"], key="q17")
if st.button("Submit Question 17", key="b17"):
    if opt17 == "D. RM220":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is D. RM220.")
# Question 18
st.write("Question 18: Simplify the ratio 18 : 24.")
opt18 = st.radio("Choose your answer:", ["A. 2 : 3", "B. 3 : 4", "C. 4 : 3", "D. 6 : 8"], key="q18")
if st.button("Submit Question 18", key="b18"):
    if opt18 == "B. 3 : 4":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 3 : 4.")
# Question 19
st.write("Question 19: The ratio of red counters to blue counters is 2 : 3. There are 20 counters altogether. How many are blue?")
opt19 = st.radio("Choose your answer:", ["A. 8", "B. 10", "C. 12", "D. 15"], key="q19")
if st.button("Submit Question 19", key="b19"):
    if opt19 == "C. 12":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 12.")
# Question 20
st.write("Question 20: A recipe uses 4 cups of flour for 6 people. How many cups are needed for 9 people?")
opt20 = st.radio("Choose your answer:", ["A. 5", "B. 6", "C. 8", "D. 9"], key="q20")
if st.button("Submit Question 20", key="b20"):
    if opt20 == "B. 6":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 6.")
# Question 21
st.write("Question 21: Which number is a multiple of both 6 and 8?")
opt21 = st.radio("Choose your answer:", ["A. 18", "B. 24", "C. 30", "D. 36"], key="q21")
if st.button("Submit Question 21", key="b21"):
    if opt21 == "B. 24":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 24.")
# Question 22
st.write("Question 22: Calculate 2.4 + 0.85.")
opt22 = st.radio("Choose your answer:", ["A. 2.485", "B. 3.15", "C. 3.25", "D. 3.85"], key="q22")
if st.button("Submit Question 22", key="b22"):
    if opt22 == "C. 3.25":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. 3.25.")
# Question 23
st.write("Question 23: Write 0.375 as a fraction in its simplest form.")
opt23 = st.radio("Choose your answer:", ["A. 3/8", "B. 3/5", "C. 37/100", "D. 375/100"], key="q23")
if st.button("Submit Question 23", key="b23"):
    if opt23 == "A. 3/8":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is A. 3/8.")
# Question 24
st.write("Question 24: Divide £45 in the ratio 2 : 3. What is the larger share?")
opt24 = st.radio("Choose your answer:", ["A. £18", "B. £20", "C. £27", "D. £30"], key="q24")
if st.button("Submit Question 24", key="b24"):
    if opt24 == "C. £27":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is C. £27.")
# Question 25
st.write("Question 25: A number is multiplied by 5 and the result is 45. What is the number?")
opt25 = st.radio("Choose your answer:", ["A. 5", "B. 9", "C. 40", "D. 50"], key="q25")
if st.button("Submit Question 25", key="b25"):
    if opt25 == "B. 9":
        st.success("Correct! Well done!")
    else:
        st.error("Incorrect. The correct answer is B. 9.")