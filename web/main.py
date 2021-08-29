import os
import sys

if os.path.abspath(os.curdir) not in sys.path:
     print('...missing directory in PYTHONPATH... added!')
     sys.path.append(os.path.abspath(os.curdir))

from api import create_app
from instance.config import Config

app = create_app()
app.app_context().push()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=Config.API_PORT, debug=True)
