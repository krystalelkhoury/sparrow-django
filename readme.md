## Welcome to Sparrow!
We’re excited to have you and hope you’ll find this guide helpful.

This repo is a WIP. In fact, if you think of ways we can improve this document, that can be your first pull request!

## What is Sparrow?
Sparrow provides a software based service that handles all leave-related paperwork, coordination, calculation and headache. We're a team that believes no one should choose between the people they love and the job they love. It's our mission to make it possible for more people to balance work and family.

## Getting Help
-Slack: Ping any of the team members @trysparrow.slack.com

-Ask in Person: Chances are, we’re right next to you right now.

## Our Stack/Technologies
We use GitHub for version control. https://github.com/trysparrow
Please make sure you have an account and that you’ve submitted your GitHub username, so we can give you edit access to the appropriate repositories. Any of the team members can help you figure this out.

The following describes how to set up a developer environment on a new Mac! If you find any mistakes in the steps described below, or if any of the commands are outdated, please let us know!

Our landing page https://trysparrow.com is built with Django, a Python-based free and open-source web framework.

## OSX dev setup

### Homebrew
Package managers make it easy-peasy to install and update applications or libraries. The most popular package manager for the OSX is Homebrew.

We can install Homebrew by copy-pasta-ing this command inside the terminal:

### Install package manager [Homebrew](https://brew.sh/)  
$ `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)”`

Follow the steps on the screen. You’ll be prompted for your username and password.

To install a package with Homebrew, simply type: brew install <formula>


### Install zsh and oh my zsh

zsh is a popular shell. Install it to get the attention you’ve always deserved and tab yourself into productivity.

$ `brew install zsh`

Oh my zsh is a *delightful* framework that adds functionality to your terminal that can make you faster and more productive. Quoting Robby Russell, oh my zsh comes with a *shitload* of plugins. It spices up your terminal with colors for your status, branch and diff Git commands, as well as a couple aliases. If you have another framework you prefer, that’s ok, but if your alternative is the raw terminal, you should install this.

$ `sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)”`


### Git
OSX comes with a pre-installed version of Git.

Let’s define your Git user (this should be the same name and email you use for Github)
git config --global user.name "Your Name Here"
git config --global user.email "your_email@youremail.com"
Python

### Install python 3
$ `brew install python`

### Pip
Pip is the package manager for python. It was installed by brew install python.


Checkout a local copy of the appropriate repository (as shown below)
$ `git clone https://github.com/trysparrow/sparrow-django.git`


## Set up your Sparrow virtual environment
A virtual environment is an environment that keeps all the tools and packages in a given place.  It’s a tool that creates an isolated Python environment for each of your projects. It’s best to install projects in an isolated folder instead of installing packages globally.

### Install virtualenv
$ `pip3 install virtualenv`
$ `cd sparrow-django`
$ `rm -rf sparrenv`
$ `virtualenv sparrenv`

## Activate virtualenv
Whenever you are working on sparrow-django, you should have your virtual environment (e.g. sparrenv) activated.
$ `source sparrenv/bin/activate`
### In your Sparrow virtual environment [with zsh, your location should look like: (sparrenv) ➜  sparrow-django git:](master)
$ `pip3 install -r requirements.txt`

### Install the python packages necessary to run the server locally
sparrow-django git:(master) ✗ pip3 install -r requirements.txt (run this command in and outside of the virtualenv?)


## Setup a local database using Postgresql
PostgresSQL is a popular relational database.

### Install postgresql using Homebrew
$ `brew install postgresql`

### Start postgres server
$ `pg_ctl -D /usr/local/var/postgres start`  

### Create new PostgreSQL DB & Local user
Note: you should only need to do this once.
[Reference Tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
$ `createdb spdb`
$ `createuser spadmin`

## Preparing to run the server
### Migrate the database (only necessary if you change the database)
$ `python3 manage.py migrate`  
### Update static files
$ `python3 manage.py collectstatic`  
### Run the server
$ `python3 manage.py runserver`  

## Contributing Code
All our code is housed on Github so we make contributions through PRs. If you’re new to Git, here’s a tutorial on basic git commands https://18f.gsa.gov/2015/03/03/how-to-use-github-and-the-terminal-a-guide/

### Here’s a step-by-step example for contributing to our landing page:
#### Work needs to be done. Let's create a new branch and go from here.
$ `git checkout -b <new-branch-name>`
#### We've written code! Let's check if it looks good locally at localhost:8000
$ `source sparrenv/bin/activate`
$ `python3 manage.py runserver`
#### Looking good. Push to origin
$ `git add <changed-files-names>`
$ `git commit -m "<short-description-of-your-code>"`
$ `git push origin <new-branch-name>`
#### Make a PR on Github
Wait for the team to review your changes. They say it's ready to ship. Merge to master.
#### Check on Render
When we merge the PR to master, our changes aren't in production yet. They're sitting on our test server at sptest.onrender.com. We double check your changes one more time. If it's good to go, we manually deploy into production. Yay!  
### A few more helpful commands
#### Update your branch
$ `git status`
#### to untrack a file
$ `git rm -r FILENAME`
#### to track a file
$ `fit add FILENAME`
$ `git commit -m “DESCRIPTIVE COMMIT MESSAGE”`

## Text Editors
Most engineers use VS Code but feel free to use atom, sublime text, vim, emacs, or whatever makes you comfortable.

## Project folders
This is all to taste, but a few (wink wink) of us put all our version-controlled projects in ~/Documents.
