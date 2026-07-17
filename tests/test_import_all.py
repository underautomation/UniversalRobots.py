#!/usr/bin/env python3
"""
Exécute l'équivalent de:
    from underautomation.universal_robots.xxx import *
pour tous les modules et sous-packages découverts récursivement.

Usage:
    python scripts/import_star_all.py [nom_du_package]

Exemples:
    python scripts/import_star_all.py
    python scripts/import_star_all.py underautomation.universal_robots

Notes:
- Cette approche déclenche l'import réel et le "star import" (exec de "from X import *"),
  ce qui permet de détecter:
    * erreurs de syntaxe,
    * imports manquants,
    * problèmes dans __all__ (noms inexistants),
    * références circulaires déclenchées à l'import.
- Le script isole l'import * dans un namespace dédié pour chaque module pour éviter
  de polluer le namespace global du script.
- Retourne un code de sortie 1 si des imports échouent, 0 sinon.
"""

import os
import sys
import pkgutil
import importlib
import traceback

def iter_modules_and_packages(package_name: str):
    """Itère sur tous les modules et sous-packages (récursivement), en incluant d'abord le package racine."""
    # Commence par tester le package lui-même
    yield package_name, True  # True = is package (racine)
    try:
        pkg = importlib.import_module(package_name)
    except Exception:
        # Si le package racine ne s'importe pas, on ne peut pas aller plus loin
        return

    if not hasattr(pkg, "__path__"):
        # Ce n'est pas un package, rien à parcourir
        return

    # Parcours récursif de tout ce qui est sous le package
    for _, name, is_pkg in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
        yield name, is_pkg

def do_star_import(module_name: str):
    """
    Exécute 'from module_name import *' dans un namespace isolé.
    Lève une exception si l'import échoue.
    """
    ns = {}
    code = f"from {module_name} import *"
    exec(code, ns, ns)

def main():
    # Ajoute la racine du repo au PYTHONPATH pour un usage local
    repo_root = os.path.abspath(".")
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

    package_name = sys.argv[1] if len(sys.argv) > 1 else "underautomation.universal_robots"

    failures = []
    tested = 0

    print(f"[INFO] Parcours et 'import *' pour le package: {package_name}\n")

    for name, is_pkg in iter_modules_and_packages(package_name):
        tested += 1
        kind = "package" if is_pkg else "module"
        try:
            do_star_import(name)
            print(f"[OK] from {name} import *   ({kind})")
        except Exception as e:
            print(f"[FAIL] from {name} import *   ({kind})")
            failures.append((name, e, traceback.format_exc()))

    print("\n=== Résumé ===")
    print(f"Total testés: {tested}")
    print(f"Échecs: {len(failures)}")

    if failures:
        print("\nDétails des échecs:")
        for name, exc, tb in failures:
            print(f"\n--- {name} ---")
            print(f"{type(exc).__name__}: {exc}")
            print(tb)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()