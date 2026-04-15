from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: float


item = Item(id=1, name="苹果", price=3.5)
# 序列化
# 对象转字典
obj1 = item.model_dump()
print("obj1:", obj1)
print(f"obj1 type: {type(obj1)}")

# 对象转JSON字符串
obj2 = item.model_dump_json()

print("obj2:", obj2)
print(f"obj2 type: {type(obj2)}")

# 排除/包含字段
print(item.model_dump(exclude={"price"}))  # 排除price
print(item.model_dump(include={"id", "name"}))  # 只包含id和name

# 反序列化
json_str = '{"id": 2, "name": "香蕉", "price": 2.5}'
# JSON字符串 -> Item对象
item2 = Item.model_validate_json(json_str)
print(f"item2: {item2}")
print(f"type(item2): {type(item2)}")

data_dict = {"id": 3, "name": "橙子", "price": 4.0}
# 从字典 -> Item对象
item3 = Item.model_validate(data_dict)
print(f"item3: {item3}")
print(f"type(item3): {type(item3)}")

# Model.model_json_schema()
model_json_schema = Item.model_json_schema()
print(model_json_schema)
print(f"type: {type(model_json_schema)}")
# {
#     "properties": {
#         "id": {"title": "Id", "type": "integer"},
#         "name": {"title": "Name", "type": "string"},
#         "price": {"title": "Price", "type": "number"},
#     },
#     "required": ["id", "name", "price"],
#     "title": "Item",
#     "type": "object",
# }
