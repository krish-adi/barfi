import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    build: {
        outDir: "../src/barfi/static/ui-st",
    },
    base: "",
    server: {
        port: 3001,
    },
});
