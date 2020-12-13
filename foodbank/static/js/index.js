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
});
