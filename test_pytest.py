import pytest
@pytest.mark.skip
def test_one():
    print("tes_one")

def test_two():
    print("tes_two")
@pytest.fixture(scope="function",autouse=True)
def test_three():
    print("tes_three")
