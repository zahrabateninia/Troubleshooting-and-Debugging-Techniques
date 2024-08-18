# Fix a slow system with Python

## Introduction
A media production company uses Network-Attached Storage (NAS) to store all data generated daily (e.g., videos, photos). 
Back up the data in the production NAS to the backupn NAS.
There's a Python script that backs up data daily. But recently, there's been a lot of data generated and the script isn't catching up to the speed.
As a result, the backup process now takes more than 20 hours to finish, which isn't efficient at all for a daily backup.


## What you'll do

- Identify what limits the system performance 
- Use ***rsync*** command instead of cp to transfer data
- Find differences between __threading__ and __multiprocessing__
