$(document).ready(function(){
    var table = $('#example').DataTable({
      
      dom: 'rtip',
    });
    $('#example tbody').on('click', 'tr', function () {
      var data = table.row(this).data();
      var id = data[0];
      var phone = "+260 - "  + data[3]
      var name = data[1] + " " + data[2];
      $('#email').text(data[6])
      $('#name').text(name)
      $('#phone').text(phone)
      $('#rowModal').modal('show');

      $('#openSecondModal').on('click', function() {
        $('#rowModal').modal('hide');
        message(id)
        });
      $('#openEditModal').on('click', function(){
        $('#rowModal').modal('hide');
        EditCustomer(id)
      })
    });


  function message(ID){
    $('#messageModal').modal('show')
    console.log(ID);
  }

  function EditCustomer(ID){
    $('#editModal').modal('show')
  }


    $('#custom-search').on('keyup', function() {
      table.search(this.value).draw();
  });

    
////////////// DRAW TABLE WITH BACKEND DATABASE ///////////////////

// function to populate the table with database content
function populateDataTable(data) {
  table.clear();
  // Add rows from API data
  data.forEach(item => {
      table.row.add([
          item.id,
          item.first_name,
          item.last_name,
          item.phone,
          item.zip_code,
          item.city,
          item.email,

      ]).draw(false); // Draw added row without redrawing entire table
  });
}

/* Making API calls to get movies from the backend */
$.ajax({
  url: '{% url "get_customers" %}', // API endpoint
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    console.log("data", data)
    populateDataTable(data); // Call function to populate DataTable
  },
  error: function(xhr, status, error) {
      console.error('Error fetching data:', error);
  }
});

////////////////// TABLE END //////////////////////////



});