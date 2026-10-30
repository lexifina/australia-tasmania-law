# Tasmania law, change by change

Every Tasmanian principal Act in force on 2026-10-29 (609 of 609 built), and every principal
statutory rule in force that day (1365 of 1365 built, in [`subordinate/`](subordinate)), as a git
repository, version by version from 1994-03-15. Each change is
one commit, credited to the amending law that made it and dated the day it took effect, at noon in Hobart. The text
is Tasmanian Legislation's point-in-time consolidation of each Act and statutory rule, read as XML from
[Tasmanian Legislation](https://www.legislation.tas.gov.au) (Office of Parliamentary Counsel, Tasmania).

## The questions, as git commands

| Question | Command |
| --- | --- |
| What did section 24 of the Acts Interpretation Act 1931 say on 1 January 2005? | `python tools/in_force_on.py 2005-01-01 acts-interpretation-act-1931 24` |
| The whole Act as it stood on 1 January 2005 | `python tools/in_force_on.py 2005-01-01 acts-interpretation-act-1931` |
| The commit that holds that day's text, and why it was made | `python tools/in_force_on.py 2005-01-01 acts-interpretation-act-1931 --commit` |
| Which Act wrote each line of a section? | `git blame acts-interpretation-act-1931/s-024.md` |
| Every change to a section, with the Act and the day | `git log --follow acts-interpretation-act-1931/s-024.md` |
| Everything one amending Act changed | `git show --stat act/2001-82` |
| The text of one point-in-time version | `git show acts-interpretation-act-1931/2022-10-24:acts-interpretation-act-1931/s-004.md` |
| What changed between two versions | `git diff --stat acts-interpretation-act-1931/2001-12-01 acts-interpretation-act-1931/2022-10-24` |
| Changes no single Act explains | `git log --grep="^Kind: "` |
| Every change with its Act and day | [`changes.csv`](changes.csv) |
| A statutory rule's provision on a day | `python tools/in_force_on.py 2024-01-01 subordinate/education-regulations-2017 2` |
| Every change to the statutory rules | `git log -- subordinate/` |
| Everything one law changed in the statutory rules | `git show --stat subordinate/sr/<year>-<number>` (or `subordinate/act/...`) |

## Dates

**Commits are dated the day the change took effect**, at noon in Hobart: AEST (UTC+10), or AEDT (UTC+11) in daylight
saving time (Tasmania's own rules, hard-coded). The day is the first day of the point-in-time version the change
first appears in (`FIRST.VALID.DATE`). Every commit carries `In-force: YYYY-MM-DD`; the Royal Assent day, where the
source records it, is in `Assented:`. To ask what the law was on a day, use `tools/in_force_on.py`, which reads the
trailer. Versions that take effect after 2026-10-29 are on the `future` branch, which is never merged.

The database's point-in-time record begins on 1994-03-15. The first commit of each Act is its version on that day
(or, for later Acts, its first version), which already holds every earlier amendment; those are not replayed.

## What "author" means

The author of a commit is the Act that made the change, with an address ending `@legislation.tas.invalid` that
cannot exist, so `git blame` names the Act: `Parliamentary Privilege Amendment Act 2001 (No. 82 of 2001)`. Changes
are credited from the source's commencement records (each records the amending Act, the day it commenced and the
provisions it affected) and its history notes. Per changed provision, on a version's first day:

- the one Act that commenced that day and whose commencement record names the provision; else
- the one such Act whose history note in the new version names it; else
- when only one Act commenced on that title that day, that Act, with `Evidence: commencement date only`.

Anything else is labelled and committed by `Tasmanian Legislation (Office of Parliamentary Counsel)`, never guessed:
`Kind: two or more Acts` (two or more name the provision; `Candidate:` trailers list them), `Kind: Act not
identified` (several Acts commenced and none names it), `Kind: no Act named` (no commencement record that day), and
`Kind: first version in the database` (the first commit of each Act).

## Files

One folder per Act (`<slug>/`), one file per section (`s-024.md`), per schedule (`sch-1.md`), per schedule
clause or section (`sch-1/cl-003.md`), plus `front.md` (title, long title, preamble, enacting words) and
`headings.md` (Part, Division and Chapter headings). One paragraph per line. A repealed provision has no file.
The source's history notes ("Section 4 amended by No. 38 of 1963") are not reproduced; a picture (a form, a plan)
is a line `[Picture in the source, not reproduced]`. Tables are one row per line, cells separated by ` | `.
Dates the source holds as date elements are printed as the site prints them ("This Act expires on 30 June 2027.").

Text a version prints but marks as not yet commenced (the site shows it in italics after "[Commences: ...]") sits
between the lines `[Not yet in force. Commences: <day, as the source gives it>]` and `[End of text not yet in force]`
(for a whole Part or Division, the marker follows its heading in `headings.md`). When it commences, the version
from that day drops the markers, and that is a commit credited like any other change. A spent amending provision
whose amendments have been incorporated is, as on the site, its number, any Part or Schedule heading, and the
source's note "The amendments effected by this section have been incorporated into ...".

## Statutory rules

The principal statutory rules in force on 2026-10-29 (regulations, rules of court, by-laws, proclamations, orders and
notices made under Acts; amending rules are not separate folders, their changes are in the rules they amend) are in
[`subordinate/`](subordinate), one folder per rule named from its title: `subordinate/education-regulations-2017/`. Files are as for the Acts
(`s-002.md` holds regulation, rule or clause 2; `sch-1/cl-003.md`, `front.md`, `headings.md`), plus `tail.md`, the
end matter the site prints ("Displayed and numbered in accordance with the Rules Publication Act 1953.", "Notified in
the Gazette on ...", the administering department). As in the Acts, date elements ("take effect on
10 July 2017") are printed as the site prints them. Commit messages label a rule's provisions `reg 2`, `r 2`,
`by-law 2` or `cl 2`, by the kind of rule its title names.

Their versions (1816, from 1991-10-23) are dated and credited by the same rules as the Acts', from
the same commencement records: 1786 commits on main (1727 credited to statutory rules, 53 to
Acts; by kind {'law': 1780, 'no-act': 2, 'several': 3, 'unclear': 1}), 289 on `future`. On a day when one law changed Acts and
statutory rules, the Acts' commit comes first and the rules' has its own commit, with its own tag
(`subordinate/act/...`, `subordinate/sr/...`), so the Acts' history is exactly what it is without the rules. Version
tags are `subordinate/<rule>/<day>`.

287 rules' version lists end in a repeal on a future day (the Subordinate Legislation Act 1992, s 11, repeals
subordinate legislation on the tenth anniversary of its making unless it ceases to be in force sooner): on `future`,
a commit deleting the rule's folder, credited to the law whose commencement record names the whole rule that day, else labelled
`Kind: repeal date only`. The rules' own kinds are `Kind: no amending law named`, `two or more laws`, `amending law
not identified` and `first version in the database`, worded as for the Acts.

## Coverage and limits

- 609 Acts, 4521 point-in-time versions; 1365 statutory rules, 1816 versions;
  3974 commits on main (2188 on Acts, 1786 on statutory rules); 300 on `future`.
- Statutory rules not built: 0; Acts not built: 0; see [NOT-BUILT.md](NOT-BUILT.md).
- 10 Acts' version lists end in a repeal on a future day (Supply and Appropriation Acts, Acts that expire):
  on `future`, a commit deleting the Act's folder, credited to the law whose commencement record names the whole Act
  that day, else labelled `Kind: repeal date only`.
- Repealed Acts and statutory rules, amending statutory rules as separate folders, and laws as made are not included.

## Reuse

Sourced from the Tasmanian Legislation website at 2026-10-30. For the latest information on Tasmanian Government
legislation please go to www.legislation.tas.gov.au. Copyright State of Tasmania; licensed under CC BY 4.0
(see [LICENSE](LICENSE) and [SOURCES.md](SOURCES.md)). The files are based on that material: reformatted into one
file per provision, with history notes removed. This record is not an official version.
