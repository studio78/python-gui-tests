class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()

    def delete_group_by_name(self, name):
        self.open_group_editor()
        # тут не понятно как найти элемент, по какому аттрибуту
        # self.group_editor.window(title=name).click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.group_delete = self.app.application.window(title="Delete group")
        self.group_delete.wait("visible")
        self.group_delete.window(auto_id="uxOKAddressButton").click()
        self.group_editor.window(auto_id="uxCloseAddressButton").click()

    def delete_group_by_index(self, index):
        self.open_group_editor()
        # elements = self.group_editor.window(control_type="UIA_TreeItemControlTypeId")
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        groups = root.children()
        groups[index].click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.group_delete = self.app.application.window(title="Delete group")
        self.group_delete.wait("visible")
        self.group_delete.window(auto_id="uxOKAddressButton").click()
        self.group_editor.window(auto_id="uxCloseAddressButton").click()