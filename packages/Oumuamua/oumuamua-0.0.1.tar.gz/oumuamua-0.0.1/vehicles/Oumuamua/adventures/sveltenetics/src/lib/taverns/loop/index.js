

/*
	loop_1 = loop ({
		wait: 2000,
		action: () => {
		 
		}
	})
	
	loop_1.play ()
	loop_1.pause () 
	loop_1.stop ()
*/


export const loop = ({
	wait,
	action
}) => {
	let playing = "no"
	
	let timeout = ""
	const the_loop = async () => {
		console.info ("the_loop", wait)
		
		if (playing === "yes") {
			setTimeout (() => {
				action ();
			})
		}
		
		await new Promise (resolve => {
			timeout = setTimeout (() => {
				resolve ()
			}, 2000)
		})
		
		if (playing === "yes") {
			clearTimeout (timeout)
			the_loop ();
		}
	}
	
	return {
		play: () => {
			if (playing === "no") {
				playing = "yes"
				the_loop ()
			}
		},
		pause: () => {
			clearTimeout (timeout)
			playing = "no"
		},
		stop: () => {
			clearTimeout (timeout)
			playing = "no"
		}
	}
}