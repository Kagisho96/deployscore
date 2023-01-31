import streamlit as st
import pandas as pd

# number = st.number_input('GPA')


# Mathematics = st.number_input('Mathematics')
# Biology = st.number_input('Biology')
# Physics = st.number_input('Physics')
# Chemistry = st.number_input('Chemistry')
# Communication = st.number_input('Communication - English')
# Programming = st.number_input('Programming')

# marks = [Mathematics, Biology, Physics, Chemistry, 
# Communication, Programming]
# student = { 
#         "code" : ['MA8001', 'B5001', 'PY909', 'CH002', 'CE922', 'CS9005'],
#         "Module" : ['Mathematics', 'Biology', 'Physics', 'Chemistry', 'Communication - English', 'Programming'],
#         "Credit Value(cv)" : [120, 120, 130, 110, 90, 120],
#         "Final Mark(fm)" : marks}

stu_A = { 
        "code" : ['MA8001', 'B5001', 'PY909', 'CH002', 'CE922', 'CS9005'],
        "Module" : ['Mathematics', 'Biology', 'Physics', 'Chemistry', 'Communication - English', 'Programming'],
        "Credit Value(cv)" : [120, 120, 130, 110, 90, 120],
        "Final Mark(fm)" : [60, 74, 54, 80, 62, 45],
    }

stu_B = { 
        "code" : ['MA8001', 'B5001', 'PY909', 'CH002', 'CE922', 'CS9005'],
        "Module" : ['Mathematics', 'Biology', 'Physics', 'Chemistry', 'Communication - English', 'Programming'],
        "Credit Value(cv)" : [120, 120, 130, 110, 90, 120],
        "Final Mark(fm)" : [78, 54, 84, 70, 72, 60],
    }

stu_C = { 
        "code" : ['MA8001', 'B5001', 'PY909', 'CH002', 'CE922', 'CS9005'],
        "Module" : ['Mathematics', 'Biology', 'Physics', 'Chemistry', 'Communication - English', 'Programming'],
        "Credit Value(cv)" : [120, 120, 130, 110, 90, 120],
        "Final Mark(fm)" : [66, 54, 50, 60, 70, 49],
    }

Student_A = pd.DataFrame(stu_A)
Student_B = pd.DataFrame(stu_B)
Student_C = pd.DataFrame(stu_C)



def cumulative_pass_score(x):
    
    x['cv*fm'] = x['Final Mark(fm)']*x['Credit Value(cv)']/sum(x['Credit Value(cv)'])
    
    x['Cumulative pass score'] = sum(x['cv*fm'])

    
    CPS =  list(x['Cumulative pass score'])[1]
    return x, CPS

Student_A, A_CPS = cumulative_pass_score(Student_A)
Student_B, B_CPS = cumulative_pass_score(Student_B)
Student_C, C_CPS = cumulative_pass_score(Student_C)


def gpa(x):
    
    if x['Cumulative pass score']> 80 and x['Cumulative pass score']<100:
        return 4.0
    if x['Cumulative pass score']> 60 and x['Cumulative pass score']<79:
        return 3.0
    if x['Cumulative pass score']> 50 and x['Cumulative pass score']<59:
        return 2.0
    if x['Cumulative pass score']> 40 and x['Cumulative pass score']<49:
        return 1.0
    
    else:
        return 0.0
    


    

def stream(x):


    
    Mathematics_ = 90
    Physics_ = 80
    
    if x['gpa']>= 2.8:

        return "Faculty of Science"
    if x['gpa']== 2.5:
        return "Arts department"
    if x['gpa'] >=3.5 and x['gpa']<=4.0:
        return "Actuarial science"
    if  x['gpa'] ==2.9 and Mathematics_ >=80 and Physics_ >=80:
        return "Actuarial science"
    if x['gpa']>=2.0 and x['gpa']<=3.0 or Mathematics_>=80:
        return "Economics"

    else:
        return 0.0






Student_A['gpa'] = Student_A.apply(gpa, axis = 1)
A_GPA = list(Student_A['gpa'])[0]
Student_B['gpa'] = Student_B.apply(gpa, axis = 1)
B_GPA = list(Student_B['gpa'])[0]
Student_C['gpa'] = Student_C.apply(gpa, axis = 1)
C_GPA = list(Student_C['gpa'])[0]
# yield


st.subheader('Student A')
st.dataframe(Student_A)
cumulative_pass_score(Student_A)
st.write('Cumulative pass score is ', A_CPS)
st.write('GPA ', A_GPA)
Mathematics_ = Student_A['Final Mark(fm)'][0]
Physics_ = Student_A['Final Mark(fm)'][2]
Student_A['course_qualify'] = Student_A.apply(stream, axis = 1)
st.write('Qualify for: ', Student_A['course_qualify'][0])




st.subheader('Student B')
st.dataframe(Student_B)
cumulative_pass_score(Student_B)
st.write('Cumulative pass score is ', B_CPS)
st.write('GPA ', B_GPA)
Mathematics_ = Student_B['Final Mark(fm)'][0]
Physics_ = Student_B['Final Mark(fm)'][2]

Student_B['course_qualify'] = Student_B.apply(stream, axis = 1)
st.write('Qualify for: ', Student_B['course_qualify'][0])






st.subheader('Student C')
st.dataframe(Student_C)

cumulative_pass_score(Student_C)
#  GPA 
st.write('Cumulative pass score is ', C_CPS)
st.write('GPA ', C_GPA)
Mathematics_ = Student_C['Final Mark(fm)'][0]
Physics_ = Student_C['Final Mark(fm)'][2]
Student_C['course_qualify'] = Student_C.apply(stream, axis = 1)
st.write('Qualify for: ', Student_C['course_qualify'][0])


