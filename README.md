# gemspector
CLI tool to identify malicious Gems distributed via RubyGems.

This project focusses on using meta-heuristics of the package to identify either malicious packages, or maliciously taken-over packages.

To scan a set of Gems defined in a Gemfile, run `scanner.py -d examples/Gemfile`

Current capabilities:
- Identifies if publicised maintainer emails are using expired domains

Future capabilities:
- Identifies if publicised maintainer emails are using compromised domains
- Identifies repository integrity mismatch with source repository
- Identifies potentially disposable/one-time-use emails for maintainers
- Identifies unusual package updates (e.g. anomalies in time of day/update descriptions)