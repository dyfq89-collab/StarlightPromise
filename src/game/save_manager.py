import json



class SaveManager:


    def __init__(self):

        self.file_name = "save.json"



    def save(self,data):

        with open(
            self.file_name,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )



    def load(self):

        try:

            with open(
                self.file_name,
                "r",
                encoding="utf-8"
            ) as f:

                return json.load(f)


        except:

            return {}
