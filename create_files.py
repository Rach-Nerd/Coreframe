import os
import json

# Create the necessary files for the user by using a project name
def create_app(name):
    # Create the main project folder whose name is the project name
    os.makedirs(name, exist_ok=True)

    # Create a file called views.py where the user can define his views
    views_path = os.path.join(app_folder, "views.py")
    with open(views_path, "w") as f:
        f.write("# views for the {} app".format(name))

    # Create a file called urls.py where the user can define the routes and the corresponding view
    urls_path = os.path.join(app_folder, "urls.py")
    with open(urls_path, "w") as f:
        f.write("# urls for the {} app".format(name))

    # Create a server.py file that the user will use to run the server
    server_path = os.path.join(app_folder, "server.py")
    with open(coreframe_path, "w") as f:
        # Here we will place the server code. I will write this later
        f.write(some_code)

    # Create a file where the meta data about the project will be stored
    meta_path = os.path.join(app_folder, "meta.json")
    with open(meta_path, "w") as f:
        data = {"project": name}
        json.dump(data, f)