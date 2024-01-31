$(function(){
    $('#filter-btn').on('click', function(){
        var filterBtn = $('#filter-btn span');
        var filterOrder = $('#filter-order')
        if (filterBtn.hasClass('glyphicon glyphicon-sort-by-attributes-alt'))
        {
            filterBtn.removeClass('glyphicon glyphicon-sort-by-attributes-alt').addClass('glyphicon glyphicon-sort-by-attributes');
            filterOrder.attr('value', 'ASC');
        }
        else if(filterBtn.hasClass('glyphicon glyphicon-sort-by-attributes'))
        {
            filterBtn.removeClass('glyphicon glyphicon-sort-by-attributes').addClass('glyphicon glyphicon-sort-by-attributes-alt');
            filterOrder.attr('value', 'DESC');
        }
        $.ajax({
            url: '/',
            type: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: $('#filter-form').serialize(),
            success: function(response){
                console.log('Form submitted successfully');
                console.log($('#filter-form').serialize())
            },
            error: function(error){
                console.log('Error submitting form', error);
            }
        });
    });
});