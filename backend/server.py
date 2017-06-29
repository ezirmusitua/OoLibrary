# -*- coding: utf-8 -*-
import os
from flask import Flask, abort, send_file, render_template

app = Flask(__name__, template_folder='./templates')


@app.route('/', defaults={ 'path': '' })
@app.route('/<path:path>')
def catch_all(path):
    base_dir = r'/'

    # Joining the base and the requested path
    abs_path = os.path.join(base_dir, path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('template.html', files=files)


if __name__ == '__main__':
    app.run(debug=True)
