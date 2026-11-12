# Python Module 05: Environment Management, Configuration & Package Architecture
### Peer Evaluation Checklist, Study Notes & Theoretical Q&A

This document serves a dual purpose:
1. **Step-by-step verification guide** for peer evaluations.
2. **Conceptual reference & Q&A notes** answering the architectural and theoretical questions raised in the subject.


### Exercise 0: The Sealed Laboratory

#### Core Concepts & Study Notes
* **Virtual Environments (`venv`):** Isolated directory trees containing a specific Python interpreter binary and an independent `site-packages` folder. This prevents dependency conflicts between projects and avoids polluting or breaking the operating system's global Python installation.
* **`sys.prefix` vs `sys.base_prefix`:**
  * `sys.base_prefix`: Always points to the underlying system-wide Python installation.
  * `sys.prefix`: Points to the currently active Python environment. Inside an active `venv`, `sys.prefix != sys.base_prefix`.
* **`pip` + `requirements.txt` vs. Poetry + `pyproject.toml`:**
  * `requirements.txt` is a flat list of dependencies installed via `pip`. It does not natively enforce deterministic lockfiles or isolate environments on its own.
  * **Poetry** (`pyproject.toml` + `poetry.lock`) manages environment creation, dependency resolution (SAT solver), and deterministic builds under the modern PEP 518/621 standard.

#### Subject Questions & Evaluation Q&A

