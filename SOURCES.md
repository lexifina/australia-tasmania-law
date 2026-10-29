# Sources and legal basis

- Source: Tasmanian Legislation (https://www.legislation.tas.gov.au), the website of the Office of Parliamentary Counsel, Department of Premier
  and Cabinet, Tasmania. Point-in-time consolidations of every Act in force, from 1994-03-15.
- Routes used (no key, public):
  - `/projectdata?ds=EnAct-BrowseDataSource` (Acts in force, principal Acts only: `PrintType="act.reprint" AND
    Repealed<>Y AND Amending<>"pure"`);
  - `/projectdata?ds=EnAct-TocDataSource&expression=view/html/inforce/current/<id>` (each Act's version list:
    first and end valid day of every point-in-time version);
  - `/projectdata?ds=EnAct-AmendmentTableDataSource` (commencement records: amending Act, day, provisions);
  - `/view/whole/xml/inforce/<first valid day>/<id>` (the version's whole text, EnAct act.dtd XML).
- Terms: https://www.legislation.tas.gov.au/copyrightanddisclaimer (read 2026-10-29): "Unless otherwise noted, all material provided on this
  website is licensed under a Creative Commons Attribution 4.0 International licence (CC BY 4.0)." Attribution
  wording as required there is in README.md and LICENSE.
- robots.txt (read 2026-10-29): `User-agent: *` / `Disallow: /admin/`; no rule for AI agents, no Crawl-delay.
