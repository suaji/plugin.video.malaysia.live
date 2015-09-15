import xbmcgui,xbmcplugin 
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty( "Fanart_Image", img )
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

icondir = xbmc.translatePath("special://home/addons/plugin.video.malaysia.live/icons/")

add_video_item('http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch001.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1442372680&myTokenPrefixhash=Yw0lWZxbeYG1AUCiIh0nCeb_TkFVyV9L3VE7QWJ9SkM=',{ 'title': 'TV 1'},img = icondir + 'tv1.png')
add_video_item('http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch003.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1442373088&myTokenPrefixhash=Qw5ICPXwhqxgoqiFo_0piBFDL9TugqnF9p99cgB3DEA=',{ 'title': 'TV 2'},img = icondir + 'tv2.png')
add_video_item('http://tv3liveios-i.akamaihd.net/hls/live/205900/ios/tv3live/master.m3u8',{ 'title': 'TV3'},img = icondir + 'tv3.png')
add_video_item('http://ntv7liveios-i.akamaihd.net/hls/live/205902/ios/ntv7live/master.m3u8',{ 'title': 'NTV7'},img = icondir + 'tv7.png')
add_video_item('http://8tvliveios-i.akamaihd.net/hls/live/205901/ios/8tvlive/master.m3u8',{ 'title': '8TV'},img = icondir + 'tv8.png')
add_video_item('http://tv9liveios-i.akamaihd.net/hls/live/205903/ios/tv9live/master.m3u8',{ 'title': 'TV9'},img = icondir + 'tv9.png')
add_video_item('http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch005.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1442373378&myTokenPrefixhash=G_RfIYAEJi1qaWTUXgdrbxPYuaPvj2qxKzaFgrIL09Y=',{ 'title': 'TVi'},img = icondir + 'tvi.png')
add_video_item('http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch006.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1442373506&myTokenPrefixhash=tbZEUxlij5AgrrqWJcx_jE54gJjjShbE7Vc27slt1x4=',{ 'title': 'Muzik Aktif'},img = icondir + 'muzik.png')
add_video_item('http://d22b8vh21p20bg.cloudfront.net/mylive/smil:bernama2_all.smil/playlist.m3u8',{ 'title': 'Bernama TV'},img = icondir + 'bern.png')
add_video_item('http://livestreaming-1528489630.ap-southeast-1.elb.amazonaws.com/liveedge/smil:rtm-ch020.smil/playlist.m3u8?myTokenPrefixstarttime=0&myTokenPrefixendtime=1442373548&myTokenPrefixhash=sg2_9TkkavLAHe-sv6hnSfdV8IFaFlwCSQ0PckYMbas=',{ 'title': '1 news'},img = icondir + '1news.png')

xbmcplugin.endOfDirectory(plugin_handle)



















