# griffe-modernized-annotations
A Griffe extension that modernizes type annotations by adopting PEP 585 and PEP 604

## Example
Without extension:
![Without Extension](assets/without-extension.png)

With extension:
![With Extension](assets/with-extension.png)

## Install
To install **griffe-modernized-annotations**, simply use pip:

```console
$ pip install griffe-modernized-annotations
```

## Usage
```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          options:
            extensions:
              - griffe_modernized_annotations
```