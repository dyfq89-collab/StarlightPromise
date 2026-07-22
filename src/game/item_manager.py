class ItemManager:


    def __init__(self):

        self.items = {


            "old_letter":
            {
                "name":"旧信件",
                "description":
                "一封写满回忆的信。"
            },


            "star_fragment":
            {
                "name":"星光碎片",
                "description":
                "闪耀着光芒的神秘碎片。"
            },


            "birthday_card":
            {
                "name":"生日卡片",
                "description":
                "准备送出的生日祝福。"
            }


        }



class ItemManager:


    def __init__(self):

        self.items = {

            ...

        }



    def get_item(self,item_id):

        return self.items.get(
            item_id
        )



    def add_item(self,item_id):

        if item_id in self.items:

            return self.items[item_id]

        return None



    def remove_item(self,item_id):

        if item_id in self.items:

            del self.items[item_id]

            return True

        return False
