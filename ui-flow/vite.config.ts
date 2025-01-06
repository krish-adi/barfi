import path from "path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
    // base: './', // Set this to './' for relative paths
    plugins: [react()],
    resolve: {
        alias: {
            "@": path.resolve(__dirname, "./src"),
        },
    },
    build: {
        outDir: "../src/barfi/flow/streamlit/static",
        chunkSizeWarningLimit: 1024,
    },
    server: {
        port: 3001,
    },
});
