from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]



from test_import_2.t_a import *
import test_import_2.t_a  as t_a

from test_import_2.t_b import *
import test_import_2.t_b  as t_b