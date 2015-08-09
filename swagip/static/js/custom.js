//Supply the command minus the url (i.e. 'wget -qO - ') and supply 'this'
function setHeaderTable(command, element) {
    //Make the clicked nav link active
    $('#headerTableNav').find('li.active').removeClass('active');
    $(element).addClass('active');

    //Change the header
    $('#headerTable thead tr th.key').html('Command:');

    //Change the rows
    $('#headerTable > tbody > tr > td.key').each(function () {

        var rowKey = $(this).html();

        if (rowKey.match(/Content-Length/i)) {
            $(this).html(command + ' ip.swagger.pro/content-length');
        }
        else if (rowKey.match(/Accept-Language/i)) {
            $(this).html(command + ' ip.swagger.pro/accept-language');
        }
        else if (rowKey.match(/Accept-Encoding/i)) {
            $(this).html(command + ' ip.swagger.pro/accept-encoding');
        }
        else if (rowKey.match(/Host/i)) {
            $(this).html(command + ' ip.swagger.pro/host');
        }
        else if (rowKey.match(/Accept/i)) {
            $(this).html(command + ' ip.swagger.pro/accept');
        }
        else if (rowKey.match(/Upgrade-Insecure-Requests/i)) {
            $(this).html(command + ' ip.swagger.pro/upgrade-insecure-requests');
        }
        else if (rowKey.match(/Connection/i)) {
            $(this).html(command + ' ip.swagger.pro/connection');
        }
        else if (rowKey.match(/Referer/i)) {
            $(this).html(command + ' ip.swagger.pro/referer');
        }
        else if (rowKey.match(/Cache-Control/i)) {
            $(this).html(command + ' ip.swagger.pro/cache-control');
        }
        else if (rowKey.match(/Source-Port/i)) {
            $(this).html(command + ' ip.swagger.pro/source-port');
        }
        else if (rowKey.match(/User-Agent/i)) {
            $(this).html(command + ' ip.swagger.pro/user-agent');
        }
        else if (rowKey.match(/Content-Type/i)) {
            $(this).html(command + ' ip.swagger.pro/content-type');
        }
        else {
            $(this).html(command + ' ip.swagger.pro');
        }
    });
}

// Supply 'this'
function resetHeaderTable(element) {
    //Make the clicked nav link active
    $('#headerTableNav').find('li.active').removeClass('active');
    $(element).addClass('active');
    //Change the header
    $('#headerTable thead tr th.key').html('Item:');

    //Change the rows
    $('#headerTable > tbody > tr > td.key').each(function () {

        var rowKey = $(this).html();

        if (rowKey.match(/Content-Length/i)) {
            $(this).html('Content-Length');
        }
        else if (rowKey.match(/Accept-Language/i)) {
            $(this).html('Accept-Language');
        }
        else if (rowKey.match(/Accept-Encoding/i)) {
            $(this).html('Accept-Encoding');
        }
        else if (rowKey.match(/Host/i)) {
            $(this).html('Host');
        }
        else if (rowKey.match(/Accept/i)) {
            $(this).html('Accept');
        }
        else if (rowKey.match(/Upgrade-Insecure-Requests/i)) {
            $(this).html('Upgrade-Insecure-Requests');
        }
        else if (rowKey.match(/Connection/i)) {
            $(this).html('Connection');
        }
        else if (rowKey.match(/Referer/i)) {
            $(this).html('Referer');
        }
        else if (rowKey.match(/Cache-Control/i)) {
            $(this).html('Cache-Control');
        }
        else if (rowKey.match(/Source-Port/i)) {
            $(this).html('Source-Port');
        }
        else if (rowKey.match(/User-Agent/i)) {
            $(this).html('User-Agent');
        }
        else if (rowKey.match(/Content-Type/i)) {
            $(this).html('Content-Type');
        }
        else {
            $(this).html('Source-IP');
        }
    });
}

$(document).ready(function () {

    $('#browser').on('click', function (e) {
        resetHeaderTable(this);
        return false;
    });

    $('#wget').on('click', function (e) {
        setHeaderTable('wget -qO -', this);
        return false;
    });

    $('#curl').on('click', function (e) {
        setHeaderTable('curl', this);
        return false;
    });

    $('#fetch').on('click', function (e) {
        setHeaderTable('fetch -qo -', this);
        return false;
    });
});