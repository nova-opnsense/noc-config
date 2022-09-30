{#
 #   Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
 #   Author: hai.nt <hai.nt@novaintechs.com>
 #   
 #   All rights reserved.
 #   
 #   --------------------------------------------------------------------------------------
 #   
 #   
 #}


<script>
    $( document ).ready(function() {
        var data_get_map = {'frm_ezmesh':"/api/noc/ezmesh/get"};
        console.log("data_get_map: ");
        console.log(data_get_map);

        mapDataToFormUI(data_get_map).done(function(data){
            console.log("data: ");
            console.log(data);
            // place actions to run after load, for example update form styles.
        });

        // link save button to API set action
        $("#saveAct").click(function(){
            saveFormToEndpoint(url="/api/noc/ezmesh/set",formid='frm_ezmesh',callback_ok=function(){
                // action to run after successful save, for example reconfigure service.
                ajaxCall(url="/api/noc/service/reload", sendData={},callback=function(data,status) {
                    // action to run after reload
                });
            });
        });

        $("#applyAct").click(function(){
            ajaxCall(url="/api/noc/service/apply", sendData={},callback=function(data,status) {
                // action to run after reload
                $("#responseMsg").removeClass("hidden");
                $("#responseMsg").html(data['message']);
                setTimeout(() => {
                    $("#responseMsg").addClass("hidden");
                }, 5000);
            });
        });

    });
</script>

<div class="alert alert-info hidden" role="alert" id="responseMsg">

</div>

<div  class="col-md-12">
    {{ partial("layout_partials/base_form",['fields':ezmeshForm,'id':'frm_ezmesh'])}}
</div>

<div class="col-md-12">
    <button class="btn btn-primary"  id="saveAct" type="button"><i class="fa fa-floppy-o" aria-hidden="true"></i> <b>{{ lang._('Save') }}</b></button>
    <button class="btn btn-primary"  id="applyAct" type="button"><b>{{ lang._('Apply') }}</b></button>
</div>
