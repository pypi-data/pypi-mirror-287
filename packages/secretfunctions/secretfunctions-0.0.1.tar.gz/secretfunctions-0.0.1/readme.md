# Introduction

basefunction is a simple library to have some commonly used functions for everyday purpose.  The functions include some
convenience functions for file handling as well as a threadpool class with automatic retry and timeout functionality.  

secretfunctions is a simple library to have a common interface for requesting secret elements like passwords etc.
we used python-decouple module but and it works fine in the beginning but after a while when using more and more modules 
it was not clear which file decouple really is using for loading the secrets. In the end we couldn't figure out when a file 
was used and how. So before investing too much time, we decided to write this simple wrapper over a toml file and make a 
query function. 


## Getting Started

The module has one class SecretFunction with one method get_secret

## Installing

```
pip install secretfunction
```

## Usage

### SecretFunctions 

```python
import secretfunction

secret_handler = secretfunctions.SecretFunctions("path_to_toml_file")
secret = secret_handler.get_secret(key="apiKey")

```

## Project Homepage

<https://dev.azure.com/neuraldevelopment/secretfunctions>

## Contribute

If you find a defect or suggest a new function, please send an eMail to <neutro2@outlook.de>
