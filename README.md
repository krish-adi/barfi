<img src="/assets/logo.png" width="100px" alt="Barfi Logo">

# Welcome to Barfi ! 👋

**A Python visual Flow Based Programming library to buld workflows that integrates into existing codebases.**

![Demo GIF](/assets/demo.gif)

**Documentation** : [find it here](https://barfi.ai/docs)

Barfi is a Flow-Based Programming framework that offers a graphical programming interface. It is designed to integrate seamlessly into your existing Python applications.

Barfi serves as an abstraction of Graphical Programming, Flow-Based Programming, or Node Programming, where a Block corresponds to a Node, and a Link (or connection) corresponds to an Edge. These concepts go by different names, each reflecting specific needs or philosophies. In Barfi, they form the foundation of a framework for building, saving, and executing workflows as needed. The framework is intentionally kept simple, providing APIs that allow customization for diverse use cases and philosophies.

Many existing visual Flow-Based Programming (FBP) libraries/frameworks operate within their own confined isolated environments, limiting their usability as components in existing applications or scripts. Barfi addresses this by decoupling the graphical programming interface from the computation environment, which eables easy integration into existing apps. The graphical interface is provided through a Streamlit widget: `st_flow` (with a Jupyter Notebook widget currently in development), while the computation environment is managed independently via the `ComputeEngine`.

> Note: The current version >= 1.0.0 introduces many changes from <= 0.7.0. Check the (changelog)[./CHANGELOG.md] for more info on this. Versions will no longer be maintained. 

## Quickstart

A workflow consists of a bunch of `Block`s connected to each other, the information of the blocks and connections is stored in a `FlowSchema`, which is then executed to execute each program/function connected to each `Block` and to propagate the data from one `Block` to another.

### Installation

Since we will be using the streamlit widget st_flow for the graphical interface here, we will install the package with the streamlit requirements:

```shell
pip install barfi[streamlit]
```

> Note: As a best practice, it is recommended to setup a virtual environment to manage the dependencies of the project. If you do not know how to do this, this blog or this section could be of help.

### Your First App

Follow this getting started guide on building your first `Blocks`, creating a `FlowSchema` and executing it using a `ComputeEngine`, save it using a `SchemaManager`.

**Getting Started** : [find it here](https://barfi.ai/docs/getting_started)

## Migration from v0

If you were using the versions <= 0.7.0, a migration guide is being written. For using version >= 1.0.0, conceptually all the concepts remain with a minor API changes. v1.0.0 introduces a stronger type checking mechanism, and decouples and `SchemaManager` and `ComputeEngine` from the UI by providing separate classes to run those functions. You can check the API docs to get familiarized on how to use them. 

## Under the hood

The Flow Editor UI is built using [ReactFlow](https://reactflow.dev/).