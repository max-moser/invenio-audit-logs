# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-License-Identifier: MIT

"""Audit logs resource config."""

from invenio_records_resources.resources import (
    RecordResourceConfig,
    SearchRequestArgsSchema,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin
from marshmallow import fields


#
# Request args
#
class AuditLogSearchRequestArgsSchema(SearchRequestArgsSchema):
    """Search parameters for audit-logs."""

    id = fields.UUID()
    resource_id = fields.String()
    resource_type = fields.String()
    user_id = fields.String()
    action = fields.String()


#
# Resource config
#
class AuditLogResourceConfig(RecordResourceConfig, ConfiguratorMixin):
    """Audit-Logs resource configuration."""

    blueprint_name = "audit_logs"
    url_prefix = "/audit-logs"

    routes = {
        "list": "/",
        "item": "/<id>",
    }

    request_view_args = {
        "id": fields.UUID(),
    }

    request_search_args = AuditLogSearchRequestArgsSchema

    response_handlers = {
        "application/vnd.inveniordm.v1+json": RecordResourceConfig.response_handlers[
            "application/json"
        ],
        **RecordResourceConfig.response_handlers,
    }
