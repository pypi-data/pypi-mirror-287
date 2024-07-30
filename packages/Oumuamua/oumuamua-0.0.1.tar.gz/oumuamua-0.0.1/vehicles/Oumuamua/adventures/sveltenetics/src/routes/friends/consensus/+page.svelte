


<script>
	
import Panel from '$lib/trinkets/panel/trinket.svelte'

import Balance from '$lib/trinkets/Consensus/Balance/Trinket.svelte'
import Summary from '$lib/trinkets/Consensus/Summary.svelte'
import Transaction from '$lib/trinkets/Consensus/Transaction.svelte'

import Net_Choices from '$lib/PTO/Nets/Choices.svelte'

const on_change = ({ net }) => {
	const net_name = net.name;
	const net_path = net.path;
	
}

import { Autocomplete } from '@skeletonlabs/skeleton';
import { popup } from '@skeletonlabs/skeleton';

let leaf = '';
let leaf_actual = ''
let popupSettings = {
	event: 'focus-click',
	target: 'popup-autocomplete',
	placement: 'bottom',
};

const onPopupDemoSelect = (event) => {
	console.info ("onPopupDemoSelect", event.detail.label)
	// leaf = event.detail.label;
	leaf_actual = event.detail.label.toLowerCase ()
}


const consensus_options = [
	{ label: 'Balance' },
	{ label: 'Summary' },
	{ label: 'Transaction' }
];
				

</script>

<svelte:head>
	<title>Consensus</title>
	<meta name="description" content="consensus" />
</svelte:head>

<section style="justify-content: start">

	<div style="height: 8px"></div>
	

	<div
		style="
			maring: 0 auto;
			display: flex;
			align-items: center;
			justify-content: center;
		"
	>
		<input
			style="
				display: block;
				padding: 8px;
				max-width: 90%;
			"
			class="input autocomplete"
			type="search"
			name="autocomplete-search"
			bind:value={ leaf }
			placeholder = "Search"
			use:popup={popupSettings}
		/>
	</div>
	
	<div 
		data-popup="popup-autocomplete"
		class="card bg-gradient-to-br variant-gradient-secondary-tertiary w-full max-w-sm max-h-48 p-4 overflow-y-auto"
		style="
			z-index: 100
		"
	>
		<Autocomplete
			bind:input={ leaf }
			options={ consensus_options }
			on:selection={onPopupDemoSelect}
		/>
	</div>

	<div style="height: 8px"></div>
	
	{#if [ "summary", "" ].includes (leaf_actual) }
	<Summary />
	{/if}
	
	{#if leaf_actual === "balance" }
	<Balance />
	{/if}
	
	{#if leaf_actual === "transaction" }
	<Transaction />
	{/if}
	
	<div style="height: 200px"></div>
	
</section>


