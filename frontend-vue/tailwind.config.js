module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [
    "./components/**/*.{vue,js}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}"
  ],
  darkMode: false, // or 'media' or 'class
  theme: {
    extend: {}
  },
  variants: {},
  plugins: []
};
