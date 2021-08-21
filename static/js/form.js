$(document).ready(function(){
    var option = $(".select option:selected");
    option.attr('disabled', 'disabled');
    option.attr('value', ' ');
    option.text('----select----');

    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    var current = 1;
    var steps = $("fieldset").length;
    
    setProgressBar(current);
   
    $(".next").click(function(){
        // $(".myform").validate() 
    current_fs = $(this).parent();
    next_fs = $(this).parent().next();
    
    //Add Class Active
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;
    
    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    next_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(++current);
    });
    
    $(".previous").click(function(){
    
    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();
    
    //Remove class active
    $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
    
    //show the previous fieldset
    previous_fs.show();
    
    //hide the current fieldset with style
    current_fs.animate({opacity: 0}, {
    step: function(now) {
    // for making fielset appear animation
    opacity = 1 - now;
    
    current_fs.css({
    'display': 'none',
    'position': 'relative'
    });
    previous_fs.css({'opacity': opacity});
    },
    duration: 500
    });
    setProgressBar(--current);
    });
    
    function setProgressBar(curStep){
    var percent = parseFloat(100 / steps) * curStep;
    percent = percent.toFixed();
    $(".progress-bar")
    .css("width",percent+"%")
    }
    
    // $(".submit").click(function(){
    // return false;
    // })
    $('#lpu').hide()
    $('#meter-menu').on('change', function(){
        if(this.value == 'lpu'){
            $('#spu').hide()
            $('#lpu').show() 
        }
        else{
            $('#spu').show()
            $('#lpu').hide()
        }
    });

    // console.log( "ready!" );
    if(typeof(Storage) !== 'undefined'){
    populateInputs();
     }
     function populateInputs(){
        // console.log('Populating');
        for(var i=0; i<sessionStorage.length; i++) {
          var temp = sessionStorage.key(i);
          if(temp.startsWith('inputData')) {
            //   console.log('Setting ' + temp.split('-')[1] +
            // ' to ' + sessionStorage.getItem(temp));
              $('#'+temp.split('-')[1]).val(sessionStorage.getItem(temp));
          }
        }
    }
    $('.saveInput').on('input', function(){
        // console.log(this.id + ' has ' + this.value);
        sessionStorage.setItem('inputData-'+this.id, this.value);
    });

    $('#id_meter_phases').on('change', function(){
        var mcur_redphase = $('#id_measured_value_current_red_phase').val();
        var mcur_yellowphase = $('#id_measured_value_current_yellow_phase').val();
        var mcur_bluephase = $('#id_measured_value_current_blue_phase').val();

        var mvol_redphase = $('#id_measured_value_voltage_red_phase').val();
        var mvol_yellowphase = $('#id_measured_value_voltage_yellow_phase').val();
        var mvol_bluephase = $('#id_measured_value_voltage_blue_phase').val();

        if(this.value == 'SINGLE PHASE'){
            var load = mcur_redphase * mvol_redphase * 0.9 * 0.25 * 0.6 / 1000;
            $('#id_load_estimation').val(load.toFixed(2));            
        }

        else if(this.value == 'THREE PHASE'){
            var average_current = mcur_redphase + mcur_yellowphase + mcur_bluephase / 3;
            var average_voltage = mvol_redphase + mvol_yellowphase + mvol_bluephase / 3;
            var load = parseFloat(average_current) *parseFloat(average_voltage) * 1.732 * 0.9 * 0.25 * 0.6 / 1000;

            $('#id_load_estimation').val(parseFloat(load.toFixed(2))); 
        }

    });

    $('#mysubmit').click(function(){
        sessionStorage.clear()
    });
    
    });

  