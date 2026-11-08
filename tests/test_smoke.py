from alltrader import __version__
from alltrader.cli import main


def test_package_smoke():
    assert __version__ == "0.1.0"
    assert main() == 0
