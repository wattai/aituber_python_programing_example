import os

from aituber.obs_adapter import OBSAdapter
from aituber.voicevox_adapter import VoicevoxAdapter
from aituber.openai_adapter import OpenAIAdapter
from aituber.youtube_comment_adapter import YoutubeCommentAdapter
from aituber.play_sound import PlaySound
from dotenv import load_dotenv

load_dotenv()


class AITuberSystem:
    def __init__(self) -> None:
        video_id = os.getenv("YOUTUBE_VIDEO_ID")
        self.youtube_comment_adapter = YoutubeCommentAdapter(video_id)
        self.openai_adapter = OpenAIAdapter()
        self.voice_adapter = VoicevoxAdapter()
        self.obs_adapter = OBSAdapter()
        self.play_sound = PlaySound(output_device_name="CABLE Input")
        pass

    def talk_with_comment(self) -> bool:
        print("コメントを読み込みます…")
        comment = self.youtube_comment_adapter.get_comment()
        if comment is None:
            print("コメントがありませんでした。")
            return False
        response_text = self.openai_adapter.create_chat(comment)
        data, rate = self.voice_adapter.get_voice(response_text)
        self.obs_adapter.set_question(comment)
        self.obs_adapter.set_answer(response_text)
        self.play_sound.play_sound(data, rate)
        return True
