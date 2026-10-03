import { defineConfig } from "vite";

const pagesBase = "/fabrica-dashboard/demos/character-rig/";

export default defineConfig({
  base: process.env.GITHUB_PAGES === "1" ? pagesBase : "/",
  publicDir: "assets",
  server: { host: true, port: 5173 },
  preview: { host: true, port: 4173 },
});
