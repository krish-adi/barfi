Compute Engine
==============

With the *editor* a schema is created using the base *Blocks* and making connections with the blocks. The data is assumed to flow from the output of one *Block* to the input of the other. The output of each *Block* is evaluated based on the computation function specified to it. And there for upon the evaluation of the compute function of each *Block*, its output is updated. 

To determine which *Block* to evaluate first ande next and so on, a computational graph is built. From the graph a topological sort is performed to determine the order in which the *Blocks* need to be evaluated.

.. Warning::
   Cycles in the *schema* cannot be evaluated at this moment. The derived compuation graph needs to be a Directed Acyclic Graph (DAG).