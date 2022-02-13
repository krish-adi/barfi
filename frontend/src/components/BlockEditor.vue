<template>
    <div id="editorCanvas">
        <!-- Save Modal -->
        <div
            class="modal"
            :style="saveModal ? 'display: block;' : 'display: none;'"
        >
            <div class="modal-content">
                <span class="close" @click="saveModal = !saveModal"
                    >&times;</span
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
                    class="modal-button-disabled"
                    @click="saveEditorData"
                >
                    Save
                </button>
            </div>
        </div>
        <!-- Load Modal -->
        <div
            class="modal"
            :style="loadModal ? 'display: block;' : 'display: none;'"
        >
            <div class="modal-content">
                <span class="close" @click="loadModal = !loadModal"
                    >&times;</span
                >
                <label>Select to load schema from list</label>
                <select v-model="loadSchemaName">
                    <option
                        v-for="(option, index) in loadSchemas"
                        :value="option"
                        :key="index"
                    >
                        {{ option }}
                    </option>
                </select>
                <button class="modal-button" @click="loadEditorData">
                    Load
                </button>
            </div>
        </div>
        <!-- Block Link Editor -->
        <baklava-editor :plugin="viewPlugin" />
        <button
            class="execute-button control-button"
            @click="executeEditorData"
        >
            Execute
        </button>
        <button
            class="save-button control-button"
            @click="saveModal = !saveModal"
        >
            Save
        </button>
        <button
            class="load-button control-button"
            @click="loadModal = !loadModal"
        >
            Load
        </button>
    </div>
</template>

<script>
import { Streamlit } from "streamlit-component-lib";
import { Editor } from "@baklavajs/core";
import { ViewPlugin } from "@baklavajs/plugin-renderer-vue";
import { OptionPlugin } from "@baklavajs/plugin-options-vue";
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
            saveModal: false,
            loadModal: false,
            saveSchemaName: "",
            loadSchemaName: "",
            loadSchemas: [],
        };
    },
    created() {
        console.log(this.args);
        this.loadSchemas = this.args.load_schema_names;
        // Register the plugins
        // The view plugin is used for rendering the nodes
        this.editor.use(this.viewPlugin);
        // The option plugin provides some default option UI elements
        this.editor.use(new OptionPlugin());

        // Show a minimap in the top right corner
        this.viewPlugin.enableMinimap = true;

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
            // added by the user as well as saved & loaded.
            this.editor.registerNodeType(el.name, Block);
        });

        // Load the editor data if load_editor_schema not equal to null.
        if (this.args.load_editor_schema) {
            this.editor.load(this.args.load_editor_schema);
        }
        this.loadSchemaName = this.args.load_schema_name
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
            this.saveModal = !this.saveModal;
        },
        loadEditorData() {
            Streamlit.setComponentValue({
                command: "load",
                schema_name: this.loadSchemaName,
            });
            this.loadModal = !this.loadModal;
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
.modal {
    position: fixed;
    z-index: 1;
    padding-top: 100px;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0, 0, 0);
    background-color: rgba(0, 0, 0, 0.4);
}
.modal-content {
    position: relative;
    background-color: #f2f2f2;
    margin: auto;
    padding: 20px;
    border: 0px solid #888;
    border-radius: 5px;
    width: 60%;
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
    display: block;
    margin: 0px auto;
    font-weight: 500 !important;
    font-size: medium !important;
    background: rgba(75, 75, 75, 1);
    border: 0px solid rgba(75, 75, 75, 1);
    color: var(--node-text);
    border-radius: 3px;
    padding: 3px 12px;
    cursor: pointer;
    outline: inherit;
}
.modal-button:hover {
    background: rgba(75, 75, 75, 0.8);
}
.modal-button-disabled {
    display: block;
    margin: 0px auto;
    font-weight: 500 !important;
    font-size: medium !important;
    background: rgb(182, 182, 182);
    border: 0px solid rgb(182, 182, 182);
    color: var(--node-text);
    border-radius: 3px;
    padding: 3px 12px;
    cursor: not-allowed;
    pointer-events: none;
    outline: inherit;
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
</style>
