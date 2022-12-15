var path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackPluginDjango = require("html-webpack-plugin-django");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

// TODO: Add comment
const templateContent = ({ htmlWebpackPlugin }) =>
  `{% load static %}
  ${htmlWebpackPlugin.tags.headTags}
  ${htmlWebpackPlugin.tags.bodyTags}`;

const __django_dir = path.resolve(__dirname, "django_hotwired")

module.exports = {
    entry: {
        app: path.resolve(__django_dir, "_assets/application.js")
    },
    output: {
        path: path.resolve(__django_dir, "_static", "dist"),
        filename: "[name].[contenthash].js",
        publicPath: "/static/dist/"
    },
    resolve: {
        extensions: ['.ts', '...'],
        alias: {
            images: path.resolve(__django_dir, '_static/images/'),
        },
    },
    plugins: [
        new HtmlWebpackPlugin({
            filename: path.resolve(__django_dir, "_templates", "webpack.html"),
            inject: false,
            templateContent: templateContent,
            scriptLoading: "defer",
            hash: false,
            minify: false,
            cache: true,
        }),
        new HtmlWebpackPluginDjango({ bundlePath: "dist" }),
        new CleanWebpackPlugin(),
        new MiniCssExtractPlugin({
            // Options similar to the same options in webpackOptions.output
            // both options are optional
            filename: "[name].[contenthash].css",
            chunkFilename: "[name].[id].css"
        })
    ],
    module: {
        rules: [{
            test: /\.ts$/i,
            use: "ts-loader",
            exclude: /node_modules/,
        }, {
            test: /\.js$/,
            include: path.resolve(__django_dir, "_assets"),
            loader: "babel-loader",
        }, {
            test: /\.(png|jpe?g|gif|svg|webp|avif)$/i,
            type: 'asset/resource',
            generator: {
                filename: 'images/[name].[contenthash:7][ext]'
            },
        }, {
            test: /\.(s[ac]ss|css)$/,
            exclude: /node_modules/,
            include: path.resolve(__django_dir, '_assets'),
            use: [
                // Creates `style` nodes from JS strings
                // 'style-loader',
                MiniCssExtractPlugin.loader,
                // Translates CSS into CommonJS
                "css-loader",
                "postcss-loader",
                // Compiles Sass to CSS
                "sass-loader"
            ]
        }]
    },
    watchOptions: {
        aggregateTimeout: 200,
        poll: 1000,
        ignored: ["**/webpack.html"],
    },
};
