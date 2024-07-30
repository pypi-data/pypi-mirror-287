



<script>

//
//	https://schum123.github.io/svelte-loading-spinners/
//


//
import Unfinished from './Trinkets/Unfinished.svelte'
//
import { onMount } from 'svelte'
//
import { Wave } from 'svelte-loading-spinners';
//
import { Modal, getModalStore } from '@skeletonlabs/skeleton';
import { ConicGradient } from '@skeletonlabs/skeleton';
//
const modal_store = getModalStore ();

$: freight = {
	showing: 'no',
	name: '',
	unfinished: {
		showing: 'yes',
	},
	back: {
		text: 'Back',
		permitted: "no",
		go: () => {}
	},
	next: {
		text: 'Unfinished',
		permitted: "no",
		has_alert: "yes",
		go: () => {
			
		}
	},
	panel: {
		text: ''
	},
	close: () => {
		console.info ('close_the_modal')
		modal_store.close ();
	}
}


export let on_prepare;
export const advance = (action) => {
	// @ advance, promote, evolve, adapt
	// @ promote
	// @ progress
	// @ habilitate
	
	const _freight = action ({ freight })
	freight = _freight;
}


const close_the_waiting_modal = () => {
	console.info ('close_the_waiting_modal')
	freight.unfinished.showing = "no"
}

const on_back_pressed = () => {
	freight.back.go ({
		freight
	})
}
const on_next_pressed = () => {
	freight.back.go ({
		freight
	})
}


onMount (() => {
	on_prepare ()
})



</script>



<div 
	style="
		position: relative;
		top: 0;
		left: 0;
		padding: 0;
		width: calc(100vw - 36px);
		height: calc(100vh - 36px);
	
		overflow-y: scroll;
	"
>
	<div
		class="bg-surface-50-900-token border border-primary-500/30"
		style="
			display: flex;
			
			position: absolute;
			top: 0;
			left: 0;
			height: 100%;
			width: 100%;
			border-radius: 8px;
			
			overflow: hidden;
			
			flex-direction: column;
		"
	>
		<div
			style="
				display: flex;
				justify-content: center;
				flex-direction: column;
			"
		>
			<header
				style="
					padding: 0.2cm 0;
					text-align: center;
					font-size: 1.2em;
				"
			>{ freight.name }</header>
			<hr class="!border-t-2" />
		</div>
	</div>
	
	<Unfinished 
		showing={ freight.unfinished.showing }
		close={ close_the_waiting_modal }
	>
		<slot name="unfinished"></slot>
	</Unfinished>
	
	{#if freight.showing === "yes" }
	<div
		style="
			position: absolute;
			top: 0;
			left: 0;
			right: 0;
			bottom: 0;
			width: 100%;
			
			box-sizing: border-box;
			padding: 0 10px 0;
			
			overflow: scroll;
		"
	>
		<div style="height: 2cm" />	
		{ JSON.stringify (freight.unfinished) }
		<slot name="leaves"></slot>
		<div style="height: 5cm" />
	</div>
	{:else}
	<div
		style="
			position: absolute;
			top: 0;
			left: 0;
			right: 0;
			bottom: 0;
			width: 100%;
			
			box-sizing: border-box;
			padding: 0 10px 0;
			
			overflow: scroll;
			
			display: flex;
			justify-content: center;
			align-items: center;
		"
	>
		<div>	
			<div style="height: 2cm" />
			<Wave 
				size="60" 
				color='rgb(var(--color-primary-500))' 
				unit="px" 
				duration="1s" 
			/>
		</div>
	</div>
	{/if}


	<footer
		class="bg-surface-50-900-token border border-primary-500/30"
		style="
			position: absolute;
			bottom: 0;
			left: 0;
			width: 100%;
			height: 70px;
		"
	>
		<hr class="!border-t-2" />
		
		<div 
			class="modal-footer"
			style="
				display: flex;
				align-items: center;
				justify-content: space-between;
			
				position: absolute;
				bottom: 0;
				left: 0;
				width: 100%;
				padding: 10px;
			"
		>
			<button 
				class="btn variant-filled" 
				on:click={ freight.close }
			>
				Quit
			</button>
			
			<div>{ freight.panel.text }</div>
		
			<div style="display: flex">
				<button 
					modal-back
				
					disabled={ freight.back.permitted != "yes" }
					on:click={ freight.back.go }
					
					class="btn variant-filled"
				>{ freight.back.text }</button>
				<div style="width: 20px"></div>
				<button 
					modal-next
				
					disabled={ freight.next.permitted != "yes" && freight.next.has_alert != "yes" }
					on:click={ freight.next.go }
					
					class="btn variant-filled" 
				>
					{#if freight.next.permitted != "yes" }
					<span>
						<Wave 
							size="13" 
							color='rgb(var(--color-primary-500))' 
							unit="px" 
							duration="1.2s" 
						/>
					</span>
					{/if}
					<span>
						{ freight.next.text }
					</span>
				</button>
			</div>
		</div>
	</footer>
</div>
