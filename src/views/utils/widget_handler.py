
class WidgetHandler():
    @staticmethod
    def find_widgets_by_class(parent_widget, widget_object,class_name):
        results = []
        for widget in parent_widget.findChildren(widget_object):
            if widget.property("class") and class_name in widget.property("class"):
                classes = widget.property("class").split(" ")
                for _class in classes:
                    if _class == class_name:
                        results.append(widget)
        return results
    @staticmethod
    def find_widget_by_id(parent_widget, widget_object, id):
        return parent_widget.findChild(widget_object, id)
    @staticmethod
    def add_class(widget, class_name):
        _class = widget.property("class")
        _class += f" {class_name}"
        widget.setProperty("class", _class)
    @staticmethod
    def remove_class(widget, class_name): 
        _class = widget.property("class")
        _class = _class.replace(f" {class_name}", "")
        widget.setProperty("class", _class)
