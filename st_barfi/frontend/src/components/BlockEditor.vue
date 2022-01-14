<template>
    <div id="editorCanvas">
        <!-- Hello, {{ args.name }}! &nbsp; -->
        <baklava-editor :plugin="viewPlugin" />
        <button class="editorData" @click="displayEditorData">Display</button>
        <button class="saveData">Save</button>
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
        };
    },
    created() {
        console.log(this.args);
        // Register the plugins
        // The view plugin is used for rendering the nodes
        this.editor.use(this.viewPlugin);
        // The option plugin provides some default option UI elements
        this.editor.use(new OptionPlugin());

        // Show a minimap in the top right corner
        this.viewPlugin.enableMinimap = true;

        // Read the infos on the node passed in from Streamlit
        // and register them.
        this.args.blocks.forEach((el) => {
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

        // Load the editor data if load_data not equal to null.
        if (this.args.load_data) {
            this.editor.load(this.args.load_data);
        }
    },
    methods: {
        displayEditorData() {
            // JSON.parse(JSON.stringify());
            console.log(this.editor.save());
            // Retrieve the editor data, and pass the new value back to
            // Streamlit via `Streamlit.setComponentValue`.
            Streamlit.setComponentValue(this.editor.save());
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
.node-editor .background {
    border-radius: 2px;
}
.editorData {
    position: absolute;
    top: 1rem;
    left: 1rem;
}
.saveData {
    position: absolute;
    top: 1rem;
    left: 6rem;
}
</style>
