from webApp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    # debug=True just means that if a change is made to the code, the web server will automatically re-run