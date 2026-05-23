# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-License-Identifier: MIT

"""Module tests."""

from flask import Flask

from invenio_audit_logs import InvenioAuditLogs


def test_version():
    """Test version import."""
    from invenio_audit_logs import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioAuditLogs(app)
    assert "invenio-audit-logs" in app.extensions

    app = Flask("testapp")
    ext = InvenioAuditLogs()
    assert "invenio-audit-logs" not in app.extensions
    ext.init_app(app)
    assert "invenio-audit-logs" in app.extensions
