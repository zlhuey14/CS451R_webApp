from webApp import create_app
from flask import Flask, render_template, request



app = create_app()

def enroll():
    selected_courses = request.form.getlist('selected_courses')
    return 'Enrollment successful'
if __name__ == '__main__':
    app.run(debug=True)
    # debug=True just means that if a change is made to the code, the web server will automatically re-run
