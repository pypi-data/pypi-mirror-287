
// https://aptos.dev/en/build/apis/fullnode-rest-api-reference#tag/general/get/

/*
	import { request_ledger_info } from '$lib/PTO/General/Ledger_Info.API'
	const { enhanced } = await request_ledger_info ({ net_path })
	const { chain_id } = enhanced;
*/

export const request_ledger_info = async ({ net_path }) => {
	const proceeds = await fetch (net_path);
	// console.log (proceeds.status)

	if (proceeds.status === 404) {

	}
	
	const enhanced = await proceeds.json ()
	
	return {
		enhanced
	};
}