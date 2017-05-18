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
