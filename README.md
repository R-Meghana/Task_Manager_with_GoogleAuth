# Task_Manager_with_GoogleAuth
 Task Manager with Invitation System

 Overview

This project is a Task Manager web application built using Django. It allows users to manage their tasks efficiently while providing an invitation system for user registration. The application features both email-based invitations and Google OAuth login for authentication. 

The system ensures smooth user registration through an invite-only system. Users can receive personalized invitation emails and use them to sign up for the platform. The project integrates features like task management, user authentication, and dynamic email notifications.

 Key Features

1. User Authentication
   - Users can register, log in, and log out.
   - Supports Google OAuth for easy sign-in with Google accounts.
   - Account creation can be done via an invitation link sent by administrators.
   
2. Task Management
   - Users can add, update, and delete tasks.
   - Tasks are organized by deadlines, priorities, and completion status.

3. Invitation System
   - Admins can send invitation emails to users to allow them to join the platform.
   - Invitations are unique, with tokens that are included in the invitation email, making registration secure.
   - Admins can track whether the invitation was used or not.

4. Email Notifications
   - Email notifications are sent to users when an invitation is triggered.
   - The invitation emails include a custom link for registration, enhancing the sign-up process.

5. Dynamic Frontend (React)
   - The React dashboard provides a modern interface for interacting with the tasks.
   - The frontend is styled with Bootstrap for a responsive design.
   - Key components such as task list, task creation, and task details are rendered dynamically.

 How It Works

1. Invitation Workflow
   - Admins send invitation emails to users through the Django Admin panel. These emails contain a link with a unique token that the user can use to register on the platform.
   - Once the user clicks the link and registers, the token is invalidated to prevent reuse.

2. Authentication
   - Users can either register through the invitation link or log in using their Google account.
   - The Google OAuth login is facilitated by Allauth, which integrates easily with Django.

3. Task Management
   - After logging in, users can manage tasks directly from the dashboard.
   - Tasks are displayed in an organized format, with various attributes such as due dates, completion status, and priority.

4. Admin Panel
   - The Django Admin interface allows administrators to manage users, view task details, and send invitation emails.
   - Admins can see the status of each invitation, including whether the invitation has been used or not.

 Installation and Setup

1. Clone the Repository
   ```bash
   cd TaskManager
   ```

2. Create a Virtual Environment
   ```bash
   python -m venv env
   source env/bin/activate   On Windows, use `env\Scripts\activate`
   ```

3. Install Dependencies
   ```bash
   pip install -r requirement.txt
   ```

4. Set Up the Database
   Run migrations to set up the database tables:
   ```bash
   python manage.py migrate
   ```

5. Create the .env File
   Create a `.env` file to store sensitive data (e.g., secret keys, email credentials) and fill it out:
   ```text
   SECRET_KEY=your_secret_key
   EMAIL_HOST_USER=your_email
   EMAIL_HOST_PASSWORD=your_email_password
   ```

6. Start the Development Server
   ```bash
   python manage.py runserver
   ```

7. Frontend 
   ```browser
   navigate to "http://127.0.0.1:8000/accounts/login" to start the application
   ```

8. Access the Application
   Open your browser and go to `http://127.0.0.1:8000/` to access the application.

 Additional Features

- User Roles and Permissions: The system allows admins to control access to certain features, such as sending invitations.
- Responsive Design: The frontend is designed to be mobile-friendly using Bootstrap, ensuring that it works well on all devices.
- User-friendly Interface: Both the user and admin interfaces are intuitive, making it easy for both users and administrators to navigate.

 Technologies Used

- Backend: Django, Django Allauth (for user authentication)
- Frontend: HTML,CSS
- Database: SQLite (default for development, can be switched to PostgreSQL for production)
- Email: SMTP (Gmail configured in settings for sending invitation emails)

 Contribution

Feel free to fork the repository, make changes, and submit pull requests. For any bugs or feature requests, please create an issue in the GitHub repository.

---

 Conclusion

This Task Manager project integrates essential task management capabilities with a robust user authentication system, allowing users to easily manage their tasks while ensuring secure and personalized registration through invitations.
