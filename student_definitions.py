from course_definitions import *


class Student():
    def __init__(self, ID: int, first: str, last: str, grade: int, current_math: Course, recommended_math: Course, requested_math: Course):
        self.ID = ID
        self.first = first
        self.last = last
        self.grade = grade # the grade for the upcoming year
        self.current_math = current_math # the math course the student is currently taking
        self.recommended_math = recommended_math # the math recommendation
        self.requested_math = requested_math # the math class the student selects

    def recommendation_matches_request(self):
        return self.requested_math == self.recommended_math

    def has_taken_math_prerequisite(self):
        if self.requested_math.prerequisite is not None:
            # if the requested_math course is int he math_options, then the student
            # either 1) has the prerequisite or 2) took a course above the prereq
            if (self.requested_math in self.recommended_math.math_options):
                return True
            else:
                return False
        else:
            return True

    def choose_lower_course(self):
        # returns a bool True if the student's requested_math is lower
        # than the student's recommended_math course
        n = len(self.recommended_math.math_options) - 1
        if self.recommended_math.math_options.index(self.requested_math) != n:
            return True
        else:
            return False
