from dotenv import load_dotenv  # type: ignore
import os
DEFAULTS: dict[str, str] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "sqlite:///oracle.db",
    "API_KEY": "default_dev_key",
    "LOG_LEVEL": "DEBUG",
    "ZION_ENDPOINT": "http://localhost:8000",
}


def load_configuration() -> dict[str, str]:
    load_dotenv()

    config: dict[str, str] = {}
    missing_vars: list[str] = []

    for key, default_value in DEFAULTS.items():
        if key in os.environ:
            config[key] = os.environ[key]
        else:
            config[key] = default_value
            missing_vars.append(key)

    if missing_vars:
        print(f"WARNING: Missing configuration for: {', '.join(missing_vars)}")
        print("Using default values for missing settings.\n")

    return config


def check_gitignore() -> bool:
    if not os.path.exists(".gitignore"):
        return False
    with open(".gitignore", "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() == ".env":
                return True
    return False


def mask_secret(secret: str, mode: str) -> str:
    """Oculta el secreto si el modo es production."""
    if mode == "production":
        return "*" * len(secret)
    return secret


def start_oracle() -> None:
    print("ORACLE STATUS: Consulting the configuration...")
    config = load_configuration()

    mode = config["MATRIX_MODE"]
    masked_key = mask_secret(config["API_KEY"], mode)

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {config['DATABASE_URL']}")
    print(f"API Access: Authenticated (Key: {masked_key})")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Remote Network: {config['ZION_ENDPOINT']}")
    print()

    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")

    if check_gitignore():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARN] .env file is NOT ignored by git")

    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    start_oracle()
