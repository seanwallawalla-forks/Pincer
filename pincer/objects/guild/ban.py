# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from ...utils import APIObject

if TYPE_CHECKING:
    from ..user.user import User


@dataclass
class Ban(APIObject):
    """Representation of the Discord Ban object

    Attributes
    ----------
    reason: Optional[:class:`str`]
        The reason for the ban
    user: :class:`~pincer.objects.user.user.User`
        The banned user
    """
    reason: Optional[str]
    user: User
