$(document).ready(function(){
var i = 1;

$("#add-column").click(function (e){
event.preventDefault();
let form_string = 'form-'+i+'-';
$('#items').append(
`<tr><th><label for="id_${form_string}column_name">Column name:</label></th><td><input type="text" name="${form_string}column_name" maxlength="50" id="id_${form_string}column_name"></td></tr>`+
`<tr><th><label for="id_${form_string}type">Type:</label></th><td><select name="${form_string}type" id="id_${form_string}type"><option value="" selected>---------</option><option value="full_name">Full name</option><option value="job">Job</option><option value="email">E-mail</option><option value="domain_name">Domain name</option><option value="phone_number">Phone number</option><option value="company_name">Company name</option><option value="text">Text</option><option value="integer">Integer</option><option value="address">Address</option><option value="date">Date</option></select></td></tr>`+
`<tr><th><label for="id_${form_string}range_from">Range from:</label></th><td><input type="number" name="${form_string}range_from" min="0" id="id_${form_string}range_from"></td></tr>`+
`<tr><th><label for="id_${form_string}range_to">Range to:</label></th><td><input type="number" name="${form_string}range_to" min="0" id="id_${form_string}range_to"></td></tr>`+
`<tr><th><label for="id_${form_string}quantity">Quantity:</label></th><td><input type="number" name="${form_string}quantity" min="0" id="id_${form_string}quantity"></td></tr>`+
`<tr><th><label for="id_${form_string}order">Order:</label></th><td><input type="number" name="${form_string}order" min="0" id="id_${form_string}order"></td></tr>`
);
i++;

let conditional_field_range_from = $(`#id_${form_string}range_from`);
let conditional_field_range_to = $(`#id_${form_string}range_to`);
let conditional_field_quantity = $(`#id_${form_string}quantity`);

$(`#id_${form_string}type`).change(function () {
    if ($(this).prop('value') === 'integer') {
        conditional_field_quantity.parent().parent().hide();
        conditional_field_range_from.parent().parent().show();
        conditional_field_range_to.parent().parent().show();
    } else if ($(this).prop('value') === 'text') {
        conditional_field_quantity.parent().parent().show();
        conditional_field_range_from.parent().parent().hide();
        conditional_field_range_to.parent().parent().hide();
    } else {
        conditional_field_quantity.parent().parent().hide();
        conditional_field_range_from.parent().parent().hide();
        conditional_field_range_to.parent().parent().hide();
    }

});

});

$('body').on('click','#delete',function (e){
    $(this).parent('div').remove();
});

});

//'<input type="button" value="delete" id="delete" />'