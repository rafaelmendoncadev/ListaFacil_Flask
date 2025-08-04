/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./app/templates/**/*.{html,js}"],
    darkMode: 'class',
  theme: {
      extend: {
        colors: {
          primary: '#059669',
          secondary: '#DC2626',
          neutral: '#6B7280'
        }
      },
    },
  plugins: [],
}

