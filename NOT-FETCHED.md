# Acts not built

In force on the build day, but at least one version could not be fetched whole (the host resets responses
larger than about 64 KB on the wire), or the source returned no usable version list. Left out entirely.

The reset happens at about 32 KB into any larger response from this host (static files too), at any
rate, over HTTP/1.0 or 1.1; other hosts serve large files to the same machine. The whole-Act XML route
does not support byte ranges. The site's own reader loads one section at a time
(`/projectdata?ds=EnAct-FragViewDataSource`), which robots.txt and the terms allow, but it serves HTML,
needs a version-list request per version, and would take about 290,000 requests for these Acts' 877
versions (fragment count x versions): not attempted. They can be added when the host serves them whole.

| Id | Title | Reason |
| --- | --- | --- |
| act-1884-019 | Conveyancing and Law of Property Act 1884 | version 1997-02-01 not served whole |
| act-1924-069 | Criminal Code Act 1924 | version 1997-02-01 not served whole |
| act-1925-038 | Traffic Act 1925 | version 1997-02-01 not served whole |
| act-1932-058 | Supreme Court Civil Procedure Act 1932 | version 1997-02-01 not served whole |
| act-1935-044 | Police Offences Act 1935 | version 2009-11-25 not served whole |
| act-1959-077 | Justices Act 1959 | version 1997-02-01 not served whole |
| act-1971-081 | Poisons Act 1971 | version 2016-10-17 not served whole |
| act-1979-035 | Fire Service Act 1979 | version 1997-02-01 not served whole |
| act-1980-019 | Land Titles Act 1980 | version 1997-02-01 not served whole |
| act-1982-011 | Petroleum (Submerged Lands) Act 1982 | version 1997-02-01 not served whole |
| act-1984-021 | Industrial Relations Act 1984 | version 2006-02-15 not served whole |
| act-1988-004 | Workers Rehabilitation and Compensation Act 1988 | version 1997-02-01 not served whole |
| act-1993-020 | Crime (Confiscation of Profits) Act 1993 | version 2014-03-01 not served whole |
| act-1993-070 | Land Use Planning and Approvals Act 1993 | version 2010-01-01 not served whole |
| act-1993-094 | Gaming Control Act 1993 | version 1999-12-22 not served whole |
| act-1993-095 | Local Government Act 1993 | version 1997-02-01 not served whole |
| act-1993-096 | Local Government (Building and Miscellaneous Provisions) Act 1993 | version 1997-02-01 not served whole |
| act-1994-044 | Environmental Management and Pollution Control Act 1994 | version 2001-05-01 not served whole |
| act-1995-025 | Living Marine Resources Management Act 1995 | version 1997-02-01 not served whole |
| act-1995-044 | Guardianship and Administration Act 1995 | version 2024-09-01 not served whole |
| act-1995-058 | Electricity Supply Industry Act 1995 | version 2015-07-01 not served whole |
| act-1995-083 | Threatened Species Protection Act 1995 | version 2001-06-27 not served whole |
| act-1995-116 | Mineral Resources Development Act 1995 | version 2013-06-28 not served whole |
| act-1997-059 | Sentencing Act 1997 | version 2018-07-01 not served whole |
| act-1997-081 | Youth Justice Act 1997 | version 2014-03-01 not served whole |
| act-1997-086 | Public Health Act 1997 | version 2015-07-01 not served whole |
| act-1998-045 | Regional Forest Agreement (Land Classification) Act 1998 | version 1998-12-18 not served whole |
| act-1999-045 | Water Management Act 1999 | version 2000-01-01 not served whole |
| act-1999-070 | Vehicle and Traffic Act 1999 | version 2002-11-01 not served whole |
| act-2001-015 | Duties Act 2001 | version 2001-07-01 not served whole |
| act-2001-076 | Evidence Act 2001 | version 2002-07-01 not served whole |
| act-2003-062 | Tasmanian Assessment, Standards and Certification Act 2003 | version 2023-07-01 not served whole |
| act-2004-051 | Electoral Act 2004 | version 2005-02-16 not served whole |
| act-2007-024 | Legal Profession Act 2007 | version 2008-04-09 not served whole |
| act-2011-029 | Asbestos-Related Diseases (Occupational Exposure) Compensation Act 2011 | version 2011-10-31 not served whole |
| act-2012-001 | Work Health and Safety Act 2012 | version 2013-01-01 not served whole |
| act-2013-002 | Mental Health Act 2013 | version 2014-02-17 not served whole |
| act-2016-025 | Building Act 2016 | version 2017-01-01 not served whole |
| act-2016-051 | Education Act 2016 | version 2017-07-10 not served whole |
| act-2019-022 | Biosecurity Act 2019 | version 2020-01-01 not served whole |
| act-2020-024 | Tasmanian Civil and Administrative Tribunal Act 2020 | version 2021-11-05 not served whole |
| act-2024-016 | Racing Regulation and Integrity Act 2024 | version 2025-02-01 not served whole |
