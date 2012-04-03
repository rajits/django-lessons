function showtab(num)
{
    $(".page").hide();
    $(".page" + num).show();

    // clear/ set which is active
    $(".tab").removeClass("selected");
    $("#tab" + num).addClass("selected");
}

$(function() {
    if ($("div#content > h1").text().search("Add") > -1) {
        // This is a new object - set default values
        var selectBox = $("#id_lessonrelation_set-0-content_type");
        selectBox.val("26").attr('selected', 'selected');

        $("#id_lessonrelation_set-0-object_id").val("1");
    }

    showtab(0);

    $(".tab").click(function() {
        showtab(this.id.replace(/[^\d]/g, ""));
    });

    // (EDU-2396) When user checks published checkbox, update
    // published_date with current date and time.
    $("#id_published").click(function() {
        DateTimeShortcuts.handleCalendarQuickLink(0, 0);
        DateTimeShortcuts.handleClockQuicklink(0, new Date().getHourMinuteSecond());
    });
});
