var margin = {top: 40, right: 10, bottom: 180, left: 10},
    width = 1000 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var formatPercent = d3.format(".0%");

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .tickFormat(formatPercent);

var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function (d) {
        return "<strong>STATE:</strong> <span style='color:red'>" + d.ST_NAME + "</span><br><strong>Military Base Count:</strong>  <span style='color:red'>" + d.count + "</span>";
    })

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.call(tip);

d3.csv("military.csv", type, function (error, data) {
    x.domain(data.map(function (d) {
        return d.ST_NAME.slice(0,2);
    }));
    y.domain([0, d3.max(data, function (d) {
        return d.count;
    })]);

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
    // .selectAll("text")
    // .style("text-anchor","end")
    // .attr("transform","rotate(-90)");

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Count");

    svg.selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function (d) {
            return x(d.ST_NAME.slice(0,2));
        })
        .attr("width", x.rangeBand())
        .attr("y", function (d) {
            return y(d.count);
        })
        .attr("height", function (d) {
            return height - y(d.count);
        })
        .on('mouseover', tip.show)
        .on('mouseout', tip.hide)

});

function type(d) {
    d.count = +d.count;
    return d;
}