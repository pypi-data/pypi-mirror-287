# fs

## Usage

```sh
pip install zyjared-fs
```

```python
from fs import matches_path, rm_path, clean_directory
from pathlib import Path

rm_path(Path('test'))

is_matched: bool = matches_path(Path('test'), [r'.*test\.py'])

removed: list[Path] = clean_directory('test', include=[r'.*test\.py'], ignore=[r'\.git'])
```
