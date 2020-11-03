#!/usr/bin/env bash
cd docs
jekyll build
cd ..
git checkout -b gh-pages-temp
git add -f docs/site
git commit -m "gh-pages update"
git subtree split --prefix docs/site -b gh-pages
git push -f origin gh-pages:gh-pages
git branch -D gh-pages
git checkout main
git branch -D gh-pages-temp
