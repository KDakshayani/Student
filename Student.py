import sys
def get_student_details(name, usn, college, email,city):
    return {
        "name": name,
        "usn": usn,
        "college": college,
        "email":email,
        "city": city
    }


if __name__ == "__main__":
    name=sys.argv[1]
    usn=sys.argv[2]
    college=sys.argv[3]
    email=sys.argv[4]
    city=sys.argv[5]

    student = get_student_details(name, usn, college, city,email)

    print("\n--- Student Details ---")
    print("Name:", name)
    print("USN:", usn)
    print("College:", college)
    print("Email:",email)
    print("City:", city)
