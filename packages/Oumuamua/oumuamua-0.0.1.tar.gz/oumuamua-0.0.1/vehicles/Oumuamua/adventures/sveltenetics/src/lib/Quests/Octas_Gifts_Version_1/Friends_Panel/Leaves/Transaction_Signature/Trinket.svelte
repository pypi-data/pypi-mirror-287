


<script>


////
///
//
import { TabGroup, Tab, TabAnchor } from '@skeletonlabs/skeleton';
//
import { onMount, onDestroy } from 'svelte';

//
//\
//\\

import { 
	refresh_truck, 
	retrieve_truck, 
	monitor_truck,
	verify_land
} from '$lib/Quests/Octas_Gifts_Version_1/Friends_Panel/Logistics/Truck'

let prepared = "no"
let Truck_Monitor;
let freight;
onMount (async () => {
	const Truck = retrieve_truck ()
	freight = Truck.freight; 
	
	freight.current.land = "Transaction_Signature"
	
	Truck_Monitor = monitor_truck ((_freight) => {
		freight = _freight;
	})
	
	prepared = "yes"
});

onDestroy (() => {
	Truck_Monitor.stop ()
});

let current_show = 0;

</script>

{#if prepared === "yes"}
{#if freight.transaction_signature.hexadecimal_string.length == 0 }
<div
	style="
		padding: 50px
	"
>
	<p>The signature was not added.</p>
</div>
{:else}
<div transaction_signature>
	<div
		style="
			text-align: center;
			padding: 1cm 0 1cm;
		"
	>
		<header
			style="
				text-align: center;
				font-size: 2em;
				padding: .2cm 0;
			"
		>Transaction Signature</header>
		<p>This Transaction Signature should be the same as the one that was created on the other trinket.</p>
	</div>
	
	<TabGroup>
		<Tab bind:group={current_show} name="tab1" value={0}>
			<span transaction_signature_object>Object</span>
		</Tab>
		<Tab bind:group={current_show} name="tab2" value={1}>
			<span transaction_signature_hexadecimal_string>Hexadecimal</span>
		</Tab>
		
		<svelte:fragment slot="panel">
			{#if current_show === 0}
				<div>
					<header
						style="
							text-align: center;
							font-size: 1.4em;
							padding: .2cm 0;
						"
					>Transaction Signature Object</header>
					<p
						style="text-align: center"
					>This is the signature that was created from the private key.</p>
					<pre
						class="bg-surface-50-900-token"
						style="
							box-sizing: border-box;
							height: 100%; 
							font-size: 1em;
							white-space: break-spaces;
							word-wrap: break-word;
							text-align: left;
						"
					>{ freight.transaction_signature.Aptos_object_fiberized }</pre>
				</div>
			{:else if current_show === 1}
				<pre
					transaction_signature_hexadecimal_string
					class="bg-surface-50-900-token"
					style="
						box-sizing: border-box;
						height: 100%; 
						font-size: 1em;
						white-space: break-spaces;
						word-wrap: break-word;
						text-align: left;
						border-radius: 6px;
					"
				>
{ freight.transaction_signature.hexadecimal_string }
				</pre>
			{/if}
		</svelte:fragment>
	</TabGroup>
</div>
{/if}
{/if}