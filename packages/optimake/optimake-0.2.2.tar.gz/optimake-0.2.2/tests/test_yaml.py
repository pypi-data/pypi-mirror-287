from pathlib import Path

import pytest
from optimake.config import Config

EXAMPLE_YAMLS = (Path(__file__).parent.parent / "examples").glob("*/optimade.yaml")


@pytest.mark.parametrize("path", EXAMPLE_YAMLS)
def test_example_yaml(path):
    assert Config.from_file(path)
