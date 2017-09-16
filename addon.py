# # -*- coding: utf-8 -*-

# from resources.lib import kodilogging
# from resources.lib import plugin

# import logging
# import xbmcaddon

# # Keep this file to a minimum, as Kodi
# # doesn't keep a compiled copy of this
# ADDON = xbmcaddon.Addon()
# kodilogging.config()

# plugin.run()


# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
# http://cdn.emasti.pk/images/stories/movies/ind/Jab-Harry-Met-Sejal-2017.jpg


VIDEOS = {'Indian Movies': [{'name': 'Jab Harry Met Sejal',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Jab-Harry-Met-Sejal-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/I-J/Jab-Harry-Met-Sejal-2017-WEBRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Half GirlFriend',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Half-Girlfriend-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/G-H/Half-Girlfriend-2017-DTHRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Behan Hogi Teri',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Behen-Hogi-Teri-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/A-B/Behen-Hogi-Teri-2017-DTHRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Guest in London',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Guest-iin-London-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/G-H/Guest-iin-London-2017-DVDRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Baadshaho (2017)',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Baadshaho-2017.jpg',
                       'video': 'http://ndl2.emasti.pk/ind/A-B/Baadshaho-2017-PDVDRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Toilet Ek Prem Katha',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Toilet-Ek-Prem-Katha-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/S-T/Toilet-Ek-Prem-Katha-2017-DVDScr.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Poorna (2017)',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Poorna-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/O-P/Poorna-2017-HDRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Bareilly Ki Barfi (2017)',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Bareilly-Ki-Barfi-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/A-B/Bareilly-Ki-Barfi-2017-PDVDRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Sweetiee Weds NRI (2017)',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Sweetiee-weds-NRI-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/S-T/Sweetiee-Weds-NRI-2017-HDTVRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Bank Chor (2017)',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Bank-Chor-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/A-B/Bank-Chor-2017-DVDRip.mkv',
                       'genre': 'Indian Movies'},
                      {'name': 'Munna Michael (2017)',
                       'thumb': 'http://cdn.emasti.pk/images/stories/movies/ind/Munna-Michael-2017.jpg',
                       'video': 'http://dm01.emasti.pk/ind/M-N/Munna-Michael-2017-DVDScr.mkv',
                       'genre': 'Indian Movies'}
                      ],
            'English Movies': [{'name': 'Gun Shy (2017)',
                      'thumb': 'http://cdn.emasti.pk/images/stories/movies/eng/Gun-Shy-2017.jpg',
                      'video': 'http://ndl2.emasti.pk/eng/G-H/Gun-Shy-2017-WEBRip.mkv',
                      'genre': 'English Movies'},
                     {'name': 'All I Need (2016)',
                      'thumb': 'http://cdn.emasti.pk/images/stories/movies/eng/All-i-Need-2016.jpg',
                      'video': 'http://cdn01.emasti.pk/eng/A-B/All-i-Need-2016-BRRip.mp4',
                      'genre': 'English Movies'},
                     {'name': 'The Basement (2017)',
                      'thumb': 'http://cdn.emasti.pk/images/stories/movies/eng/The-Basement-2017.jpg',
                      'video': 'http://ndl2.emasti.pk/eng/A-B/The-Basement-2017-WEBRip.mkv',
                      'genre': 'English Movies'}
                     ],
            'Dubbed Movies': [{'name': 'Hits Man Body Guard Hindi(Dubbed)',
                      'thumb': 'http://cdn.emasti.pk/images/stories/movies/eng/The-Hitmans-Bodyguard-2017.jpg',
                      'video': 'http://ndl2.emasti.pk/engurd/The-Hitmans-Bodyguard-2017-Hindi-HDRip.mpg',
                      'genre': 'Dubbed Movies'},
                     {'name': 'The Mummy (Dual Audio) (2017)',
                      'thumb': 'http://cdn.emasti.pk/images/stories/movies/eng/The-Mummy-2017.jpg',
                      'video': 'http://dm01.emasti.pk/engurd/The-Mummy-2017-BRRip-Hindi-Eng.mkv',
                      'genre': 'Dubbed Movies'},
                     {'name': 'Kingsman: The Secret Service (Dual Audio) (2014)',
                      'thumb': 'http://cdn.emasti.pk//images/stories/movies/eng/kingsman.jpg',
                      'video': 'http://ndl2.emasti.pk/engurd/Kingsman-The-Secret-Service-2014-BRRip-Eng-Hindi.mkv',
                      'genre': 'Dubbed Movies'}
                     ],
                'TV SHOWS': [{'name': 'WWE Monday Night RAW (9/sept/2017)',
                      'thumb': 'http://cdn.emasti.pk//images/stories/raw111.jpg',
                      'video': 'http://cdn01.emasti.pk/wwe/raw/RAW-9th-September-2017-HDTv.mp4',
                      'genre': 'TV SHOWS'},
                     {'name': 'Smackdown Live (6/5/2017)',
                      'thumb': 'http://cdn.emasti.pk//images/stories/Smackdown.jpg',
                      'video': 'http://ndl2.emasti.pk/tv/wwe/smackdown/Smackdown-Live-5th-September-2017-HDTv.mp4',
                      'genre': 'TV SHOWS'},
                     {'name': 'WWE Main Event (8/sept/2017)',
                      'thumb': 'http://cdn.emasti.pk//images/stories/WWEMainEvent.jpg',
                      'video': 'http://ndl3.emasti.pk/tv/wwe/mainevent/Main-Event-8th-September-2017-HDTv.mp4',
                      'genre': 'TV SHOWS'}
                     ],
            'Live Tv': [{'name': 'News One',
                      'thumb': 'http://www.freeetv.com/images/02_logo/news_one_pakistan.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=e-hAh7d3STY',
                      'genre': 'Live Tv'},
                     {'name': 'Samaa',
                      'thumb': 'https://www.samaa.tv/live/images/Samaa-Live.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=Wyq6YeoM2ZA',
                      'genre': 'Live Tv'},
                     {'name': 'Geo News',
                      'thumb': 'https://pbs.twimg.com/profile_images/832991740961386498/jNVc_ulo.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=e1XD1pEAjNA',
                      'genre': 'Live Tv'},
                     {'name': 'Ary News',
                      'thumb': 'https://en.dailypakistan.com.pk/wp-content/uploads/2017/01/ARY-GEO-LEGAL-BATTLE.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=WAeLTNhvG1E',
                      'genre': 'Live Tv'},
                     {'name': 'Bol News',
                      'thumb': 'https://i.ytimg.com/vi/9Uw2IWEsDOs/hqdefault.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=iupxBJ5Cv1w',
                      'genre': 'Live Tv'},
                     {'name': 'Din News',
                      'thumb': 'http://www.customercarepk.com/wp-content/uploads/2016/07/Din-News-300x155.png',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=TWy1bG17A7E',
                      'genre': 'Live Tv'},
                     {'name': '92 News',
                      'thumb': 'http://poll.com.pk/img/polls/10801_10704-Channel-92-News-Live-Streaming-HD.png.png',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=8F2UHHBpMeE',
                      'genre': 'Live Tv'},
                     {'name': "Saudi 2 live Stream",
                      'thumb': 'http://www.livetvswatch.com/thumb/uploads/saudi-ksa-2-tv-live-from-saudi-arabia.png',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=16Dc_D0QutU',
                      'genre': 'Live Tv'},
                     {'name': "Holy Quran live Stream",
                      'thumb': 'https://i0.wp.com/zubifun.net/wp-content/uploads/2017/05/Quran-TV-Live-TV-Saudi-Arabia.jpeg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=RoMrU9fQp9k',
                      'genre': 'Live Tv'},
                     {'name': "Ptv Sports Live",
                      'thumb': 'http://sports.ptv.com.pk/public/user/assets/images/LivestreamSports.jpg',
                      'video': 'plugin://plugin.video.youtube/play/?video_id=eC1-7ynTnGA',
                      'genre': 'Live Tv'},
                     {'name': "BT Sports Live",
                      'thumb': 'https://www.thelogodb.com/images/media/logo/vsuvvu1433963716.png',
                      'video': 'http://wowza2.mysoltv.com:1992/BT_Sports_3_HD/index.m3u8',
                      'genre': 'Live Tv'},
                     {'name': "BBC 1 HD",
                      'thumb': 'https://upload.wikimedia.org/wikipedia/commons/1/1a/BBC_One_2002.png',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23734.ts',
                      'genre': 'Live Tv'},
                     {'name': "Comedy Central HD",
                      'thumb': 'https://static.telus.com/common/cms/images/tv/satellite/new-channel-logos/TheComedyNetworkHDEast.png',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23725.ts',
                      'genre': 'Live Tv'},
                     {'name': "Film 4 HD",
                      'thumb': 'http://cdn.playbuzz.com/cdn/37d7914b-ba72-452e-ad14-28ac35d2962c/4a04e622-3d58-48bc-a079-e820bcc4e3d1.jpg',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23720.ts',
                      'genre': 'Live Tv'},
                     {'name': "Sky Sports 1F HD",
                      'thumb': 'http://e1.365dm.com/11/11/660x350/f1panel1_2682703.jpg',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23749.ts',
                      'genre': 'Live Tv'},
                     {'name': "Sky Movies Thriller HD",
                      'thumb': 'http://www.tsihosting.co.uk/ontvnow/wp-content/uploads/sites/4/2013/10/Sky-Movies-logo.jpg',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23761.ts',
                      'genre': 'Live Tv'},
                     {'name': "Sky Sports MIX HD",
                      'thumb': 'http://ksassets.timeincuk.net/wp/uploads/sites/54/2016/03/sky-sports-mix-1.jpg',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23748.ts',
                      'genre': 'Live Tv'},
                     {'name': "Sony Tv HD",
                      'thumb': 'http://tvcric.site/wp-content/uploads/2014/05/Sony-TV-Live-Streaming-HD.jpg',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23825.ts',
                      'genre': 'Live Tv'},
                     {'name': "Live OK",
                      'thumb': 'http://www.dafont.com/forum/attach/orig/2/7/275662.jpg',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23821.ts',
                      'genre': 'Live Tv'},
                     {'name': "Star Plus",
                      'thumb': 'https://upload.wikimedia.org/wikipedia/commons/5/52/Star_Plus_Logo.jpg',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23820.ts',
                      'genre': 'Live Tv'},
                     {'name': "Star Utsav",
                      'thumb': 'https://i.ytimg.com/vi/Ms9e1BhNXz0/maxresdefault.jpg',
                      'video': 'http://no1dadicated.tk:8000/live/cuda/cuda/23819.ts',
                      'genre': 'Live Tv'}
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.
    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.
    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.
    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.
    :return: The list of video categories
    :rtype: list
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.
    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.
    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.
    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.
    :param category: Category name
    :type category: str
    """
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.
    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring
    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])