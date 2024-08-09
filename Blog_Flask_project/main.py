# This project is a Flask-based web application that dynamically displays job postings.
# It retrieves job data from an API and renders it on a website in a blog-style format.
# The application provides users with a detailed view of the job descriptions,
# making it easy to browse and understand the requirements and responsibilities of each position.


from flask import Flask, render_template
from post import Post
import requests

# Fetch posts data from API
posts_data = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()

# Debugging: Print the structure of the posts variable
print(posts_data)  # This shows the structure

# Since posts_data is a dictionary, extract the 'job_posting' and treat it as a single post
if 'job_posting' in posts_data:
    job_posting_text = posts_data['job_posting']
    post_objects = [Post(1, "Job Posting", "CNC Programmer/Operator Role", job_posting_text)]
else:
    print("Unexpected structure:", posts_data)
    post_objects = []

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
