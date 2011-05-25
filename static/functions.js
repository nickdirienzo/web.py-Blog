$(document).ready(function() {
	var postId = 0;
	$('.toggle-content ').toggle(function() {
		postId = parseInt($(this).attr('id').charAt($(this).attr('id').length-1));
		if((postId == $('.post-title').length-1) || ($('.post-title').length-1 == 0)) {
			$('#post-content-'+postId).hide('fast');
			$('#toggle-content-'+postId).text('Show Post Content');
		} else {
			$('#post-content-'+postId).show('fast');
			$('#toggle-content-'+postId).text('Hide Post Content');
		}
	}, function() {
		postId = parseInt($(this).attr('id').charAt($(this).attr('id').length-1));
		if((postId == $('.post-title').length-1) || ($('.post-title').length-1 == 0)) {
			$('#post-content-'+postId).show('fast');
			$('#toggle-content-'+postId).text('Hide Post Content');
		} else {
			$('#post-content-'+postId).hide('fast');
			$('#toggle-content-'+postId).text('Show Post Content');
		}
	});
});
