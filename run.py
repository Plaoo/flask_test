'''Questo file si occupa di caricare il server, caricando i file
precedentemente creati'''
import os

# from esempi.db import app
# from esempi.simple import app
# from esempi.html_inline import app
# from esempi.html_inline_second import app
# from esempi.html_esterno import app
# from esempi.routing import app
# from esempi.custom_errors import app
#from esempi.request_info import app
#from esempi.redirects import app
from esempi.database import app

if __name__ == "__main__":
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))

    app.run(host=host, port=port)
