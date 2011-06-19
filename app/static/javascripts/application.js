$(document).ready(function() {
	$('body').delegate('.hoverable', 'hover', function() {
		$(this).toggleClass('hover');
	});

	$("#topics li").click(function() {
		document.location.href = $(this).children("a").attr("href");
	});

});



var AgendaTrends = {
	parseDate: function(date) {
		console.log(date);
		var components = date.split('-');
		console.log(components);
		return Date.UTC(parseInt(components[0]), parseInt(components[1])-0, parseInt(components[2]));
    }



};
