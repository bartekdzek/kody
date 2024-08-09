# Flask Job Posting Blog

This project is a Flask-based web application that serves as a dynamic job posting blog. The application retrieves job postings from a JSON file or an API and displays them in a blog-style format on a website. It includes the ability to view detailed descriptions of each job, allowing users to easily browse and understand the various job opportunities.

## Features

- **Dynamic Content Rendering**: The application fetches job data and dynamically renders it on the website using Flask templates.
- **Detail View**: Users can click on a job title to view the full job description on a separate page.
- **Responsive Design**: The front-end is built using HTML and CSS, ensuring that the website is responsive and user-friendly across different devices.

## Project Structure

The project is organized into the following key files and directories:

### 1. `main.py`

This is the main entry point for the Flask application. It sets up the Flask server and handles the routing for the application. The file performs the following tasks:

- Initializes the Flask application.
- Defines routes for the home page (`/`) and individual job posting pages (`/post/<int:post_id>`).
- Loads job data from a JSON file or an API.
- Renders templates with the job data.

### 2. `post.py`

This file contains the `Post` class, which is used to create job post objects. Each job post object has attributes like `id`, `title`, `subtitle`, and `body`, which are used to display the job details on the website.

### 3. `templates/`

This directory contains the HTML templates used by Flask to render the web pages. The main templates include:

- **`index.html`**: The home page template that lists all job postings with their titles and subtitles.
- **`post.html`**: The detail page template that displays the full job description when a user clicks on a job title.

### 4. `static/css/`

This directory contains the CSS files used for styling the web pages. The main CSS file is:

- **`styles.css`**: Contains the custom styles for the application, including layout, colors, and typography.

### 5. `data.json`

This file (or API) contains the job postings data in JSON format. Each job posting includes an ID, title, subtitle, and body. The data is loaded into the application and used to render the job posts on the website.

