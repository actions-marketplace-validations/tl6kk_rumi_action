# rumi.file_rumi.action.action
# Integration of file_rumi with github action
#
# Author: Tianshu Li
# Created: Nov.1 2021

"""
Integration of file_rumi with github action
"""

##########################################################################
# Imports
##########################################################################


import os
import shutil

from git import repo

from rumi.file_rumi.reader import FileReader
from rumi.file_rumi.reporter import FileReporter

# Get args from environemt variables as defined in action.yaml
# For file_rumi.reader
repo_path = os.environ["INPUT_REPO_PATH"]
branch = os.environ["INPUT_BRANCH"]
content_paths = os.environ["INPUT_CONTENT_PATHS"]
extensions = os.environ["INPUT_EXTENSIONS"]
target_files = os.environ["INPUT_TARGET_FILES"]
pattern = os.environ["INPUT_PATTERN"]
langs = os.environ["INPUT_LANGS"]
src_lang = os.environ["INPUT_SRC_LANG"]

# For file_rumi.reporter
detail_src_lang = os.environ["INPUT_DETAIL_SRC_LANG"]
detail_tgt_lang = os.environ["INPUT_DETAIL_TGT_LANG"]
stats_mode = os.environ["INPUT_STATS_MODE"]
details_mode = os.environ["INPUT_DETAILS_MODE"]


##########################################################################
# File_rumi Action
##########################################################################


reader = FileReader(
    repo_path=repo_path,
    branch=branch,
    langs=langs,
    content_paths=content_paths.split(","),
    extensions=extensions.split(","),
    pattern=pattern,
    src_lang=src_lang
)
print(target_files)
print(target_files.split(","))
for file in target_files.split(","):
    reader.add_target(file)

commits = reader.parse_history()


reporter = FileReporter(
    repo_path=reader.repo_path,
    src_lang=detail_src_lang,
    tgt_lang=detail_tgt_lang
)

if stats_mode:
    stats = reporter.get_stats(commits)
    reporter.print_stats(stats)

if details_mode:
    details = reporter.get_details(commits)
    reporter.print_details(stats)
