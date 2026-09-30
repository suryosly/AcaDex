# print("__________________________________________________")
# print("..................................................")
# print("             Welcome to AcaDex!")
# print(" This is a simple academic management system.")
# print("__________________________________________________")

# print("=>1. Subjects")
# print("=>2. Attendance")
# print("=>3. Assignments")
# #print("4. Tasks")
# print("=>4. Dashboard")
# print("=>5. Exit")
# print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")

subjectlist =[]


def subjects():
    while True:
        print("-------------------------------")
        print("Subjects Menu")
        print("->1. Add Subject")
        print("->2. View Subjects")
        print("->3. Back to Main Menu")
        print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            subject_name = input("Enter subject name: ")
            subjectlist.append(subject_name)
            print(f"Subject '{subject_name}' added successfully.")
        elif choice == "2":
            if len(subjectlist) == 0:
                print("No subjects found.")
            else:
                print("Subjects:")
                print(subjectlist)

        elif choice == "3":
            return
        else:
            print("invalid choice, try again!")
        
    

attendance_data = {}
def attendance():
    while True:
        print("\n================================")
        print("          Attendance")
        print("================================")
        print("1. Add/Update Attendance")
        print("2. View Attendance")
        print("3. Back")
        print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            if len(subjectlist) == 0:
                print("\nPlease add subjects first.")
                continue

            print("\nYour Subjects:")
            number = 1
            for subject in subjectlist:
                print(f"{number}. {subject}")
                number += 1

            number = int(input("\nSelect a subject: "))

            if 1 <= number <= len(subjectlist):
                subject = subjectlist[number - 1]

                attended = int(input("Classes attended: "))
                total = int(input("Total classes: "))

                if attended > total:
                    print("Classes attended cannot be greater than total classes.")
                elif total <= 0:
                    print("Total classes must be greater than zero.")
                else:
                    attendance_data[subject] = {
                        "attended": attended,
                        "total": total
                    }

                    print(f"Attendance for {subject} updated.")
            else:
                print("Invalid subject number.")

        elif choice == "2":
            if len(attendance_data) == 0:
                print("\nNo attendance records yet.")
            else:
                print("\nYour Attendance:")

                for subject, data in attendance_data.items():
                    percentage = (data["attended"] / data["total"]) * 100

                    print(
                        f"{subject}: "
                        f"{data['attended']}/{data['total']} "
                        f"({percentage:.2f}%)"
                    )

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

assignment_data = []
def assignments():
    
    while True:
        print("\n================================")
        print("         Assignments")
        print("================================")
        print("1. Add Assignment")
        print("2. View Assignments")
        print("3. Mark as Completed")
        print("4. Back")
        print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter assignment name: ")
            subject = input("Enter subject: ")
            due_date = input("Enter due date (DD-MM-YYYY): ")

            assignment = {
                "name": name,
                "subject": subject,
                "due_date": due_date,
                "completed": False
            }

            assignment_data.append(assignment)

            print("\nAssignment added successfully.")

        elif choice == "2":
            if len(assignment_data) == 0:
                print("\nNo assignments added yet.")

            else:
                print("\nYour Assignments:")

                number = 1

                for assignment in assignment_data:
                    if assignment["completed"]:
                        status = "Completed"
                    else:
                        status = "Pending"

                    print(f"\n{number}. {assignment['name']}")
                    print(f"   Subject: {assignment['subject']}")
                    print(f"   Due: {assignment['due_date']}")
                    print(f"   Status: {status}")

                    number += 1

        elif choice == "3":
            if len(assignment_data) == 0:
                print("\nNo assignments available.")

            else:
                print("\nYour Assignments:")

                number = 1

                for assignment in assignment_data:
                    print(f"{number}. {assignment['name']}")
                    number += 1

                selected = int(input("\nEnter assignment number: "))

                if 1 <= selected <= len(assignment_data):
                    assignment_data[selected - 1]["completed"] = True
                    print("\nAssignment marked as completed.")

                else:
                    print("Invalid assignment number.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
    
def dashboard():
    
    print("\n================================")
    print("           Dashboard")
    print("================================")

    print(f"\nTotal Subjects: {len(subjectlist)}")

    if len(attendance_data) == 0:
        print("Attendance: No records yet")
    else:
        total_attended = 0
        total_classes = 0

        for subject in attendance_data:
            attended = int(attendance_data[subject]["attended"])
            total = int(attendance_data[subject]["total"])

            total_attended += attended
            total_classes += total

        overall_percentage = (total_attended / total_classes) * 100

        print(f"Overall Attendance: {overall_percentage:.2f}%")

    pending = 0
    completed = 0

    for assignment in assignment_data:
        if assignment["completed"]:
            completed += 1
        else:
            pending += 1

    print(f"Assignments Pending: {pending}")
    print(f"Assignments Completed: {completed}")
    input("\nPress Enter to return to the main menu...")


while True:
    print("__________________________________________________")
    print("..................................................")
    print("             Welcome to AcaDex!")
    print(" This is a simple academic management system.")
    print("__________________________________________________")

    print("=>1. Subjects")
    print("=>2. Attendance")
    print("=>3. Assignments")
    #print("4. Tasks")
    print("=>4. Dashboard")
    print("=>5. Exit")
    print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^")

    choice = input("Please select an option (1-5): ")
    if choice == "1":
        subjects()
    elif choice == "2":
        attendance()
    elif choice == "3":
        assignments()
    elif choice == "4":
        dashboard()
    elif choice == "5":
        print("Exiting AcaDex. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
        input("\nPress Enter to return to the main menu...")
        
    


