const navSlide = () => {
	const burgrer = document.querySelector('.burger');
	const nav = document.querySelector('.nav-links');
	const navLinks = document.querySelectorAll('.nav-links li');
	//Toggle Nav
	burger.addEventListener('click', ()=>{
		nav.classList.toggle('nav-active');

		navLinks.forEach((link, index)=>{
		if(link.style.annimation){
			link.style.animation = '';
		}
		else{
			link.style.animation = 'navLinkFade 0.5s ease forwards ${index/7 + 1.5}s';
		}
	});
	});
}



const main = ()=>{
	navSlide();
}

main();