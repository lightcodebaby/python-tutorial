categories = []


category_ids = "select id from category"
run("insert into category_closure (ancestor_id, descendant_id) values (category_ids, category_ids)")
for category in categories:
    parent = category["parent"]
    while parent != None:
        run("insert into category_closure (ancestor_id, descendant_id) values (parent, category)")
        parent = get_parent(parent)


