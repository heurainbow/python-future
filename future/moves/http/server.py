from __future__ import absolute_import
from future.utils import PY3

if PY3:
    from http.server import *
else:
    from BaseHTTPServer import *
    from CGIHTTPServer import *
    from SimpleHTTPServer import *
    from CGIHTTPServer import _url_collapse_path     # needed for a test
