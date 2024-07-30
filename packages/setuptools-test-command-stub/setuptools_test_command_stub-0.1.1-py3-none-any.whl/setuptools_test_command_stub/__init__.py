def patch():
    import sys
    from unittest.mock import MagicMock

    try:
        from build._builder import _DEFAULT_BACKEND
    except ImportError:
        ...
    else:
        # For bypassing ProjectBuilder.from_isolated_env
        _DEFAULT_BACKEND["requires"] = "setuptools-test-command-stub"

    sys.modules["setuptools.command.test"] = MagicMock()
