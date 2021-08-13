# rload
A simple file monitoring with code reloader for Python 3.

---
# Example
```py

from rload import Rload, EventType

rload = Rload(__name__, ignored_paths=['__pycache__'])

@rload.on('change')
def handle_change(type: EventType, data: Dict):
    print(type, data)

@rload.on('reload')
def handle_reload(data):
    print('Reloading', data)

@rload.on('reloaded')
def handle_reloaded(data):
    print('Reloaded', data)

def test():
    print('This is a test')

if __name__ == "__main__":
    rload.run(target=test)

```





