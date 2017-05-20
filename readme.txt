Git is a version control system.
Git is free software.
# git commond :

#create respository :
git init

#two commit cmd
git add xxx [[xxx] +]
git commit -m "xxx,,xxx"

#status
git status

#diff
git diff xxx

# git reset
git log
git log --pretty=oneline
git reset --hard HEAD^
git reset --hard HEAD~5

# git goto
git reflog
git reset --hard 18a691c

# git and github
git remote add origin git@github.com:Yong-bin/awesome-python3-webapp.git
git push -u origin master
git push origin master

git clone git@github.com:Yong-bin/awesome-python3-webapp.git

add by yongbin

# add git branch step
git branch : check branch
git branch <name> : create branch
git checkout <name> : switch branch
git checkout -b <name> :create and switch branch
git merge <name> : merge to current branch
git branch -d <name> : delete branch
# add by yongbin

# add git conflict
git chechout -b feature1
giet add readme.txt
git commit -m "AND simple"
git checkout master
get add readme.txt
git commit -m "& simple"
git merge feature1
git status
git add readme.txt
git commit -m "conflict fixed"
git log --graph --pretty=oneling --abbrv-commit
git branch -d feature1
# add by yongbin

# add by yongbin
hah

# add by yongbin

# add git stash
git status
git stash
git checkout master
git checkout -b issue-101
git add readme.txt
git commit -m "fix bug 101"
git checkout master
git merge --no-ff -m "merged buf fix 101" issue-101
git branch -d issue-101
git checkout dev
git status
git stash list
git stash pop
git stash apply stash@{0}
# add by yongbin
