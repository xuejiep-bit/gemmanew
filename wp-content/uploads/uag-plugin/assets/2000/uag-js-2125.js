document.addEventListener("DOMContentLoaded", function(){ 				window.addEventListener( 'DOMContentLoaded', () => {
					const blockScope = document.querySelector( '.uagb-block-15d8b2c5' );
					if ( ! blockScope ) {
						return;
					}

					const anchorElement = blockScope.querySelector('a');
					if (!anchorElement) {
						return;
					} 

					 
					blockScope.addEventListener('keydown', (event) => {
						if ( 13 === event.keyCode || 32 === event.keyCode ) {
							event.preventDefault();
							 
							anchorElement.click();	
						}
					} );
				} );
			window.addEventListener( 'load', function() {
	UAGBButtonChild.init( '.uagb-block-5ed7bb6f' );
});
window.addEventListener( 'load', function() {
	UAGBButtonChild.init( '.uagb-block-d67e5a42' );
});
window.addEventListener( 'load', function() {
	UAGBButtonChild.init( '.uagb-block-9f6a6892' );
});
 });