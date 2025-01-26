# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Release dates are in YYYY-MM-DD

## [1.1.0] - 2025-01-26

-   Drop support Python 3.8, as it has reached end of life. Support only Python 3.9 and above. v +1.0.x will support Python 3.8. Essentialy to help users migrate to the current v +1.1.x.
-   Add support for async compute functions.
    -   `Block.add_compute` now supports binding a async compute function.
    -   `ComputeEngine.execute()` now supports async compute functions in sync and async contexts.
    -   `await ComputeEngine.async_execute()` is the new method to execute the flow schema asynchronously.
-   Add support for parallel execution of nodes.
    -   `ComputeEngine(execution_mode='parallel')` will execute the nodes in parallel. Default is parallel, can be set to serial using `execution_mode='serial'`.
    -   Default execution mode is parallel.
    -   `ComputeEngine.execute()` now supports parallel execution of nodes in sync and async contexts.
    -   `await ComputeEngine.async_execute()` is the new method to execute the flow schema asynchronously.

## [1.0.1] - 2025-01-13

-   Fix install errors with packaging errors from poetry. Package build to use poetry 2.0.1.

## [1.0.0] - 2025-01-05

Following are major changes from v0. For using >= v1.0.0 your codebase needs to be adopted. Check for the latest documentation [here](https://barfi.ai/docs)

-   `st_flow` is the new streamlit ui which replaces `st_barfi`. Refer to the new API to add interfaces and options [here](https://barfi.ai/docs/st_flow)
-   All objects are typed as dataclasses and not as `dict`. This applies to `Block`, `FlowSchema`, `SchemaManager`, `ComputeEngine` and the return from `st_flow` which is `StreamlitFlowResponse`.
-   `FlowSchema` is the object that now contains all the information about the schemasm the connections and blocks referred.
-   `barfi.flow.block` now contains all the `Block` module scripts. Refer to the new API to add interfaces and options [here](https://barfi.ai/docs/block)
-   `barfi.flow.schema` contains the `SchemaManager` which will be used to save, load, update, delete schemas.Refer to the new API to add interfaces and options [here](https://barfi.ai/docs/schema_manager)
-   `barfi.flow.compute` contains the `ComputeEngine` which will be used to execute the `FlowSchema`. Refer to the new API to add interfaces and options [here](https://barfi.ai/docs/compute_engine)
-   This version also introduces some types, and will henceforth the library will be typed. Refer to the types [here](https://barfi.ai/docs/types)
-   The UI Flow Editor has now been migrated to use React instead of Vue. And, makes use of ReactFlow as the rendering component for the flows.

## [0.7.0] - 2022-08-30

-   Add Block state to store data private to the block. Using block.get_state('key'), block.set_state('key').
-   Block state also stores execution status and errors. Using block.get_state('info'), block.set_state('info'). Note: 'info' is a reserved key.
-   When a block fails on its compute function, its descendants are skipped and the rest of the blocks are computed.
-   Add delete schema function. (@zabrewer)

## [0.6.1] - 2022-07-25

-   Fix base_blocks_list passed to the compute engine.

## [0.6.0] - 2022-07-19

-   Add option to categories the Blocks with a category in a sub-menu in the context menu on right-click>add-node.

## [0.5.0] - 2022-03-19

-   Add Block option.
-   Add tests for Block option and update tests for interfaces.
-   Add get, set for option to be used inside compute_engine and update compute_engine to handle option value from frontend

## [0.4.4] - 2022-03-16

-   Change barfo.Block method references from `calculate` to `compute`

## [0.4.3] - 2022-03-15

-   Change the frontend BlockEditor.vue to make use of listeners to make the unique names of the Blocks.

## [0.4.2] - 2022-02-27

-   Change add_input and add_output for the Block. TO provide ease of linting and checks.
-   Change the structure of the compute engine.
-   Add unittest
-   Add documentation and structure to the docs to be deployed to readthedocs.org

## [0.4.2] - 2022-02-27

-   Change add_input and add_output for the Block. TO provide ease of linting and checks.
-   Change the structure of the compute engine.
-   Add unittest
-   Add documentation and structure to the docs to be deployed to readthedocs.org

## [0.4.0] - 2022-02-27

-   Implement compute engine checks
-   Change menu for computation, load, save of schema

## [0.2.0] - 2022-02-13

-   ComputeEnginge class, with execute method
-   Client has Menu to Save and List schemas into a db.
-   Functions for managing save/load schemas

## [0.1.0] - 2022-02-12

-   Initial release.
-   Contains Block-Builder class
-   Contains the Compute engine function
-   Contains the frontend-client to use as Streamlit component - st_barfi()
