# gemspector
CLI tool to identify malicious Gems distributed via RubyGems.

This project focusses on using meta-heuristics of the package to identify either malicious packages, or maliciously taken-over packages.

### Heuristics

To make the scorecarding of packages as relevant to real-world examples of compromised/malicious packages, we will use [OpenSSF's Malicious Packages](https://github.com/ossf/malicious-packages/tree/main) repository as our data source.

This allows us to review our heuristics & scoring against actual examples of compromised and malicious packages, to determine their effectiveness in correctly scoring insecure packages.

Prospective heuristics are as follows:
- [x] Number of authors/contributors
- [ ] Number of versions of the package
- [ ] Active maintenance of the package (e.g. updates within the last X months)
- [ ] Age of the package
- [ ] Age of the source code repository (if available)
- [ ] Number of authors/contributors to source code repository (if available)
- [ ] Number of packages authors/contributors also maintain
- [ ] Integrity mismatches between source code repository and package code (if available)
- [ ] Author/contributor email domains (check if expired)
- [ ] Author/contributor email domains (check if compromised)
- [ ] Author/contributor disposable email usage (package)
- [ ] Author/contributor disposable email usage (source code repository)
- [ ] Cryptographic signing of packages
- [ ] Source code repository security (e.g. protected branches)
- [ ] Presence & security of build pipelines

### How to run

To scan a set of Gems defined in a Gemfile, run `scanner.py -d examples/Gemfile`