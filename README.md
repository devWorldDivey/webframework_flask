# webframework_flask
A introduction to Flask and how to utilize it in real web application.
# How to run Flask in Visual Studio?    https://code.visualstudio.com/docs/python/tutorial-flask
# How to activate virtual environment?  e:/Divey_Project/flask/project1_taskmanager/webframework_flask/env/Scripts/activate.bat
# How to create database when model is defined? https://stackoverflow.com/questions/34122949/working-outside-of-application-context-flask
    <!-- First method
    Instead of calling create_all() in your code, call manually in the flask shell which is CLI
    Go to your terminal and type flask shell, then
    db.create_all()

    Second method
    As it says in the runtime error message,This typically means that you attempted to use functionality that needed the current application. To solve this, set up an application context with app.app_context().Open the python terminal in your project directory and manually add a context
    from project_name import app, db
    app.app_context().push()
    db.create_all() -->

    How I have solved d.create_all() problems?
        https://stackoverflow.com/questions/73961938/flask-sqlalchemy-db-create-all-raises-runtimeerror-working-outside-of-applicat
            FOR CMD
                >>> from project import app, db
                >>> app.app_context().push()
                >>> db.create_all()
    
    How I have resolved this 
        TypeError: scoped_session.commit() takes 1 positional argument but 2 were given
            db.seesion.commit() -----> Remove t from commit parameters
    
        


