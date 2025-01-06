# {{ cookiecutter.project_name }}

<!--- BADGES: START --->
[![CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/tests.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/tests.yml)
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }})
[![Packaging status](https://repology.org/badge/tiny-repos/python:{{ cookiecutter.project_slug }}.svg)](https://repology.org/project/python:{{ cookiecutter.project_slug }}/versions)
<!--- BADGES: END --->

{{ cookiecutter.project_description }}

## License
{%- if cookiecutter.license == "Apache 2.0" %}
```
Copyright {% now 'local', '%Y' %} {{ cookiecutter.author_name }}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
{%- elif cookiecutter.license == "AGPL v3" %}
```
Copyright (C) {% now 'local', '%Y' %}  {{ cookiecutter.author_name }}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
{%- elif cookiecutter.license == "Proprietary" %}
```
Copyright (C) {{ cookiecutter.author_name }}. All rights reserved.

Please contact {{ cookiecutter.author_email }} for licensing terms.
```
{%- endif %}
