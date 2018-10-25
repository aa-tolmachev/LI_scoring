from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

#import main
from Moduls import main as main

#import NBKI_DPL
from Moduls.NBKI_PDL import *
#import Moduls.NBKI_PDL  as NP
from Moduls.CLIENT_INFO import *

