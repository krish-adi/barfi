Schema
======

As introduced in the earlier sections, a *schema* is a constructed data flow diagram composed of the base *Blocks*. It captures all the *Blocks* on the editor along with all the connections made to it. 

On saving a *schema*, a *schema.barfi* database file is created in the project folder that stores all the schemas. A unique name must be given upon saving a *schema*. Schemas can be loaded using the `load_schema` argument to `st_barfi`. This way schemas needn't to be created each time. 

A list of all saved schemas can be viewed in the interface by using the **Menu** button. And in the same **Menu** schemas can be saved. 

At the script level, the method `barfi.barfi_schemas()` can be used to get the names of all the schemas saved in the database. 

API Reference
-------------

``barfi.barfi_schemas()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :width: 100%
   :widths: 25 75
   :header-rows: 0

   * - **Parameters**
     - **None**
   * - 
     - *None*
   * - **Returns**
     - **list** : *List of str*
   * - 
     - A list of all the saved schemas as a list of strings.                         

**Example**

.. code-block:: python
  :linenos:

  from barfi import barfi_schemas
  import streamlit as st

  saved_schemas = barfi_schemas()

  select_schema = st.selectbox('Select a saved schema:', saved_schemas)

  feed = Block(name='Feed')
  feed.add_input()
  result = Block(name='Result')
  result.add_output()

  barfi_result = st_barfi(base_blocks= [feed, result], load_schema=select_schema)

