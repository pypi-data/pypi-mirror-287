## FlussTools

Head for Python scripts for river analyses.

The full documentation is available at [https://flusstools.readthedocs.io](https://flusstools.readthedocs.io/en/latest/).

### Create Requirements.txt

`pip-tools` helps to manage `requirements.txt` with more control. It separates direct dependencies from transitive ones.

1. **Install `pip-tools`**:

```sh
pip install pip-tools
```

2. **Create `requirements.in`**:

   List your direct dependencies in a `requirements.in` file. For example:

```plaintext
requests
numpy
```

3. **Compile `requirements.txt`**:

   Run `pip-compile` to generate `requirements.txt` from `requirements.in`:

```sh
pip-compile requirements.in
```


