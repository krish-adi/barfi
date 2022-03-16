# Quickstart

To get started with using **barfi**, you need to setup a virtual environment and install barfi using `pip`.

## Installation

Setup a virtual environment for your project. If you do not know how to do this, [**this blog**](https://krishadi.com/zettelkasten/python.html) or [**this section**](https://docs.streamlit.io/library/get-started/installation#set-up-your-virtual-environment) could be of help. 

Inside your virtual environment, install the package using:
```shell
pip install barfi
```

## Usage

The fundamental part of **barfi** is a **Block**. A {doc}`block` contains inputs, outputs and some computation. More details on what is a **block** and how to build one can be found here: {doc}`block`. In the demo below, is an example of a *block* with one output (`feed`) and another *block* with one input (`result`). It is built using the `Block` class provided in `barfi`.

To use barfi in a graphical environment, make use of the [streamlit](https://docs.streamlit.io/) component {doc}`streamlit-widget` that is built into `barfi`. Import `st_barfi` and pass in the base blocks as an array to build the graphical editor.

To run the script, simply follow streamlit's run command from the terminal. `streamlit run app.py`.

***app.py***
```python
from barfi import st_barfi, Block

feed = Block(name='Feed')
feed.add_output()

result = Block(name='Result')
result.add_output()

st_barfi(base_blocks=[feed, result])
```

Run the file `app.py` in command line using streamlit's run command:

```shell
streamlit run app.py
```