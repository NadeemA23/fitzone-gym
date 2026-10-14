# FitZone Gym

I built FitZone Gym as my final project for the Code Institute Full Stack Software Development course.

The idea behind the website is to let people look at gym memberships, create an account and book fitness classes online.

I used Django to build the website and Stripe to handle membership payments in test mode. Once someone has an active membership, they can book classes, cancel bookings and check their membership details from their dashboard.

I also added a separate set of features for gym staff so they can add, edit and delete classes without giving regular members access to those options.

The project uses a PostgreSQL database and is deployed on Render.

## Live Website

[FitZone Gym — Live Website](https://fitzone-gym-w9h2.onrender.com/)

## GitHub Repository

[FitZone Gym — GitHub Repository](https://github.com/NadeemA23/fitzone-gym)

## Project Goals

When I started building FitZone Gym, I wanted to create a website that would allow people to manage their gym membership and book classes online.

My main goals were:

- Make it easy for visitors to see the different membership plans and gym classes.
- Allow people to register and log in to their own accounts.
- Let users pay for a membership securely using Stripe.
- Make sure only people with an active membership can book classes.
- Give members a dashboard where they can check their membership and bookings.
- Allow members to cancel classes they can no longer attend.
- Give gym staff the ability to add, edit and delete classes.
- Make sure regular members cannot access staff-only features.

## Target Audience

FitZone Gym is aimed at people who want to join a gym, manage their membership online and book fitness classes. It is also designed for gym staff who need to manage the available classes.

## User Stories

### Visitors

- As a visitor, I want to see the different membership plans so I can decide which one suits me.
- As a visitor, I want to view the available gym classes before joining.
- As a visitor, I want to create an account so I can purchase a membership.

### Registered Users

- As a registered user, I want to log in and access my account.
- As a registered user, I want to purchase a gym membership online.
- As a member, I want to check whether my membership is active.
- As a member, I want to book classes without having to contact the gym.
- As a member, I want to see my bookings and cancel them if my plans change.

### Gym Staff

- As a staff member, I want to add new classes to the website.
- As a staff member, I want to edit existing classes if any details change.
- As a staff member, I want to remove classes that are no longer available.
- As a staff member, I want these options to be restricted so regular users cannot make changes.

## Features

FitZone Gym has several features that allow visitors to explore the website, members to manage their accounts and gym staff to manage classes.

### Navigation Bar

I added a navigation bar so users can move between the different pages of the website.

The options shown depend on whether someone is logged in and whether they have staff access.

### Homepage

The homepage introduces FitZone Gym and gives visitors a starting point to explore the website.

I included a link to the membership plans so visitors can easily see the available options.

### Membership Plans

This page shows the different membership plans available.

Each plan includes its name, description and price, allowing visitors to compare the options before deciding which membership to purchase.

### User Registration and Login

I added a registration and login system so users can create their own accounts.

When someone registers, they need to enter their details and create a password. Django's authentication system handles the login process and checks that the account details are valid.

Users can also log out when they have finished using the website.

### Membership Payments

I used Stripe Checkout to allow users to purchase gym memberships.

When a user selects a membership plan, they are taken to Stripe to complete the payment. The website then checks the payment status before activating their membership.

I used Stripe in test mode for this project, so no real payments are taken.

### Member Dashboard

I created a dashboard where logged-in users can view their membership information and see the classes they have booked.

This gives members one place to check their account without having to look through different pages.

### Gym Classes and Bookings

I added a classes page where users can see the gym classes available to book.

Each class has information such as its name, instructor, date, time and the number of spaces available.

I also added checks to make sure only users with an active membership can book classes. If someone tries to book the same class twice, the website prevents a duplicate booking.

Classes also have a capacity limit to stop more people booking than there are spaces available.

### Cancelling Bookings

Members can cancel classes they have already booked.

I added this feature so users can manage their bookings without needing to contact gym staff.

When a booking is cancelled, it is removed from the member's bookings.

### Staff Class Management

I created a separate set of features for gym staff to manage classes.

Staff members can:

- Add new gym classes.
- Edit existing class details.
- Delete classes that are no longer needed.

I used Django's staff permissions to restrict these features. Regular users cannot access the class management pages, even if they try to open the URLs directly.

I tested these features by creating a class, changing its details and then deleting it. I also checked that an ordinary user could not access the staff-only pages.

## Technologies Used

I used a number of technologies to build FitZone Gym.

### Languages

- **HTML5** – Used to structure the pages.
- **CSS3** – Used to style the website and its layout.
- **Python** – Used for the backend functionality.
- **JavaScript** – Used for any interactive features that require it.

### Frameworks and Libraries

- **Django** – The main Python framework I used to build the website. It handles the database models, views, forms, authentication and other backend features.
- **Bootstrap** – Used for styling and responsive layouts, where applicable.

### Database

- **PostgreSQL** – Used to store information such as user accounts, membership plans, memberships, gym classes and bookings.

### Payments

- **Stripe** – Used to process membership payments through Stripe Checkout in test mode.

### Development and Deployment

- **Git** – Used to track changes throughout development.
- **GitHub** – Used to store the project repository.
- **GitHub Codespaces** – The development environment I used to write and test the code.
- **Render** – Used to deploy the website online.
- **Django Test Framework** – Used to run automated tests for the gym classes and booking functionality.

## Database Design

I used Django models to organise and store the information needed for FitZone Gym. The website uses PostgreSQL when deployed on Render.

I created four main models for the membership and class booking features.

### MembershipPlan

This model stores the different gym memberships available.

It includes:

- Name of the membership
- Description
- Price
- Duration in days

### UserMembership

This model keeps track of the membership a user has purchased.

It includes:

- The user who owns the membership
- The membership plan they selected
- Membership start and end dates
- Whether the membership is active
- Stripe checkout session ID

Each user can have one UserMembership record, which is linked to a MembershipPlan.

### GymClass

This model stores the information for each gym class.

It includes:

- Class name and description
- Instructor
- Date and time
- Maximum number of spaces available

### Booking

This model stores the classes that users have booked.

Each booking is linked to a user and a gym class. This allows the website to show members their bookings and check how many spaces are still available.

### Model Relationships

The models are connected using Django's relationship fields.

- **User and UserMembership:** One-to-one relationship.
- **MembershipPlan and UserMembership:** One-to-many relationship.
- **User and Booking:** One-to-many relationship.
- **GymClass and Booking:** One-to-many relationship.

I used these relationships so the website can keep track of which users have memberships and which classes they have booked.

## Security and Access Control

When building FitZone Gym, I wanted to make sure users could only access the features they were allowed to use.

### User Authentication

I used Django's built-in authentication system to handle registration, login and logout.

Passwords are handled by Django rather than being stored as plain text.

### Membership Restrictions

I added checks to stop users from booking gym classes unless they have an active membership.

The booking system also checks whether a class is full and prevents users from booking the same class more than once.

These checks are carried out in the backend rather than relying only on which buttons are visible.

### Staff Permissions

I restricted the class management features to staff accounts.

Regular users can view classes, but they cannot add, edit or delete them.

I tested this by logging in with a regular account and trying to access the staff management pages directly.

### Payment Security

I used Stripe Checkout to handle membership payments rather than collecting card details directly on my website.

The website checks the Stripe payment status before activating a membership.

Stripe was used in test mode during development.

### Forms and Data Protection

I used Django forms to validate information submitted by users.

For example, the class form checks that the capacity is at least one.

Django's CSRF protection is also used on forms that submit changes.

### Environment Variables

Sensitive configuration values, such as the Django secret key and Stripe API credentials, are kept outside the source code using environment variables.

## Testing

I tested FitZone Gym throughout development to check that the main features worked and that users could not access features they were not supposed to use.

I carried out manual testing on the live website and also added automated tests using Django's testing framework.

### Automated Testing

I added five automated tests to the `classes/tests.py` file to check some of the main class and booking features.

The tests cover the following:

| Test | What I Checked | Result |
|---|---|---|
| Class list page | The class list page loads successfully | Pass |
| Gym class creation | A gym class can be created and saved | Pass |
| Class capacity validation | A class cannot have a capacity of zero | Pass |
| Membership restrictions | A user without an active membership cannot book a class | Pass |
| Duplicate bookings | A user cannot book the same class twice | Pass |

All five tests passed when I ran them in my development environment.

I used the following command to run the tests:

`python manage.py test classes`

The tests use a separate temporary test database, so they do not change the information stored on the live website.

I added these tests to check that the booking rules and class validation were working as expected.

### Manual Testing

I also tested the website manually to make sure the main features worked as expected.

I tested different situations, including what happens when a user enters invalid information or tries to access something they are not allowed to use.

| Feature | What I Tested | Result |
|---|---|---|
| Registration | Registering an account with valid details | Pass |
| Registration validation | Leaving required fields empty and using a common password | Pass |
| Login | Logging in with an existing account | Pass |
| Membership payment | Completing a Stripe test payment | Pass |
| Membership activation | Checking that a successful payment activates the membership | Pass |
| Class booking | Booking a class with an active membership | Pass |
| Membership restriction | Trying to book without an active membership | Pass |
| Booking cancellation | Cancelling an existing booking | Pass |
| Staff access | Trying to access staff pages using a regular account | Pass |
| Add class | Creating a new gym class | Pass |
| Edit class | Changing an existing class | Pass |
| Delete class | Removing a class | Pass |
| Required fields | Trying to submit an incomplete class form | Pass |
| Class capacity | Trying to create a class with zero capacity | Pass |

### Staff CRUD Testing

I tested the class management features using a staff account.

First, I created a class called CRUD Test Class and checked that it appeared on the classes page.

I then edited the class, changed its name to CRUD Test Class Updated and changed its capacity to 15.

After checking that the changes were saved, I deleted the class and confirmed it no longer appeared on the classes page.

I also logged in using a regular account and checked that the staff management options were not available. I tried opening the staff URLs directly and confirmed that access was restricted.

### Form Validation Testing

I tested the Add Gym Class form using different inputs.

When I left a required field empty, the browser prevented the form from being submitted.

When I entered a negative capacity, the browser displayed a validation message.

I also entered a capacity of zero to check the validation I had added to the Django form. The form displayed the message:

"Class capacity must be at least 1."

This helped me check that invalid class capacities were rejected.

## Bugs and Fixes

While building FitZone Gym, I came across a few problems that I had to fix before the website worked properly.

### Membership Button Not Working

At first, the View Memberships button on the homepage wasn't taking users to the membership plans.

I found that the button still had `href="#"` instead of a link to the memberships page.

I updated the link and tested it again to make sure it opened the correct page.

### Dashboard Template Error

When I first tried opening the dashboard, Django displayed a `TemplateDoesNotExist` error because the dashboard template hadn't been created.

I added the missing template and checked that the dashboard loaded.

I also had a template syntax error caused by an incorrect Django template tag, which I fixed before testing the page again.

### Stripe Checkout Issues

I had some problems getting the membership checkout working correctly.

Initially, the Continue to Payment button wasn't working as expected. I checked the checkout view and the Stripe settings until I was able to reach the Stripe payment page.

I also had to make sure that a membership was only activated after a successful payment had been verified.

### Class Capacity Validation

I tested the class form to see what happened when an invalid capacity was entered.

I used Django form validation to make sure a class couldn't be saved with a capacity of zero.

After adding the validation, I tested the form again and confirmed that it displayed an error message.

### Automated Testing

I added automated tests after building the main class booking features.

These helped me check that class creation, capacity validation and booking restrictions worked correctly.

All five tests passed when I ran the test suite.

## Deployment

I deployed FitZone Gym using Render so the website could be accessed online.

I used GitHub to store my project and connected the repository to Render for deployment.

### Deploying the Website

The main steps involved were:

1. Pushing my project files to GitHub.
2. Creating a web service on Render and connecting it to my GitHub repository.
3. Setting up the environment variables needed for Django and Stripe.
4. Configuring the PostgreSQL database for the deployed website.
5. Running the database migrations to create the required tables.
6. Deploying the application and checking that the website loaded correctly.

### Environment Variables

I used environment variables for sensitive settings rather than putting private keys directly into my code.

These include the Django secret key, database connection details and Stripe API credentials.

### Live Website

The deployed website can be viewed here:

[FitZone Gym](https://fitzone-gym-w9h2.onrender.com/)

### Deployment Testing

After deploying the website, I tested the main features to check that they worked on the live version.

This included registering and logging in, purchasing a membership using Stripe test mode, booking classes and testing the staff management features.

## Accessibility and Responsive Design

I wanted FitZone Gym to be easy to use and navigate on different devices.

### Responsive Design

I have tried to keep the website layout clear and easy to follow, with navigation links and forms that are straightforward to use.

Responsive design is important because some users may access the website on a phone or tablet rather than a computer.

### Accessibility

I considered accessibility when building the website, including:

- Using headings to separate different sections.
- Keeping navigation consistent across the website.
- Using labels on forms so users know what information to enter.
- Displaying validation messages when incorrect information is entered.
- Making buttons and links clear so users know what they do.

### Further Testing

I plan to check the website at different screen sizes and use accessibility testing tools to identify any problems.

I will document the results of these checks and make improvements where needed.

## Future Improvements

Although FitZone Gym has the main features I wanted to include, there are still a few things I would like to add or improve in the future.

### Membership Renewals

I would like to add an option for members to renew their memberships before they expire, without having to go through the full process again.

### Email Confirmations

Another feature I would like to add is automatic emails when someone purchases a membership or books a gym class.

This would give members confirmation of their purchases and bookings.

### Class Timetable

I would like to improve the classes page by adding a weekly timetable so members can see which classes are available on different days.

### Member Profiles

I would also like to give members more options to manage their personal details from their dashboard.

### Further Design Improvements

I would like to continue improving the website's appearance and mobile layout, especially after carrying out more testing on different screen sizes.

## Credits and Acknowledgements

### Technologies and Documentation

I used the following documentation and resources while developing FitZone Gym:

- [Django Documentation](https://docs.djangoproject.com/) – For understanding Django models, views, forms and authentication.
- [Python Documentation](https://docs.python.org/3/) – For Python language reference.
- [Stripe Documentation](https://docs.stripe.com/) – For integrating Stripe Checkout.
- [Render Documentation](https://render.com/docs) – For deploying the website.
- [GitHub Documentation](https://docs.github.com/) – For using GitHub and managing my repository.

### Acknowledgements

I would like to thank Code Institute for the course materials and the opportunity to develop my full-stack development skills.

I also used ChatGPT for guidance while working on the project, troubleshooting errors, testing and organising my documentation but everything was done by me.

## Entity Relationship Diagram (ERD)