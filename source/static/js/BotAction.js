$(function () {
   $('#new-bot-btn').click(function () {
       let modal = $('#new-bot-modal');
       modal.addClass('is-active');

       $('.new-bot-model-close').click(function () {
            modal.removeClass('is-active');
       });
   });
});