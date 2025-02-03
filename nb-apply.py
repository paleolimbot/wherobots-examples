import sys
import glob
import subprocess
from pathlib import Path

here = Path(__file__).parent


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        raise ValueError(
            "Must supply at least one argument for jupyter nbconvert <args> <notebook>"
        )

    notebooks = glob.glob("**/*.ipynb", recursive=True)
    if not notebooks:
        raise ValueError("No notebooks in working directory")

    success = []
    for notebook in notebooks:
        nb_args = ["jupyter", "nbconvert"] + args + [notebook]

        result = subprocess.run(nb_args)

        if result.returncode == 0:
            print(f"✅ {nb_args}")
            success.append(True)
        else:
            print(f"❌ {nb_args}")
            success.append(False)

    if all(success):
        sys.exit(0)
    else:
        sys.exit(-1)
