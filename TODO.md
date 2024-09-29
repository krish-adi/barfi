# TODOs

## P0

-   [x] migrate to poetry for better deps management and local dev experience
-   [x] test the static files build in src
-   [x] migrate frontend client to react
-   [x] migrate to using react-flow
    -   [x] add react-flow to the frontend src
    -   [x] custom nodes based on what was available from baklava.js, cutom design from the examples given
    -   [x] investigate the schema that react-flow generates
    -   [x] react-flow to barfi schema
    -   [x] test is the schema + compute engine works
    -   [x] test for naming multiple nodes of same type (add a number generator to increase it incrementally)
    -   [x] investigate schema sent from python st.client to the ui-client for making the migration possible
    -   [x] able to construct the graph given a schema
-   [x] make export in ui simple and handle migrations in the backend
-   [x] change custom node to base block node
-   [x] custom actions on react flow -> node store
    -   [x] delete node on ui -> del node in
-   [ ] add strong type cheing on the python side
-   [ ] add schema version to the schema saved and sent from ui-flow
    -   [ ] Check for saving old schema
    -   [ ] Check for loading old schema
-   [ ] check if options work
    -   [ ] if options from schema are loaded
    -   [ ] if options 
-   [ ] state data are different across all the places.
    -   [ ] when a component is loaded from schema to editor, option values must be loaded from the store. essentially option values must only be from the store.
    -   [ ] when a block is loaded from barfi-state into editor, it must be transformed to be in type `Node`
    -   [ ] keep node and baseBlock different. but you can refresh the nodes added to the editor from the baseblock.
    -   [ ] migrate BarfitateNode to FlowStateNode.
-   [ ] check data scemas and types across the app from base-block, node, base-block are different in py and ts
    -   [ ] ideal should be blacks have only "name", nodes have name which is the label and type which is the name from baseblock
-   [ ] migrate the TextOption to a display option with display as text

```
interface TextOption {
    name: string;
    type: "TextOption";
    value: string;
}
```

## P1

-   [ ] algorithm changes
    -   [ ] move away from networkx
    -   [ ] add possibility for cycles
    -   [ ] multiple root nodes, implying multple flows possible
-   [ ] use the theme props given by the newer streamlit clients
-   [ ] move barfi client to separate pkg
