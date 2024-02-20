module.exports = {
  content: [
    './templates/**/*.html', // путь к вашим HTML файлам
  ],
  theme: {
    extend: {
      colors: {
        primary: '#ff0000', 
        secondary: '#00ff00', 
      },
      fontFamily: {
        sans: ['Roboto', 'sans-serif']
      },
      spacing: {
        '72': '18rem', 
      },
    },
  },
  plugins: [

  ],
};
