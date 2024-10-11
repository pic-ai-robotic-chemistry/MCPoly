import pytest
from MCPoly.orcaset import multiorca
from MCPoly.status import status
from MCPoly import view3d
from MCPoly.sscurve import multiple
from MCPoly.lmpset import mould
from MCPoly.moldraw import molecule

def object_orcaset():
    return multiorca(['Atoms1', 'Atoms2'], loc='./MCPoly/tests/data_orcaset/')

def object_status():
    return status('Atoms1', loc='./MCPoly/tests/data_status/')

def object_sscurve():
    return multiple(['Polymer1','Polymer2'], loc='./MCPoly/tests/data_sscurve/')

def object_lmpset():
    return mould('CCOH', loc='./MCPoly/tests/data_lmpset/')

def test_view3d():
    return view3d('Atoms1',loc='./MCPoly/tests/data_status/')

# Under Construction
def object_moldraw():
    return molecule('Bu', loc='./MCPoly/tests/data_moldraw/')