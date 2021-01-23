# https://velog.io/@tree9295/pytest-python-%EC%BD%94%EB%93%9C%EB%A5%BC-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EB%B4%85%EC%8B%9C%EB%8B%A4

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import pytest
from sample.greeting import addvalue

def test_add():
    assert addvalue(3, 6) == 9
