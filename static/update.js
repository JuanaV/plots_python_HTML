$(function() {


    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', 
        function(data,radar) {
          $('#result').text(data.result);
          radar.options.scales.yAxes[0].ticks.min = -60;
          radar.options.scales.yAxes[0].ticks.max = 50;
          radar.update();

        });
      return false;
    };
    

    setInterval(submit_form, 600);
  });