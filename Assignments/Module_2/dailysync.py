#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool # Used to create a pool of worker processes for parallel execution.

def run(task): # task: Represents a directory or file path to be synced
    print(task)

    # Run rsync using subprocess.call() with the following options:
    # -v: Verbose mode.
    # -a: Archive mode (preserves symbolic links, permissions, timestamps, etc.).
    # -r: Recursive mode to copy directories.
    # -q: Quiet mode (minimizes output).
    subprocess.call(["rsync", "-varq", task, dest])

src = "data/prod/"
dest = "data/prod_backup/"

# os.listdir(src) lists all files and directories in the source directory.
dir_tasks = [os.path.join(src, x) for x in os.listdir(src)] # The result is a list of tasks (each task being a path to a directory or file).
p = Pool(len(dir_tasks))
#  Assign each task to a worker process
p.map(run, dir_tasks)


# My Notes:

# rsync is a powerful and versatile Linux command for transferring and synchronizing files between local and
# remote devices. Unlike traditional copy commands,
# rsync uses a delta-transfer algorithm to only transmit the differences between the source and destination files.