serve:
    hugo server --buildDrafts

sync: commit pull push

save: commit push

pull:
    git pull --rebase

push:
    git push

commit:
    git add .
    git commit -m "feat: update at `date '+%Y/%m/%d %H:%M'`"
