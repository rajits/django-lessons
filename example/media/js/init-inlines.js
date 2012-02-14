$(function() {
	// Is this a new or existing object?
	if ($("div#content > h1").text().search("Add") > -1) {
		$("#id_lessonrelation_set-0-content_type option").eq(26).attr('selected', 'selected');
	}
})
