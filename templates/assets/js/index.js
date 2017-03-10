// Index Pgae
function notify_radarr(announcement_id) {
    console.log("Notifying radarr again for announcement: " + announcement_id);
    
    alite({
            url: '/radarr/notify',
            method: 'POST',
            data: {
                id: announcement_id
            },
        }).then(function (result) {
            console.log('radarr_notify result: ', result);
            if (result == 'ERR') {
                // radarr rejected the announcement
                toastr.error("radarr still declined this torrent...");
            } else {
                // radarr accepted the announcement
                toastr.success("radarr approved the torrent this time!");
            }
        }).catch(function (err) {
            console.error('radarr_notify error: ', err);
            toastr.error("Error notfying radarr of this announcement??");
        });  
}