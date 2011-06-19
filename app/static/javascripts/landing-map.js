var mapStyles =
[
  {
    featureType: "administrative",
    elementType: "labels",
    stylers: [
      { visibility: "off" }
    ]
  },{
    featureType: "landscape",
    elementType: "all",
    stylers: [
      { visibility: "simplified" }
    ]
  },{
    featureType: "road",
    elementType: "all",
    stylers: [
      { visibility: "off" }
    ]
  },{
    featureType: "poi",
    elementType: "all",
    stylers: [
      { visibility: "off" }
    ]
  },{
    featureType: "transit",
    elementType: "all",
    stylers: [
      { visibility: "off" }
    ]
  },{
    featureType: "all",
    elementType: "all",
    stylers: [

    ]
  }
];

function initializeWithCoords(coords) {
/*
    var latlng = new google.maps.LatLng(coords.latitude, coords.longitude);
    var mapType = new google.maps.StyledMapType(
            mapStyles
            );

    var options = {
        zoom: 5,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true
    };
    var map = new google.maps.Map(document.getElementById("map-viewer"), options);

    map.mapTypes.set('myMapStyle', mapType);
    map.setMapTypeId('myMapStyle');
*/

    var po = org.polymaps;

    var quantile = pv.Scale.quantile()
        .quantiles(9)
        .domain(pv.values(states))
        .range(0, 8);

    var format = pv.Format.date("%B %e, %Y");
    

    var map = po.map()
        .container(document.getElementById('map-viewer').appendChild(po.svg("svg")))
        .center({ lat: coords.latitude, lon: coords.longitude })
        .zoomRange([5, 6])
        .zoom(4)
        .add(po.interact());

    map.add(po.geoJson()
            .url("http://polymaps.appspot.com/state/{Z}/{X}/{Y}.json")
            .on("load", load));

    map.container().setAttribute("class", "Blues");

    function load(e) {
      for (var i = 0; i < e.features.length; i++) {
        var feature = e.features[i], d = states[feature.data.id.substring(6)];
        if (d == undefined) {
          feature.element.setAttribute("display", "none");
        } else {
          feature.element.setAttribute("class", "q" + quantile(d) + "-" + 9);
          feature.element.appendChild(po.svg("title").appendChild(
              document.createTextNode(feature.data.properties.name + ": "
              + format(d).replace(/ [ ]+/, " ")))
              .parentNode);
        }
      }
    }
    


}

function loadLegislatorsWithCoords(coords) {
    $.getJSON('/api/legislators', 
            { 
              'latitude': coords.latitude,
              'longitude': coords.longitude 
            },
        function(data) {
            loadLegislators(data.legislators);
        }
    );
}


var legislators_g = null;
function loadLegislators(legislators) {
    legislators_g = legislators;
    $("#reps").empty();
    for ( var i = 0, len = legislators.length; i < len; ++i ) {
        var legislator = legislators[i].legislator;
        console.log(legislator);
        if ( legislator['facebook_id'] !== undefined ) {
            
            var anchor = $("<a href=\"" + legislator['website'] + "\"><img src=\"http://graph.facebook.com/" + legislator['facebook_id'] + "/picture\"/></a>" +
                    "<div class=\"tooltip\"><table>" +
                    "<tr><th>Name:</th><td>" + legislator['firstname'] + " " + legislator['lastname'] + "</td>" +
                    "<tr><th>Chamber:</th><td>" + legislator['chamber'].titleize() + "</td></tr>" +
                    "</table></div>")
                .tooltip({ position: "center right", relative: true});
            var listItem = $("<div class=\"rep\" id=\"" +  legislator['fec_id'] + "\"></div>")
                .append(anchor)
                .css({ top: (i*50) + "px" });
            $("#reps").append(listItem);

        }

    }

}


var moved_g = false;
function handleRepMentions(data) {
    console.log(data);

    var options = {
        title: {
            text: "Mentions"
        },
        xAxis: {
            title: { 
                text: null
            },
            labels: {
                rotation: 0,
                style: { color: "#FFF", fontSize: "10px" },
                step: 2
            },
            categories: $.map(data.rep_mentions, function(rep) {
                                return rep.fec_id;
                                })

        },
        yAxis: {
            title: "Mentions"
        },
        legend: {
            enabled: false
        },
        chart: {
            renderTo: 'map-viewer',
            zoomType: 'x',
            defaultSeriesType: 'bar'
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Mentions',
            data: $.map(data.rep_mentions, function(rep) {
                    return rep.mentions;
                    })
        }]
    };


    if ( !moved_g ) {
        $.each(data.rep_mentions, function(idx) {
                $("#" + this.fec_id).animate({
                    left: "+=30",
                    top: "+=" + (idx * 75 + 75)
                });
        });
        moved_g = true;
    }


    console.log(options);


    var chart = new Highcharts.Chart(options);

    $("#subscribe").slideDown('slow');



}




var client = new simplegeo.ContextClient('VsTU8grV92mP6NZMbwtdyQ8mNh7MyUQw');

client.getLocation({enableHighAccuracy: true}, function(err, position) {
        if (err) {
            // could not retrieve location
            console.log("ERROR");
        } else {
            console.log(position);
            initializeWithCoords(position.coords);
            loadLegislatorsWithCoords(position.coords);
        }


});



$(document).ready(function() {
    $("#topic-form").submit(function(e) {
        $.getJSON('/api/rep_mentions', 
            { reps: $.map( legislators_g, function(legislator, idx) {
                return legislator.legislator.fec_id;
                }).join(','),
              topic: $("#search").val()
            },
            handleRepMentions
        );

        e.preventDefault();
        return false;

    });
});

	

			
