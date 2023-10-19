# Developer Guide

The objective of the guide is to provide a rigorous documentation on the set up and maintenance of this repositiory

## 1. Setting up .gitignore

The following files are excluded from source control but are not included in `.gitignore`. This is to ensure the teams' settings and configuration are not shared with the public as per industry conventions

- `.vscode` and other Editor directories

To prevent it from being pushed, devs can use the following command:

```
git update-index --assume-unchanged <file_path>
```

## 2. Installing dependencies

In root, run the following command

```
npm install
```
