# Abstract
Designed to save pstats log to folder...
# Install
```bash
    pip3 install git+https://github.com/GrafLearnt/pstats_extender.git
```
# Usage
```python
import pstats_extender


@pstats_extender.profile()
def some_function():
    ...
```
## or
```python
import pstats_extender


with pstats_extender.profile(
    sortby=pstats_extenter.SortKey.CUMULATIVE, directory="../pstats"
):
    # your code here
```
## or
```python
import pstats_extender


with pstats_extender.profile():
    # your code here
```


## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
