## Information
<a href="https://pypi.python.org/pypi/AdvancedTagscriptEngine/">
    <img src="https://img.shields.io/pypi/pyversions/AdvancedTagscriptEngine" alt="AdvancedTagScriptEngine" />
</a>
<a href="https://pypi.python.org/pypi/AdvancedTagscriptEngine/">
    <img src="https://img.shields.io/pypi/v/AdvancedTagScriptEngine" alt="PyPI - Version">
</a>
<a href="https://tagscriptengine.readthedocs.io/en/latest/?badge=latest">
    <img src="https://readthedocs.org/projects/tagscriptengine/badge/?version=latest" alt="Documentation Status" />
</a>
<a href="https://pypi.python.org/pypi/AdvancedTagscriptEngine/">
    <img src="https://img.shields.io/pypi/dm/AdvancedTagScriptEngine" alt="PyPI - Downloads" />

</a>

This repository is a fork of JonSnowbd's [TagScript](https://github.com/JonSnowbd/TagScript), a string templating language.
This fork adds support for Discord object adapters and a couple Discord related blocks, as
well as multiple utility blocks. Additionally, several tweaks have been made to the engine's
behavior.

This TagScriptEngine is used on [MELON, a Discord bot](https://melonbot.io/invite).
An example implementation can be found in the [Tags cog](https://github.com/japandotorg/Seina-Cogs/tree/main/tags).

Additional documentation on the TagScriptEngine library can be [found here](https://tagscriptengine.readthedocs.io/en/latest/).

## Installation

Download the latest version through pip:

```
pip(3) install AdvancedTagScriptEngine
```

Download from a commit:

```
pip(3) install git+https://github.com/japandotorg/TagScriptEngine.git@<COMMIT_HASH>
```

Install for editing/development:

```
git clone https://github.com/japandotorg/TagScriptEngine.git
pip(3) install -e ./TagScriptEngine
```

## What?

AdvancedTagScriptEngine is a drop in easy to use string interpreter that lets you provide users with ways of
customizing their profiles or chat rooms with interactive text.

For example TagScript comes out of the box with a random block that would let users provide
a template that produces a new result each time its ran, or assign math and variables for later
use.

## Dependencies

`Python 3.8+`

`pyparsing`

`discord.py`

`Red-DiscordBot` [optional]
