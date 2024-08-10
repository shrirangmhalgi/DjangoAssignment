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
    <li> Signup view: Implement the Signup view in views.py, which handles user registration with inputs for name, email, and password. Ensure that the email field is unique.
    <li> Login view: Implement the Login view in views.py, which requires inputs for email and password.
    <br>
    <img src='screenshots/task 3.3 3.4.png'>
    <br>
</ol>



<h1> Task 4: MODELS & ADMIN - Set up a superuser account using Django's manage.py command and verify the superuser endpoint by accessing the admin interface to ensure proper configuration and functionality.</h1>


<h2> Microtasks: Lets Dive into the Django Shell to explore the Power of Command Line Magic for Managing Your Django Project! python manage.py shell </h2>
<ol>
  <li> Setup Superuser - Create a superuser using Django's manage.py command. python manage.py createsuperuser - Verify the superuser endpoint by visiting the admin interface.
    <br>
    <br>
    <img src='screenshots/task 4.1.png'>
    <br>
  <li> Create a new user instance : new_user = User.objects.create(username="example_user", email="user@example.com", password="example123")
  <li> Retrieve all Users : all_users = User.objects.all()
    <br>
    <br>
    <img src='screenshots/task 4.1.1 4.1.2.png'>
    <br>
  <li> Retrieve a single user by name: For example : username = “john” user_by_name = User.objects.get(username=username)
    <br>
    <br>
    <img src='screenshots/task 4.1.3.png'>
    <br>
  <li> Delete a user by username : username_to_delete= “john” user_to_delete = User.objects.get(username=username_to_delete)
    <br>
    <br>
    <img src='screenshots/task 4.1.4.png'>
    <br>
  <li> Create a new instance using object obj = YourModel.objects.create(field1=value1, field2=value2)
    <br>
    <br>
    <img src='screenshots/task 4.1.5.png'>
    <br>
  <li> Query objects queryset = YourModel.objects.filter(field1=value1)
    <br>
    <br>
    <img src='screenshots/task 4.1.6.png'>
    <br>   
  <li> Update an object obj.field1 = new_value obj.save()
    <br>
    <br>
    <img src='screenshots/task 4.1.7.png'>
    <br>
  <li> Delete an object obj.delete()
    <br>
    <br>
    <img src='screenshots/task 4.1.8.png'>
    <br>
</ol>



<h1> Task 5: CRUD OPERATIONS Implement CRUD (Create, Read, Update, Delete) operations for managing user data within the Django login system.</h1>

<h2> Microtasks: </h2>
<ol>
  <li> 1. Implement CRUD Operations - Create four additional views functions for CRUD operations. Get all user details view: Retrieves and displays details of all users. Get a single user using by email view: Retrieves and displays details of a specific user based on their name. Update User details To delete a user using its email. - These views handle read, update, and delete operations for user data. - Use Postman to test and perform CRUD operations API’s.
    <h3> Read - All Users</h3>
    <br>
    <img src='screenshots/task 5.1.png'>
    <br>
    <h3> Read - Single User</h3>
    <br>
    <img src='screenshots/task 5.2.png'>
    <br>
    <h3> Update - </h3>
    <br>
    <img src='screenshots/task 5.4.png'>
    <h3> Delete - </h3>
    <br>
    <img src='screenshots/task 5.3.png'>
    <br>
</ol>


