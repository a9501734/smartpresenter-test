@echo off
setlocal

cd /d "%~dp0"

set /p REPO_URL=Enter GitHub repository URL (e.g. https://github.com/yourusername/yourrepo.git): 

echo Initializing Git repository...
git init

echo Adding files...
git add .

echo Making initial commit...
git commit -m "Initial commit"

echo Setting remote origin...
git remote add origin %REPO_URL%

echo Renaming branch to main...
git branch -M main

echo Pushing to GitHub...
git push -u origin main

echo Done!
pause
