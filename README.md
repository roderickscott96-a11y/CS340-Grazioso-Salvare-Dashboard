# CS 340 Client/Server Development Portfolio

## About This Repository

This repository contains my final work from CS 340 Client/Server Development. The main project was created for Grazioso Salvare, a rescue-animal training organization. The application uses MongoDB, Python, PyMongo, and Dash to allow users to search and filter animal shelter records through an interactive dashboard.

The final dashboard includes rescue-type filters, an interactive data table, a breed distribution chart, and a geolocation map.

## How do you write programs that are maintainable, readable, and adaptable?

I try to keep my programs organized by separating different responsibilities instead of putting everything into one large file. One example from this course was the CRUD Python module I created in Project One. The CRUD module handles the connection to MongoDB and contains the create, read, update, and delete functions.

This was useful in Project Two because I was able to import the same module into my dashboard instead of rewriting the database code. It made the dashboard easier to read and made troubleshooting easier because the database logic and dashboard code were separated.

I could use this type of CRUD module again in future projects that need to connect Python to MongoDB. The same structure could be adapted for inventory systems, customer information, or other applications that need to store and retrieve data.

## How do you approach a problem as a computer scientist?

I usually start by breaking a problem into smaller parts and getting each part working before putting everything together. For the Grazioso Salvare project, I first worked with the MongoDB database and CRUD operations. After the database connection was working, I built the data table, added the rescue filters, and then connected the chart and map.

This project was different from some of my earlier assignments because several parts of the application depended on each other. The database, Python module, dashboard, filters, and visualizations all had to communicate correctly.

In future projects, I would continue breaking requirements into smaller tasks, testing each part as I go, and making sure I understand what the client needs before designing the database and application.

## What do computer scientists do, and why does it matter?

Computer scientists use programming, data, and problem-solving skills to create systems that make tasks easier and information more useful. This can include building databases, creating software, automating processes, and designing interfaces for users.

For a company like Grazioso Salvare, this type of application can save a lot of time. Instead of manually searching through thousands of animal records, users can select a rescue type and quickly view dogs that match the needed criteria. The charts and map also make the information easier to understand.

This project helped me understand how database development and software development can work together to solve a real-world problem.
