def render_template(file_path):
    # Open the HTML file that the user will provide and read its content
    with open(file_path) as f:
        template = f.read()

    # If the HTML file is empty, return an error message
    if os.path.exists(file_path) and not template:
        template = f"<p>The HTML file at {file_path} was empty</p>"

    # Else, return the HTML code inside the file
    return template