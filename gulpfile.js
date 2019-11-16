// Include gulp
var gulp = require('gulp');

// Include Our Plugins
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var autoprefixer = require('autoprefixer');
var postcss = require('gulp-postcss');

var paths = {
  styles: {
    src: 'collection/static/scss/*.scss',
    dest: 'collection/static/css'
  },
  scripts: {
    src: 'collection/static/js/*.js',
    dest: 'collection/static/js'
  }
};

//Compile Our Sass
function styles() {
  return gulp.src(paths.styles.src)
    .pipe(sass())
    .pipe(gulp.dest(paths.styles.dest));
};

// Concatenate
function scripts() {
  return gulp.src(paths.scripts.src, { sourcemaps: true })
        .pipe(concat('all.js'))
        .pipe(gulp.dest(paths.scripts.dest));
};

// Watch Files For Changes
function watch() {
  gulp.watch(paths.styles.src, styles);
  gulp.watch(paths.scripts.src, scripts);
}

var build = gulp.series(styles, scripts);


exports.styles = styles;
exports.scripts = scripts;
exports.watch = watch;
/*
 * Define default task that can be called by just running `gulp` from cli 
 */

//var build = gulp.series(sass);

exports.default = build;