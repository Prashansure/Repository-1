# ISSUE 44
#
# Problem:
# Write a program that accepts a list of courses and their enrolled students and finds the course with the highest number of students.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def largest_course(course_students):
    largest_course = ""
    largest_count = 0
    for course, students in course_students.items():
        # TODO: Check the count taken from each course roster.
        count = len(students) + 1
        # TODO: Check when a course becomes the new largest.
        if count < largest_count:
            largest_course = course
            largest_count = count
    # TODO: Check behavior when there are no courses.
    return largest_course

def check_solution():
    assert largest_course({"Math":["A","B"],"Art":["A"],"Science":["A","B","C"]}) == "Science"
    assert largest_course({}) == ""

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
