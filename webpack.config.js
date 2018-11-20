const webpack = require('webpack');
const path = require('path');

module.exports = {
    "entry": [__dirname + "/webpack/index.js"],
    "output": {
        "path": path.resolve(__dirname, 'webpack/dist'),
        "filename": "js/bundle.js",
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
                        loader: 'css-loader'
                    },
                    {
                        loader: 'postcss-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            },
            {
                test: /\.woff($|\?)|\.woff2($|\?)|\.ttf($|\?)|\.eot($|\?)|\.svg($|\?)/,
                loader: 'file-loader',
                options: {
                    name: 'fonts/[name].[ext]',
                }
            }
        ]
    },
    watchOptions: {
        poll: 1000 // Check for changes every second
    }
}