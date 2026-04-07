from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def default_target_dir() -> Path:
    return Path.home() / ".ai-skills" / "implementation-explainer"


def install_skill(repo_root: Path, target_dir: Path) -> Path:
    source = repo_root / "skill" / "implementation-explainer"
    destination = target_dir

    if not source.exists():
        raise FileNotFoundError(f"Skill source folder not found: {source}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)

    shutil.copytree(source, destination)
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the implementation-explainer skill package."
    )
    parser.add_argument(
        "--target-dir",
        type=Path,
        default=default_target_dir(),
        help="Directory where the skill should be installed. Defaults to ~/.ai-skills/implementation-explainer.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    destination = install_skill(repo_root=repo_root, target_dir=args.target_dir.expanduser())
    print(f"Installed skill to: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
