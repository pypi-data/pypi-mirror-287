
<script>



import Polytope_1 from './Polytope_1.svelte'
import { Modal, getModalStore } from '@skeletonlabs/skeleton';
const modal_store = getModalStore ();

/*
let conference_instance;
const prepare_modal = () => {
	console.info ({ conference_instance })
	
	conference_instance.open_the_polytope ({
		
	})
}
*/

const prepare = () => {
	return {
		name: "Transfer",
		next: "yes",
		back: "yes"
	}
}
const enhance = () => {
	return {}
}


export const open_the_polytope = ({
	name = ""
}) => {
	modal_store.trigger ({
		type: 'component',
		component: {
			ref: Polytope_1,
			props: { 
				modal_store,
				name
			}
		}
	});
}



</script>

<div>
	<button 
		on:click={ open_the_polytope }
	
		type="button" 
		class="btn variant-filled"
	>Open Polytope</button>
</div>