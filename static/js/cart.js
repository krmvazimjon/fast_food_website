console.log('Working')

// menu.htmlda add cart bolimiga datalarini yozish kk 

// mahsulotni id sini olish uchun js kodlaridan foydalanamiz
var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, "action:", action)
	})
}

// 6 - bosqich
// Add cart bosilsa uni qaysi user bosyabdi shu malumotni olishimiz uchun js kodlarudan foydalanamiz
// base.html ga js kpodlarini yozb kelishimiz kk 


var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:',productId,"action:",action)

		console.log('User:', user)
		if(user == 'AnonymousUser'){
			console.log('Not logging in')
		}else{
			updateUserOrder(productId, action)
		}
	})
}

// 7-bosqich
// js yordamida Backend POST yuborish uchun Token olishimiz kk 

function updateUserOrder(productId, action){
console.log('User is liggin')

	var url = '/update_item/'
	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body:JSON.stringify({'productId': productId, 'action': action})
	})
	.then((response) =>{
		return response.json()
	})
	.then((data) =>{
		console.log('data:', data)
		location.reload()
	})
}