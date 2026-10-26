import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def test_deps_yaml_scripts_exist():
    """deps_rocker copies each script_* entry into the image, so a missing one breaks rockerc."""
    for deps in REPO.glob("*.deps.yaml"):
        in_scripts = False
        for line in deps.read_text(encoding="utf-8").splitlines():
            if re.match(r"^\S", line):
                in_scripts = line.startswith("script_")
            elif in_scripts and (m := re.match(r"^\s*-\s*(\S+)", line)):
                assert (REPO / m.group(1)).is_file(), f"{deps.name} lists missing {m.group(1)}"


def test_dependabot_docker_dirs_have_a_dockerfile():
    """Dependabot reports a missing dependency file for a docker entry with no Dockerfile."""
    config = (REPO / ".github" / "dependabot.yml").read_text(encoding="utf-8")
    entries = re.findall(
        r'package-ecosystem:\s*"?docker"?\s*\n\s*directory:\s*"?([^"\n]+)"?', config
    )
    for directory in entries:
        assert (REPO / directory.lstrip("/") / "Dockerfile").is_file(), directory
