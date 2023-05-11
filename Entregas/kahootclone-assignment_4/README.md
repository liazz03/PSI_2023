Evaluation criteria

### To pass with 5 points it is necessary to satisfy the following criteria completely:
- It is possible to create a questionnaire and play with it locally. The score of
the participants is shown after every question.
- The file uploaded to Moodle includes a git repository.
- The code has been stored in a git repository accesible to all the members of
the work pair and this repository is private.
- When running the tests, the number of fails is not larger than ten, and the
code that satisfies the tests is functional.

### If the following criteria are accomplished, a grade up to 5.9 might be achieved:
- All the previous criteria are accomplished completely.
- When running the tests in local, the number of fails is not larger than six and
the code that satisfies them is functional.
- It is not possible to create/delete/edit questionnaires/questions/answers for
users NOT connected (“logged”) even when accessing directly to the associated
URLs with the different services.
- It is not possible to join games, or create results (guess) for participants without knowing the publicId of a game, even when directly accessing the associated URLs with the different services.

### If the following criteria are accomplished, a grade up to 6.9 might be achieved:
- All the previous criteria are accomplished completely.
- The two requested projects are deployed in render.com. In the file settings.py the path of the first project in render.com is assigned to the variable ALLOWED HOSTS and the path corresponding to the second one to CORS ORIGIN WHITELIST. Besides being deployed, both projects must work correctly in render.com.
- The database admin application (admin/) is deployed and accesible in render.com using the username/password alumnodb.
- The appplication is deployed in render.com in production mode.
- Using the admin application it is possible to create, list, or remove objects belonging to all the required models.

### If the following criteria are accomplished, a grade up to 7.9 might be achieved:
- All the previous criteria are accomplished completely.
- Heritage has been used in Django when creating the web pages.
- Every form that is either related with a model, or requested explicitly in the assignment, has been built using the form system implemented by Django.
- CSS files or environments such as bootstrap have been used to define the styles.
- When running the tests, the number of fails is not larger than four and the code that satisfies them is functional.
- The web application has a user interface that is user friendly and visually neat. Visually the web application must NOT be similar to the model we have provided in render.com.

### If the following criteria are accomplished, a grade up to 8.9 might be achieved:
- All the previous criteria are accomplished completely.
- The code is readable, efficient, well-structured, and commented.
- The tools provided by the framework are used.
- The following are examples of the previous points:
    * The queries are done by the database. That is, the methods in views.py do not retrieve all elements of a table (i.e. ClassName.objects.all()) and the search is done by the functions defined en views.py (for object in class: if object.name==’Pedro’: ...).
    * The errors are properly processed and understandable message errors are returned.
    * The web application properly manages accesses to non existing pages or with inadequate permissions.
    * The code presents a consistent style and the functions are commented including their author. Note: the author of a function must be unique.
    * The style criteria highlighted by Flake8 are applied in a coherent way. Flake8 does not return any error when executed on the code programmed by the student.
    * The files created with Vue.js must satisfy the criteria highlighted by lint (command npm lint).
- The user manual is included and appropriate.
- When running the tests, the number of fails is not larger than two and the code that satisfies them is functional.
- If we reduce the size of the browser window or use the zoom, all the elements in the page are still accessible and no functionality is lost.

### If the following criteria are accomplished, a grade up to 10 might be achieved
- All the previous criteria are accomplished completely.
- The application is robust and responds adequately even if invalid parameters are provided.
- All the tests provide satisfactory results.
- The coverage for the Django files that contain the models, views, and forms is over 99%. If the proposed tests do not generate the necessary coverage, create a new file called tests additional.py and add the necessary tests in it.


Note: Late final submission → take away a point for each late day (or fraction) in the submission.

Note: The code used in the assessment of the assignment will be the one submitted to Moodle. Under no circumstance, the existing code in render.com, Github, or any other repository will be used.