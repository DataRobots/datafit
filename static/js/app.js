console.log("Displaying js")
$('#file').on('change',function(){
                //get the file name
                var fileName = $(this).val();
                //replace the "Choose a file" label
                $(this).next('.custom-file-label').html(fileName);
            })
   

   // variables for drop down menu for features independent and dependent selection
console.log("defined variables")
var columnurl = '/';
var columnheader_x;
var columnheader_y;
console.log("defined variables")
// load state drop down from Flask Route

//d3.json(columnurl).then(function(columndata){
 // console.log(columndata);

  Plotly.d3.json(columnurl,function(error,columndata){
  if (error) {
    return console.warn(error);
    };
  
console.log(columnurl);
    console.log(columndata);
    console.log("hello");

//   columndata[0].column_names.forEach(function(name) {
//   Plotly.d3
//       .select("#columnheader_y")
//       .append('option')
//       .attr('value', name)
//       .attr('class', 'dropdown')
//       .text(name)
// });

})