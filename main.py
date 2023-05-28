from terminaltables import AsciiTable
project_name = "CWA Calculator"
underline = "========================================================="

def add_marks():
    number_of_courses = int(input("Enter number of courses done: "))
    print("Enter credit hour of each course and marks obtained.")
    print(underline)
    total_marks = []
    total_credit = []
    table_data = []
    for i in range(number_of_courses):
        credit_hour = int(input("Enter credit hour for course #{}: ".format(i+1)))
        marks_obtained = float(input("Enter marks obtained: "))
        if marks_obtained >= 70:
            print("Grade: A")
        elif marks_obtained >= 60:
            print("Grade: B")
        elif marks_obtained >= 50:
            print("Grade: C")
        elif marks_obtained >= 40:
            print("Grade: D")
        else:
            print("Grade: F")
        print(underline)
        total_marks.append(marks_obtained*credit_hour)
        total_credit.append(credit_hour)
        data = []
        data.append(credit_hour)
        data.append(marks_obtained)
        table_data.append(data)
    table = AsciiTable([["Credit Hours","Marks"],*table_data])
    print(table.table)
    sem_average = sum(total_marks)/sum(total_credit)
    print("Semester weighted marks: ",sum(total_marks))
    print("Semester calculated credit: ",sum(total_credit))
    print("Semester average: ",sem_average)
    print(underline)
    previous_total_marks = float(input("Enter cumulative weighted  marks: "))
    previous_total_credit = int(input("Enter cumulative calculated credit: "))
    cumulative_average = (sum(total_marks) + previous_total_marks)/(sum(total_credit) + previous_total_credit)
    print("Cumulative Weighted Average(CWA): ",cumulative_average)
    print(underline)

def main():
    print(project_name)
    print(underline)
    add_marks()

if __name__ == "__main__":
    main()

