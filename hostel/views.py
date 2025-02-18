from django.shortcuts import render, redirect


def start(request):
    error = None
    if request.method == 'POST':
        hostel_name = request.POST.get('hostel_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate password and confirm password
        if password != confirm_password:
            error = "Passwords do not match!"
        else:
            # Save hostel name and password in the session
            request.session['hostel_name'] = hostel_name
            request.session['password'] = password
            return redirect('home')  # Redirect to home page

    return render(request, 'hostel/start.html', {'error': error})

def home(request):
    hostel_name = request.session.get('hostel_name', 'Guest')  # Default to 'Guest' if not set
    return render(request, 'hostel/home.html', {'hostel_name': hostel_name})

def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'Admin' and password == '123456':
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        else:
            error = "Incorrect Username and Password"
    return render(request, 'hostel/admin_login.html', {'error': error})

def admin_dashboard(request):
    return render(request, 'hostel/admin_dashboard.html')

def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')  # Get the username (hostel name)
        password = request.POST.get('password')

        # Validate username and password
        if username == request.session.get('hostel_name') and password == request.session.get('password'):
            return redirect('user_dashboard')  # Redirect to user dashboard
        else:
            error = "Incorrect Username or Password"
    return render(request, 'hostel/user_login.html', {'error': error})

def add_person(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        dob = request.POST.get('dob')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')
        work_place_college = request.POST.get('work_place_college')  # Change key to match others
        gender = request.POST.get('gender')
        room_no = request.POST.get('room_no')

        # Check if the room exists in rooms.txt
        room_exists = False
        try:
            with open("rooms.txt", "r") as file:
                for line in file:
                    if f"Room No.: {room_no}" in line:
                        room_exists = True
                        break
        except FileNotFoundError:
            pass

        if not room_exists:
            # If the room does not exist, return an error message
            return render(request, 'hostel/add_person.html', {'error': 'Room does not exist!'})

        # Save to persons.txt if the room exists
        with open("persons.txt", "a") as file:
            file.write(f"First Name: {first_name}, Last Name: {last_name}, Father Name: {father_name}, Mother Name: {mother_name}, DOB: {dob}, Contact: {contact}, Email: {email}, Address: {address}, Work Place/College: {work_place_college}, Gender: {gender}, Room No.: {room_no}\n")

        return redirect('admin_dashboard')  # Redirect to admin dashboard after saving
    return render(request, 'hostel/add_person.html')

def add_room(request):
    if request.method == 'POST':
        room_no = request.POST.get('room_no')
        no_of_beds = request.POST.get('no_of_beds')

        # Check if the room already exists (dummy check for demonstration)
        rooms = ["101", "102"]  # Replace with actual room data from the database or file
        if room_no in rooms:
            return render(request, 'hostel/add_room.html', {'error': 'Room already exists!'})

        # Save to a text file (for demonstration)
        with open("rooms.txt", "a") as file:
            file.write(f"Room No.: {room_no}, Number of Beds: {no_of_beds}\n")

        return render(request, 'hostel/add_room.html', {'success': 'Room added successfully!'})
    return render(request, 'hostel/add_room.html')

def checkin(request):
    if request.method == 'POST':
        name = request.POST.get('checkin_name')
        room_no = request.POST.get('checkin_room_no')
        time = request.POST.get('checkin_time')

        # Save CheckIn data to a text file
        with open("checkin_checkout.txt", "a") as file:
            file.write(f"Type: CheckIn, Name: {name}, Room No.: {room_no}, Time: {time}\n")

        return redirect('checkin_checkout')
    return redirect('checkin_checkout')

def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('checkout_name')
        room_no = request.POST.get('checkout_room_no')
        purpose = request.POST.get('checkout_purpose')
        time = request.POST.get('checkout_time')

        # Save CheckOut data to a text file
        with open("checkin_checkout.txt", "a") as file:
            file.write(f"Type: CheckOut, Name: {name}, Room No.: {room_no}, Purpose: {purpose}, Time: {time}\n")

        return redirect('checkin_checkout')
    return redirect('checkin_checkout')

def checkin_checkout(request):
    records = []
    try:
        with open("checkin_checkout.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                record = {}
                for part in parts:
                    key, value = part.split(": ")
                    record[key.lower()] = value
                records.append(record)
    except FileNotFoundError:
        pass

    return render(request, 'hostel/checkin_checkout.html', {'records': records})

def visitor_info(request):
    if request.method == 'POST':
        visitor_name = request.POST.get('visitor_name')
        contact_no = request.POST.get('contact_no')
        reason = request.POST.get('reason')
        address = request.POST.get('address')
        person_name = request.POST.get('person_name')
        room_no = request.POST.get('room_no')

        # Debug: Print the received data
        print(f"Visitor Name: {visitor_name}, Contact No.: {contact_no}, Reason: {reason}, Address: {address}, Person Name: {person_name}, Room No.: {room_no}")

        # Save visitor data to a text file
        try:
            with open("visitors.txt", "a") as file:
                file.write(f"Visitor Name: {visitor_name}, Contact No.: {contact_no}, Reason: {reason}, Address: {address}, Person Name: {person_name}, Room No.: {room_no}\n")
            print("Data saved to visitors.txt")  # Debug: Confirm data is saved
        except Exception as e:
            print(f"Error saving data: {e}")  # Debug: Log any errors

        return render(request, 'hostel/visitor_info.html', {'success': True})
    return render(request, 'hostel/visitor_info.html')

def view_info(request):
    # Read data from text files
    with open("persons.txt", "r") as file:
        persons = file.readlines()
    with open("rooms.txt", "r") as file:
        rooms = file.readlines()
    return render(request, 'hostel/view_info.html', {'persons': persons, 'rooms': rooms})

def all_persons_info(request):
    persons = []
    try:
        # Read saved data from the file
        with open("persons.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                person = {}
                for part in parts:
                    if ": " in part:  # Ensure the part contains the expected separator
                        key, value = part.split(": ")
                        # Normalize the key to match the expected format
                        key = key.lower().replace(" ", "_")
                        person[key] = value

                # Map the keys to match the template's expected keys
                person["name"] = f"{person.get('first_name', '')} {person.get('last_name', '')}".strip()
                person["contact"] = person.get("contact", "")
                person["room_no"] = person.get("room_no.", "")  # Ensure this matches the key in the file
                person["work_place_college"] = person.get("work_place/college", "")  # Ensure this matches the key in the file

                persons.append(person)
    except FileNotFoundError:
        print("File 'persons.txt' not found.")

    return render(request, 'hostel/all_persons_info.html', {'persons': persons})

def room_info(request):
    room_no = request.GET.get('room_no')
    room_details = []

    if room_no:
        try:
            # Read saved data from the file
            with open("persons.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    person = {}
                    for part in parts:
                        if ": " in part:  # Ensure the part contains the expected separator
                            key, value = part.split(": ")
                            key = key.lower().replace(" ", "_")  # Normalize the key
                            person[key] = value

                    # Debug: Print the person dictionary
                    print("Person:", person)

                    # Filter by room number (case-insensitive)
                    if 'room_no.' in person and person['room_no.'].strip().lower() == room_no.strip().lower():
                        # Map the keys to match the template's expected keys
                        mapped_person = {
                            "name": f"{person.get('first_name', '')} {person.get('last_name', '')}".strip(),
                            "contact": person.get("contact", ""),
                            "work_place_college": person.get("work_place/college", ""),
                            "room_no": person.get("room_no.", "")
                        }
                        room_details.append(mapped_person)
                    else:
                        print("Room No. not found in person:", person)  # Debug: Log missing room_no
        except FileNotFoundError:
            print("File 'persons.txt' not found.")  # Debug: Log file not found error

    # Debug: Print the room details
    print("Room Details:", room_details)

    return render(request, 'hostel/room_info.html', {'room_no': room_no, 'room_details': room_details})

def leave_application(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room_no = request.POST.get('room_no')
        contact_no = request.POST.get('contact_no')
        reason = request.POST.get('reason')
        return_date = request.POST.get('return_date')

        # Save leave application data to a text file
        with open("leave_applications.txt", "a") as file:
            file.write(f"Name: {name}, Room No.: {room_no}, Contact No.: {contact_no}, Reason: {reason}, Return Date: {return_date}\n")

        return redirect('admin_dashboard')  # Redirect to admin dashboard after saving
    return render(request, 'hostel/leave_application.html')

def fee_detail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room_no = request.POST.get('room_no')
        month = request.POST.get('month')
        fee_status = request.POST.get('fee_status')

        # Debug: Print the received data
        print(f"Name: {name}, Room No.: {room_no}, Month: {month}, Fee Status: {fee_status}")

        # Save fee detail data to a text file
        try:
            with open("fee_details.txt", "a") as file:
                file.write(f"Name: {name}, Room No.: {room_no}, Month: {month}, Fee Status: {fee_status}\n")
            print("Data saved to fee_details.txt")  # Debug: Confirm data is saved
        except Exception as e:
            print(f"Error saving data: {e}")  # Debug: Log any errors

        return redirect('admin_dashboard')  # Redirect to admin dashboard after saving
    return render(request, 'hostel/fee_detail.html')

def admin_feedback(request):
    feedback_data = []
    try:
        # Read feedback data from the file
        with open("feedback.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                feedback_entry = {}
                for part in parts:
                    if ": " in part:  # Ensure the part contains the expected separator
                        key, value = part.split(": ")
                        key = key.lower().strip()  # Normalize the key
                        if key == "room no" or key == "room no.":  # Handle variations
                            key = "room_no"
                        feedback_entry[key] = value
                feedback_data.append(feedback_entry)
                print("Parsed Feedback Entry:", feedback_entry)  # Debug: Print parsed data
    except FileNotFoundError:
        print("File 'feedback.txt' not found.")  # Debug: Log file not found error

    return render(request, 'hostel/admin_feedback.html', {'feedback_data': feedback_data})

def user_dashboard(request):
    return render(request, 'hostel/user_dashboard.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room_no = request.POST.get('room_no')
        feedback_text = request.POST.get('feedback')

        # Save feedback data to a text file
        with open("feedback.txt", "a") as file:
            file.write(f"Name: {name}, Room No.: {room_no}, Feedback: {feedback_text}\n")

        return redirect('user_dashboard')  # Redirect to user dashboard after saving
    return render(request, 'hostel/feedback.html')

def logout(request):
    # Redirect to the home page after logout
    return redirect('home')