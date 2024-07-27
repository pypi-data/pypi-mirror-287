# streamlit-diff-viewer
git-like diff viewer for streamlit webapp

![](docs/head.png)

## Installation

```bash
pip install streamlit-typst
```

## Usage

```python
from streamlit_typst import st_typst

text = "a = 1"
st_typst(text)
```

run example:

```bash
streamlit run example.py
```

![img.png](docs/img.png)

## Buiding from source

### Prerequisites

- nodejs >= 18.x
- yarn >= 1.22.x
- poetry >= 1.2.x
- python >= 3.8.x

### Building

```bash
./build.sh
```

### Publishing

```bash
poetry publish
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
