import shutil
from pathlib import Path

from sh import run_rstblog


def pr(line):
    print(line.strip())


def build(clean=False):
    if clean:
        build_dir = Path('_build')
        if build_dir.exists():
            shutil.rmtree(str(build_dir))
    run_rstblog.build(_out=pr)

def serve():
    return run_rstblog.serve(_out=pr)
