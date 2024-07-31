from common.autotest.handle_allure import allure_title, allure_sub_suite, allure_severity, allure_tag, allure_suite, \
    allure_link, allure_story, allure_feature,allure_step

class AllurePlugin(object):
    @staticmethod
    def allure_title(cls, title: str) -> None:
        """allure中显示的用例标题"""
        allure_title(title)

    @staticmethod
    def allure_feature(cls, feature: str) -> None:
        """allure中显示的用例模块"""
        allure_feature(feature)

    @staticmethod
    def allure_story(cls,story: str) -> None:
        """allure中显示的用例模块"""
        allure_story(story)

    @staticmethod
    def allure_link(cls, _link: str, _name=None) -> None:
        """allure中显示的用例模块"""
        allure_link(url=_link, name=_name)

    @staticmethod
    def allure_suite(cls, _name: str) -> None:
        """allure中显示的用例模块"""
        allure_suite(_name)

    @staticmethod
    def allure_tag(cls, _name: str) -> None:
        """allure中显示的用例模块"""
        allure_tag(_name)

    @staticmethod
    def allure_sub_suite(cls, _name: str) -> None:
        """allure中显示的用例模块"""
        allure_sub_suite(_name)

    @staticmethod
    def allure_severity(cls,severity_level: str) -> None:
        """allure中显示的用例等级"""
        allure_severity(severity_level)

    @staticmethod
    def allure_step(cls, step: str, content: str)-> None:
        """allure打印步骤信息"""
        allure_step(step, content)