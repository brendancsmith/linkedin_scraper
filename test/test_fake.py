import pytest


# TODO: Remove this file after adding real tests
@pytest.mark.skip(reason="Workaround to GH Actions considering 0 tests as failure")
def test_fake():
    assert True
