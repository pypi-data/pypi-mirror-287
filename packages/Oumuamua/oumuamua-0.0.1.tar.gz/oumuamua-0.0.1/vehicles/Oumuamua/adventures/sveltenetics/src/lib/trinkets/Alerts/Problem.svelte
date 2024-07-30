



<script>


/*
import Problem_Alert from '$lib/trinkets/Alerts/Problem.svelte'
<Problem_Alert 
	text={}
/>
*/

/*
<ConicGradient stops={conicStops} spin 
		width="w-6"
	/>
*/

import { ConicGradient } from '@skeletonlabs/skeleton';
import { Wave } from 'svelte-loading-spinners';

export let text;

const conicStops = [
	{ color: 'transparent', start: 0, end: 25 },
	{ color: 'rgb(var(--color-primary-500))', start: 75, end: 100 }
];

</script>

{#if typeof text === "string" && text.length >= 1}
<aside 
	class="alert variant-soft-error" 
	style="
		display: flex; 
		flex-direction: row;
		align-items: center;
		
		padding: 12px; 
		margin-top: 8px
	"
>
	
	<Wave size="20" color="#FF3E00" unit="px" duration="1s" />
	<div class="alert-message" style="padding: 0 0 0 10px; margin: 0;">
		<p>{ text }</p>
	</div>
</aside>
{/if}