> **Q1: What does a virtual environment actually isolate, and what does it NOT isolate?**  
> **A:** What it isolates: Only your Python packages (site-packages) and their CLI commands. Each project gets its own separate folder of libraries so versions don't clash between projects.
> 
> What it does NOT isolate: The operating system, your files/network, or the base Python version itself (it just links to the Python already installed on your machine—it's not a virtual machine or Docker).

> **Q2: Why would you ever choose Poetry over a plain requirements.txt?**  
> **A:** Exact reproducibility (poetry.lock): requirements.txt only lists the packages you write, but their sub-dependencies can change and break your code later. Poetry locks the exact version of every dependency and sub-dependency so it works identically on every computer.
> 
> Smart conflict resolution & cleanup: Poetry checks that all library versions are compatible before installing, separates dev tools (like flake8) from production in one file, and removes unused sub-dependencies when you uninstall a package (whereas pip leaves junk behind).

> **Q3: Why is installing packages into the global Python environment dangerous?**  
> **A:** Different projects often require incompatible versions of the same library (e.g., Project A needs `numpy==1.24` while Project B requires `numpy==2.0`). Installing globally causes version collisions ("dependency hell") and can break critical OS utilities that rely on system Python packages.

> **Q4: How does Python know whether it is running inside a virtual environment?**  
> **A:** When a `venv` is activated, Python reads its `pyvenv.cfg` file and updates `sys.prefix` to point to the virtual environment's directory, while `sys.base_prefix` remains anchored to the base system installation. Comparing `sys.prefix != sys.base_prefix` reliably detects isolation.

> **Q5: Why did we set `package-mode = false` in `pyproject.toml`?**  
> **A:** Because we are using Poetry strictly as a dependency and environment manager for standalone scripts (`loading.py`), rather than building a distributable wheel/sdist package to publish on PyPI. Without `package-mode = false`, Poetry expects a matching package folder and a `README.md` inside `ex0/`.

#### Step-by-Step Verification

1. **Scenario A — Unsealed Environment (Global):**
   Ensure that no virtual environment is active in your current shell (run `deactivate` if needed):

   ```bash
   python3 ex0/construct.py
   ```

   * **Expected:** Detects `sys.prefix == sys.base_prefix` and warns that the laboratory is **not sealed** and that installing reagents directly into the global system is unsafe.

2. **Scenario B — Sealed Environment (`venv`):**
   ```bash
   python3 -m venv lab_env
   source lab_env/bin/activate
   python3 ex0/construct.py
   ```
   * **Expected:** Confirms the laboratory is **sealed**, showing the interpreter path inside `lab_env` and the isolated `site-packages` path.

3. **Reagents Verification (`pip` and `requirements.txt`):**
   ```bash
   python3 ex0/loading.py                 # Runs before install -> graceful warning, no crash
   pip install -r ex0/requirements.txt    # Installs pandas/numpy
   python3 ex0/loading.py                 # Runs after install -> progress bar + versions
   ```

4. **Poetry Verification:**
   ```bash
   deactivate
   cd ex0
   poetry install
   poetry run python loading.py
   ```


### Exercise 1: The Matrix Oracle

#### Core Concepts & Study Notes
* **Twelve-Factor App Configuration:** Configuration that varies between environments (`development`, `staging`, `production`) must be separated from source code and injected via environment variables.
* **Precedence Hierarchy:** Shell environment variables (`os.environ`) **always override** values defined in `.env` files (`load_dotenv(override=False)` is the default behavior). This allows operators to override settings in production without modifying files on disk.
* **Secret Management:** Never commit `.env` files containing real credentials to Git. Commit `.env.example` with safe placeholder templates and list `.env` in `.gitignore`.

#### Subject Questions & Evaluation Q&A

> **Q1: Why is an environment variable a better place for a secret than a constant in your source code? What is still not safe about it?**  
> **A:** Why it's better: It keeps secrets out of Git history (where deleted constants remain visible forever) and lets you change keys across development and production servers without modifying source code.
> 
> What is still NOT safe: Environment variables live in plaintext in memory. They can still leak through inherited child processes (subprocess), accidental debug/crash logs, plain .env files on disk, or /proc/<PID>/environ inspection on Linux.

> **Q2: What happens if `load_dotenv()` is called when a variable is already exported in the terminal shell?**  
> **A:** By default (`override=False`), `python-dotenv` will **not** overwrite existing shell environment variables. Shell exports take highest precedence, enabling commands like `MATRIX_MODE=production python3 oracle.py` to override local `.env` settings seamlessly.

> **Q3: Why mask secrets in `production` mode while showing them in `development` mode?**  
> **A:** In `development`, developers need visibility to verify configuration loading and debug connection strings. In `production`, logs and terminal outputs are often captured by monitoring systems or shared across teams; masking prevents accidental credential leaks.

> **Q4: What is the difference between `.env` and `.env.example`?**  
> **A:** `.env.example` is tracked in Git and documents the required configuration keys with dummy values so teammates know what to configure. `.env` contains actual environment-specific secrets and is strictly excluded via `.gitignore`.

#### Step-by-Step Verification

1. **Environment setup:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r ex1/requirements.txt
   ```

2. **Scenario A — Missing `.env` (Fallback & Warnings):**
   ```bash
   cd ex1
   python3 oracle.py
   ```
   * **Expected:** Lists the 5 missing keys with a clean warning, falls back to `development` defaults, and displays `[OK]` on security checks.

3. **Scenario B — Local `.env` Loaded:**
   ```bash
   cp .env.example .env
   python3 oracle.py
   ```
   * **Expected:** Loads values cleanly with no missing-key warnings; API key is visible in `development` mode.

4. **Scenario C — Production Shell Override:**
   ```bash
   MATRIX_MODE=production python3 oracle.py
   ```
   * **Expected:** Switches mode to `production` and masks `API_KEY` (`************************`).


### Exercise 2: The Sacred Scroll

#### Core Concepts & Study Notes
* **Packages vs. Modules:** A `.py` file is a **module**. A directory containing an `__init__.py` file is a **package**.
* **Controlling the Public API (`__init__.py`):** When a user imports a package (`import alchemy`), Python executes `alchemy/__init__.py`. Anything imported or defined inside `__init__.py` becomes accessible directly at the package level (`alchemy.create_fire()`). Submodules not imported there remain hidden unless explicitly accessed (`alchemy.elements.create_earth()`).
* **Package Metadata:** Dunder attributes like `__version__` and `__author__` defined in `__init__.py` provide standard package introspection.

#### Subject Questions & Evaluation Q&A

> **Q1: alchemy/elements.py defines create_earth, yet ft_alembic_1.py cannot reach it through import alchemy. Nothing was hidden, nothing was made private. So what exactly did __init__.py change?**  
> **A:** Python packages don't auto-expose their submodules. __init__.py controls what gets bound to the top-level package namespace when you run import alchemy. Nothing was made private—create_earth just wasn't imported into alchemy's namespace, so the alchemy object has no attribute with that name (raising an AttributeError), though it remains fully accessible via alchemy.elements.create_earth().

> **Q2: Why are `create_fire` and `create_water` accessible via `alchemy.create_fire()`, while `create_earth` raises an `AttributeError`?**  
> **A:** Because `alchemy/__init__.py` explicitly imports `create_fire` and `create_water` from `.elements`, binding them to the `alchemy` package namespace. `create_earth` and `create_air` are not imported in `__init__.py`, so they remain encapsulated inside the `alchemy.elements` submodule.

> **Q3: What is the purpose of `__all__` in `__init__.py`?**  
> **A:** `__all__` defines the official list of public symbol names exported when someone performs `from alchemy import *` and serves as explicit documentation for linters (`flake8` F401) and developers about which attributes belong to the public interface.

#### Step-by-Step Verification

1. **Execution:**
   ```bash
   cd ex2
   python3 ft_sacred_scroll.py
   ```
   * **Expected:**
     - `alchemy.elements.*` calls all 4 functions successfully.
     - `alchemy.create_fire()` and `alchemy.create_water()` succeed.
     - `alchemy.create_earth()` and `alchemy.create_air()` raise `AttributeError` (caught and displayed).
     - Prints `__version__` and `__author__`.


### Exercise 3: The Transmutation

#### Core Concepts & Study Notes
* **Absolute Imports (`from alchemy.elements import create_fire`):** Specify the full module path starting from the top-level package root (`sys.path`). They are unambiguous, easy to read, and recommended by PEP 8 for general use.
* **Relative Imports (`from .basic import lead_to_gold`, `from ..potions import healing_potion`):** Use leading dots to navigate relative to the current module's `__name__` within the package hierarchy:
  * `.` = current package directory
  * `..` = parent package directory
* **Execution Context Rule:** Files using relative imports cannot be executed directly as standalone scripts (`python3 alchemy/transmutation/advanced.py` fails with `ImportError: attempted relative import with no known parent package`); they must be imported through a top-level entry point (`ft_pathway_debate.py`) or run with `python3 -m`.

#### Subject Questions & Evaluation Q&A

> **Q1: When should you choose absolute imports vs. relative imports?**  
> **A:** **Absolute imports** are preferred across distinct subpackages or external boundaries because they clearly state where a resource lives and won't break if the importing file is moved. **Relative imports** are useful inside tightly coupled internal subpackages so that renaming the top-level package doesn't require rewriting internal imports.

> **Q2: Why does running a file with relative imports directly (`python3 advanced.py`) fail?**  
> **A:** When Python runs a file directly, its `__name__` is set to `"__main__"` instead of its package path (`"alchemy.transmutation.advanced"`), so Python has no package hierarchy context to resolve `.` or `..`.

#### Step-by-Step Verification

1. **Execution:**
   ```bash
   cd ex3
   python3 ft_pathway_debate.py
   ```
   * **Expected:** Confirms `basic.py` (absolute imports), `advanced.py` (relative imports), and `alchemy.transmutation` package-level access all resolve and return the expected strings.

---

### Exercise 4: The Grimoire (Circular Dependencies)

#### Core Concepts & Study Notes
* **How Python Imports Work (`sys.modules`):**
  1. When module `A` is imported, Python creates an empty module object in `sys.modules['A']` *before* executing `A`'s code top-to-bottom.
  2. If `A` executes `from B import func_b` on line 1, Python pauses `A` and starts executing `B`.
  3. If `B` executes `from A import func_a` on line 1, Python sees `'A'` is already in `sys.modules`, skips re-executing `A`, and immediately looks for `func_a` inside the half-empty `A` object. Since `A` paused on line 1, `func_a` hasn't been defined yet $\rightarrow$ **`ImportError`**.
* **Resolution Patterns:**
  1. **Import the module object, not the symbol (`from . import light_validator`):** Python binds the reference to the module object in `sys.modules` immediately without requiring its functions to exist at load time. Attribute lookup (`light_validator.validate_ingredients(...)`) happens later at runtime when both modules have finished loading.
  2. **Deferred / Local Imports:** Placing `from .light_validator import validate_ingredients` inside the function body rather than at the top of the file.
  3. **Dependency Inversion / Shared Module:** Extracting shared data (`allowed_ingredients`) into a third neutral module that both import without referencing each other.

#### Subject Questions & Evaluation Q&A

> **Q1: Both grimoires describe two files that need each other. Why does only one of them explode?**  
> **A:** Both have a circular dependency, but from .module import func (Dark Grimoire) forces Python to resolve func immediately while the module is still half-loaded (causing ImportError). Importing the module object (from . import module in Light Grimoire) only binds a reference to the module in sys.modules and delays looking up the function until runtime, after both files have finished loading.

> **Q2: Why does `ft_kaboom_1.py` crash with `ImportError: cannot import name ... from partially initialized module`?**  
> **A:** Because `dark_spellbook.py` and `dark_validator.py` both perform top-level symbol imports (`from .module import function`) of each other. `dark_spellbook` pauses before defining `dark_spell_allowed_ingredients` while waiting for `dark_validator` to load, and `dark_validator` immediately tries to extract that not-yet-defined symbol from the partially initialized `dark_spellbook` module.

> **Q3: How did you solve the circular dependency in the Light Grimoire, and what are the alternatives?**  
> **A:** In `light_spellbook.py` and `light_validator.py`, we imported the **entire module objects** (`from . import light_validator` and `from . import light_spellbook`) rather than specific symbols. Because Python registers the module object in `sys.modules` before executing its body, both files receive a valid module reference and defer function resolution until runtime. Alternative solutions include **local imports inside functions** or **refactoring shared constants into a separate third module**.

#### Step-by-Step Verification

1. **Scenario A — Circular Import Failure (`ft_kaboom_1.py`):**
   ```bash
   cd ex4
   python3 ft_kaboom_1.py
   ```
   * **Expected:** Catches and displays the circular `ImportError` on `dark_spell_allowed_ingredients`.

2. **Scenario B — Resolved Dependency (`ft_kaboom_0.py`):**
   ```bash
   python3 ft_kaboom_0.py
   ```
   * **Expected:** Executes cleanly and prints `Testing record light spell: Spell recorded: Fantasy (Earth, wind and fire - VALID)`.