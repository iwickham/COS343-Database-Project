import pyodbc
from dotenv import DotEnv
from flask import Flask, request, session

dotenv = DotEnv()

# Database connection parameters
server = dotenv.get('server')
database = dotenv.get('database')
username = dotenv.get('username')
password = dotenv.get('password')



# Establish a database connection
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                            ';DATABASE=' + database +
                            ';UID=' + username +
                            ';PWD=' + password)

# Function to register a new user
def register_user(firstname, lastname, email, role, bio, major, year):
    cursor = connection.cursor()
    try:
        # Call the stored procedure to insert a new cabinet member
        cursor.execute("{CALL InsertCabinetMember (?, ?, ?, ?, ?, ?, ?)}", firstname, lastname, email, role, bio, major, year)
        connection.commit()
        print("User registered successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

# Function to authenticate user login
def login_user(email, password):
    cursor = connection.cursor()
    try:
        # Check user credentials by querying the database
        cursor.execute("SELECT * FROM CabinetMembers WHERE Email = ? AND Password = ?", email, password)
        user = cursor.fetchone()

        if user:
            print("Login successful!")
            # Perform actions after successful login, if any
        else:
            print("Invalid email or password. Please try again.")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

# Function to handle user logout
def logout_user():
    # Implement your logout logic here
    session.pop('user_id', None)

# Example usage
if __name__ == "__main__":
    # Register a new user
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    email = input("Enter your email address: ")
    role = input("Enter your role: ")
    bio = input("Enter in bio")
    major = input("Enter in your major")
    year = input("Enter in your year")
    register_user(firstname, lastname, email, role, bio, major, year)

    # You can implement login and logout functionality similarly using the respective functions.
