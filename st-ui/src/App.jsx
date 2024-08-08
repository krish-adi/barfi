import { useEffect } from "react";
import { withStreamlitConnection, Streamlit } from "streamlit-component-lib";

function App({ args }) {
    // const { title, input_schema } = args;

    useEffect(() => {
        Streamlit.setFrameHeight();
    });

    const onClick = (values) => {
        console.log(args);
        // Streamlit.setComponentValue(values);
    };

    return (
        <button className="" onClick={onClick}>
            Run!
        </button>
    );
}

const StreamlitAppComponent = withStreamlitConnection(App);
export default StreamlitAppComponent;
