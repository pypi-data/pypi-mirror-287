


<script>
	


///
//
import { AppRail, AppRailTile, AppRailAnchor } from '@skeletonlabs/skeleton';
import { Modal, getModalStore } from '@skeletonlabs/skeleton';
//
//
import Layer_Octas_Gifts_Friends from '$lib/Quests/Octas_Gifts_Version_1/Friends_Panel/Trinket.svelte'
import Layer_Octas_Faucet from '$lib/Quests/Octas_Faucet/Trinket.svelte'
//
import { parse_styles } from '$lib/trinkets/styles/parse'
import Panel from '$lib/trinkets/panel/trinket.svelte'
//
//\

const trends = {
	panel: {
		position: 'relative',
		display: 'inline-flex',
		//'width': '33%', 
		'height': '200px',
		'align-items': 'center',
		'justify-content': 'center',
		'flex-direction': 'column'
	},
	anchor: parse_styles ({
		position: 'absolute',
		height: '100%',
		width: '100%',
		
		display: 'flex',
		'align-items': 'center',
		'justify-content': 'center',
		'text-decoration': 'none',
		'text-align': 'center',
		'font-size': '2em'
	})
}

const modal_store = getModalStore ();

const octas_gifts_v1 = () => {
	console.log ('sending from account_1 to account_2')	
	
	modal_store.trigger ({
		type: 'component',
		component: {
			ref: Layer_Octas_Gifts_Friends,
			props: { 
				modal_store
			}
		}
	});
}

const octas_faucet = () => {
	modal_store.trigger ({
		type: 'component',
		component: {
			ref: Layer_Octas_Faucet,
			props: { 
				modal_store
			}
		}
	});
}

</script>

<style>

@media (max-width: 600px) {
    .latest-block-panel {
		flex-direction: column !important;
	}
}

</style>

<svelte:head>
	<title>Moves</title>
	<meta name="description" content="Aptos Moves" />
</svelte:head>

<section
	quests_address
	style={ parse_styles ({
		position: 'relative',
		display: 'grid',
		'width': '100%',
		'grid-template-columns': 'repeat(auto-fit, minmax(400px, 1fr))',
		'grid-gap': '10px'
	}) }
>
	<Panel 
		styles={ trends.panel }
	>		
		<div class="relative inline-block">
			<span class="badge variant-soft-primary absolute -right-0 z-10"
				style="
					left: 50%;
					bottom: -30px;
					transform: translateX(-50%);
				"
			>Version 1</span>
			<button 
				faucet
				
				on:click={ octas_faucet }
				type="button" 
				class="btn bg-gradient-to-br variant-gradient-primary-secondary"
				style="
					font-size: 1.3em;
					padding: 12px 36px;
					margin-top: 10px
				"
			>Faucet</button>
		</div>
	</Panel>

	<Panel 
		styles={ trends.panel }
	>		
		<div class="relative inline-block">
			<span class="badge variant-soft-primary absolute -right-0 z-10"
				style="
					left: 50%;
					bottom: -30px;
					transform: translateX(-50%);
				"
			>Version 1</span>
			<button 
				octas_gifts__version_1
				
				on:click={ octas_gifts_v1 }
				type="button" 
				class="btn bg-gradient-to-br variant-gradient-primary-secondary"
				style="
					font-size: 1.3em;
					padding: 12px 36px;
					margin-top: 10px
				"
			>Transfer</button>
		</div>

		<div
			style="
				display: none;
				padding: 0.3cm 0 0
			"
		>
			<span class="badge variant-soft-primary">0x1::aptos_account::transfer</span>
		</div>
	</Panel>
</section>

