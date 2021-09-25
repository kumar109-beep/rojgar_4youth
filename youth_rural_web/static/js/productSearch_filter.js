var sortByFilter = '';
// ===================================================================================================================================
//                                               product search & filter function
// ===================================================================================================================================
function search_filter_products(){
    $('#loadmoreProductSpinner').css('display','none');
	$('#noMoreProductDiv').css('display','none');

    var categoryFilter = [];
    $('input:checkbox.categoryClass').each(function () {
        var sThisVal = (this.checked ? $(this).val() : "");
        if(sThisVal != ''){
            categoryFilter.push(parseInt(sThisVal));
        }
   });
    // var sortByFilter = '';
    sortByFilter = sortByFilter.trim();
    var priceRangeFilter = [];
    priceRangeFilter.push(parseInt(0));
    priceRangeFilter.push(parseInt($("#priceRange").val()));
    var searchString = $("#productSearch").val().trim();
    // =================================================================================
    //                             Dynamic filter key
    // =================================================================================
    var filterKey = '';
    // CASE : 01
    if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'FilterAll';
    }
    // CASE : 02
    else if(sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'SortPriceByRangeWithSearchBox';
    }
    // CASE : 03
    else if(categoryFilter.length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'categortyPriceRangeWithSearchBox';
    }
    // CASE : 04
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && searchString.trim().length !=0){
        filterKey = 'categorySortPriceWithSearchBox';
    }
    // CASE : 05
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 ){
        filterKey = 'sideFilterAll';
    }
    // CASE : 06
    else if(sortByFilter.trim().length !=0 && priceRangeFilter.length !=0){
        filterKey = 'sortBypriceWithrange';
    }
    // CASE : 07
    else if(categoryFilter.length !=0 && priceRangeFilter.length !=0){
        filterKey = 'categoryWithPriceRange';
    }
    // CASE : 08
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 ){
        filterKey = 'categoryWithSortByPrice';
    }
    // CASE : 09
    else if(priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'sortByPriceRangeWithSearchBox';
    }
    // CASE : 10
    else if(sortByFilter.trim().length !=0 && searchString.trim().length !=0){
        filterKey = 'sortByPriceWithSearchBox';
    }
    // CASE : 11
    else if(categoryFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'categoryWithsearchBox';
    }
    // CASE : 12
    else if(searchString.trim().length !=0){
        filterKey = 'serachBox';
    }
    // CASE : 13
    else if(categoryFilter.length !=0){
        filterKey = 'category_filter';
    }
    // CASE : 14
    else if(sortByFilter.trim().length !=0){
        filterKey = 'sortByPrice';
    }
    // CASE : 15
    else if(priceRangeFilter.length !=0){
        filterKey = 'priceRange';
    }

    console.log('categoryFilter[]', categoryFilter)
    console.log('sortBy_Filter', sortByFilter)
    console.log('priceRangeFilter[]', priceRangeFilter)
    console.log('search_String', searchString)
    console.log('filterKey',filterKey)
    // =================================================================================
    //                                  AJAX call
    // =================================================================================
    $.ajax({
        type: 'GET',
        url: "/product_search_filter",
        data: {'categoryFilter[]': categoryFilter,'sortBy_Filter': sortByFilter,'priceRangeFilter[]': priceRangeFilter,'search_String': searchString,'filterKey':filterKey},
        success: function (response) {
            console.log(response['filteredData']);

            if(response['filteredData']['data'].length == 0){
                var blank_data = '<div class="text-center">\
                                    <img src="https://eshoppingnepal.com/photos/nproduct.png" style="margin-left:;">\
                                </div>';
                $('#productDisplaySection').html('');
                $('#filterSection').css('display','');
                $('#productDisplaySection').append(blank_data);
            }else{
                $('#filterSection').css('display','');
                $('#productDisplaySection').html('');
                $('#productDisplaySection').append('<div class="text-center mt-5"><div class="spinner-border text-info" style="width: 5rem; height: 5rem;" role="status">\
                                                        <span class="sr-only">Loading...</span>\
                                                    </div></div>');
                 var dataStr = '';
                for(var i=0;i<response['filteredData']['data'].length;i++){
                    var data = '<div class="col-md-4 mb-4 mb-md-5 pt-2" style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">\
                                <a href="/product-detail/product-query/'+response['filteredData']['data'][i]['id']+'"><div class="p-cont">\
                                    <img src="http://13.233.247.133:1000/static/'+response['filteredData']['data'][i]['productCoverImages']+'"  style="border-radius: 10px;">\
                                </div>\
                                <small><p class="  text-center mt-3" style="font-weight:700;">'+response['filteredData']['data'][i]['productName']+'</p></small></a>\
                                <div class="text-left mb-1">\
                                    <button class="btn btn-sm btn-warning" style="pointer-events: none;"><i class="fas fa-rupee-sign"></i>'+response['filteredData']['data'][i]['productPrice']+'.00</button>\
                                </div>\
                            </div>';
                    dataStr = dataStr + data;
                }
                $('#productDisplaySection').html('');
                $('#productDisplaySection').append(dataStr);
            }
        }
    });
    // =================================================================================
}


