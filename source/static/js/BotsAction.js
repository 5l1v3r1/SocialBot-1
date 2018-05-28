$(document).ready(function () {
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
                        <div class="field is-grouped is-grouped-right">
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
            }
        }
    });
});