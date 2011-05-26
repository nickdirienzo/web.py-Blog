$(document).ready(function() {
	var postId = 0;
	$('.toggle-content').toggle(function() {
		postId = $(this).attr('id').match(/(\d+)/)[0];
		if((postId == $('.post-title').length-1) || ($('.post-title').length-1 == 0)) {
			$('#post-content-'+postId).hide('fast');
			$('#toggle-content-'+postId).text('Show Post Content');
		} else {
			$('#post-content-'+postId).show('fast');
			$('#toggle-content-'+postId).text('Hide Post Content');
		}
	}, function() {
		postId = $(this).attr('id').match(/(\d+)/)[0];
		if((postId == $('.post-title').length-1) || ($('.post-title').length-1 == 0)) {
			$('#post-content-'+postId).show('fast');
			$('#toggle-content-'+postId).text('Hide Post Content');
		} else {
			$('#post-content-'+postId).hide('fast');
			$('#toggle-content-'+postId).text('Show Post Content');
		}
	});
});
