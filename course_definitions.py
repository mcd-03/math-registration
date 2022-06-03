class Course():
    def __init__(self, name: str, description=None, math_options=None, prequisite=None):
        self.name = name
        self.description = description
        self.math_options = math_options
        self.prequisite = prequisite

    def __repr__(self):
        return self.name


# instantiate Courses
Math_6 = Course("Math 6")
Math_6_H = Course("Math 6 Honors")
Math_6_AH = Course("Math 6 Accelerated Honors")

Math_7 = Course("Math 7")
Math_7_H = Course("Math 7 Honors")
Math_7_AH = Course("Math 7 Accelerated Honors", prequisite=Math_6_H)
Math_1_7th = Course("Math 1", prequisite=Math_6_AH)

Math_8 = Course("Math 8")
Math_1 = Course("Math 1")
Math_1_2 = Course("Math 1/2", prequisite=Math_7_AH)
Math_2_3 = Course("Math 2/3", prequisite=Math_1_7th)

# define math_options
Math_6.math_options = [Math_6, Math_6_H]
Math_6_H.math_options = [Math_6, Math_6_H]

Math_7.math_options = [Math_7, Math_7_H]
Math_7_H.math_options = [Math_7, Math_7_H]
Math_7_AH.math_options = [Math_7, Math_7_H, Math_7_AH]
Math_1_7th.math_options = [Math_7, Math_7_H, Math_7_AH, Math_1_7th]

Math_8.math_options = [Math_8, Math_1]
Math_1.math_options = [Math_8, Math_1]
Math_1_2.math_options = [Math_8, Math_1, Math_1_2]
Math_2_3.math_options = [Math_8, Math_1, Math_1_2, Math_2_3]

# todo add descriptions for each math class