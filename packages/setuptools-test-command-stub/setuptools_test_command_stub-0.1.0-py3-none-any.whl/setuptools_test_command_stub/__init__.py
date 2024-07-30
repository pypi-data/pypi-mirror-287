def patch():
    import sys
    from unittest.mock import MagicMock

    sys.modules["setuptools.command.test"] = MagicMock()
