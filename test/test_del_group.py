import random


def test_delete_some_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group("test group %s" % str(random.randint(1000, 9999)))
    old_groups = app.groups.get_group_list()
    group_index = random.randint(0, len(old_groups)-1)
    app.groups.delete_group_by_index(group_index)
    new_groups = app.groups.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    del old_groups[group_index]
    assert old_groups == new_groups
