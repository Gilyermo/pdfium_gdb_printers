import gdb.printing
from . import core

def register_printers(obj):
    gdb.printing.register_pretty_printer(obj, core.printer)
