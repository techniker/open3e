"""Tests for O3Eclass resource handling."""

from unittest.mock import MagicMock


def _bare_instance():
    """Build an O3Eclass without running __init__ (which needs real CAN hardware)."""
    from open3e.Open3Eclass import O3Eclass

    o3e = O3Eclass.__new__(O3Eclass)
    o3e.uds_client = MagicMock()
    return o3e


class TestClose:
    """close() must release the socketcan fd, not just the UDS client.

    udsoncan closes the ISO-TP layer but never the underlying python-can bus,
    which leaks one raw CAN socket per ECU and produces
    'WARNING:can.bus:SocketcanBus was not properly shut down'.
    """

    def test_close_shuts_down_can_bus(self):
        o3e = _bare_instance()
        bus = MagicMock()
        o3e.bus = bus

        o3e.close()

        o3e.uds_client.close.assert_called_once()
        bus.shutdown.assert_called_once()
        assert o3e.bus is None, "handle must be cleared so the fd is not reused"

    def test_close_without_bus_is_safe(self):
        """DoIP mode has no CAN bus; close() must not raise."""
        o3e = _bare_instance()
        o3e.bus = None

        o3e.close()

        o3e.uds_client.close.assert_called_once()

    def test_close_survives_failing_shutdown(self):
        """A bus that errors on shutdown must not break engine cleanup."""
        o3e = _bare_instance()
        bus = MagicMock()
        bus.shutdown.side_effect = OSError("already gone")
        o3e.bus = bus

        o3e.close()

        bus.shutdown.assert_called_once()

    def test_close_is_idempotent(self):
        """_cleanup may close the same ECU twice; the fd is only released once."""
        o3e = _bare_instance()
        bus = MagicMock()
        o3e.bus = bus

        o3e.close()
        o3e.close()

        bus.shutdown.assert_called_once()
