$(document).ready(function() {
	$('body').delegate('.hoverable', 'hover', function() {
		$(this).toggleClass('hover');
	});

	$("#topics li").click(function() {
		document.location.href = $(this).children("a").attr("href");
	});

});
