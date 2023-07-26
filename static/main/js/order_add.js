/***************************************** select option search *********************************************************/

$(document).ready(function() {
    // Target the select element and apply Select2
    $("#customer_name").select2();
});

$(document).ready(function() {
    // Target the select element and apply Select2
    $("#collector_name").select2();
});

$(document).ready(function() {
    // Target the select element and apply Select2
    $("#delivery_boy_name").select2();
});

$(document).ready(function() {
    // Target the select element and apply Select2
    $("#wholesaler_name").select2();
});


/***************************************** Calculation Automatixc Amount field add *********************************************************/

// // Function to calculate the total based on MRP and Quantity
// function calculateTotal() {
//     const mrp = parseFloat(document.getElementById('mrp').value);
//     const quantity = parseInt(document.getElementById('quantity').value);
//     const total = mrp * quantity;
//     document.getElementById('total').value = total.toFixed(2);

//     // Update the Amount field with the same value as the Total field
//     document.getElementById('collector_amount').value = total.toFixed(2);
//     document.getElementById('delivery_boy_amount').value = quantity;
// }

// // Call the calculateTotal function when MRP or Quantity changes
// document.getElementById('mrp').oninput = calculateTotal;
// document.getElementById('quantity').oninput = calculateTotal;



// //       ///     ////  ///        //   ///   ///    ///   ///   ///  ///  ///  //  //// /  ////// 

// // Function to calculate the total based on MRP and Quantity
// function calculateTotal2() {
//     const purchase_mrp = parseFloat(document.getElementById('purchase_mrp').value);
//     const purchase_quantity = parseInt(document.getElementById('purchase_quantity').value);
//     const purchase_total = purchase_mrp * purchase_quantity;

//     document.getElementById('purchase_total').value = purchase_total.toFixed(2);

//     // Update the Amount field with the same value as the Purchase Quantity field
//     document.getElementById('quantity').value = purchase_quantity;
// }

// // Call the calculateTotal2 function when MRP or purchase_Quantity changes
// document.getElementById('purchase_mrp').oninput = calculateTotal2;
// document.getElementById('purchase_quantity').oninput = calculateTotal2;


// Function to calculate the total based on MRP and Quantity
function calculateTotal() {
    const purchase_mrp = parseFloat(document.getElementById('purchase_mrp').value);
    const purchase_quantity = parseInt(document.getElementById('purchase_quantity').value);
    const purchase_total = purchase_mrp * purchase_quantity;

    // Set the calculated values to their respective fields
    document.getElementById('purchase_total').value = purchase_total.toFixed(2);
    document.getElementById('quantity').value = purchase_quantity;

    // Calculate the total based on MRP and the newly updated quantity
    const mrp = parseFloat(document.getElementById('mrp').value);
    const total = mrp * purchase_quantity;
    document.getElementById('total').value = total.toFixed(2);

    // Update the Amount field with the same value as the Total field
    document.getElementById('collector_amount').value = total.toFixed(2);
    document.getElementById('delivery_boy_amount').value = purchase_quantity;
}

// Call the calculateTotal function when MRP or purchase_Quantity changes
document.getElementById('purchase_mrp').oninput = calculateTotal;
document.getElementById('purchase_quantity').oninput = calculateTotal;
document.getElementById('mrp').oninput = calculateTotal; // To handle the case when MRP changes independently of purchase_quantity


/***************************************** automatic field add same as customer *********************************************************/


// Function to update customer details based on selected customer and checkbox status
function updateCustomerDetails() {
    const customerId = document.getElementById('customer_name').value;
    const showDetails = document.getElementById('show_details').checked;
    if (!showDetails || !customerId) {
        document.getElementById('name').value = '';
        document.getElementById('mobile').value = '';
        document.getElementById('address').value = '';
        return;
    }

    // Make an AJAX GET request to fetch the customer details
    $.ajax({
        type: 'GET',
        url: '/get_customer_details/',  // Replace with the URL for your get_customer_details view
        data: {
            customer_id: customerId,
            show_details: showDetails
        },
        dataType: 'json',
        success: function (data) {
            document.getElementById('name').value = data.name;
            document.getElementById('mobile').value = data.mobile;
            document.getElementById('address').value = data.address;
        },
        error: function (xhr, textStatus, errorThrown) {
            console.log('Error:', errorThrown);
        }
    });
}

// Call the updateCustomerDetails function when the customer selection changes
document.getElementById('customer_name').addEventListener('change', updateCustomerDetails);

// Call the updateCustomerDetails function when the checkbox status changes
document.getElementById('show_details').addEventListener('change', updateCustomerDetails);








/***************************************** form hide and show *********************************************************/


function toggleFormSectionTwo() {
    var HomeRadio = document.getElementById("Home");
    var BankRadio = document.getElementById("Bank");
    
    var HomeSection = document.getElementById("IdHome");
    var BankSection = document.getElementById("IdBank");
    

    if (HomeRadio.checked) {
        HomeSection.style.display = "contents";
        BankSection.style.display = "none";
        
    } else if (BankRadio.checked) {
        HomeSection.style.display = "none";
        BankSection.style.display = "contents";
        
    } else {
        HomeSection.style.display = "none";
        BankSection.style.display = "none";
        
    }
}