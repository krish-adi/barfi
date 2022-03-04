# Barfi

**A visual Flow Based Programming widget library that integrates into your existing workflow.**

Existing visual Flow Based Programming (FBP) libraries in Python run in their own/separate environment. They are not integratable into existing workflows, nor can they be used as a component in your existing scripts. The main limitation for the existing Python libraries in this space is the lack of domain specific use-case. 

Barfi aims to bridge that. And, hope to add domain specific use-cases. 

__Demo GIF__

## Introduction

Barfi is a Flow Based Programming environment that provides a graphical programming environment. A schema is built using barfi-Block and barfi-Link provided in the Barfi library. A barfi-ComputeEngine is then used to execute the schema, and the results are obtained. 

Each barfi-Block has come properties that makes this possible. Firstly, each Block has Input and Output interfaces that link to other Blocks. Each Block can carry an executable function, that is specified by the user. This function can access/get data from the Input interface, perform calculations and set the Output interface. 

In general, Barfi is an abstraction of the Graphical Programming, Flow Based Programming or Node programming. Where the Block is synonymous to Node, and a Link is synonymous to an Edge. There are many ways to call this, each serving a specific need or a philosophy. For, Barfi I've kept it simple, so that it can be customized to different use-cases and philosophy. 

```{toctree}
:hidden:

self
quickstart
demo
```