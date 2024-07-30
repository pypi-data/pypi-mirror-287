




<script>

import Panel from '$lib/trinkets/panel/trinket.svelte'

</script>

<style>

@media (max-width: 600px) {
    .latest-block-panel {
		flex-direction: column !important;
	}
}
a {
	line-height: 110%;
}

</style>

<svelte:head>
	<title>Roomies</title>
	<meta name="description" content="Roomies" />
</svelte:head>

<div>
	<div 
		style="padding: 25px 0"
		class="text-column"
	>
		<h1>Roomies</h1>
		<p 
			style="
				text-align: center;
				padding: .25cm 0;
			"
		>This region has the local settings that effect the dapp.</p>
	</div>
</div>