{/* <div class="col-md-4 mb-4 mb-md-5 pt-2" style='box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;'>
    <a href="{% url 'product_detail' i.id %}"><div class="p-cont">
        <img src="http://13.233.247.133:1000/static/{{i.productCoverImages}}">
    </div>
    <small><p class="  text-center mt-3" style='font-weight:700;'>{{i.productName}}</p></small></a>
    <div class="text-left mb-1">
        <button class="btn btn-sm btn-warning" style="pointer-events: none;"><i class="fas fa-rupee-sign"></i> {{i.productPrice}}.00</button>
    </div>
</div> */}


function sortByPrice_products(thisTxt){
    $('#loadmoreProductSpinner').css('display','none');
	$('#noMoreProductDiv').css('display','none');

    var categoryFilter = [];
    $('input:checkbox.categoryClass').each(function () {
        var sThisVal = (this.checked ? $(this).val() : "");
        if(sThisVal != ''){
            categoryFilter.push(parseInt(sThisVal));
        }
   });
    sortByFilter = $(thisTxt).attr('id').trim();
    var priceRangeFilter = [];
    priceRangeFilter.push(parseInt(0));
    priceRangeFilter.push(parseInt($("#priceRange").val()));
    var searchString = $("#productSearch").val().trim();
    // =================================================================================
    //                             Dynamic filter key
    // =================================================================================
    var filterKey = '';
    // CASE : 01
    if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'FilterAll';
    }
    // CASE : 02
    else if(sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'SortPriceByRangeWithSearchBox';
    }
    // CASE : 03
    else if(categoryFilter.length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'categortyPriceRangeWithSearchBox';
    }
    // CASE : 04
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && searchString.trim().length !=0){
        filterKey = 'categorySortPriceWithSearchBox';
    }
    // CASE : 05
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 ){
        filterKey = 'sideFilterAll';
    }
    // CASE : 06
    else if(sortByFilter.trim().length !=0 && priceRangeFilter.length !=0){
        filterKey = 'sortBypriceWithrange';
    }
    // CASE : 07
    else if(categoryFilter.length !=0 && priceRangeFilter.length !=0){
        filterKey = 'categoryWithPriceRange';
    }
    // CASE : 08
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 ){
        filterKey = 'categoryWithSortByPrice';
    }
    // CASE : 09
    else if(priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'sortByPriceRangeWithSearchBox';
    }
    // CASE : 10
    else if(sortByFilter.trim().length !=0 && searchString.trim().length !=0){
        filterKey = 'sortByPriceWithSearchBox';
    }
    // CASE : 11
    else if(categoryFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'categoryWithsearchBox';
    }
    // CASE : 12
    else if(searchString.trim().length !=0){
        filterKey = 'serachBox';
    }
    // CASE : 13
    else if(categoryFilter.length !=0){
        filterKey = 'category_filter';
    }
    // CASE : 14
    else if(sortByFilter.trim().length !=0){
        filterKey = 'sortByPrice';
    }
    // CASE : 15
    else if(priceRangeFilter.length !=0){
        filterKey = 'priceRange';
    }
    // =================================================================================
    //                                  AJAX call
    // =================================================================================
    $.ajax({
        type: 'GET',
        url: "/product_search_filter",
        data: {'categoryFilter[]': categoryFilter,'sortBy_Filter': sortByFilter,'priceRangeFilter[]': priceRangeFilter,'search_String': searchString,'filterKey':filterKey},
        success: function (response) {
            console.log(response['filteredData']);

            if(response['filteredData']['data'].length == 0){
                var blank_data = '<div class="text-center">\
                                    <img src="https://eshoppingnepal.com/photos/nproduct.png" style="margin-left:;">\
                                </div>';
                $('#productDisplaySection').html('');
                $('#filterSection').css('display','');
                $('#productDisplaySection').append(blank_data);
            }else{
                $('#filterSection').css('display','');
                $('#productDisplaySection').html('');
                $('#productDisplaySection').append('<div class="text-center mt-5"><div class="spinner-border text-info" style="width: 5rem; height: 5rem;" role="status">\
                                                        <span class="sr-only">Loading...</span>\
                                                    </div></div>');
                 var dataStr = '';
                for(var i=0;i<response['filteredData']['data'].length;i++){
                    var data = '<div class="col-md-4 mb-4 mb-md-5 pt-2" style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">\
                                <a href="/product-detail/product-query/'+response['filteredData']['data'][i]['id']+'"><div class="p-cont">\
                                    <img src="http://13.233.247.133:1000/static/'+response['filteredData']['data'][i]['productCoverImages']+'" style="border-radius: 10px;">\
                                </div>\
                                <small><p class="  text-center mt-3" style="font-weight:700;">'+response['filteredData']['data'][i]['productName']+'</p></small></a>\
                                <div class="text-left mb-1">\
                                    <button class="btn btn-sm btn-warning" style="pointer-events: none;"><i class="fas fa-rupee-sign"></i>'+response['filteredData']['data'][i]['productPrice']+'.00</button>\
                                </div>\
                            </div>';
                    dataStr = dataStr + data;
                }
                $('#productDisplaySection').html('');
                $('#productDisplaySection').append(dataStr);
            }
        }
    });
    // =================================================================================
}


