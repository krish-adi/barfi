# Barfi

**A Python visual Flow Based Programming library that integrates into your existing workflow.**

![Demo GIF](/docs/source/_static/demo.gif)

**Documentation** : [find it here](https://barfi.readthedocs.io/en/latest/)

Barfi is a Flow Based Programming environment that provides a graphical programming interface. It is integratable into your existing Python workflows. A schema is built using `barfi.Block`s. Then the schema is executed with `barfi.ComputeEngine`.

Each `barfi.Block` has some properties that enable the FBP and schema building. Firstly, each Block has Input and Output interfaces that link to other Blocks. Each Block can carry an executable function, that is specified by the user. This function can access/get data from the Input interface, perform computations or calculations and set the Output interface. 

In general, Barfi is an abstraction of the Graphical Programming, Flow Based Programming or Node programming. Where the Block is synonymous to Node, and a Link (connection) is synonymous to an Edge. There are many ways to call this, each serving a specific need or a philosophy. For, Barfi I've kept it simple, so that it can be customized to different use-cases and philosophy. 

Existing visual Flow Based Programming (FBP) libraries in Python run in their own/separate environment. They are not integratable into existing workflows, nor can they be used as a component in your existing scripts. Barfi bridges this with a Streamlit widget, and a Jupyter-Notebook widget is in the roadmap. 

The other main limitation for the existing Python libraries is the lack of domain specific components. Barfi has a roadmap to add domain specific components. 

## Quickstart

### Installation

In your Python project virtual environment install using pip:

```shell
pip install barfi
```

### Graphical Interface

- Barfi has a Streamlit component with the API `barfi.st_barfi`. 

- Plans are on way to build a Jupyter-Notebok widget. 

## Under the hood

The frontend is built using Vue and [BaklavaJS](https://github.com/newcat/baklavajs). Some of the implemented backend logic are borrowed from [BaklavaJS](https://github.com/newcat/baklavajs).
