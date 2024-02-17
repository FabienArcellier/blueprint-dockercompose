import os

import alfred


@alfred.command("test", help="run automatic test on docker image")
def hello_world():
    alfred.run('pytest test')
