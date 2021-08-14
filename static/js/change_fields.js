let conditional_field_range_from = $("#id_form-0-range_from");
let conditional_field_range_to = $("#id_form-0-range_to");
let conditional_field_quantity = $("#id_form-0-quantity");

$("#id_form-0-type").change(function () {
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