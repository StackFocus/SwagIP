//Supply the command minus the url (i.e. 'wget -qO - ') and supply 'this'
function setHeaderTable(command, element) {

    //Reset to defaults
    resetHeaderTable(element);

    //Change the table header
    $('#headerTable thead tr th.key').html('Command:');

    //Change the rows
    $('#headerTable > tbody > tr > td.key').each(function () {

        var rowKey = $(this).html();

        if (rowKey.match(/json/i)) {
            $(this).html(command + HOSTNAME + '/all');
        }
        else if (rowKey.match(/source-ip/i)) {
            $(this).html(command + HOSTNAME + '/');
        }
        else {
            $(this).html(command + HOSTNAME + '/' + rowKey.toLowerCase());
        }
    });
}

// Supply 'this'
function resetHeaderTable(element) {

    //Make the clicked nav link active
    $('#headerTableNav').find('li.active').removeClass('active');
    $(element).addClass('active');

    //Change the table header
    $('#headerTable thead tr th.key').html('Item:');

    //Set the rows to default
    $('#headerTable > tbody > tr > td.key').each(function () {

        if (($(this).html()).match(/(.*)[\/]$/i)) {
            $(this).html('source-ip');
        }
        else if (($(this).html()).match(/(.*)[\/]all$/i)) {
            $(this).html('JSON');
        }
        else {
            $(this).html(($(this).html()).replace(/(.*)[\/]/i, ''));
        }
    });
}

$(document).ready(function () {

    $('#browser').on('click', function (e) {
        resetHeaderTable(this);
        return false;
    });

    $('#wget').on('click', function (e) {
        setHeaderTable('wget -qO - ', this);
        return false;
    });

    $('#curl').on('click', function (e) {
        setHeaderTable('curl ', this);
        return false;
    });

    $('#fetch').on('click', function (e) {
        setHeaderTable('fetch -qo - ', this);
        return false;
    });

    $('#powershell').on('click', function (e) {
        setHeaderTable('Invoke-RestMethod -URI http://', this);
        return false;
    });
});
