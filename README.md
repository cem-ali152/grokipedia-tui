![Python](https://badgen.net/badge/icon/3.12.0?icon=https://www.svgrepo.com/show/452091/python.svg\&label=python)
“A terminal-based Grokipedia client that supports both command-line arguments (usable) and an interactive text-based user interface (coming soon)
## Usage
![](https://github.com/cem-ali152/grokipedia-tui/blob/main/demo.gif)
That's it!


## Compiling the Code

First, **Python 3.12** must be installed (a different version has not been tested at this time). It is recommended that you create a **Python virtual environment** (e.g., `conda` or `venv`).

After entering the virtual environment, install the necessary dependencies:

```cmd
pip install -r requirements.txt
```

This will make the code executable.

If you want, you can use the following command to create an **executable file**:

```cmd
pip install pyinstaller & pyinstaller main.py
```
## Arggs

| Option      | Long Option          | Description                                        |
| ----------- | -------------------- | -------------------------------------------------- |
| `-h`        | `--help`             | Show this help message and exit                    |
| `-q QUERY`  | `--query QUERY`      | Search query (example: `mustafa_kemal_ataturk`)    |
| `-t`        | `--typeahead`        | Run the Typeahead API                              |
| `-f`        | `--full-text-search` | Run the Full Text Search API                       |
| `-s`        | `--search`           | Perform a basic search                             |
| `-T`        | `--tui`              | coming soon..                                      |
| `-l LIMIT`  | `--limit LIMIT`      | Set the output result limit                        |
| `-o OFFSET` | `--offset OFFSET`    | Offset value                                       |

## Support

If you want to support the project and help it grow, even a small donation is appreciated.  
Remember, this project develops thanks to contributions from users like you.
