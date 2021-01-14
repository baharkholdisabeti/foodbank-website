// Initialize and add the map
function initMap(longitude, latitude) {
    // The location of branch
    const coords = { lat: parseFloat(latitude), lng: parseFloat(longitude) };
    // The map, centered at coords
    const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 14,
    center: coords,
    });
    // The marker, positioned at coords
    const marker = new google.maps.Marker({
    position: coords,
    map: map,
    });
}

// JQuery that's being run when the page loads
$( document ).ready(function() {
    $("img.img-fluid.checkbox").imgCheckbox({
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
    // to make sure modal doesn't close when modal is also clicked on
    $('#moreInfoModal').click(function (e) {
        e.stopPropagation();
    });
    // for opening a modal
    $('div[name ="branch_listing"]').click(function(e) {
        $('#modalTitle').html($(this).attr('branch_name'));
        // creating html code to display needs on modal
        // must split since needsList is read as a string
        var needsList = $(this).attr('needs').split(',');
        var needsDisplay = '<p><b>Needs:<b></p>';
        var x; 
        // remove empty case
        if (needsList[0] != "[]"){
            for (x=0; x<needsList.length; x+=1){
                // some string stripping is required because the needs are read a long string
                thisNeed = needsList[x].replace('[','').replace(']','').replaceAll("'", "");
                if (thisNeed.charAt(0) == " "){
                    thisNeed = thisNeed.substring(1);
                }
                //needsDisplay += '<p1>' + needsList[x].replace('[','').replace(']','').replaceAll("'", "") + '</p1><br>';
                //alert("<img src=\"{% static 'media/finalicons/" + thisNeed + ".png' %}\">");
                needsDisplay += "<img src='/foodbank/static/media/finalicons/" + thisNeed + ".png' %}\" alt='" + thisNeed + "' class='result-needs'>";
            } 
        }
        needsDisplay += '<br><br>'; 
        $('#modalNeeds').html($(needsDisplay));
        $('#moreInfoModal').modal('show');

        // add map marker!
        var longitude = $(this).attr('lng');
        var latitude = $(this).attr('lat');
        initMap(longitude, latitude);

        // makes sure $(document).click is not also triggered
        e.stopPropagation();
    });
});
