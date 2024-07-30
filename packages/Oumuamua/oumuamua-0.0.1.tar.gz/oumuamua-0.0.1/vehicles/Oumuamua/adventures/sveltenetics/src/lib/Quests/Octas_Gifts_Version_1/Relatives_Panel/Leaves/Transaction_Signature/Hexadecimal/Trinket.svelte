
<script>

import { make_barcode } from '$lib/Barcode/make'
//
import { onMount, onDestroy } from 'svelte';
import { ConicGradient } from '@skeletonlabs/skeleton';
//

import { 
	refresh_truck, 
	retrieve_truck, 
	monitor_truck,
	verify_land
} from '$lib/Quests/Octas_Gifts_Version_1/Relatives_Panel/Logistics/Truck'
let prepared = "no"
let Truck_Monitor;
let freight;
onMount (async () => {
	const Truck = retrieve_truck ()
	freight = Truck.freight; 
		
	Truck_Monitor = monitor_truck ((_freight) => {
		freight = _freight;
	})
	
	prepared = "yes"
});
onDestroy (() => {
	Truck_Monitor.stop ()
});



</script>

{#if prepared === "yes" }
<div>
	<pre
		signature_hexadecimal_string
		
		class="bg-surface-50-900-token"
		style="
			box-sizing: border-box;
			height: 100%; 
			font-size: 1em;
			white-space: break-spaces;
			word-wrap: break-word;
			text-align: left;
			
			padding: 12px;
			border-radius: 8px;
		"
	>{ freight.Unsigned_Transaction_Signature.hexadecimal_string }</pre>
</div>
{/if}