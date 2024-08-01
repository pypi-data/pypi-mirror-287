# Progress Indicator Library

A Python library providing two classes for displaying progress indicators in the console: `ProgressIndicator` and `ProgressBar`. These classes help visualize ongoing tasks by displaying an animated spinner or a progress bar, respectively.

[![Publish](https://github.com/leonardogonzalolaura/workspace_progress_basic/actions/workflows/publish.yml/badge.svg)](https://github.com/leonardogonzalolaura/workspace_progress_basic/actions/workflows/publish.yml)
![PyPI version](https://img.shields.io/pypi/v/progress_basic.svg)

![Python Versions](https://img.shields.io/pypi/pyversions/progress_basic.svg)


## Installation

To install the library, you can use pip:

```bash
pip install progress_basic
```

# Usage
## ProgressIndicator
The ProgressIndicator class displays an animated spinner with a customizable message and color.

Example

```python
from progress_basic.format.color_text import AnsiColors
from progress_basic.progress_basic import ProgressIndicator

with ProgressIndicator("Processing", color=AnsiColors.OKBLUE) as pi:
    # Simulate a long-running task
    time.sleep(5)
```

## ProgressBar
The ProgressBar class displays a progress bar that updates as tasks progress, with customizable total steps, message, interval, bar length, and color.

Example
```python
from progress_basic.format.color_text import AnsiColors
from progress_basic.progress_bar import ProgressBar

total_steps = 100

with ProgressBar(total_steps, message="Loading", color=AnsiColors.OKBLUE) as pb:
    for i in range(total_steps):
        pb.update(i + 1)
        time.sleep(0.1)  # Simulate work
```


# Classes
### `ProgressIndicator`
A class for displaying an animated spinner with a customizable message and color.

### `ProgressBar`
A class for displaying a progress bar that updates as tasks progress, with customizable total steps, message, interval, bar length, and color.




