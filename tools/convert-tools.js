/**

use to convert detexify data to png
need to know key

You can find key here: http://detexify.kirelabs.org/symbols.html

after this command run mogrify -format png data/latex2e-OT1-_infty/*.svg
change latex2e-OT1-_infty to right folder


**/

// import
var mkdirp = require('mkdirp');
var request = require('request-json');
var _ = require("underscore");
//var svg2png = require("svg2png");
var fs = require("fs");
var sys = require('sys')
var exec = require('child_process').exec;
var execSync = require('child_process').execSync;

// setup

var key = "latex2e-OT1-_infty"
if (process.argv.length >= 3){
    key = process.argv[2]
}

var folder_path = "./data/" + key + "/"
var host = "http://127.0.0.1:5984/"
var database = "detexity"
var url = database + "/_design/tools/_view/by_id?key=%22" + key + "%22&reduce=false&include_docs=true"
var client = request.createClient(host);
var svg_begin = '<svg style="overflow: hidden; position: relative;" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="400" version="1.1" height="400">'
var svg_end = '</svg>'
var path_begin = '<path transform="matrix(1,0,0,1,0,0)" fill="none" stroke="#000" d="'
var path_end = '" stroke-width="5" stroke-linecap="round"></path>'

var stroke2path = function(stroke) {
    if(!stroke){return ;}
    var first = _.first(stroke);
    var path = _.map(_.rest(stroke), function(point) { return ["L", point.x, point.y]; })
    if (path.length == 0)
        return [["M", first.x, first.y], ["l", 0, 0.1]];
    else
        return [["M", first.x, first.y]].concat(path);
}

// make folder
mkdirp(folder_path, function (err) {
    if (err) console.error(err)
    // else console.log('pow!')
});

// get data
client.get(url, function(err, res, body) {
    console.log(body.rows.length);
    body.rows.forEach(function(element, index, array){
        var svgstring = "";
        element.doc.data.forEach(function(de, di, da){
            var pathstring = _.map(stroke2path(de), function(a){return a[0]+a[1]+","+a[2]}).join("")
            svgstring += (path_begin + pathstring + path_end);
        })
        
        // console.log(svgstring);
        var svgdata = svg_begin + svgstring + svg_end;
        // console.log(data);
        // var outputbuffer = svg2png.sync(new Buffer(svgdata))
        var filename = folder_path+index;
        var fsvg = filename + ".svg";
        var fpng = filename + ".png";
        var cmd = "convert "+fsvg + " " + fpng;
        fs.writeFile(fsvg, svgdata, function(err){
		  console.log(index);
        });
        // execSync(cmd);

    })
});











