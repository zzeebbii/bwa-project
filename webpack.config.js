const webpack = require('webpack');
const path = require('path');

module.exports = {
    "entry": [__dirname + "/webpack/index.js", __dirname + "/webpack/sass/main.scss"],
    "output": {
        "path": path.resolve(__dirname, 'webpack/dist'),
        "filename": "js/bundle.js"
    },
    "module": {
        "rules": [
            {
                "test": /\.scss$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: 'css/[name].css',
                        }
                    },
                    {
                        loader: 'extract-loader'
                    },
                    {
                        loader: 'css-loader?-url'
                    },
                    {
                        loader: 'postcss-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            }
        ]
    },
    watchOptions: {
        poll: 1000 // Check for changes every second
    }
}