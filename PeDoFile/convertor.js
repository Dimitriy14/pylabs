const word2pdf = require('word2pdf');
const fs = require('fs-extra');
 
(async () => {
	const NUMBER_OF_LABS = 6;

	fs.ensureDir('../ready')
	const convert = async (labNumber) => {
		return new Promise(async(res) => {
			try {
				console.log(`Converting lab${labNumber}`)
				const data = await word2pdf(`../lab${labNumber}/lab${labNumber}.docx`)
		    	fs.writeFileSync(`../ready/lab${labNumber}.pdf`, data);
		    	console.log(`lab N${labNumber} converted`)
			} catch(e) {
				console.log(`Error while converting lab N${labNumber}`)
			}
			res();
		})
	}

	for(let labNumber = 1; labNumber <= NUMBER_OF_LABS; labNumber++) {
		convert(labNumber);
	}
})()
