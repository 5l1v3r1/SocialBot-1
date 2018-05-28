$(document).ready(function () {
    let appsContent = $('#apps-content');
    let postObj = {
        action: 'get_apps'
    };
    let oauthData = {};

    $.ajax({
        type: "POST",
        beforeSend: function(request) {
            request.setRequestHeader('Content-Type', 'application/json');
        },
        url: "/api/config",
        data: JSON.stringify(postObj),
        processData: false,
        success: function(data) {
            if (typeof data === 'string') {
                data = JSON.parse(data)
            }

            console.log(data);

            if (data.error) {
                appsContent.html("<p style='margin: 1rem 2rem'>No apps configured. You can add an app with 'New App'.</p>")
            } else {
                let apps = data.apps;
                let sz = apps.length;
                let table_html = '';

                for (let i = 0; i < sz; i++) {
                    let tableControls = `
                    <td>
                        <div class="field is-grouped is-grouped-right">
                            <p class="control">
                                <a class="button add-user-btn" id="${apps[i].app_name}">
                                    Add user
                                 </a>
                            </p>
                            <p>
                                <a class="button remove-user-btn" id="${apps[i].app_name}">
                                    Remove user
                                </a>
                            </p>
                        </div>
                    </td>`;
                    table_html += `<tr><td width="5%"><i class="fas fa-rocket"></i></td><td>${apps[i].app_name}</td>${tableControls}</tr>`
                }
                $('#apps-table-body').html(table_html);

                $('.add-user-btn').click(function () {
                    let addUserModal = $('#add-user-modal');
                    addUserModal.addClass('is-active');
                    let app = this.id;

                    $('.add-user-modal-close').click(function () {
                        addUserModal.removeClass('is-active');
                    });

                    $('#add-user-next-modal').click(function () {
                        let req = {
                            'action': 'add_user',
                            'app_name': app
                        };

                        $.ajax({
                            type: "POST",
                            beforeSend: function(request) {
                                request.setRequestHeader('Content-Type', 'application/json');
                            },
                            url: "/api/config",
                            data: JSON.stringify(req),
                            processData: false,
                            success: function(data) {
                                data = JSON.parse(data);

                                if (data.message && data.code === 200 && data.dump) {
                                    console.log(data);
                                    oauthData = data.dump;
                                    addUserModal.removeClass('is-active');
                                    let addUserPINModal = $('#add-user-form-modal');
                                    addUserPINModal.addClass('is-active');

                                    $('.add-user-form-modal-close').click(function () {
                                        addUserPINModal.removeClass('is-active');
                                    });

                                    $('#add-user-save-modal').click(function () {
                                        let pinInput = $('#add-user-pin-input');
                                        let pinHelp = $('#add-user-pin-help');
                                        let nameInput = $('#add-user-name-input');
                                        let nameHelp = $('#add-user-name-help');

                                        if (!nameInput) {
                                            nameInput.addClass('is-danger');
                                            nameHelp.addClass('is-danger');
                                            nameHelp.html('Missing a Username.')
                                        } else if (!pinInput.val()) {
                                            pinInput.addClass('is-danger');
                                            pinHelp.addClass('is-danger');
                                            pinHelp.html('Missing a Pin Code.');
                                        } else {
                                            let requ = oauthData;
                                            requ.action = 'add_user_pin';
                                            requ.pin_code = pinInput.val();
                                            requ.username = nameInput.val();

                                            $.ajax({
                                                type: "POST",
                                                beforeSend: function(request) {
                                                    request.setRequestHeader('Content-Type', 'application/json');
                                                },
                                                url: "/api/config",
                                                data: JSON.stringify(requ),
                                                processData: false,
                                                success: function(data) {
                                                    data = JSON.parse(data);

                                                    if (data.message && data.code === 200) {
                                                        addUserPINModal.removeClass('is-active');
                                                        location.reload();
                                                    } else {
                                                        console.log('Something went wrong!');
                                                        console.log(data);
                                                    }
                                                }
                                            });
                                        }
                                    });

                                } else {
                                    console.log('Something went very wrong.');
                                    console.log(data);
                                }
                            }
                        });
                    });
                });
            }
        }
    });


   $('#new-app-btn').click(function () {
       let modal = $('#new-app-modal');
       modal.addClass('is-active');

       $('.new-app-modal-close').click(function () {
            modal.removeClass('is-active');
       });

       $('#new-app-next-modal').click(function () {
            modal.removeClass('is-active');
            let formModal = $('#new-app-form-modal');
            let nameInput = $('#new-app-name-input');
            let keyInput = $('#new-app-key-input');
            let secretInput = $('#new-app-secret-input');
            let nameHelp = $('#new-app-name-help');
            let keyHelp = $('#new-app-key-help');
            let secretHelp = $('#new-app-secret-help');

            formModal.addClass('is-active');
            $('.new-app-modal-close').click(function () {
                formModal.removeClass('is-active');
            });

            nameInput.keypress(function () {
                nameInput.removeClass('is-danger');
                nameHelp.html('');
                nameHelp.removeClass('is-danger');
            });

            keyInput.keypress(function () {
                keyInput.removeClass('is-danger');
                keyHelp.html('');
                keyHelp.removeClass('is-danger');
            });

            secretInput.keypress(function () {
                secretInput.removeClass('is-danger');
                secretHelp.html('');
                secretHelp.removeClass('is-danger');
            });

            $('#new-app-save-modal').click(function () {
                if (!nameInput.val()) {
                    nameInput.addClass('is-danger');
                    nameHelp.addClass('is-danger');
                    nameHelp.html('Missing a Name.');
                } else if (!keyInput.val()) {
                    keyInput.addClass('is-danger');
                    keyHelp.addClass('is-danger');
                    keyHelp.html('Missing a Consumer Key.');
                } else if (!secretInput.val()) {
                    secretInput.addClass('is-danger');
                    secretHelp.addClass('is-danger');
                    secretHelp.html('Missing a Consumer Secret.');
                } else {
                    let req = {
                        'action': 'add_app',
                        'app_name': nameInput.val(),
                        'consumer_key': keyInput.val(),
                        'consumer_secret': secretInput.val()
                    };

                    $.ajax({
                        type: "POST",
                        beforeSend: function(request) {
                            request.setRequestHeader('Content-Type', 'application/json');
                        },
                        url: "/api/config",
                        data: JSON.stringify(req),
                        processData: false,
                        success: function(data) {
                            data = JSON.parse(data);

                            if (data.message && data.code === 200) {
                                formModal.removeClass('is-active');
                                location.reload();
                            } else {
                                console.log('Something went wrong!');
                                console.log(data);
                            }
                        }
                    });
                }
            });
       });
   });
});