# BringUpAutomation


This Repo is to automate the Bring up Sequence for various Platforms

Platforms include: 
- Leda 
- Pandia
- Future Platforms*

Pre Requisites:
- Bender Build Prior to the Bring Up process i.e. Nano FTAB, Nano SA, FSB FTAB, FSB SA
- Confirm the Train (for example LuckFennel for Pandia Bring up) for the PR Restore
- CFE bin files

Each Platform has different stages/tests which as a Platform Software Engineer we might want to test:

- Artifact Downloads for various (SA and FTAB for Nano/FSB) Bender Builds: We might be needing to download the bootloader scripts i.e. loading_config.ax file which is present inside package.tgz for Standalone Builds.
- Install Per Resquisites for Bring up such as Home Diagnostics
- Application Processor Restore: 
  - with Baseband Firmware
  - without Baseband Firmware
- CFE Test 
- Baseband Firmware Test

