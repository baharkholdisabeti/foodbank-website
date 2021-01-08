// Initialize and add the map
function initMap() {
    // The location of Uluru
    const uluru = { lat: -25.344, lng: 131.036 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 4,
    center: uluru,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
    position: uluru,
    map: map,
    });
}

// JQuery that's being run when the page loads
$( document ).ready(function() {
    $("img").imgCheckbox({
        onload: function(){
            // Do something fantastic!
            $(this).select();
        },
        onclick: function(el){
            var isChecked = el.hasClass("imgChked"),
            imgEl = el.children()[0];  // the img element
            
        console.log(imgEl.name + " is now " + (isChecked? "checked": "not-checked") + "!");
        }
    });

    // for clicking out of the modal
    $(document).click(function() {
        $('#moreInfoModal').modal('hide');
    });
    // for opening a modal
    $('div[name ="branch_listing"]').click(function(e) {
        $('#modalTitle').html($(this).attr('branch_name'));
        // creating html code to display needs on modal
        // must split since needsList is read as a string
        var needsList = $(this).attr('needs').split(',');
        var needsDisplay = '<p1>Needs:</p1><br>';
        var x; 
        for (x=0; x<needsList.length; x+=1){
            // some string stripping is required because the needs are read a long string
            needsDisplay += '<p1>' + needsList[x].replace('[','').replace(']','').replaceAll("'", "") + '</p1><br>';
        } 
        needsDisplay += '<br><br>'; 
        $('#modalNeeds').html($(needsDisplay));
        $('#moreInfoModal').modal('show');

        // add map marker!
        initMap();

        // makes sure $(document).click is not also triggered
        e.stopPropagation();
    });
});
