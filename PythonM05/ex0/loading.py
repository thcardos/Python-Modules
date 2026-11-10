import importlib


def check_dependency(module_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "unknown")
        return True, str(version)
    except ModuleNotFoundError:
        return False, ""


def load_reagents() -> None:
    reagents: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
    }

    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")

    missing: list[str] = []

    for name, description in reagents.items():
        is_installed, version = check_dependency(name)
        if is_installed:
            print(f"[OK] {name} ({version}) - {description}")
        else:
            print(f"[MISSING] {name} - Not installed")
            missing.append(name)

    print()
    if missing:
        print("WARNING: Missing reagents detected!")
        print("Install with pip:")
        print("pip install -r ex0/requirements.txt")
        print("\nInstall with Poetry:")
        print("poetry install")
    else:
        print("pip vs Poetry:")
        print(
            "requirements.txt declares what to install; "
            "pip resolves it at install time."
        )
        print(
            "pyproject.toml declares the same constraints, "
            "and Poetry pins the resolved"
        )
        print("versions in poetry.lock so every install is identical.")
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    load_reagents()
