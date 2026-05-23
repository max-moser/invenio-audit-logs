# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-License-Identifier: MIT

"""View functions for audit logs API."""

from flask import Blueprint

blueprint = Blueprint("invenio_audit_logs", __name__)


def create_audit_logs_blueprint(app):
    """Create app blueprint."""
    ext = app.extensions["invenio-audit-logs"]
    return ext.audit_log_resource.as_blueprint()
