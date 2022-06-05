





//################################################################################

// ### 1. MAKE A PREDICTION ON THE IMAGE OR MULTIPLE IMAGES THAT THE USER SUBMITS

//#################################################################################


async function model_makePrediction(fname) {

	// clear the previous variable from memory.
	let image = undefined;
	
	image = $('#selected-image').get(0);
	
	// Pre-process the image
	let tensor = tf.fromPixels(image)
	.resizeNearestNeighbor([96,96]) // change the image size here
	.toFloat()
	.div(tf.scalar(255.0))
	.expandDims();

	
	// Pass the tensor to the model and call predict on it.
	// Predict returns a tensor.
	// data() loads the values of the output tensor and returns
	// a promise of a typed array when the computation is complete.
	// Notice the await and async keywords are used together.
	let predictions = await model.predict(tensor).data();
	let top5 = Array.from(predictions)
		.map(function (p, i) { // this is Array.map
			return {
				probability: p,
				className: TARGET_CLASSES[i] // we are selecting the value from the obj
			};
				
			
		}).sort(function (a, b) {
			return b.probability - a.probability;
				
		}).slice(0, 3);

	let inc = 0;
	let tb = 0;
	let norm = 0;
	top5.forEach(function (p) {
	
		$("#prediction-list").append(`<li style="list-style-type:none;">${p.className}: ${p.probability.toFixed(3)}</li>`);
		//console.log(inc++);
		console.log(p.probability);
		
		if(p.className == 'Normal'){
			norm = p.probability.toFixed(3);
		}
		if(p.className == 'Tuberculosis'){
			tb = p.probability.toFixed(3);
		}
		inc++;
	});
	inc = 0;
	console.log(norm);
	console.log(tb);

	if(norm > tb){
		$('#diagnosis').html('<span  id="tbdiagnosis" style="color: green;">The scan shows no Tuberculosis symptoms</span>');
	}
	if(norm < tb){
		$('#diagnosis').html('<span id="tbdiagnosis" style="color: red;">The scan shows Tuberculosis symptoms</span>');
	}

	
		
}



function model_delay() {
	
	return new Promise(resolve => setTimeout(resolve, 200));
}


async function model_delayedLog(item, dataURL) {
	
	// We can await a function that returns a promise.
	// This delays the predictions from appearing.
	// Here it does not actually serve a purpose.
	// It's here to show how a delay like this can be implemented.
	await model_delay();
	
	// display the user submitted image on the page by changing the src attribute.
	// The problem is here. Too slow.
	$("#selected-image").attr("src", dataURL);
	$("#displayed-image").attr("src", dataURL); 
	
	// log the item only after a delay.

}



async function model_processArray(array) {
	
	for(var item of fileList) {
		
		
		let reader = new FileReader();
		
		// clear the previous variable from memory.
		let file = undefined;
	
		
		reader.onload = async function () {
			
			let dataURL = reader.result;
			
			await model_delayedLog(item, dataURL);
			
			
			
			var fname = file.name;
			
			// clear the previous predictions
			$("#prediction-list").empty();
			
			// 'await' is very important here.
			await model_makePrediction(fname);
		}
		
		file = item;
		
		// Print the name of the file to the console
        //console.log("i: " + " - " + file.name);
			
		reader.readAsDataURL(file);
	}
}













