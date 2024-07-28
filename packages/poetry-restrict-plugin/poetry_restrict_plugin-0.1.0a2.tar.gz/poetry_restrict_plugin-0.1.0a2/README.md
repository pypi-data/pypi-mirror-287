# poetry-restrict-plugin

This Poetry plugin aims to restrict Poetry's allowed accesses to what it needs
to fulfill its function, the goal is to apply [principle of least
privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) to our
development tooling.


## Motivation

What's the worst thing that could happen if you install a malicious Python
dependency on your computer? Which information could it gather from your files,
and how could it make itself a permanent home on your computer?

With `poetry-restrict-plugin`, that looks as follows:

```sh
$ poetry run cat ~/.ssh/config
poetry-restrict-plugin: Landlock engaged.
cat: /home/jc/.ssh/config: Permission denied
$ poetry run ls ~/.ssh
poetry-restrict-plugin: Landlock engaged.
ls: cannot open directory '/home/jc/.ssh': Permission denied
```


## Installation

At time of writing, `poetry-restrict-plugin` is only supported on Linux with
[the Landlock LSM](https://docs.kernel.org/userspace-api/landlock.html) enabled.

With [`pipx`](https://pipx.pypa.io/stable/docs/):

```sh
pipx inject poetry poetry-restrict-plugin
```

For other installation methods, see the [Poetry plugin
documentation](https://python-poetry.org/docs/plugins/#using-plugins).


## Disclaimer

`poetry-restrict-plugin` is not a perfect sandbox, and probably never will be.
If you're looking for something like that,
[nsjail](https://github.com/google/nsjail) might be interesting for you.


<!-- vim: set textwidth=80 sw=2= ts=2: -->
