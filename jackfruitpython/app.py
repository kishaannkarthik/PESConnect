
import customtkinter as ctk 
import csv 
import os
from datetime import datetime
from other import other
from backend import backend 
from passw import passw as pw

class app:
    global ch
    ch =" "
    root = ctk.CTk()
    def login():
        found = False
        user = username_entry.get().strip()
        pwd = password_entry.get().strip()
        if not os.path.exists("users.csv"):
            with open("users.csv", "w", newline='') as f:
                pass
        with open("users.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) >= 2:
                    new = pw.decode(row[1].strip())
                    if row[0].strip() == user and new == pwd: 
                        global user_1
                        user_1 = user
                        other.cache(user_1)  # Populate cache after login
                        found = True
                        if len(row) == 2:
                            app.root.destroy()
                            app.cgui()
                        else:
                            app.root.destroy()
                            app.main()
                        break
            if found == False:
                popup = ctk.CTkToplevel()
                popup.geometry("300x100")
                ctk.CTkLabel(popup, text="Do you want to signup").pack(pady=20)
                button_yes = ctk.CTkButton(popup, text="Yes", command=lambda: [app.signup(user,pwd), popup.destroy()])
                button_yes.pack(side="left", padx=20)
                button_no = ctk.CTkButton(popup, text="No", command=lambda: [popup.destroy(), app.root.destroy()])
                button_no.pack(side="right", padx=20)
    def login_gui():
        app.root.title("Login/SignUp")
        app.root.geometry("400x300")
        global username_entry, password_entry
        ctk.CTkLabel(app.root, text="Username:").pack(pady=10)
        username_entry = ctk.CTkEntry(app.root)
        username_entry.pack(pady=10)
        ctk.CTkLabel(app.root, text="Password:").pack(pady=10)
        password_entry = ctk.CTkEntry(app.root, show="*")
        password_entry.pack(pady=10)
        login_button = ctk.CTkButton(app.root, text="Login", command=app.login)
        login_button.pack(pady=20)
        app.root.mainloop()
    def signup(user, pwd):
        print("in signup")
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            pwd = pw.encode(pwd)
            writer.writerow([user,pwd])
            popup = ctk.CTkToplevel()
            popup.geometry("200x100")
            ctk.CTkLabel(popup, text="Signup Successful").pack(pady=20)
            ok_button = ctk.CTkButton(popup, text="OK", command=lambda: [popup.destroy(), app.root.destroy(), app.cgui()])
            ok_button.pack(pady=10)
            global user_1
            user_1 = user 
    def create_profile(user):
        found = False
        rows = []
        with open("users.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 0 and row[0].strip() == user:
                    found = True
                    row.append(ch)
                if row:  # Only append non-empty rows
                    rows.append(row)
        if found:
            with open("users.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
    def select_course(choice):
        global ch
        if choice != "None":
            ch += '#'+ choice
    def cgui():
        global ch
        ch = "0"  # Reset ch for new profile creation
        app.root = ctk.CTk()
        app.root.title("Create Profile")
        app.root.geometry("600x800")
        ctk.CTkLabel(app.root, text="Select Your Destination station:").pack(pady=(20))
        ctk.CTkComboBox(app.root, values=["None","Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya",
         "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Kuvempu Road",
         "Srirampura", "Mantri Square Sampige Road","Chickpet",    "Krishna Rajendra Market",    "National College",    "Lalbagh Botanical Garden",
         "South End Circle",    "Jayanagar",    "R.V. Road",    "Banashankari",    "Rashtreeya Vidyalaya Road",  
         "J.P. Nagar",    "Yelachenahalli","Konanakunte Cross","Doddakallasandra","Silk Institute","Whitefield (Kadugodi)", "Hopefarm Channasandra", "Kadugodi Tree Park", "Pattanduru Agrahara",
          "Sri Sathya Sai Hospital", "Nallurhalli", "Kundalahalli", "Seetharamapalya", "Hoodi",
         "Garudacharpalya", "Mahadevapura", "K.R. Puram", "Benniganahalli", "Baiyappanahalli",
         "Swami Vivekananda Road", "Indiranagar", "Halasuru", "Trinity", "M.G. Road", "Cubbon Park",
          "Vidhana Soudha", "Sir M. Visvesvaraya Station", "Nadaprabhu Kempegowda Station (Majestic)",
          "City Railway Station", "Magadi Road", "Hosahalli", "Vijayanagar", "Attiguppe",
          "Deepanjali Nagar","Nayandahalli", "Rajarajeshwari Nagar", "Jnanabharathi",
          "Pattanagere", "Kengeri", "Kengeri Bus Terminal", "Challaghatta"], command=app.select_course).pack(pady=(20))
        ctk.CTkLabel(app.root, text="Select Your Sports Interest:").pack(pady=(20))
        ctk.CTkCheckBox(app.root, text="Basketball", command=lambda: app.select_course("Basketball")).pack(pady=(20))
        ctk.CTkCheckBox(app.root, text="Batminton", command=lambda: app.select_course("Batminton")).pack(pady=(20))
        ctk.CTkCheckBox(app.root, text="Squash", command=lambda: app.select_course("Squash")).pack(pady=(20))
        ctk.CTkCheckBox(app.root, text="Gym", command=lambda: app.select_course("Gym")).pack(pady=(20))
        ctk.CTkCheckBox(app.root, text="Volleyball", command=lambda: app.select_course("Volleyball")).pack(pady=(20))
        ctk.CTkCheckBox(app.root, text="Table Tennis", command=lambda: app.select_course("Table Tennis")).pack(pady=(20))
        ctk.CTkCheckBox(app.root, text="Kabaddi", command=lambda: app.select_course("Kabaddi")).pack(pady=(20))
        ctk.CTkLabel(app.root, text="Select Your Course:").pack(pady=(20))
        ctk.CTkSegmentedButton(app.root, values=["ECE","CSE","MECH","CIVIL","BBA","MBA","MCA","LAW","DESIGN","BCA"], command=app.select_course).pack(pady=(20))
        ctk.CTkButton(app.root, text="Submit", command=lambda:[app.root.destroy(), app.create_profile(user_1),app.main(),other.cache(user_1)]).pack(pady=(20))
        app.root.mainloop()
    def main(): 
        app.mainroot = ctk.CTk()
        app.mainroot.title("Main Dashboard")
        app.mainroot.geometry("500x400")
        app.show_main_dashboard()
        app.mainroot.mainloop()
    def show_main_dashboard():
        # Clear all widgets from mainroot
        for widget in app.mainroot.winfo_children():
            widget.destroy()
        
        app.mainroot.title("Main Dashboard")
        app.mainroot.geometry("500x400")
        
        # Welcome label
        welcome_text = f"Welcome, {user_1}!"
        ctk.CTkLabel(app.mainroot, text=welcome_text, font=("Arial", 24, "bold")).pack(pady=30)
        
        # Main options label
        ctk.CTkLabel(app.mainroot, text="What would you like to do?", font=("Arial", 16)).pack(pady=20)
        
        # Create Event Button
        create_event_button = ctk.CTkButton(
            app.mainroot, 
            text="Create Event", 
            command=app.create_event,
            width=300,
            height=50,
            font=("Arial", 16)
        )
        create_event_button.pack(pady=20)
        
        # Show Events Button
        show_events_button = ctk.CTkButton(
            app.mainroot, 
            text="Show Available Events", 
            command=app.show,
            width=300,
            height=50,
            font=("Arial", 16)
        )
        show_events_button.pack(pady=20)
        
        # Logout Button
        logout_button = ctk.CTkButton(
            app.mainroot, 
            text="Logout", 
            command=lambda: [app.mainroot.destroy(), app.login_gui()],
            width=300,
            height=40,
            font=("Arial", 14),
            fg_color="gray"
        )
        logout_button.pack(pady=30)
    def create_event(): 
        # Destroy all widgets in mainroot
        for widget in app.mainroot.winfo_children():
            widget.destroy()
        
        app.mainroot.title("Create Event")
        app.mainroot.geometry("500x600")
        
        
        # Get sports list
        metro_result = backend.metro(user_1,None)
        if metro_result and len(metro_result) >= 2:
            spot_list, course_list = metro_result
            # Extract first element if it's a list
            spot = spot_list[0] if isinstance(spot_list, list) and spot_list else (spot_list if spot_list else None)
            course = course_list if course_list else None
        else:
            spot, course = None, None 
        sports_list = ["Basketball", "Batminton", "Squash", "Gym", "Volleyball", "Table Tennis", "Kabaddi"]
        event_types = sports_list + ([f"{spot}"] if spot else []) + ["Study"]
        
        # Title
        ctk.CTkLabel(app.mainroot, text="Create New Event", font=("Arial", 20, "bold")).pack(pady=20)
        
        # Event Name/Type ComboBox
        ctk.CTkLabel(app.mainroot, text="Event Type:").pack(pady=(10, 5))
        event_type_combo = ctk.CTkComboBox(app.mainroot, values=event_types, state="readonly")
        event_type_combo.set("Select Event Type")
        event_type_combo.pack(pady=5)
        
        # Date Entry
        ctk.CTkLabel(app.mainroot, text="Date (YYYY-MM-DD):").pack(pady=(15, 5))
        date_entry = ctk.CTkEntry(app.mainroot, placeholder_text="e.g., 2024-12-25")
        date_entry.pack(pady=5)
        
        # Time Entry
        ctk.CTkLabel(app.mainroot, text="Time (HH:MM):").pack(pady=(15, 5))
        time_entry = ctk.CTkEntry(app.mainroot, placeholder_text="e.g., 14:30")
        time_entry.pack(pady=5)
        
        # Maximum Attendees Entry
        ctk.CTkLabel(app.mainroot, text="Maximum Number of Attendees:").pack(pady=(15, 5))
        max_attendees_entry = ctk.CTkEntry(app.mainroot, placeholder_text="Enter number")
        max_attendees_entry.pack(pady=5)
        
        # Submit function
        def submit_event():
            event_type = event_type_combo.get()
            date = date_entry.get().strip()
            time = time_entry.get().strip()
            max_attendees = max_attendees_entry.get().strip()
            
            # Validation
            if event_type == "Select Event Type" or not event_type:
                popup = ctk.CTkToplevel(app.mainroot)
                popup.geometry("300x100")
                ctk.CTkLabel(popup, text="Please select an event type").pack(pady=20)
                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                return
            
            if not date:
                popup = ctk.CTkToplevel(app.mainroot)
                popup.geometry("300x100")
                ctk.CTkLabel(popup, text="Please enter a date").pack(pady=20)
                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                return
            
            if not time:
                popup = ctk.CTkToplevel(app.mainroot)
                popup.geometry("300x100")
                ctk.CTkLabel(popup, text="Please enter a time").pack(pady=20)
                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                return
            
            if not max_attendees or not max_attendees.isdigit():
                popup = ctk.CTkToplevel(app.mainroot)
                popup.geometry("300x100")
                ctk.CTkLabel(popup, text="Please enter a valid number for max attendees").pack(pady=20)
                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                return
            if event_type == "Study":
                study_result = backend.study(user_1)
                if study_result:
                    event_type = study_result[0] if isinstance(study_result, list) and study_result else (study_result if study_result else "Study")
            if spot and event_type == str(spot):
                if isinstance(course, list) and course:
                    event_type = course[0]
                elif course:
                    event_type = str(course)



            # Validate date format
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                popup = ctk.CTkToplevel(app.mainroot)
                popup.geometry("300x100")
                ctk.CTkLabel(popup, text="Invalid date format. Use YYYY-MM-DD").pack(pady=20)
                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                return
            
            # Validate time format
            try:
                datetime.strptime(time, "%H:%M")
            except ValueError:
                popup = ctk.CTkToplevel(app.mainroot)
                popup.geometry("300x100")
                ctk.CTkLabel(popup, text="Invalid time format. Use HH:MM").pack(pady=20)
                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                return
            
            # Save event to CSV
            event_data = [user_1, event_type, date, time, max_attendees,1]
            
            # Check if events.csv exists, create if not
            if not os.path.exists("events.csv"):
                with open("events.csv", "w", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Creator", "Event Type", "Date", "Time", "Max Attendees", "Current Attendees"])
            
            # Append event to CSV
            with open("events.csv", mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(event_data)
            
            # Success popup
            popup = ctk.CTkToplevel(app.mainroot)
            popup.geometry("300x100")
            ctk.CTkLabel(popup, text="Event created successfully!").pack(pady=20)
            ctk.CTkButton(popup, text="OK", command=lambda: [popup.destroy(), app.show_main_dashboard()]).pack(pady=10)
        
        # Submit Button
        submit_button = ctk.CTkButton(app.mainroot, text="Create Event", command=submit_event)
        submit_button.pack(pady=30)
        
        # Cancel Button
        cancel_button = ctk.CTkButton(app.mainroot, text="Cancel", command=app.show_main_dashboard, fg_color="gray")
        cancel_button.pack(pady=5)

    def show():
        # Populate cache first
        global cache
        cache = other.cache(user_1)
        
        show_window = ctk.CTkToplevel(app.mainroot)
        show_window.title("Available Events")
        show_window.geometry("700x700")
        
        # Title
        ctk.CTkLabel(show_window, text="Available Events", font=("Arial", 24, "bold")).pack(pady=20)
        
        # Create scrollable frame for events
        scrollable_frame = ctk.CTkScrollableFrame(show_window, width=650, height=550)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Check if events.csv exists
        if not os.path.exists("events.csv"):
            ctk.CTkLabel(scrollable_frame, text="No events available yet.", font=("Arial", 16)).pack(pady=50)
            close_button = ctk.CTkButton(show_window, text="Close", command=show_window.destroy, width=200)
            close_button.pack(pady=20)

            return
        
        # Read events from CSV and filter out past events
        events = []
        current_datetime = datetime.now()
        
        # Get user profile data from cache
        # Profile structure: cache[0]=username, cache[1]=password, cache[2]=profile_data (or separate columns)
        user_sports = []
        user_stations = []
        user_course = None
        
        if cache and len(cache) > 2:
            # Check if profile data is in a single column (cache[2]) or separate columns
            profile_data = cache[2] if len(cache) > 2 else ""
            
            # Parse profile data - format is "0#station#sport1#sport2#course" or separate columns
            if profile_data:
                profile_parts = profile_data.split('#') if isinstance(profile_data, str) else []
                # Remove "0" and empty strings
                profile_parts = [p.strip() for p in profile_parts if p.strip() and p.strip() != "0"]
                
                # All possible values
                all_stations = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya",
                    "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Kuvempu Road",
                    "Srirampura", "Mantri Square Sampige Road","Chickpet", "Krishna Rajendra Market", "National College", "Lalbagh Botanical Garden",
                    "South End Circle", "Jayanagar", "R.V. Road", "Banashankari", "Rashtreeya Vidyalaya Road",  
                    "J.P. Nagar", "Yelachenahalli","Konanakunte Cross","Doddakallasandra","Silk Institute","Whitefield (Kadugodi)", "Hopefarm Channasandra", "Kadugodi Tree Park", "Pattanduru Agrahara",
                    "Sri Sathya Sai Hospital", "Nallurhalli", "Kundalahalli", "Seetharamapalya", "Hoodi",
                    "Garudacharpalya", "Mahadevapura", "K.R. Puram", "Benniganahalli", "Baiyappanahalli",
                    "Swami Vivekananda Road", "Indiranagar", "Halasuru", "Trinity", "M.G. Road", "Cubbon Park",
                    "Vidhana Soudha", "Sir M. Visvesvaraya Station", "Nadaprabhu Kempegowda Station (Majestic)",
                    "City Railway Station", "Magadi Road", "Hosahalli", "Vijayanagar", "Attiguppe",
                    "Deepanjali Nagar","Nayandahalli", "Rajarajeshwari Nagar", "Jnanabharathi",
                    "Pattanagere", "Kengeri", "Kengeri Bus Terminal", "Challaghatta"]
                all_sports = ["Basketball", "Batminton", "Squash", "Gym", "Volleyball", "Table Tennis", "Kabaddi"]
                all_courses = ["ECE","CSE","MECH","CIVIL","BBA","MBA","MCA","LAW","DESIGN","BCA"]
                
                # Parse profile parts
                for part in profile_parts:
                    if part in all_stations:
                        user_stations.append(part)
                    elif part in all_sports:
                        user_sports.append(part)
                    elif part in all_courses:
                        user_course = part
            
            # Also check if data is in separate columns (cache[3] for sports, cache[4] for course)
            if len(cache) > 3 and cache[3]:
                sports_str = cache[3].strip()
                if sports_str and sports_str != "0":
                    sports_list = sports_str.split('#') if isinstance(sports_str, str) else []
                    for sport in sports_list:
                        sport = sport.strip()
                        if sport and sport != "0" and sport not in user_sports:
                            user_sports.append(sport)
            
            if len(cache) > 4 and cache[4]:
                course_str = cache[4].strip()
                if course_str and course_str != "0" and not user_course:
                    user_course = course_str
        
        # List of all possible sports for event type checking
        all_sports = ["Basketball", "Batminton", "Squash", "Gym", "Volleyball", "Table Tennis", "Kabaddi"]
        
        with open("events.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header
            for row in reader:
                if len(row) >= 6:  # Ensure row has all required columns
                    event_date = row[2]
                    event_time = row[3]
                    event_type = row[1]
                    
                    # Parse event date and time
                    try:
                        event_datetime_str = f"{event_date} {event_time}"
                        event_datetime = datetime.strptime(event_datetime_str, "%Y-%m-%d %H:%M")
                        
                        # Only add event if it hasn't passed and matches user profile
                        should_include = False
                        
                        # Check if event matches user profile
                        # 1. Check if it's a sports event and matches user's sports interests
                        if event_type in all_sports:
                            if user_sports and event_type in user_sports:
                                should_include = True
                        
                        # 2. Check if it's a metro station event and matches user's destination station
                        elif user_stations and event_type in user_stations:
                            should_include = True
                        
                        # 3. Check if it's a study/course event and matches user's course
                        elif user_course and event_type == user_course:
                            should_include = True
                        
                        if should_include and event_datetime > current_datetime:
                            events.append(row)
                    except ValueError:
                        # If date/time format is invalid, skip this event
                        continue
        
        if not events:
            ctk.CTkLabel(scrollable_frame, text="No events available yet.", font=("Arial", 16)).pack(pady=50)
            close_button = ctk.CTkButton(show_window, text="Close", command=show_window.destroy, width=200)
            close_button.pack(pady=20)
            show_window.mainloop()
            return
        
        # Store post widgets for collapsing
        post_widgets = []
        
        # Function to update attendee count and collapse post
        def accept_event(event_index, post_frame, event_row):
            # Read all events
            rows = []
            with open("events.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                header = next(reader, None)
                rows.append(header)
                for row in reader:
                    rows.append(row)
            
            # Find and update the specific event
            event_row_index = None
            for i, row in enumerate(rows[1:], start=1):  # Skip header
                if (len(row) >= 6 and 
                    row[0] == event_row[0] and 
                    row[1] == event_row[1] and 
                    row[2] == event_row[2] and 
                    row[3] == event_row[3]):
                    event_row_index = i
                    break
            
            if event_row_index is not None:
                # Increment current attendees
                current_attendees = int(rows[event_row_index][5])
                max_attendees = int(rows[event_row_index][4])
                
                # Check if event is full
                if current_attendees >= max_attendees:
                    popup = ctk.CTkToplevel(show_window)
                    popup.geometry("300x100")
                    ctk.CTkLabel(popup, text="Event is full!").pack(pady=20)
                    ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
                    return
                
                rows[event_row_index][5] = str(current_attendees + 1)
                
                # Write back to CSV
                with open("events.csv", mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                
                # Collapse the post (hide it)
                post_frame.pack_forget()
                
                # Show success message
                popup = ctk.CTkToplevel(show_window)
                popup.geometry("300x100")
                ctk.CTkLabel(popup, text="Event accepted!").pack(pady=20)
                ctk.CTkButton(popup, text="OK", command=popup.destroy).pack(pady=10)
        
        # Create a post for each event
        for idx, event in enumerate(events):
            creator = event[0]
            event_type = event[1]
            date = event[2]
            time = event[3]
            max_attendees = event[4]
            current_attendees = event[5] if len(event) > 5 else "0"
            
            # Create post frame
            post_frame = ctk.CTkFrame(scrollable_frame, corner_radius=10)
            post_frame.pack(pady=10, padx=10, fill="x")
            
            # Event title (main title)
            title_label = ctk.CTkLabel(
                post_frame, 
                text=event_type, 
                font=("Arial", 20, "bold"),
                anchor="w"
            )
            title_label.pack(pady=(15, 5), padx=20, anchor="w")
            
            # Creator label
            creator_label = ctk.CTkLabel(
                post_frame,
                text=f"Created by: {creator}",
                font=("Arial", 12),
                text_color="gray",
                anchor="w"
            )
            creator_label.pack(pady=(0, 10), padx=20, anchor="w")
            
            # Date and Time
            datetime_label = ctk.CTkLabel(
                post_frame,
                text=f"📅 Date: {date}  |  🕐 Time: {time}",
                font=("Arial", 14),
                anchor="w"
            )
            datetime_label.pack(pady=5, padx=20, anchor="w")
            
            # Attendees info
            attendees_label = ctk.CTkLabel(
                post_frame,
                text=f"👥 Attendees: {current_attendees} / {max_attendees}",
                font=("Arial", 14),
                anchor="w"
            )
            attendees_label.pack(pady=5, padx=20, anchor="w")
            
            # Accept Event button
            accept_button = ctk.CTkButton(
                post_frame,
                text="Accept Event",
                command=lambda idx=idx, pf=post_frame, er=event: accept_event(idx, pf, er),
                width=200,
                height=35,
                font=("Arial", 14)
            )
            accept_button.pack(pady=(10, 15), padx=20)
            
            post_widgets.append(post_frame)
        
        # Close button
        close_button = ctk.CTkButton(show_window, text="Close", command=show_window.destroy, width=200)
        close_button.pack(pady=20)
        
 


if __name__ == "__main__":
    app.login_gui()
