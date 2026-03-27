"""Pytest configuration for the tsrl test suite."""
import os

import pytest


# ---------------------------------------------------------------------------
# Worker nice-ness (xdist workers only)
# ---------------------------------------------------------------------------

def pytest_configure(config):
    """Register the tsrl_nice_workers plugin if xdist is available."""
    config.pluginmanager.register(_NiceWorkersPlugin(), "tsrl_nice_workers")


class _NiceWorkersPlugin:
    """Lower the OS priority of xdist worker processes.

    Each worker detects that it *is* a worker via the ``workerinput`` attribute
    that xdist sets on the config object, then calls ``os.nice(10)`` once.
    This keeps parallel test runs from starving interactive processes.
    """

    def pytest_sessionstart(self, session):
        if getattr(session.config, "workerinput", None) is not None:
            # We are inside an xdist worker subprocess — lower priority.
            try:
                os.nice(10)
            except OSError:
                pass  # non-Unix or permission denied; ignore silently


# ---------------------------------------------------------------------------
# @pytest.mark.serial support
# ---------------------------------------------------------------------------

def pytest_collection_modifyitems(config, items):
    """Move @pytest.mark.serial tests to the 'serial' xdist group.

    xdist routes items with ``pytest.mark.xdist_group("serial")`` to a single
    worker, preserving ordering and preventing parallel interference.
    """
    for item in items:
        if item.get_closest_marker("serial"):
            item.add_marker(pytest.mark.xdist_group("serial"))
