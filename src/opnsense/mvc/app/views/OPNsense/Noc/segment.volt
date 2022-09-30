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
        $("#grid-segment").UIBootgrid(
            {   search:'/api/noc/segment/searchItem/',
                get:'/api/noc/segment/getItem/',
                set:'/api/noc/segment/setItem/',
                add:'/api/noc/segment/addItem/',
                del:'/api/noc/segment/delItem/',
                toggle:'/api/noc/segment/toggleItem/'
            }
        );
    });

</script>


<table id="grid-segment" class="table table-condensed table-hover table-striped" data-editDialog="DialogSegment">
    <thead>
        <tr>
            <th data-column-id="uuid" data-type="string" data-identifier="true"  data-visible="false">{{ lang._('ID') }}</th>
            <th data-column-id="enabled" data-width="6em" data-type="string" data-formatter="rowtoggle">{{ lang._('Enabled') }}</th>
            <th data-column-id="hubId" data-type="string">{{ lang._('Hub ID') }}</th>
            <th data-column-id="name" data-type="string">{{ lang._('Name') }}</th>
            <th data-column-id="lastUpdate" data-type="string">{{ lang._('Last Update') }}</th>
            <th data-column-id="status" data-type="string">{{ lang._('Status') }}</th>
            <th data-column-id="commands" data-width="7em" data-formatter="commands" data-sortable="false">{{ lang._('Commands') }}</th>
        </tr>
    </thead>
    <tbody>
    </tbody>
    <tfoot>
        <tr>
            <td></td>
            <td>
                <button data-action="add" type="button" class="btn btn-xs btn-default"><span class="fa fa-plus"></span></button>
                <button data-action="deleteSelected" type="button" class="btn btn-xs btn-default"><span class="fa fa-trash-o"></span></button>
            </td>
        </tr>
    </tfoot>
</table>


{{ partial("layout_partials/base_dialog",['fields':formSegment,'id':'DialogSegment','label':lang._('Edit segment')])}}
