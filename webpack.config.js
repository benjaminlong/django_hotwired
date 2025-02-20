var path = require('path');
const glob = require("glob-all");
const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackPluginDjango = require("html-webpack-plugin-django");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { PurgeCSSPlugin } = require("purgecss-webpack-plugin");

// TODO: Add comment
const templateContent = ({ htmlWebpackPlugin }) =>
  `{% load static %}
  ${htmlWebpackPlugin.tags.headTags}
  ${htmlWebpackPlugin.tags.bodyTags}`;

// const __django_dir = path.resolve(__dirname, "django_hotwired")
const __front_dir = path.resolve(__dirname, "client")

module.exports = {
    entry: {
        app: path.resolve(__front_dir, "src/app.js")
    },
    output: {
        path: path.resolve(__front_dir, "build/dist"),
        filename: "[name].[contenthash].js",
        publicPath: "/static/dist/"
    },
    resolve: {
        extensions: ['.ts', '...'],
        alias: {
            images: path.resolve(__front_dir, 'public/images'),
        },
    },
    plugins: [
        new HtmlWebpackPlugin({
            filename: path.resolve(__front_dir, "src", "templates", "webpack.html"),
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
        }),
        new PurgeCSSPlugin({
            // defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
            // defaultExtractor: (content) => content.match(/[\w-/:]+(?<!:)/g) || [],
            defaultExtractor: content => content.match(/[^<>"'`\s]*[^<>"'`\s:]/g) || [],
            paths: glob.sync(
              // path.join(__front_dir, "src/**/*.html"),
              // { nodir: true }
              [
                path.join(__front_dir, "src/**/*.{js,jsx,ts,tsx,html}"),
                path.join(__front_dir, "src/components/**/*.{js,jsx,ts,tsx,html}"),
                path.join(__front_dir, "src/templates/**/*.{js,jsx,ts,tsx,html}"),
              ],
            ),

        }),
    ],
    module: {
        rules: [{
            test: /\.ts$/i,
            use: "ts-loader",
            exclude: /node_modules/,
        }, {
            test: /\.js$/,
            include: path.resolve(__front_dir, "src"),
            loader: "babel-loader",
        }, {
            test: /\.(png|jpe?g|gif|svg|webp|avif)$/i,
            type: "asset/resource",
            generator: {
                filename: "images/[name].[contenthash:7][ext]"
            },
        }, {
            test: /\.(s[ac]ss|css)$/,
            exclude: /node_modules/,
            include: path.resolve(__front_dir, "src"),
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
