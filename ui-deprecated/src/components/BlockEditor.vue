<template>
    <div id="editorCanvas">
        <!-- Menu Modal -->
        <div
            class="modal"
            :style="menuModal ? 'display: block;' : 'display: none;'"
        >
            <div class="modal-content">
                <span class="close" @click="menuModal = !menuModal"
                    >&times;</span
                >

                <div class="tab">
                    <button
                        class="tablinks"
                        :class="listTab ? 'active' : ''"
                        @click="activateTab('listTab')"
                    >
                        List
                    </button>
                    <button
                        class="tablinks"
                        :class="saveTab ? 'active' : ''"
                        @click="activateTab('saveTab')"
                    >
                        Save
                    </button>
                </div>

                <div
                    class="tabcontent"
                    :style="listTab ? 'display: block;' : 'display: none;'"
                >
                    <label>List of saved schemas</label>

                    <ul>
                        <li v-for="(schema, index) in loadSchemas" :key="index">
                            {{ schema }}
                        </li>
                    </ul>
                    <p>
                        Current schema:
                        <span style="font-weight: 600">{{
                            this.loadSchemaName
                        }}</span>
                    </p>
                </div>

                <div
                    class="tabcontent"
                    :style="saveTab ? 'display: block;' : 'display: none;'"
                >
                    <label>Enter name to save schema as</label>
                    <input v-model="saveSchemaName" placeholder="Schema name" />
                    <button
                        v-if="saveSchemaName !== ''"
                        class="modal-button"
                        @click="saveEditorData"
                    >
                        Save
                    </button>
                    <button
                        v-else
                        class="modal-button modal-button-disabled"
                        @click="saveEditorData"
                    >
                        Save
                    </button>
                    <p v-if="this.saveSchemaName === this.loadSchemaName">
                        The entered schema name is similar to one already
                        existing in the database, saving will override the data
                        for the schema name.
                    </p>
                </div>
            </div>
        </div>
        <!-- Block Link Editor -->
        <baklava-editor :plugin="viewPlugin" />
        <div class="button-menu">
            <button @click="menuModal = !menuModal">Menu</button>
            <button @click="executeEditorData">Execute</button>
        </div>
    </div>
</template>

<script>
import { Streamlit } from "streamlit-component-lib";
import { Editor } from "@baklavajs/core";
import { ViewPlugin } from "@baklavajs/plugin-renderer-vue";
import { OptionPlugin } from "@baklavajs/plugin-options-vue";
import { Engine } from "@baklavajs/plugin-engine";
import { BlockBuilder } from "./BlockBuilder";

export default {
    name: "BlockEditor",
    // Arguments that are passed to the plugin in Python are
    // accessible in props `args`. Here, we access the "name" arg.
    props: ["args"],
    data() {
        return {
            editor: new Editor(),
            viewPlugin: new ViewPlugin(),
            engine: new Engine(true),
            menuModal: false,
            listTab: true,
            saveTab: false,
            saveSchemaName: "",
            loadSchemaName: "",
            loadSchemas: [],
            BlockNameID: {},
        };
    },
    created() {
        this.loadSchemas = this.args.load_schema_names;
        // Register the plugins
        // The view plugin is used for rendering the nodes
        this.editor.use(this.viewPlugin);
        // The option plugin provides some default option UI elements
        this.editor.use(new OptionPlugin());
        // The engine plugin computes the nodes in the graph in the
        // correct order using the "compute" methods of the nodes
        this.editor.use(this.engine);

        // Show a minimap in the top right corner
        this.viewPlugin.enableMinimap = true;

        console.log(this.args);
        // Read the infos on the node passed in from Streamlit
        // and register them.
        this.args.base_blocks.forEach((el) => {
            const Block = BlockBuilder({
                BlockName: el.name,
                Inputs: el.inputs,
                Outputs: el.outputs,
                Options: el.options,
            });
            // register the nodes we have defined, so they can be
            // added by the user as well as saved & loaded. Add a
            // category to it if it exists.

            if (Object.prototype.hasOwnProperty.call(el, "category")) {
                this.editor.registerNodeType(el.name, Block, el.category);
            } else {
                this.editor.registerNodeType(el.name, Block);
            }

            // this.editor.registerNodeType(el.name, Block);
            this.BlockNameID[el.name] = 1;
        });

        // Load the editor data if load_editor_schema not equal to null.
        if (this.args.load_editor_schema) {
            this.editor.load(this.args.load_editor_schema);
        }
        this.loadSchemaName = this.args.load_schema_name;

        // Change name of the added node to get a unique name.
        this.editor.events.addNode.addListener(this, (data) => {
            this.editor._nodes.forEach((node) => {
                if (node.id === data.id) {
                    node.name = node.name + "-" + this.BlockNameID[data.name]++;
                }
            });
        });
    },
    methods: {
        executeEditorData() {
            // Retrieve the editor data, and pass the new value back to
            // Streamlit via `Streamlit.setComponentValue`.
            Streamlit.setComponentValue({
                command: "execute",
                editor_state: this.editor.save(),
            });
        },
        saveEditorData() {
            Streamlit.setComponentValue({
                command: "save",
                schema_name: this.saveSchemaName,
                editor_state: this.editor.save(),
            });
            this.saveSchemaName = "";
            this.menuModal = !this.menuModal;
        },
        activateTab(tabName) {
            if (tabName === "listTab") {
                this.listTab = true;
                this.saveTab = false;
            }
            if (tabName === "saveTab") {
                this.listTab = false;
                this.saveTab = true;
            }
        },
    },
};
</script>

