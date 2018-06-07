$(document).ready(function () {
    let action = { bot_name:"DEFAULT", method:"DEFAULT", action:"configure_bot" };

    let req = {
        action: 'get_bots'
    };
    let botsContent = $('#bots-content');

    $.ajax({
        type: "POST",
        beforeSend: function(request) {
            request.setRequestHeader('Content-Type', 'application/json');
        },
        url: "/api/config",
        data: JSON.stringify(req),
        processData: false,
        success: function(data) {
            console.log(data);
            data = JSON.parse(data);

            if (data.error) {
                botsContent.html("<p style='margin: 1rem 2rem'>No bots configured. You can a bot by adding an app and then adding a bot.</p>")
            } else {
                let bots = data.bots;
                let sz = bots.length;
                let table_html = '';

                for (let i = 0; i < sz; i++) {
                    let tableControls = `
                    <td>
                        <div class="field is-grouped is-grouped-right" id="${bots[i].bot_name}-buttons">
                            <p class="control">
                                <a class="button add-bot-btn" id="${bots[i].bot_name}">
                                    Configure Bot
                                 </a>
                            </p>
                        </div>
                    </td>`;
                    table_html += `<tr><td width="5%"><i class="fas fa-user"></i></td><td>${bots[i].bot_name} (${bots[i].app_name})</td>${tableControls}</tr>`
                }
                $('#bots-table-body').html(table_html);

                $('.add-bot-btn').click(function(){
                    action.bot_name = $(this).attr('id');
                    $('#configuration1-modal').addClass('is-active');
                });
            }
        }
    });

    req = {'action': 'get_bot_actions'};

    $.ajax({
        type: "POST",
        beforeSend: function(request) {
            request.setRequestHeader('Content-Type', 'application/json');
        },
        url: "/api/config",
        data: JSON.stringify(req),
        processData: false,
        success: function(data) {
            console.log(data);
            data = JSON.parse(data);
            let start_buttons = [];
            let sz = data.bot_actions.length;

            for (let i = 0; i < sz; i++) {
                let item = data.bot_actions[i];
                start_buttons.push('#' + item.bot_name + '-' + item.action_name);
                console.log(start_buttons);

                $('#' + item.bot_name + '-buttons').append(
                    `<p class="control">
                        <a class="button is-success add-bot-btn" id="${item.bot_name}-${item.action_name}">
                            Start
                         </a>
                    </p>`
                )
            }

            for (let i = 0; i < start_buttons.length; i++) {
                $(start_buttons[i]).click(function () {
                    let info = start_buttons[i].split('-');
                    let bot_name = info[0].replace('#', '');
                    let action_name = info[1];

                    console.log(bot_name, action_name);

                    let postData = {
                        bot_name: bot_name,
                        action_name: action_name,
                        action: 'start_bot'
                    };

                    $.ajax({
                        type: "POST",
                        beforeSend: function(request) {
                            request.setRequestHeader('Content-Type', 'application/json');
                        },
                        url: "/api/bot",
                        data: JSON.stringify(postData),
                        processData: false,
                        success: function(data) {
                            console.log(data);
                        }
                    });
                });
            }
        }
    });

    $('#checkbox-reply').click(function() {
        $(".replybox").toggle(this.checked);
    });

    $('#configuration1-next').click(function() {
        $('#configuration2-modal').addClass('is-active');
        $('#configuration1-modal').removeClass('is-active');
    });

    $("#configuration2-next").click(function(){
        if (action.actions) delete action.actions;
        action.method = $('#source option:selected').val();

        action.actions = [];

        let cAction = {};

        if (action.method === "react_to_my_mentions" ||
            action.method === "react_to_my_timeline") {
            let text_tags = $('#text-tags option:selected');
            let filterText = $("#filtertext");
            let actionName = $('#action-name');

            action.action_name = actionName.val();

            if (text_tags.val() === "exactly") {
                cAction["exactly"] = filterText.val();
            } else if (text_tags.val() === "tags") {
                cAction["tags"] = filterText.val().split(" ");
            }

            let checkbox = [];
            let reply = $("#checkbox-reply");
            let follow = $("#checkbox-follow");
            let favor = $("#checkbox-favor");


            if (reply.is(':checked')){
                checkbox.push(reply.val());
            }
            if (favor.is(':checked')){
                checkbox.push(favor.val());
            }

            if (follow.is(':checked')){
                checkbox.push(follow.val());
            }

            if (checkbox.length === 1){
                checkbox = checkbox[0];
            }

            cAction["action"] = checkbox;

            if( reply.is(':checked')){
                cAction["text"] = $("#replytext").val();
            }
        }

        action.actions.push(cAction);

        $.ajax({
            type: "POST",
            beforeSend: function (request) {
                request.setRequestHeader('Content-Type', 'application/json');
            },
            url: "/api/config",
            data: JSON.stringify(action),
            processData: false,
            success: function (data) {
                console.log(data);
                location.reload();
            }
        });


    });

    $('.close-modal').click(function() {
        $('.modal').removeClass('is-active');
    });

    $('configuration-modal-close').click(function() {
        $('.modal').removeClass('is-active');
    });
});