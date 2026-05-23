# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-License-Identifier: MIT

"""Audit Logs Service Permissions."""

from invenio_administration.generators import Administration
from invenio_records_permissions.generators import Disable, SystemProcess
from invenio_records_permissions.policies import BasePermissionPolicy


class AuditLogPermissionPolicy(BasePermissionPolicy):
    """Permission policy for audit logs."""

    can_search = [Administration(), SystemProcess()]
    can_create = [SystemProcess()]
    can_read = [Administration(), SystemProcess()]
    can_update = [Disable()]
    can_delete = [Disable()]
    can_create_or_update_many = [Disable()]
