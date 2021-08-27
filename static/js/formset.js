let initialFormsLength = document.querySelectorAll(".column-form").length
let columnForm = document.querySelectorAll(".column-form")
let container = document.querySelector("#form-container")
let addButton = document.querySelector("#add-column")
let formNum = columnForm.length-1  // Get the number of the last form on the page with zero-based indexing


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

    let label_field_range_from = $(`label[for="id_form-${i}-range_from"]`);
    let label_field_range_to = $(`label[for="id_form-${i}-range_to"]`);
    let label_field_quantity = $(`label[for="id_form-${i}-quantity"]`);

    let label_field_id = $(`label[for*="-id"]`);

    conditional_field_quantity.hide();
    conditional_field_range_from.hide();
    conditional_field_range_to.hide();

    label_field_quantity.hide();
    label_field_range_from.hide();
    label_field_range_to.hide();

    label_field_id.hide();

    $(`#id_form-${i}-type`).change(function () {
        if ($(this).prop('value') === 'integer') {
            conditional_field_quantity.hide();
            conditional_field_range_from.show();
            conditional_field_range_to.show();

            label_field_quantity.hide();
            label_field_range_from.show();
            label_field_range_to.show();
        } else if ($(this).prop('value') === 'text') {
            conditional_field_quantity.show();
            conditional_field_range_from.hide();
            conditional_field_range_to.hide();

            label_field_quantity.show();
            label_field_range_from.hide();
            label_field_range_to.hide();
        } else {
            conditional_field_quantity.hide();
            conditional_field_range_from.hide();
            conditional_field_range_to.hide();

            label_field_quantity.hide();
            label_field_range_from.hide();
            label_field_range_to.hide();
        }

});
}


addButton.addEventListener('click', addForm)


function addForm(e){
    e.preventDefault()

    let newForm = columnForm[0].cloneNode(true)  //Clone the column form
    let formRegex = RegExp(`form-(\\d){1}-`,'g')  //Regex to find all instances of the form number

    formNum++ //Increment the form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`) //Update the new form to have the correct form number
    container.insertBefore(newForm, addButton) //Insert the new form at the end of the list of forms

    let conditional_field_range_from = $(`#id_${`form-${formNum}-`}range_from`);
    let conditional_field_range_to = $(`#id_${`form-${formNum}-`}range_to`);
    let conditional_field_quantity = $(`#id_${`form-${formNum}-`}quantity`);

    let label_field_range_from = $(`label[for="id_form-${formNum}-range_from"]`);
    let label_field_range_to = $(`label[for="id_form-${formNum}-range_to"]`);
    let label_field_quantity = $(`label[for="id_form-${formNum}-quantity"]`);


    $(`#id_${`form-${formNum}-`}type`).change(function () {
        if ($(this).prop('value') === 'integer') {
            conditional_field_quantity.hide();
            conditional_field_range_from.show();
            conditional_field_range_to.show();

            label_field_quantity.hide();
            label_field_range_from.show();
            label_field_range_to.show();
        } else if ($(this).prop('value') === 'text') {
            conditional_field_quantity.show();
            conditional_field_range_from.hide();
            conditional_field_range_to.hide();

            label_field_quantity.show();
            label_field_range_from.hide();
            label_field_range_to.hide();
        } else {
            conditional_field_quantity.hide();
            conditional_field_range_from.hide();
            conditional_field_range_to.hide();

            label_field_quantity.hide();
            label_field_range_from.hide();
            label_field_range_to.hide();
        }

    });

}
