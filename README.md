# lesspass.py

A lesspass implementation in Python

## Requirements

- Python 2.7 - 3.5

## CLI

CLI lets you to use configuration from JSON file with profile settings. Standard
LessPass tools don't allow to set login and site in profile. This application
has this feature which is very helpful in cases when you have automatically
generated usernames which cannot be changed (popular in banking etc.).

You can use CLI in three ways. First one:

`cli.py file site login`

gets profile from `~/.lesspass/file.json`. If login and site are configured in
profile file, they are ignored and values from cli are used.

Second way:

`cli.py file`

All parameters needed to generate password are placed in `file`.

Third way:

`cli.py site login`

Default profile is used.

### CLI Installation

The simplest way to install CLI is to make symlink in one of directories from
system `$PATH` variable. In my case it looked like this:

`ln -s ~kacper/data/bin/lesspass $(realpath ./cli.py)`

(`~kacper/data/bin/` is in my `$PATH` variable)

## Tests

    python -m py.test

## See also

- [lesspass.go](https://github.com/mevdschee/lesspass.go)
- [lesspass.php](https://github.com/mevdschee/lesspass.php)
