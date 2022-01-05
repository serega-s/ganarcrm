module.exports = {
  pwa: {
    name: "GanarCRM",
    themeColor: "#4DBA87",
    msTileColor: "#000000",
    appleMobileWebAppCapable: "yes",
    appleMobileWebAppStatusBarStyle: "black",
    manifestPath: "public/manifest.json",

    // configure the workbox plugin
    // workboxPluginMode: "InjectManifest",
    // workboxOptions: {
    //   swSrc: "src/service-worker.js",
    // },
  },
}
