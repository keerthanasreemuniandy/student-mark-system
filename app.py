import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Course: Python Programming")

st.write("Enter data for THREE (3) students only.")

students = []

# Input for 3 students
for i in range(3):

    st.subheader(f"Student {i+1}")

    student_name = st.text_input(
        f"Enter Student Name {i+1}",
        key=f"name{i}"
    )

    gender = st.radio(
        f"Select Gender {i+1}",
        ("Male", "Female"),
        key=f"gender{i}"
    )

    marks = st.number_input(
        f"Enter Marks {i+1}",
        min_value=0,
        max_value=100,
        step=1,
        key=f"marks{i}"
    )

    students.append([student_name, gender, marks])

# Submit button
if st.button("Submit"):

    try:

        # Exception Handling
        for s in students:
            if s[0].strip() == "":
                raise ValueError(
                    "Student name cannot be empty!"
                )

        # Lists
        names = []
        genders = []
        marks_list = []
        results = []
        course = []

        # Process data
        for s in students:

            names.append(s[0])
            genders.append(s[1])
            marks_list.append(s[2])
            course.append("Python Programming")

            # Pass / Fail
            if s[2] >= 50:
                results.append("Pass")
            else:
                results.append("Fail")

        # NumPy Analysis
        marks_array = np.array(marks_list)

        mean_marks = np.mean(marks_array)
        max_marks = np.max(marks_array)

        # Pandas DataFrame
        df = pd.DataFrame({
            "Student Name": names,
            "Gender": genders,
            "Course": course,
            "Marks": marks_list,
            "Result": results
        })

        # Display Student Data
        st.subheader("Student Data")
        st.dataframe(df)

        # Analysis
        st.subheader("Analysis")

        st.write(
            "Mean Marks:",
            round(mean_marks, 2)
        )

        st.write(
            "Maximum Marks:",
            max_marks
        )

        # Sort ascending
        sorted_df = df.sort_values(
            by="Marks",
            ascending=True
        )

        # Display sorted records
        st.subheader("Sorted Student Records")
        st.dataframe(sorted_df)

        # Graph
        st.subheader("Marks Graph")

        fig, ax = plt.subplots()

        ax.bar(names, marks_list)

        ax.set_xlabel("Student Name")
        ax.set_ylabel("Marks")
        ax.set_title("Students Marks")

        st.pyplot(fig)

    except ValueError as e:
        st.error(e)