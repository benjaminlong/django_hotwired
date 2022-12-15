var path = require('path');

module.exports = {
   entry: {
      stimulus: './assets/stimulus/application.js',
      turbolinks: './assets/turbolinks/application.js'
   },
   output: {
      path: path.resolve(__dirname, 'django_stimulus/static/js'),
      //filename: 'stimulus_controllers.js'
      filename: '[name].bundle.js'
   },
   mode:'development',
   module: {
      rules: [
         {
            test: /\.js$/,
            include: path.resolve(__dirname, 'assets'),
            loader: 'babel-loader',
            query: {
               presets: ["@babel/preset-env"]
            }
         }
      ]
   }
};
