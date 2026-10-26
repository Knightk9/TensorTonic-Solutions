def build_expression_graph(leaves: list, operations: list) -> tuple:
    nodes = []
    # Dùng dictionary để tra cứu nhanh giá trị (data) của các node đã tạo
    data_map = {} 
    
    final_id = None

    # 1. Xử lý Leaves trước (đúng thứ tự đầu vào)
    for leaf in leaves:
        node = {
            "id": leaf["id"],
            "data": float(leaf["data"]),
            "grad": 0.0,
            "op": "",
            "parents": []
        }
        nodes.append(node)
        data_map[leaf["id"]] = node["data"]
        final_id = leaf["id"]

    for op in operations:
        left_val = data_map[op["left"]]
        right_val = data_map[op["right"]]
        
        if op["op"] == "+":
            val = left_val + right_val
        elif op["op"] == "*":
            val = left_val * right_val
            
        node = {
            "id": op["id"],
            "data": float(val),
            "grad": 0.0,
            "op": op["op"],
            "parents": [op["left"], op["right"]]
        }
        nodes.append(node)
        data_map[op["id"]] = node["data"]
        final_id = op["id"]

    return (nodes, final_id)

