# TODOs

## P0

-   [x] migrate to poetry for better deps management and local dev experience
-   [x] test the static files build in src
-   [x] migrate frontend client to react
-   [ ] migrate to using react-flow
    -   [x] add react-flow to the frontend src
    -   [x] custom nodes based on what was available from baklava.js, cutom design from the examples given
    -   [x] investigate the schema that react-flow generates
    -   [x] react-flow to barfi schema
    -   [x] test is the schema + compute engine works
    -   [ ] test for naming multiple nodes of same type (add a number generator to increase it incrementally)
    -   [ ] investigate schema sent from python st.client to the ui-client for making the migration possible
    -   [ ] able to construct the graph given a schema
-   [ ] custom actions on react flow -> node store
    -   [ ] delete node on ui -> del node in

## P1

-   [ ] algorithm changes
    -   [ ] move away from networkx
    -   [ ] add possibility for cycles
    -   [ ] multiple root nodes, implying multple flows possible
-   [ ] use the theme props given by the newer streamlit clients
-   [ ] move barfi client to separate pkg
