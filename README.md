# FLOW LOGIN

- User logs in
- get all the details and check if user exist
    - if user does not exist or details are wrong, return error
    - if user exists, get user type, save userid and usertype in localstorage, then redirect to appropriate page

# REGISTRATION CUSTOMER FLOW
- User fills in form
- get details from form (allow the user to choose user type (CLUB, CUSTOMER OR STUDENT))
- if all details are correct a new user is created, 

# REGISTRATION FOR ADMIN

...........................................



# Cinema Management System
A feature-rich and comprehensive web application designed to streamline and simplify the process of managing a cinema, including ticket booking, user account management, and implementing special discounts for club members and students.

# Features
-User Authentication and Role-Based Access Control: The AccountManager and customAuth apps handle user authentication and ensure proper access control based on the user's role.
-User Account Management: The AccountManager app allows for account management for customers, students, and club members, providing a seamless user experience.
-Ticket Booking and Seat Selection: The CinemaManager, Customer, and Student apps provide an easy-to-use interface for users to book tickets, choose their seats, and manage their bookings.
-Showings and Cinema Management: The CinemaManager app handles the scheduling and management of movie showings, as well as other cinema-related information such as screen sizes and seating capacities.
-Club Membership Management and Discounts: The Club app manages club memberships, allowing members to enjoy exclusive discounts on ticket purchases and manage their account balances.
-Student Discounts and Account Management: The Student app offers special discounts for student users, providing an incentive for students to enjoy movies at a reduced cost.
-Frontend Templates and Views: The Fe and group_14 apps handle frontend templates, providing a consistent and visually appealing user interface for all components of the system.
# Installation

Set up a Python virtual environment using python -m venv venv and activate it with source venv\Scripts\activate (Windows).
Install the required dependencies using pip install -r requirements.txt.
Run the Django migrations using python manage.py migrate to set up the necessary database schema.
Start the Django development server using python manage.py runserver, and access the application in your browser by navigating to http://localhost:8000/.
# Usage
Registration: Users can create accounts as customers, students, or club members.
Browsing and Booking: Customers, students, and club members can browse showings, book tickets, and view their booking history.
Discounts: Club members and students can enjoy discounted ticket prices and manage their account balances.
Administration: Administrators can manage users, showings, ticket bookings, and cinema-related information through a dedicated admin interface.
