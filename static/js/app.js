$(function() {
  $('input[type=file]').change(function(){
    var t = $(this).val();
    var labelText = 'File : ' + t.substr(12, t.length);
    $(this).prev('label').text(labelText);
  })
});


// drop down selection
$(document).ready(function(){
 $('.dropdown').dropdown({multi_select:true});
});

$.fn.dropdown = function(options) {
	console.log('I am in');
	var $input = this.find('input'),
		$options_list = this.find('.options_list'),
		$seleted_list = $options_list.siblings('.selected_list'),
		settings = $.extend({}, {multi_select: false}, options);
    $input.on('click', function(){
		$options_list
			.slideDown("fast");
	});

    $options_list.on('click','.option', function() {
		var $selected_option = $(this),
			data_value = $(this).attr('data-value'),
			data_text = $(this).text().trim();
		$input
			.attr('data-value',data_value)
			.val(data_text);
		if(settings.multi_select) {
			var $item = $('<div class="item" data-value=""><span class="text"></span><span class="remove_item">x</span></div>');
			$item
				.attr('data-value',data_value)
				.find('.text')
				.text(data_text);
			$seleted_list.append($item);
			$selected_option.remove();
			$options_list
				.siblings('input')
				.attr("data-value","")
				.val("");
		}
		$options_list.slideUp("fast");
    });

    $seleted_list.off('click').on('click','.item .remove_item',function() {
    	var $clicked_item = $(this).parents('.item'),
    		item_text = $clicked_item
    						.find('.text')
    						.text()
    						.trim(),
    		item_data_value = $clicked_item.attr('data-value'),
    		$item = $('<div class="option" data-value="'+item_data_value+'">'+item_text+'</div>');
    	$clicked_item.addClass('removed_item');
    	setTimeout(function() {
    		$options_list.append($item);
	        $clicked_item.remove();
	    }, 500);
    });
    return this;
}

$.fn.selectedList = function() {
	var list = [];
	this.find('.selected_list .item').each(function(ind, option) {
		list.push({
			key: $(option).attr('data-value'),
			value: $(option).find('.text').text().trim()
		})
	});
	return list;
};


// Radio button and drop down updates
$(function(){
    
    var select = $('#category'),
        options = select.find('option');
    
  $('[name=algorithm]').click(function(){
        if ($(this).val() == "supervised") {
          
        
          select.find('option[value="Algorithm1"]').hide();
          select.find('option[value="Algorithm2"]').hide();
          select.val("");
        
        } else {
          select.find('option[value="Algorithm4"]').show();
          select.find('option[value="Algorithm5"]').show();
        }
        // console.log(hideItems);
        // var visibleItems = options.filter('[value*="' + $(this).val()  + '"]').show();
        // options.not(visibleItems).hide();
    });
});