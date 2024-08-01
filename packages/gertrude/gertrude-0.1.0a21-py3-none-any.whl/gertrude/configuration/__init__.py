# Gertrude --- GTD done right
# Copyright © 2020-2022 Tanguy Le Carrour <tanguy@bioneland.org>
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

import os

PREFIX = "GERTRUDE_"


def read_config_from_env() -> dict[str, str]:
    result = {}
    for k, v in os.environ.items():
        if k.startswith(PREFIX):
            result[k[len(PREFIX) :]] = v
    return result
