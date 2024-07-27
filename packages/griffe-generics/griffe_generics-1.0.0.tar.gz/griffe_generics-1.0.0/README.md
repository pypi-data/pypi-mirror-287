# griffe-generics
A Griffe extension that resolves generic type parameters as bound types in subclasses

## Install
To install **griffe-generics**, simply use pip:

```console
$ pip install griffe-generics
```

## Usage
```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            extensions:
              - griffe_generics
```