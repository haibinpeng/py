# 作者: Michael(phb)
# 2023年04月16日17时10分59秒

from pymongo import MongoClient


class TestMongo:
    # 实例化client，建立连接
    def __init__(self):
        client = MongoClient(host="192.168.1.111", port=27017)
        self.collection = client["test2"]["stu1"]

    # 插入一条数据，我们可以自己指定id，不指定就是自动生成
    def test_insert(self):
        ret1 = self.collection.insert({"_id": 1001, "name": "xiaowang", "age": 10})
        print(ret1)

    # 插入多条数据
    def test_insert_many(self):
        data_list = [{"name": "test{}".format(i)} for i in range(10)]
        print(data_list)
        self.collection.insert_many(data_list)

    # 查询一个记录
    def find_one(self):
        t = self.collection.find_one({"name": "xiaowang"})
        print(t)

    # 查询所有记录
    def find_many(self):
        t = self.collection.find({"gender": True})  # 如果要查true和false，要写为python True和False
        print(t)
        print(list(t))
        # 查询出来的结果t内含有游标，遍历到最后以后，再次遍历不会有输出
        # for i in t:
        #     print(i)

        for j in t:
            print(j, "*" * 100)

        print(list(t))

    def try_update_one(self):
        # update_ one更新一条数据
        self.collection.update_one({"name": "xiaowang"}, {"$set": {"name": "new_test200"}})

    def try_update_many(self):
        # update_ one 更新全部数据
        self.collection.update_many({"age": 25}, {"$set": {"age": 20}})

    def try_delete_one(self):
        # delete_ one删除一条数据
        self.collection.delete_one({"name": "test1"})

    def try_delete_many(self):
        # delete_ may删除所有满足条件的数据,真正
        ret = self.collection.delete_many({"name": {"$regex": "^test"}})
        print(ret)

    # 查询所有记录
    def find_many_regex(self):
        t = self.collection.find({"name": {'$regex': "^x"}})
        print(t)
        print(list(t))


if __name__ == "__main__":
    testMongo = TestMongo()
    # testMongo.find_many()
    # testMongo.test_insert()
    # testMongo.test_insert_many()
    # testMongo.try_update_one()
    # testMongo.try_update_many()
    # testMongo.try_delete_one()
    # testMongo.find_many_regex()
    # testMongo.try_delete_many()
    testMongo.find_many_regex()
