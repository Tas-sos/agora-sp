/*jshint node:true*/
/* global require, module */
var EmberApp = require('ember-cli/lib/broccoli/ember-app');

module.exports = function(defaults) {
  var app = new EmberApp(defaults, {
    outputPaths: {
      app: {
        css: {
          'theme-eosc': '/assets/theme-eosc.css',
          'theme-ni4os': '/assets/theme-ni4os.css',
        },
      },
    },
  });

  return app.toTree();
};
