# game-store
Django app based on models and django built-in admin site

This is an example of a basic Django app using only the Django admin site features (no custom views), to show how you can create a simple application with almost no coding, just using Django features.
In addition, the Django import-export library is used to allow user to export and import multiple rows from CSV or excel files.

Here's a short video that demonstrates how to use the application: http://recordit.co/v3HieLCTXT
Field descriptions are in Spanish.

To run this app:
- Install Django
- Create a new virtual environment and activate it.
- Install the dependencies in requirements.txt with pip (pip install -r requirements.txt)
- Run migrations (python3 manage.py migrate)
- Start the server (python3 manage.py runserver)
- Access to http://localhost:8000/admin and you'll be ready to start.

We're using Postgres as relational database.
For this example there are no summary tables. For this purpose I would recommend to use PowerBI or Metabase, to retrieve data from the original transactional database and do the reports and tables using the BI capabilities.
