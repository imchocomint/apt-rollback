# apt-rollback
Tool to rollback an APT package by one version.

This is the first thing I really wrote for a while. AI do not involve much within the core function; the only thing I'd let Copilot do is getting the package name from command line. Gemini only recommend me some ways to extract package versions from `apt-cache`.

## Usage
Go to release and download arb. Put to somewhere in your $PATH (e.g. /usr/local/bin).

To downgrade a package, run: `arb <package name>`

## To-do
- [ ] adding a pinpoint and unpinpoint function. That should be easy.
- [ ] reformat the code.

## Why?
A lot of people are using Debian experimental or such distro (e.g. PikaOS). Sometimes a package is so buggy that you would want to go back, but apt have no direct command to do that. So I wrote this. 

## Notes
- apt-rollback can work with packages from differrent repositories (e.g. packages from experimental in a sid system), provided that the package is installed.
- apt-rollback can not be used to install older version of a package.
