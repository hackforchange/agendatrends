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
		var components = date.split('-');
		return Date.UTC(parseInt(components[0]), parseInt(components[1])-0, parseInt(components[2]));
    },

	chartDateFormatter: function() {
		return Highcharts.dateFormat("<em>%B</em><br/>%d", this.value);
	},

	DATES_RESOLUTION: 4

};


String.prototype.titleize = function() {
    return this.substring(0,1).toUpperCase() + this.substring(1);

}
