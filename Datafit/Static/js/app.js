console.log('I am loaded');
function get_data_scientist(){
	
	const defaultURL = "/data_scientist";
	d3.json(defaultURL).then(function(data) {
 	var data1 = [data['plot1']];
 	var data2 = [data['plot2']];
 	var data3 = [data['plot3']];
  	console.log('data',data);
  	var layout1 = { title: 'Score Vs Skill' };
  	var layout2 = { title: 'Score Vs Education' };
  	var layout3 = { title: 'Score Vs Tool' };
  	Plotly.newPlot("plot", data1, layout1);
  	Plotly.newPlot("plot2", data2, layout2);
  	Plotly.newPlot("plot3", data3, layout3);

});

}

function get_data_analyst(){
	
	const defaultURL = "/data_analyst";
	d3.json(defaultURL).then(function(data) {
 	var data1 = [data['plot1']];
 	var data2 = [data['plot2']];
 	var data3 = [data['plot3']];
  	console.log('data',data);
  	var layout1 = { title: 'Score Vs Skill' };
  	var layout2 = { title: 'Score Vs Education' };
  	var layout3 = { title: 'Score Vs Tool' };
  	Plotly.newPlot("plot", data1, layout1);
  	Plotly.newPlot("plot2", data2, layout2);
  	Plotly.newPlot("plot3", data3, layout3);
});

}

function get_data_engineer(){
	
	const defaultURL = "/data_engineer";
	d3.json(defaultURL).then(function(data) {
 	var data1 = [data['plot1']];
 	var data2 = [data['plot2']];
 	var data3 = [data['plot3']];
  	console.log('data',data);
  	var layout1 = { title: 'Score Vs Skill' };
  	var layout2 = { title: 'Score Vs Education' };
  	var layout3 = { title: 'Score Vs Tool' };
  	Plotly.newPlot("plot", data1, layout1);
  	Plotly.newPlot("plot2", data2, layout2);
  	Plotly.newPlot("plot3", data3, layout3);

});


}
