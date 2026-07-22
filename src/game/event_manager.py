class EventManager:


    def __init__(self):

self.events = {

    "old_letter_found":
    "你发现了一封旧信件，里面记录着重要的回忆。",


    "forest_secret":
    "你发现森林深处隐藏的星光碎片。",


    "final":
    "所有回忆汇聚成星光。",


    "find_letter":
    "你发现了一封旧信件！\n任务完成！",


    "open_box":
    "你打开宝箱，里面放着一枚闪耀的星星碎片。",


    "look_star":
    "窗外的星光照亮了你的回忆。"

}



    def trigger(self,event):

        return self.events.get(
            event,
             "这里什么也没有发生。"
        )
