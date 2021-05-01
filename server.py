#gunicorn
#model -> View -> Templete -> Response

# Load html template
# ------------------
def load_template(template_name='', context={}):
    html_data = ""
    with open(template_name, 'r') as f:
        html_data = f.read()
        html_data = html_data.format(**context)
    return html_data

# File and Path setup
# ------------------
def app(environ, start_response):
    path = environ.get("PATH_INFO")

    if path.endswith("/"):
        path = path[:-1]

    if path == "": # index / root
        data = home(environ)
    elif path == "/contact":
        data = contact_us(environ)
    else:
        data = load_template(template_name='404.html', context={"path": path})

    data = data.encode("utf-8")

    start_response(
        f"200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])

# Routing
# -------
def home(environ):
    return load_template(template_name='index.html',  context={})

def contact_us(environ):
    return load_template(template_name='contact.html', context={})