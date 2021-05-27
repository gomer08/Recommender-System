# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc_rules.krb'):
           [1622072612.1360707, 'bc_rules_bc.py'],
         ('', '', 'facts.kfb'):
           [1622072612.1617718, 'facts.fbc'],
        },
        compiler_version)

