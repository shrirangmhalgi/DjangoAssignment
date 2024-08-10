# DjangoAssignment
This is a repository to practice django skills: Screenshots are included for each and every task

<h1> Task 1: SETTING UP PROJECT </h1>

<h2> Microtasks: </h2>
<ol>
  <li> Create a Virtual Environment: DjangoAssignment - Create a virtual environment named "DjangoAssignment" to isolate project dependencies.
    <br>
    <br>
    <img src='screenshots/task 1.1.png'>
    <br>
  <li> Activate the Virtual Environment - Activate the virtual environment to use it for installing and running Django.
  <li> Install Django - Install Django within the activated virtual environment to use it for the project.
    <br>
    <br>
    <img src='screenshots/task 1.2, 1.3.png'>
    <br>
  <li> Create a New Django Project: Login System - Create a new Django project named "Login System" where all configurations and settings will reside.
  <li> Create a New Django Application: “Loginify” - Create a new Django application within the project to handle the login functionality.
    <br>
    <br>
    <img src='screenshots/task 1.4, 1.5.png'>
    <br>
</ol>


<h1> Task 2: CREATE VIEWS AND URLS FOR LOGIN SYSTEM </h1>

<h2> Microtasks: </h2>
<ol>
  <li> Create Views - Create views within the "Loginify" Django application to handle login functionality. Create a view that returns an HTTP response with the text "Hello, world!" for testing purposes.
    <br>
    <br>
    <img src='screenshots/task 2.1 urls.png'>
    <br>
  <li> Define URL Patterns - Define URL patterns in the "urls.py" file of the "Loginify" Django application to map views to specific URLs. Ensure that the URL patterns are properly configured to match the desired endpoints.
    <h3> Hello World - </h3>
    <img src='screenshots/task 2.2 hello.png'>
    <br>
    <h3> Login Page - </h3>
    <img src='screenshots/task 2.2 login.png'>
    <br>
</ol>


<h1> Task 3: Define Models for Login System </h1>

<h2> Microtasks: </h2>
<ol>
  <li> Models : Create a “UserDetails” Model which has fields below Username: Use models.CharField(max_length=50, primary_key=True) Email: Use models.EmailField(unique=True) Password: Use models.CharField(max_length=12, blank=True) Implement views in views.py for signup, login.
    <br>
    <br>
    <img src='screenshots/task 3.1.png'>
    <br>
  <li> Define URLs and Templates Define URL patterns in urls.py for the implemented views. Create HTML templates for signup and login forms, confirmation page, and success message. Upon successful signup, redirect to the login page. Upon successful login, display a success message.
    <h3> URL Redirection - </h3>
    <img src='screenshots/task 3.2 a.png'>
    <br>
    <h3> Signup Page - </h3>
    <img src='screenshots/task 3.2 c.png'>
    <br>
    <h3> Login Page - </h3>
    <img src='screenshots/task 3.2 b.png'>
    <h3> Success Page - </h3>
    <img src='screenshots/task 3.2 d.png'>
    <br>
</ol>
