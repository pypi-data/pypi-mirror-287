# Gertrude --- GTD done right
# Copyright © 2023, 2024 Tanguy Le Carrour <tanguy@bioneland.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from abc import ABC, abstractmethod
from typing import Optional

from .entities import Project
from .value_objects import Name, ProjectId, ShortName


class Projects(ABC):
    @abstractmethod
    def all(self) -> list[Project]: ...

    @abstractmethod
    def by_id(self, id: ProjectId) -> Optional[Project]: ...

    @abstractmethod
    def by_name(self, name: Name) -> Optional[Project]: ...

    @abstractmethod
    def by_short_name(self, short_name: ShortName) -> Optional[Project]: ...

    @abstractmethod
    def save(self, project: Project) -> None: ...
