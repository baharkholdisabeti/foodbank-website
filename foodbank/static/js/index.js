// set latitude and longitude of branches
function getLatLong(){
    var hash={};
    hash={ "The Burlington Food Bank":"43.331800,-79.821060","Guelph Food Bank":"43.536840,-80.262370" }
    return hash;
}

// Initialize and add the map
function initMap(branchName) {
    var hash = getLatLong();
    var longlat = hash[branchName].split(",");
    longlat[0] = parseFloat(longlat[0]);
    longlat[1] = parseFloat(longlat[1]);
    // The location of branch
    const coords = { lat: longlat[0], lng: longlat[1] };
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
        initMap($(this).attr('branch_name'));

        // makes sure $(document).click is not also triggered
        e.stopPropagation();
    });
});
