  # This file is supposed to be used with the git-filter-repo python script from https://github.com/newren/git-filter-repo
  # as `python3 .../git-filter-repo.py --force --commit-callback "$(cat git-filter-add-signoff.py)"`
  # Mind to adapt the following before:
  #
  # Filter: Only replace commit messages of the following commit.author_name s:
  usernames = [b"Sebastian Schmittner", b"HackMD", b"Artur A Philipp", b"debian"]
  #
  # Sign off as the first username + this email:
  email = b"sebastian.schmittner@eecc.de"
  #
  # See https://htmlpreview.github.io/?https://github.com/newren/git-filter-repo/blob/docs/html/git-filter-repo.html#CALLBACKS
  # for more details on the script. Excerpt:
  # 
  # * Commit: `branch`, `original_id`, `author_name`, `author_email`,
  #         `author_date`, `committer_name`, `committer_email`,
  #         `committer_date`, `message`, `file_changes` (list of
  #         FileChange objects, each containing a `type`, `filename`,
  #         `mode`, and `blob_id`), `parents` (list of hashes or integer
  #         marks)
  #
  #
  if commit.author_name in usernames and b"Signed-off-by:" not in commit.message:
      commit.message = commit.message + b"\n\nSigned-off-by: " + usernames[0] + b" <" + email + b">"
