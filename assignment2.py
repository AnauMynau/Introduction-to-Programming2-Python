courses = {
 "CS101": ("Intro to Computer Science", "Dr. Smith", 30, set()),
 "MATH203": ("Calculus II", "Dr. Johnson", 25, set()),
 "PHY150": ("General Physics", "Dr. Clark", 20, set()),
 "ENG102": ("English Composition", "Dr. Taylor", 40, set()),
 "BIO110": ("Introduction to Biology", "Dr. Lee", 35, set())
}

registered_courses = set()

while True:
    print("""Welcome to the Course Registration System!
            1. View all courses
            2. Register for a course
            3. Drop a course
            4. View my courses
            5. Exit
""")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        print("Thank you for using the Course Registration System! Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")
    
    if choice == "1":
        for code, (title, instructure, capacity, enrolled_students) in courses.items():
            input(f"Course Code: {code}")
            print(f"Course Title: {title}")
            print(f"Instructor: {instructure}")
            print(f"Capacity: {capacity}")
            print(f"Enrolled: {len(enrolled_students)}")
            print()
            
    elif choice == "2":
        course_code = input("Enter the course code: ").upper()
        if course_code in courses:
            title, instructure, capacity, enrolled_students = courses[course_code]
            if len(enrolled_students) < capacity:
                if course_code not in registered_courses:
                    enrolled_students.add("student")
                    registered_courses.add(course_code)
                    print(f"Successfully rigistered for {title}.")
                else:
                    print("You are alresdy registered for this course.")
            else:
                print("Course is full.")
        else:
            print("Invalid course code.")
    
    elif choice == "3":
        course_code = input("Enter the course code: ").upper()
        if course_code in registered_courses:
            courses[course_code][3].remove("student")
            registered_courses.remove(course_code)
            print(f"Successfully dropped {course_code}.")
        else:
            print("You are not registered for this course.")
            
    
    elif choice == "4": 
        if not registered_courses:
            print("You are not registered for any courses.")
        else:
            print("You are registered for the following courses:")
            for course_code in registered_courses:
                title = courses[course_code][0]
                print(f"{course_code} - {title}")
        
        
        