# Rewinding your commits to clean them up


You can use `git reset --soft HEAD^1` to go back in time to undo a
commit without losing history.

This branch has a commit with a broken testcase that was
misimplemented.

Rebasing will clean up that history so every commit looks clean.

People reading your commit history don't have to figure out which
particular line was broken and then fixed.

```bash
$ git reset --soft HEAD^1
<make edits here>
$ git commit -a
```


