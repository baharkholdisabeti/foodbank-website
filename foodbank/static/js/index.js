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

// find all modules with that need visible or hidden depending on visible boolean
function makeVisible (checkedImages, visible, all){    
    if (all){
        $('div[name ="branch_listing"]').css("visibility", "visible");
        return;
    }
    // default make all hidden
    $('div[name ="branch_listing"]').css("visibility", "hidden");
    if (visible){
        for (var i = 0; i<checkedImages.length; i+=1){
            var filterby = $(checkedImages[i]).attr('filterby');
            $('div[name ="branch_listing"]')
                .filter(function( index ) {
                    // turn string needs into array
                    var needsList = $(this).attr('needs')
                    return (needsList.includes(filterby));
                }).css("visibility", "visible");
        }
    }
}

// updates visibility of branch modules based on need filter
function updateVisibility(filterby, isChecked){ 
    var checkedImgs = []
    var uncheckedImgs = []
    checkedImgs = $("img.img-fluid.checkbox").filter(function( index, el ) {
        var thisFilterby = $(this).attr('filterby');
        return (($(this).hasClass("checked")) || (thisFilterby==filterby && isChecked)) ;
    });
    // if no filters selected, make all elements visible
    if (!checkedImgs.length){
        makeVisible(uncheckedImgs, true, true);
        return;
    }
    // check which filters are selected and turn them visible
    // turn others hidden
    makeVisible(checkedImgs, true, false);
}

// JQuery that's being run when the page loads
$( document ).ready(function() {
    $("img.img-fluid.checkbox").imgCheckbox({
        onload: function(){
            $(this).select();
        },
        onclick: function(el){
            var isChecked = el.hasClass("imgChked");
            imgEl = el.children()[0];  // the img element
            var filterby = $(imgEl).attr('filterby');
            // add checked class to element if it is clicked on
            if (isChecked){
                $(imgEl).addClass("checked");
            }
            else{
                $(imgEl).removeClass("checked");
            }
            updateVisibility(filterby, isChecked)
            /*if (isChecked){
                $('div[name ="branch_listing"]').filter(function() {
                    $(this).toggle($(this).attr('needs').includes(filterby))
                });
            }
            else{
                $('div[name ="branch_listing"]').filter(function() {
                    $(this).toggle(!$(this).attr('needs').includes(filterby))
                });
            } */
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
