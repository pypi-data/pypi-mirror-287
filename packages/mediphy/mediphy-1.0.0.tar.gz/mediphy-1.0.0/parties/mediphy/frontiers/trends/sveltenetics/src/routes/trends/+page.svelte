
<script>

import { onMount, onDestroy, beforeUpdate } from 'svelte'

import { ask_for_freight } from '$lib/Behavior/Trucks'
const { mongo_address } = ask_for_freight ();

console.info ({ mongo_address })

import { ask_trend_count } from '$lib/trends_mongo/ask_count.mongo.js'

onMount (async () => {
	const { enhanced } = await ask_trend_count ()
	console.info ({ enhanced })
})

</script>


<div>
	<header>trends</header>

</div>