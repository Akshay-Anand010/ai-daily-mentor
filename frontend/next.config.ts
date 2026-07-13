import type { NextConfig } from "next";
// GitHub Pages is a static host. The API, database and scheduled worker run
// separately (for example on Render or Railway).
const repository = process.env.GITHUB_REPOSITORY?.split("/")[1];
const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,
  basePath: process.env.GITHUB_ACTIONS && repository ? `/${repository}` : "",
};
export default nextConfig;