<style>
#editorCanvas {
    position: relative;
    height: 85vw;
    width: 100vw;
}
.button-menu {
    position: absolute;
    top: 1rem;
    left: 1rem;
}
.load-button {
    position: absolute;
    top: 1rem;
    left: 10.7rem;
}
.button-menu button {
    font-weight: 500 !important;
    font-size: small !important;
    background: rgba(75, 75, 75, 1);
    border: 2px solid rgba(75, 75, 75, 1);
    filter: drop-shadow(0 0 3px rgba(0, 0, 0, 0.8));
    transition: box-shadow 0.1s linear, filter 0.1s linear;
    color: var(--node-text);
    border-radius: 3px;
    padding: 1px 7px;
    margin: 0 0.5rem;
    cursor: pointer;
    outline: inherit;
}
.button-menu button:hover {
    background: rgba(75, 75, 75, 0.4);
    border: 2px solid rgba(75, 75, 75, 0.4);
}
.modal {
    position: fixed;
    z-index: 1;
    padding-top: 100px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.6);
}
.modal-content {
    position: relative;
    background: #ffffff;
    margin: auto;
    padding: 20px;
    border: 0px solid #888;
    border-radius: 5px;
    width: 60%;
    text-align: left;
}
label {
    display: block;
    margin: 0 0 12px 0;
    font-weight: 500 !important;
}
input,
select {
    width: 60%;
    margin: 0 0 16px 0;
    padding: 8px 12px;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}
.modal-button {
    display: inline-block;
    margin-left: 1rem;
    font-weight: 500 !important;
    font-size: medium !important;
    background: rgba(75, 75, 75, 1);
    border: 0px solid rgba(75, 75, 75, 1);
    color: var(--node-text);
    border-radius: 3px;
    padding: 8px 12px;
    cursor: pointer;
    outline: inherit;
}
.modal-button:hover {
    background: rgba(75, 75, 75, 0.8);
}
.modal-button-disabled {
    background: rgb(182, 182, 182);
    border: 0px solid rgb(182, 182, 182);
    cursor: not-allowed;
    pointer-events: none;
}
.close {
    right: 13px;
    top: 4px;
    position: absolute;
    color: #aaaaaa;
    font-size: 22px;
    font-weight: bold;
    cursor: pointer;
}
.close:hover,
.close:focus {
    color: #000;
    text-decoration: none;
}
.tab {
    overflow: hidden;
    padding: 0 20px;
}
.tablinks {
    background: #ffffff;
    color: #0d6efd;
    float: left;
    border: none;
    border-radius: 3px;
    outline: none;
    cursor: pointer;
    padding: 5px 0;
    width: 60px;
    margin: 0 5px;
    transition: 0.3s;
    font-size: 14px;
}
.tablinks:hover {
    border-bottom: none;
    background: #72aafe;
    color: #ffffff;
}
.tablinks.active {
    background: #0d6efd;
    color: #ffffff;
}
.tabcontent {
    padding: 20px 30px 5px 30px;
    transition: 0.3s;
}
.tabcontent ul {
    height: 73px;
    margin: 5px 30px 5px 10px;
    padding: 5px 40px;
    background: #f2f2f2;
}
.tabcontent ul {
    overflow: hidden;
    overflow-y: scroll;
}
</style>
