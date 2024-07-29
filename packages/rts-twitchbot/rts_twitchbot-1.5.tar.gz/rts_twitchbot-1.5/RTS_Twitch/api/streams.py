from ExtraDecorators import validatetyping
from RTS_Twitch.toolset import paginate, single
from ExtraUtils.validate_dict import validate_dict

@validatetyping
async def get_stream_keys(channel_id:int)->dict:
    '''{
      "stream_key": "live_12345678_abcdefgh",
    }'''
    url= f"https://api.twitch.tv/helix/streams/key?broadcaster_id={channel_id}"
    return await single(channel_id,url)

@validatetyping
async def get_streams(channel_id:int,user_ids:list=[])->dict:
    '''[{
      "id": "26007494656",
      "user_id": "23161357",
      "user_name": "LIRIK",
      "game_id": "509670",
      "type": "live",
      "title": "HeyGuys",
      "viewer_count": 9001,
      "started_at": "2018-03-20T15:00:00Z",
      "language": "en",
      "thumbnail_url": "https://link/to/thumbnail.jpg",
      "tag_ids": [
        "6ea6bca4-4712-4ab9-a906-e3336a9d8039"
      ]
    },
    ...
    ]'''
    appender = "?user_id="+channel_id
    if user_ids:
        for user_id in user_ids:
            appender += f"&user_id={user_id}"
    

    url= f"https://api.twitch.tv/helix/streams?"+appender
    return await paginate(channel_id,url)

@validatetyping
async def get_followed_streams(channel_id:int,first:int=20)->dict:
    '''[{
      "id": "26007494656",
      "user_id": "23161357",
      "user_name": "LIRIK",
      "game_id": "509670",
      "type": "live",
      "title": "HeyGuys",
      "viewer_count": 9001,
      "started_at": "2018-03-20T15:00:00Z",
      "language": "en",
      "thumbnail_url": "https://link/to/thumbnail.jpg",
      "tag_ids": [
        "6ea6bca4-4712-4ab9-a906-e3336a9d8039"
      ]
    },
    ...
    ]'''
    url= f"https://api.twitch.tv/helix/streams/followed?user_id={channel_id}&first={first}"
    return await paginate(channel_id,url)

# missing create_stream_marker
# missing get_stream_markers