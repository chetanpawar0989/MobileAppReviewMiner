/**
 * Created by Viral on 11/10/2014.
 */

var $ = window.$;
var data = []
var divIdChange = "";
     function changeSelection(divId){


                $('#criteria_all_reviews').removeClass('criteria_links_click');
                $(divIdChange).removeClass("criteria_links_click");
                divIdChange = "#criteria_" + divId + "";

                document.getElementById('Performance').style.display = 'none';
                document.getElementById('UserInterface').style.display = 'none';
                document.getElementById('Compatibility').style.display = 'none';
                document.getElementById('Request').style.display = 'none';
                document.getElementById('General').style.display = 'none';
                document.getElementById('all_reviews').style.display = 'none';
                document.getElementById('after_review_buttons').style.display = 'none';
                document.getElementById(divId).style.display = 'block';

                $('#criteria_links').height(
                    $(divId).height()
                );

                $(divIdChange).addClass("criteria_links_click");
                $('#graph_view').removeClass('btn-primary');
                $('#text_view').addClass('btn-primary');
            }

    function displayAll(){

    //            document.getElementById('Performance').style.display = 'block';
    //            document.getElementById('UserInterface').style.display = 'block';
    //            document.getElementById('Compatibility').style.display = 'block';
    //            document.getElementById('Request').style.display = 'block';
    //            document.getElementById('General').style.display = 'block';
    //            changeCriteriaDivHeight();

    }

    function changeCriteriaDivHeight(){
    //            $('#criteria_links').height(
    //                $('#Performance').height() + $('#UserInterface').height() + $('#Compatibility').height() + $('#Request').height() +
    //                   $('#General').height() + 300
    //
    //            );
    }





function drawChart(data){


	d3.select("body").selectAll("svg").remove();
	var width = 500,
    height = 500,
    radius = Math.min(width, height) / 2;

	var color = d3.scale.category20();

	var margin = {top: 0, right: 0, bottom: 0, left: 100};

	var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    .innerRadius(0);

	var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) { return d.votes; });

	var svg = d3.select("#after_review_buttons").append("svg")
    .attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + (margin.left+ width / 2) + "," + (margin.top+ height/2) +")");


	data.forEach(function(d) {
		d.votes = +d.votes;
	});

	console.log(pie(data));
	console.log("pie.....");
	var g = svg.selectAll(".arc")
      .data(pie(data))
	  .enter().append("g")
      .attr("class", "arc");
	   console.log(g);
       console.log("arc.....");
	   g.append("path")
      .attr("d", arc)
      .style("fill", function(d, i) { return color(i); });
       console.log(g);
       g.append("text")
      .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
      .attr("dy", ".35em")
      .style("text-anchor", "middle")
	  .style("paddingLeft", "50px")
      .text(function(d) { return d.data.name; });
}

    function changeView(type){
        if(type=="text"){
             //document.getElementById('Performance').style.display = 'none';
            $('#graph_view').removeClass('btn-primary');
            $('#text_view').addClass('btn-primary');
            changeSelection("all_reviews");

        }
        else{
             $(divIdChange).removeClass('criteria_links_click');            
             $('#criteria_all_reviews').addClass('criteria_links_click');
             document.getElementById('Performance').style.display = 'none';
             document.getElementById('UserInterface').style.display = 'none';
             document.getElementById('Compatibility').style.display = 'none';
             document.getElementById('Request').style.display = 'none';
             document.getElementById('General').style.display = 'none';
             document.getElementById('all_reviews').style.display = 'none';
             document.getElementById('after_review_buttons').style.display = 'block';
             drawChart(data);
             $('#text_view').removeClass('btn-primary');
             $('#graph_view').addClass('btn-primary');
        }
    }

$(document).ready(function() {
     changeSelection("all_reviews");

     if(categoryLength[0]!=0)
        data.push({name: 'Performance', votes: categoryLength[0]});
     if(categoryLength[1]!=0)
        data.push({ name: 'UserInterface', votes: categoryLength[1]});
     if(categoryLength[2]!=0)
        data.push({ name: 'Compatibility', votes: categoryLength[2]});
     if(categoryLength[3]!=0)
        data.push({ name: 'General', votes: categoryLength[3]});
     if(categoryLength[4]!=0)
        data.push({ name: 'Request', votes: categoryLength[4]});

//         data = [
//             { name: 'Performance', votes: categoryLength[0] },
//             { name: 'UserInterface', votes: categoryLength[1] },
//             { name: 'Compatibility', votes: categoryLength[2] },
//             { name: 'General', votes: categoryLength[3]},
//             { name: 'Request', votes: categoryLength[4]}
//         ]
     //}
	//drawChart(data);
});