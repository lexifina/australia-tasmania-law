"""What did a Tasmanian Act say on a day?

    python tools/in_force_on.py 2010-01-01 acts-interpretation-act-1931            # the whole Act
    python tools/in_force_on.py 2010-01-01 acts-interpretation-act-1931 24         # section 24
    python tools/in_force_on.py 2010-01-01 acts-interpretation-act-1931 "sch-1/cl-3"
    python tools/in_force_on.py 2010-01-01 acts-interpretation-act-1931 --commit   # the commit and why

Reads the In-force trailers on main (main is in in-force order), so a commit counts from its in-force day, not from
its git date.
"""
import re
import subprocess
import sys


def git(*a) -> str:
    return subprocess.run(['git', *a], capture_output=True, encoding='utf-8', errors='replace').stdout


def key_of(p: str) -> str:
    p = p.strip()
    if re.fullmatch(r'\d+[A-Za-z]*', p):
        m = re.match(r'(\d+)(.*)', p)
        return f's-{m.group(1).zfill(3)}{m.group(2)}'
    m = re.fullmatch(r'(sch-[^/]+)/(s|cl)-?(\d+)([A-Za-z]*)', p)
    if m:
        return f'{m.group(1)}/{m.group(2)}-{m.group(3).zfill(3)}{m.group(4)}'
    return p.removesuffix('.md')


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    day, act = sys.argv[1], sys.argv[2].strip('/')
    rest = [a for a in sys.argv[3:] if a != '--commit']
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', day):
        sys.exit('day must be YYYY-MM-DD')
    log = git('log', 'main', '--format=%H%x1f%(trailers:key=In-force,valueonly,separator=)', '--', act + '/')
    sha = None
    for line in log.splitlines():
        h, _, when = line.partition('\x1f')
        if when.strip() and when.strip() <= day:
            sha = h
            break
    if not sha:
        sys.exit(f'{act}: no version in force on {day} in this record')
    if '--commit' in sys.argv:
        print(git('log', '-1', '--format=%H%n%an%n%n%B', sha))
        return
    if rest:
        path = f'{act}/{key_of(rest[0])}.md'
        out = git('show', f'{sha}:{path}')
        if not out:
            sys.exit(f'{path}: not in force on {day} (no such provision in that version)')
        sys.stdout.write(out)
        return
    files = [f for f in git('ls-tree', '-r', '--name-only', sha, '--', act + '/').splitlines() if f.endswith('.md')]

    def order(f):
        return [int(x) if x.isdigit() else x for x in re.split(r'(\d+)', f)]
    for f in sorted(files, key=order):
        sys.stdout.write(f'==> {f}\n' + git('show', f'{sha}:{f}') + '\n')


if __name__ == '__main__':
    main()
