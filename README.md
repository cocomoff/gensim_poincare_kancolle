# Environment setup

- Python 3.9.1
- poetry 1.1.4

```bash
$ poetry init
$ poetry add dill gensim plotly jupyterlab
$ poetry run jupyter labextension install jupyterlab-plotly
```

# How to run

- After preprocessing, please launch jupter lab and run codes in cells

```bash
$ poetry run python preprocess.py
$ poetry run jupyter lab
```