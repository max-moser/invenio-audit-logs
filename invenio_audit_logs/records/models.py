# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-License-Identifier: MIT

"""Base model classes for Audit Logs in Invenio."""

from invenio_db import db
from invenio_records.models import RecordMetadataBase
from sqlalchemy.types import String


class AuditLog(db.Model, RecordMetadataBase):
    """Model class for Audit Log."""

    __tablename__ = "audit_logs_metadata"

    encoder = None

    action = db.Column(String(255), nullable=False)

    resource_type = db.Column(String(255), nullable=False)

    user_id = db.Column(String(255), nullable=False)
