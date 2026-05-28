document.addEventListener("DOMContentLoaded", function(){ 				window.addEventListener( 'DOMContentLoaded', () => {
					const blockScope = document.querySelector( '.uagb-block-545f19e6' );
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
			window.addEventListener( 'DOMContentLoaded', function() {
	UAGBInlineNotice.init( {"c_id":null,"cookies":false,"close_cookie_days":1,"noticeDismiss":"uagb-dismissable","icon":"playstation"}, '.uagb-block-d63f9d3b' );
});
window.addEventListener( 'DOMContentLoaded', function() {
	UAGBInlineNotice.init( {"c_id":null,"cookies":false,"close_cookie_days":1,"noticeDismiss":"uagb-dismissable","icon":"phone-flip"}, '.uagb-block-c8007a2c' );
});
window.addEventListener( 'DOMContentLoaded', function() {
	UAGBInlineNotice.init( {"c_id":null,"cookies":false,"close_cookie_days":1,"noticeDismiss":"uagb-dismissable","icon":"envelope"}, '.uagb-block-366a7ced' );
});
window.addEventListener("DOMContentLoaded", function(){
	UAGBForms.init( {"block_id":"6082195f","reCaptchaEnable":false,"reCaptchaType":"v2","reCaptchaSiteKeyV2":"","reCaptchaSiteKeyV3":"","afterSubmitToEmail":"","afterSubmitCcEmail":"","afterSubmitBccEmail":"","afterSubmitEmailSubject":"Form Submission","sendAfterSubmitEmail":true,"confirmationType":"message","hidereCaptchaBatch":false,"captchaMessage":"Please fill up the above captcha.","confirmationUrl":""}, '.uagb-block-6082195f', 2036 );
});
 });