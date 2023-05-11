Evaluation criteria

Note: When grading this assessment, the aesthetics will NOT be considered (it will
be evaluated in the next assignment).

# To pass with 5 points it is necessary to satisfy the following criteria completely:
- All the needed files to run the application have been submitted on time.
- The code was stored in a git repository and this repository is private.
- The file uploaded to Moodle contains a git repository.
- The script populate.py exists and is functional.
- The application can be executed locally.
- When running the tests in local, the number of fails is not larger than four and the code that satisfies the tests is functional.
- The code of the tests was not modified.
- The application works against the database created in https://neon.tech and implemented using PostgreSQL.
- The database admin application is deployed and accessible in the local Django server using as user name and password alumnodb.
- It is possible to create and remove objects belonging to all the requested models using the admin application.
- IMPORTANT: we need https://neon.tech URI in order to grade this assignment. Please write it down in a file called env and place it in the proyect root directory.

# If the following criteria are accomplished, a grade up to 6.9 might be achieved:
- All the criteria in the previous paragraph are totally satisfied.
- The application is deployed in Render.com. In the file settings.py the path to
Render.com is assigned to the variable ALLOWED_HOSTS. Besides being deployed,
the application works correctly in Render.com.
- The code submitted to Moodle is identical to the one deployed in Render.com.
- The database admin application is deployed and accessible in Render.com using
as user name and password alumnodb.
- It is possible to create and remove objects belonging to all the requested models
using the admin application.
- All the templates inherit from base.html.
- IMPORTANT: If you update the variable ALLOWED_HOSTS using a enviroment
variable add it to the env file.

# If the following criteria are accomplished, a grade up to 7.9 might be achieved::
- All the criteria in the previous paragraph are totally satisfied.
- Render.com is deployed in production mode. DEBUG=FALSE and SECRET_KEY is not stored in settings.py.
- All the views (classes/methods implemented in views.py) inherit from classes.
- When the tests are executed, the number of fails is not larger than two and the code that satisfies the tests is functional.
- The code is readable, efficient, well-structured, and commented.
- The tools provided by the framework are used.
- The following are examples of the previous points:
    * Every form that involves a model is created in such a way that it inherits directly or indirectly from class forms.Form.
    * The searches are done by the database. Do not not load all the elements of a table and implement the search in the views defined in view.py.
    * The errors are properly processed and understandable message errors are returned.
    * The code presents a consistent style and the functions are commented including their author. Note: the author of a function must be unique.
    * The style criteria highlighted by Flake8 are applied in a coherent way. Flake8 does not return any error when executed on the code programmed by the student.
- It is impossible to impersonate a user (or participant) without knowing their user name and password (or game.publicId). For example: (a) it is not possible to modify a questionnaire/question/answer without previously doing a login and accessing directly to the corresponding URL, (b) it is not possible to create answers guess without knowing the game.publicId, etc.

# If the following criteria are accomplished, a grade up to 8.9 might be achieved:
- All the previous criteria are accomplished completely.
- Every test and all the run checks output success results.
- If we reduce the size of the browser window or use the zoom, all the elements in the page are still accessible and no functionality is lost.

# To aim for the maximum grade, the following criteria must be accomplished:
- All the previous criteria are accomplished completely.
- The coverage for the files that contain the models, views, and forms is over 99%.
- Sound in pages seen by participants was implemented.