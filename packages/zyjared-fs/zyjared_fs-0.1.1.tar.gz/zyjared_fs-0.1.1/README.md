# zyjared-fs

## Installation

```sh
pip install zyjared-fs
```

## Usage

```python
from zyjared_fs import matches_path, rm_path, clean_directory
from pathlib import Path

rm_path(Path('test'))

is_matched: bool = matches_path(Path('test'), [r'.*test\.py'])

removed: list[Path] = clean_directory('test', include=[r'.*test\.py'], ignore=[r'\.git'])
```
