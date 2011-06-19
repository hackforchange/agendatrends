var lastestData = {};
var updateExtremes = function() {
    var extremes = this.getExtremes();

    if ( (extremes.max - extremes.min)/(1000*24*3600) > AgendaTrends.DATE_RESOLUTION ) {
        return;
    }

    $("#results-feed").empty();
    $.each(latestData['people'], function(name, person) {
            $("#results-feed").append("<h3>" + name + "</h3>");
            var theDiv = $("<div></div>");
            var theList = $("<ul></ul>");
            theDiv.append(theList);
            for ( var i = 0, len = person.data.length; i < len; ++i ) {
                var date = AgendaTrends.parseDate(person.data[i].date);
                if ( date > extremes.min && date < extremes.max ) {
                    theList.append("<li><a href=\"" + person.data[i].source + "\">" + person.data[i].source + "</a></li>");
                }
            }
            $("#results-feed").append(theDiv);
    });
    $("#results-feed").accordion({
        collapsible: true
    });
};

var options = {
    title: {
        text: $("#chart").data("topic")
    },
    xAxis: {
        title: { 
            text: null
        },
        type: 'datetime',
        events: {
            setExtremes: updateExtremes
        },
        labels: {
            formatter: AgendaTrends.chartDateFormatter,
            rotation: 0,
            style: { color: "#444444", fontSize: "10px" },
            step: 2
        }

    },
    yAxis: {
        title: {
            text: 'Mentions'
        },
    },
    chart: {
        renderTo: 'chart',
        zoomType: 'x',
        defaultSeriesType: 'area'
    },
    credits: {
        enabled: false
    },
    series: []
};



$.getJSON($("#chart").data("url"), function(data) {
    latestData = data;
    $.each(data['people'], function(name, person) {
        var series = {
            name: name,
            data: []
        };
        var dates = {};

        for ( var i = 0, len = person.data.length; i < len; ++i ) {
            var date = person.data[i].date;
            if ( !(date in dates) ) {
                dates[date] = 0;
            }
            dates[date]++;
        }

        $.each(dates, function(key, value) {
            series.data.push([AgendaTrends.parseDate(key), value]);
        });


        options.series.push(series)
    });

    var chart = new Highcharts.Chart(options);

});

