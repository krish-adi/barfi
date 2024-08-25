# TODOs

## P0

-   [x] migrate to poetry for better deps management and local dev experience
-   [x] test the static files build in src
-   [x] migrate frontend client to react
-   [ ] migrate to using react-flow
    -   [x] add react-flow to the frontend src
    -   [x] custom nodes based on what was available from baklava.js, cutom design from the examples given
    -   [x] investigate the schema that react-flow generates
    -   [ ] understand scema sent from python st.client to the ui-client for making the migration possible
    -   [ ] able to construct the graph given a schema
-   [ ] custom actions on react flow -> node store
    -   [ ] delete node on ui -> del node in 
-   [ ] algorithm changes
    -   [ ] multiple root nodes, implying multple flows possible

## P1

-   [ ] use the theme props given by the newer streamlit clients
-   [ ] move barfi client to separate pkg