function getPriceRange(thisTxt){
    $('#loadmoreProductSpinner').css('display','none');
	$('#noMoreProductDiv').css('display','none');
    
    console.log($(thisTxt).val());
    $('#maxPrice').text('');
    $('#maxPrice').text($(thisTxt).val());

    var categoryFilter = [];
    $('input:checkbox.categoryClass').each(function () {
        var sThisVal = (this.checked ? $(this).val() : "");
        if(sThisVal != ''){
            categoryFilter.push(parseInt(sThisVal));
        }
   });
    // var sortByFilter = '';
    sortByFilter = sortByFilter.trim();
    var priceRangeFilter = [];
    priceRangeFilter.push(parseInt(0));
    priceRangeFilter.push(parseInt($("#priceRange").val()));
    var searchString = $("#productSearch").val().trim();
    // =================================================================================
    //                             Dynamic filter key
    // =================================================================================
    var filterKey = '';
    // CASE : 01
    if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'FilterAll';
    }
    // CASE : 02
    else if(sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'SortPriceByRangeWithSearchBox';
    }
    // CASE : 03
    else if(categoryFilter.length !=0 && priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'categortyPriceRangeWithSearchBox';
    }
    // CASE : 04
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && searchString.trim().length !=0){
        filterKey = 'categorySortPriceWithSearchBox';
    }
    // CASE : 05
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 && priceRangeFilter.length !=0 ){
        filterKey = 'sideFilterAll';
    }
    // CASE : 06
    else if(sortByFilter.trim().length !=0 && priceRangeFilter.length !=0){
        filterKey = 'sortBypriceWithrange';
    }
    // CASE : 07
    else if(categoryFilter.length !=0 && priceRangeFilter.length !=0){
        filterKey = 'categoryWithPriceRange';
    }
    // CASE : 08
    else if(categoryFilter.length !=0 && sortByFilter.trim().length !=0 ){
        filterKey = 'categoryWithSortByPrice';
    }
    // CASE : 09
    else if(priceRangeFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'sortByPriceRangeWithSearchBox';
    }
    // CASE : 10
    else if(sortByFilter.trim().length !=0 && searchString.trim().length !=0){
        filterKey = 'sortByPriceWithSearchBox';
    }
    // CASE : 11
    else if(categoryFilter.length !=0 && searchString.trim().length !=0){
        filterKey = 'categoryWithsearchBox';
    }
    // CASE : 12
    else if(searchString.trim().length !=0){
        filterKey = 'serachBox';
    }
    // CASE : 13
    else if(categoryFilter.length !=0){
        filterKey = 'category_filter';
    }
    // CASE : 14
    else if(sortByFilter.trim().length !=0){
        filterKey = 'sortByPrice';
    }
    // CASE : 15
    else if(priceRangeFilter.length !=0){
        filterKey = 'priceRange';
    }
    // =================================================================================
    //                                  AJAX call
    // =================================================================================
    $.ajax({
        type: 'GET',
        url: "/product_search_filter",
        data: {'categoryFilter[]': categoryFilter,'sortBy_Filter': sortByFilter,'priceRangeFilter[]': priceRangeFilter,'search_String': searchString,'filterKey':filterKey},
        success: function (response) {
            console.log(response['filteredData']);

            if(response['filteredData']['data'].length == 0){
                var blank_data = '<div class="text-center">\
                                    <img src="https://eshoppingnepal.com/photos/nproduct.png" style="margin-left:;">\
                                </div>';
                $('#productDisplaySection').html('');
                $('#filterSection').css('display','');
                $('#productDisplaySection').append(blank_data);
            }else{
                $('#filterSection').css('display','');
                $('#productDisplaySection').html('');
                $('#productDisplaySection').append('<div class="text-center mt-5"><div class="spinner-border text-info" style="width: 5rem; height: 5rem;" role="status">\
                                                        <span class="sr-only">Loading...</span>\
                                                    </div></div>');
                 var dataStr = '';
                for(var i=0;i<response['filteredData']['data'].length;i++){
                    var data = '<div class="col-md-4 mb-4 mb-md-5 pt-2" style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">\
                                <a href="/product-detail/product-query/'+response['filteredData']['data'][i]['id']+'"><div class="p-cont">\
                                    <img src="http://13.233.247.133:1000/static/'+response['filteredData']['data'][i]['productCoverImages']+'" style="border-radius: 10px;">\
                                </div>\
                                <small><p class="  text-center mt-3" style="font-weight:700;">'+response['filteredData']['data'][i]['productName']+'</p></small></a>\
                                <div class="text-left mb-1">\
                                    <button class="btn btn-sm btn-warning" style="pointer-events: none;"><i class="fas fa-rupee-sign"></i>'+response['filteredData']['data'][i]['productPrice']+'.00</button>\
                                </div>\
                            </div>';
                    dataStr = dataStr + data;
                }
                $('#productDisplaySection').html('');
                $('#productDisplaySection').append(dataStr);
            }
        }
    });
    // =================================================================================
}
