# Introduction
  
secretfunctions is a simple library to have a common interface for requesting secret elements like passwords etc.
we used python-decouple module but and it works fine in the beginning but after a while when using more and more modules 
it was not clear which file decouple really is using for loading the secrets. In the end we couldn't figure out when a file was used and how. 
So before investing too much time, we decided to write this simple wrapper over a dotenv file and make a query function. 

The class SecretFunction has a singleton and in the constructor the file "~/.env" is loaded. With the function get_secret_key() you can query the values and receive either the value itself or a default, which is None by default.

## Getting Started

The module has one class SecretFunction with one method get_secret

## Installing

```
pip install secretfunction
```

## Usage

### SecretFunctions 

```python
import secretfunctions

secret_handler = secretfunctions.SecretFunctions()
print(secret_handler.get_secret_key("EOD2PD_API_KEY"))

```
if your ~/.env file exists and you have a key "EOD2PD_API_KEY in there, you receive the value of the key, otherwise you receive None.

That simple.

## Project Homepage

<https://dev.azure.com/neuraldevelopment/secretfunctions>

## Contribute

If you find a defect or suggest a new function, please send an eMail to <neutro2@outlook.de>
