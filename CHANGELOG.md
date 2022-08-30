# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Release dates are in YYYY-MM-DD

## [0.7.0] - 2022-08-30

- Add Block state to store data private to the block. Using block.get_state('key'), block.set_state('key').
- Block state also stores execution status and errors. Using block.get_state('info'), block.set_state('info'). Note: 'info' is a reserved key.
- When a block fails on its compute function, its descendants are skipped and the rest of the blocks are computed.
- Add delete schema function. (@zabrewer)

## [0.6.1] - 2022-07-25

- Fix base_blocks_list passed to the compute engine. 

## [0.6.0] - 2022-07-19

- Add option to categories the Blocks with a category in a sub-menu in the context menu on right-click>add-node. 

## [0.5.0] - 2022-03-19

- Add Block option.
- Add tests for Block option and update tests for interfaces.
- Add get, set for option to be used inside compute_engine and update compute_engine to handle option value from frontend

## [0.4.4] - 2022-03-16

- Change barfo.Block method references from `calculate` to `compute`

## [0.4.3] - 2022-03-15

- Change the frontend BlockEditor.vue to make use of listeners to make the unique names of the Blocks.

## [0.4.2] - 2022-02-27

- Change add_input and add_output for the Block. TO provide ease of linting and checks.
- Change the structure of the compute engine.
- Add unittest
- Add documentation and structure to the docs to be deployed to readthedocs.org

## [0.4.2] - 2022-02-27

- Change add_input and add_output for the Block. TO provide ease of linting and checks.
- Change the structure of the compute engine.
- Add unittest
- Add documentation and structure to the docs to be deployed to readthedocs.org

## [0.4.0] - 2022-02-27

- Implement compute engine checks 
- Change menu for computation, load, save of schema

## [0.2.0] - 2022-02-13

- ComputeEnginge class, with execute method
- Client has Menu to Save and List schemas into a db.
- Functions for managing save/load schemas

## [0.1.0] - 2022-02-12

- Initial release.
- Contains Block-Builder class
- Contains the Compute engine function
- Contains the frontend-client to use as Streamlit component - st_barfi()
