$(document).ready(function() {
	var postId = 0;
	$('.post-title').toggle(function() {
		postId = parseInt($(this).attr('id').charAt($(this).attr('id').length-1));
		$('#post-content-'+postId).hide('slow');
	}, function() {
		postId = parseInt($(this).attr('id').charAt($(this).attr('id').length-1));
		$('#post-content-'+postId).show('slow');
	});
});
