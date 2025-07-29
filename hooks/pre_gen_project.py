import re
import sys


NAMESPACE_REGEX = r"^[a-z][_a-z0-9]*(\.[a-z][_a-z0-9]*)*$"
namespace_import = "{{ cookiecutter.project_namespace_import }}"
if namespace_import and not re.match(NAMESPACE_REGEX, namespace_import):
    print(f"ERROR: '{namespace_import}' is not a valid Python namespace import path!")
    print(
        f"       It must follow regex '{NAMESPACE_REGEX}', i.e. 'one_two' or 'one_two.three'"
    )
    sys.exit(1)


PROJECT_NAME_REGEX = r"^[a-zA-Z][ _a-zA-Z0-9]*[a-zA-Z0-9]$"
project_name = "{{ cookiecutter.project_name }}"
if not re.match(PROJECT_NAME_REGEX, project_name):
    print(f"ERROR: '{project_name}' is not a valid project name!")
    print(f"       It must follow regex '{PROJECT_NAME_REGEX}'")
    sys.exit(1)


PROJECT_SLUG_REGEX = r"^[a-z][-a-z0-9]*[a-z0-9]$"
project_slug = "{{ cookiecutter.project_slug }}"
if not re.match(PROJECT_SLUG_REGEX, project_slug):
    print(f"ERROR: '{project_slug}' is not a valid project slug!")
    print(f"       It must follow regex '{PROJECT_SLUG_REGEX}'")
    sys.exit(1)


ENTRY_POINT_REGEX = PROJECT_SLUG_REGEX
entry_point = "{{ cookiecutter.entry_point }}"
if entry_point and not re.match(ENTRY_POINT_REGEX, entry_point):
    print(f"ERROR: '{entry_point}' is not a valid project entry point!")
    print(f"       It must follow regex '{ENTRY_POINT_REGEX}'")
    sys.exit(1)
