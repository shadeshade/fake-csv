let initialFormsLength = document.querySelectorAll(".column-form").length
let columnForm = document.querySelectorAll(".column-form")
let container = document.querySelector("#form-container")
let addButton = document.querySelector("#add-column")
let formNum = columnForm.length-1


for(var i = 0; i < initialFormsLength; i++) {

    let initialForm = columnForm[i]
    initialForm.innerHTML = initialForm.innerHTML + '<input type="button" value="delete" id="delete" />'
    container.insertBefore(initialForm, addButton)

    $('body').on('click','#delete',function (e){
        $(this).parent().remove();
    });

}


for(var i = 0; i < initialFormsLength; i++) {

    let conditional_field_range_from = $(`#id_form-${i}-range_from`);
    let conditional_field_range_to = $(`#id_form-${i}-range_to`);
    let conditional_field_quantity = $(`#id_form-${i}-quantity`);

    $(`#id_form-${i}-type`).change(function () {
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
}


addButton.addEventListener('click', addForm)


function addForm(e){
    e.preventDefault()

    let newForm = columnForm[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
    container.insertBefore(newForm, addButton)

    let conditional_field_range_from = $(`#id_${`form-${formNum}-`}range_from`);
    let conditional_field_range_to = $(`#id_${`form-${formNum}-`}range_to`);
    let conditional_field_quantity = $(`#id_${`form-${formNum}-`}quantity`);

    $(`#id_${`form-${formNum}-`}type`).change(function () {
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

}
