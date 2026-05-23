# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-License-Identifier: MIT

"""Resources module."""

from .config import AuditLogResourceConfig
from .resource import AuditLogResource

__all__ = (
    "AuditLogResource",
    "AuditLogResourceConfig",
)
