/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./a_users/templates/**/*.html",
    "./templates/**/*.html",
    "./**/templates/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        roboto: ["Roboto", "serif"],
      },
    },
  },
  plugins: [],
};
