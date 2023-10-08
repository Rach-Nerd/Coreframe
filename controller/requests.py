import os
import importlib.util
import re

def handle_request(project_path, route, method, form):
    # Get the HTML code for the route by using a get_view function
    response_body = get_view(route, project_path)

    # Return 404 Error if there is no response
    if not response_body:
        return "HTTP/1.1 404 Not Found\nContent-Type: text/plain\nContent-Length: 9\n\nNot Found"

    # Else, return the response in HTTP format with a code of 200 (success)
    # Embed the HTML code within this response
    return "HTTP/1.1 200 OK\nContent-Type: text/html\nContent-Length: {}\n\n{}".format(len(response_body), response_body)

def extract_function(urls_page_content, route):
    # Find the urls array defined
    match = re.search(r"urls = (\[.+\])", urls_page_content)
    if not match:
        return False

    # Process the urls array
    urls = eval(match.group(1))

    # Find the correct route and return it
    for u in urls:
        if u[0] == url:
            return u[1]
    return False

def get_view(route, project_path):
    # Getting the urls.py file
    urls_path = os.path.join(project_path, "urls.py")

    # If the file does not exist, return False
    if not os.path.exists(urls_path):
        return False

    # Read the contents of the urls.py file
    with open(urls_path, "r") as f:
        contents = f.read()

    # Step 1: Get the function name from the urls.py that corresponds to the provided route
    function_name = extract_function(contents, route)

    # Find the views.py file
    views_path = os.path.join(project_path, "views.py")

    # Extract the file's content
    spec = importlib.util.spec_from_file_location("views", str(views_path))
    views_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(views_module)

    # Get the function from the file
    view_func = getattr(views_module, function_name)

    # Return the template from the view
    return view_func()