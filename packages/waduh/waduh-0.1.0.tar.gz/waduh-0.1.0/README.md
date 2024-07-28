# Waduh

'Waduh' is a multifunction library for python.

## Getting Started

- Install it
```sh
pip install waduh
```

- Import it
```py
from waduh.utils import get_time
```

- Ready to use
```py
result = get_time('hour')
print(result) 
```

## API
- ```waduh.utils```, Contain some useful function.
  - ```Person(str, int)```, A class for basic personal information (Name and Age).
  - ```greet(str)```, A function for greets the submitted name.
  - ```get_time(str)```, A function for getting current time in second, minute, and hour
  - ```check_package(str)```, A function for checking if the pip package is installed or not.
- ```waduh.math```, Contain math function.
  - A function for basic math operation.
  ```py
  add(int, int)
  substract(int, int)
  multiply(int, int)
  distribute(int, int)
  ``` 
