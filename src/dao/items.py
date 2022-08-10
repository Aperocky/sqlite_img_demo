from sqlitedao import TableItem


class Image(TableItem):

    TABLE_NAME = "images"
    INDEX_KEYS = ["ref"]
    ALL_COLUMNS = {
        "ref": str
    }

    def __init__(self, row_tuple=None, **kwargs):
        super().__init__(row_tuple, **kwargs)
        self.load_tuple()

    def load_tuple(self):
        self.ref = self.row_tuple["ref"]


class User(TableItem):

    TABLE_NAME = "users"
    INDEX_KEYS = ["user_id"]
    ALL_COLUMNS = {
        "user_id": str,
        "completed": int,
    }

    def __init__(self, row_tuple=None, **kwargs):
        super().__init__(row_tuple, **kwargs)
        self.load_tuple()

    def complete(self, completed=True):
        self.row_tuple["completed"] = 1
        self.completed = True

    def load_tuple(self):
        self.user_id = self.row_tuple["user_id"]
        self.completed = bool(self.row_tuple["completed"])


class UserImage(TableItem):

    TABLE_NAME = "user_images"
    INDEX_KEYS = ["pair_id"]
    ALL_COLUMNS = {
        "pair_id": str,
        "user_id": str,
        "ref": str,
        "score": int
    }

    def __init__(self, row_tuple=None, **kwargs):
        super().__init__(row_tuple, **kwargs)
        self.load_tuple()

    def score_result(self, score):
        self.score = score
        self.row_tuple["score"] = score

    def load_tuple(self):
        self.pair_id = self.row_tuple["pair_id"]
        self.user_id = self.row_tuple["user_id"]
        self.ref = self.row_tuple["ref"]
        self.score = self.row_tuple["score"]
