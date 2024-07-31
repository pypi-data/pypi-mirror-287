from loguru import logger
from common.common.constant import Constant
from common.data.handle_common import get_system_key,set_system_key,print_debug
from common.plat.mysql_platform import MysqlPlatForm
from common.data.data_process import DataProcess
from common.plat.service_platform import ServicePlatForm



class ATFPlatForm(object):

    @classmethod
    def getCycleByResult(self,  restult: str = "'通过','未执行','失败','自动化执行'"):
        _list = []
        if DataProcess.isNotNull(get_system_key(Constant.TEST_SRTCYCLE_ID)):
            _list = MysqlPlatForm.get_test_autotest_run(get_system_key(Constant.ISSUE_KEY),
                                                         get_system_key(Constant.TEST_SRTCYCLE_ID),
                                                         restult)
        return _list

    @classmethod
    def getCaseNameByCycle(self, restult: str = "'通过','未执行','失败','自动化执行'"):
        """
        获取用例列表
        """
        case_name_list = []
        count = 7
        temp = 1
        while temp <= count:
            case_name_list = ATFPlatForm.getCycleByResult(restult)
            if DataProcess.isNotNull(case_name_list):
                temp = 10
            else:
                temp = temp + 1
        if DataProcess.isNotNull(case_name_list):
            case_name_list_str = ""
            for temp in case_name_list:
                case_name_list_str = case_name_list_str + temp['casename'] + ";"
            logger.info(f"获取满足条件【{restult}】测试用例:" + case_name_list_str)
            return case_name_list
        else:
            logger.warning(f"获取满足条件【{restult}】测试用例:空")
            return case_name_list

    @classmethod
    def getCaseNameList(self):
        """
        获取用例列表
        """
        case_name_list = []
        if DataProcess.isNotNull(get_system_key('Result')):
            case_name_list = ATFPlatForm.getCaseNameByCycle(get_system_key('Result'))
        else:
            case_name_list = ATFPlatForm.getCaseNameByCycle()
        if DataProcess.isNotNull(case_name_list):
            from common.plugin.pytest_plugin import PytestPlugin
            PytestPlugin.initRunCyleCase()
            return case_name_list
        else:
            return case_name_list


    @classmethod
    def sent_result_byCaseName(self, CaseName, CaseID, result, comment):
        if DataProcess.isNotNull(get_system_key(Constant.TEST_SRTCYCLE_ID)):
            _runid = self.getCaseRun(CaseID, CaseName)['caserunid']
            if _runid != '00000':
                ServicePlatForm.updateByRunid(_runid, result, comment)
                logger.info(f'用例名称:{CaseName} 用例编号:{CaseID}  运行ID：{_runid}  结果:{result}  结果描述:{comment} 推送成功')
            else:
                print_debug(f'用例名称:{CaseName} 用例编号:{CaseID}  运行ID：{_runid}  结果:{result}  结果描述:{comment} 推送失败')


    @classmethod
    def syncCycleNameCase(self):
        ATFPlatForm.syncCycleBasic()
        if DataProcess.isNotNull(get_system_key(Constant.TEST_SRTCYCLE_ID)):
            ServicePlatForm.syncCycleCase(get_system_key(Constant.TEST_SRTCYCLE_ID))


    @classmethod
    def syncCycleBasic(self):
        if DataProcess.isNotNull(get_system_key(Constant.TEST_SRTCYCLE_ID)):
            cycleId = get_system_key(Constant.TEST_SRTCYCLE_ID)
            issueKey =""
            try:
                testPlan = ServicePlatForm.getTestPlanInfo(get_system_key(Constant.TEST_SRTCYCLE_ID).strip())
                set_system_key(Constant.TEST_SRTCYCLE_ID, str(testPlan['cycleId']))
                set_system_key(Constant.TEST_SRTCYCLE_NAME, testPlan['cycleName'])
                set_system_key(Constant.TEST_SRTCYCLE_URL, testPlan['cycleUrl'])

                set_system_key(Constant.ISSUE_KEY, testPlan['issueKey'])
                issueKey = testPlan['issueKey']
                set_system_key(Constant.TEST_TestPlan_ID, str(testPlan['testPlanId']))
                set_system_key(Constant.TEST_TestPlan_NAME, testPlan['testPlanName'])
                set_system_key(Constant.TEST_TestPlan_URL, testPlan['testPlanUrl'])
            except Exception as e:
                logger.error(f"获取周期{cycleId}中测试计划:{issueKey}\n 异常:" + repr(e))

    @classmethod
    def getCaseInfoByNameOrID(self, issueKey, caseName:str=""):
        info = ServicePlatForm.getCaseInfoByNameOrID(issueKey,caseName)
        return info


    @classmethod
    def getCaseRun(self, issuekey, name:str=""):
        cycleId = get_system_key(Constant.TEST_SRTCYCLE_ID)
        run = {'caserunid':'00000','caseid':'00000','status':'00000','casename':'00000'}
        if DataProcess.isNotNull(cycleId):
            run = ServicePlatForm.getCaseRun(cycleId, issuekey, name)
        return run









