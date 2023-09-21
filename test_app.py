
import streamlit as st
import barfi as bf

node = bf.Block("Block")
node.add_input("In")
node.add_output("Out")
node.add_option("Data", "input")

st.markdown("""
	<style>
	iframe {
		border-radius: 15px;
	}
	</style>
""", unsafe_allow_html=True)

bf.st_barfi(
	[node],
	style="""
		.button-menu {
			visibility: hidden;
		}
		.node {
			visibility: hidden;
		}
		.node > .__title {
			visibility: visible;
		}
		.node > .__content {
            background: red;
			border-radius: 0px 0px 32px 32px;
			visibility: visible;
        }
		.node-editor > .background {
			background: green;
		}
		svg {
			color: blue;
		}
	""",
)