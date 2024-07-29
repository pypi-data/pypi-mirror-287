# -*- coding: utf-8 -*-
"""
Copyright(C) 2024 baidu, Inc. All Rights Reserved

# @Time : 2024/6/4 15:04
# @Author : lidai@baidu.com
# @Email: lidai@baidu.com
# @File : st_render.py
# @Software: PyCharm
"""
import re

import streamlit as st
from bceinternalsdk.client.validator import local_name as local_name_validator
from gaea_operator.utils.accelerator import get_accelerator
from vistudiost.cache.cache import get_dataset
from vistudiost.cache.cache import get_model
from vistudiost.cache.cache import get_pipeline, get_artifact, create_job, list_artifact, list_items
from vistudiost.cache.cache import list_model_store, get_model_store
from vistudiost.components import render_st_flavour, \
    render_st_advanced_parameters, render_st_model_detail
from vistudiost.components.advanced_parameter_component import get_advance_parameters
from vistudiost.components.base_component import WindmillComponent
from vistudiost.pages.pipeline.base import get_spec_raw
from vistudiost.pages.pipeline.base import set_pipeline_params
from vistudiost.utils.random import random_string
from vistudiost.utils.render import object_format, st_write, find_index
from windmillartifactv1.client.artifact_api_artifact import parse_artifact, get_name as get_dataset_name
from windmillclient.client.windmill_client import WindmillClient
from windmillmodelv1.client.model_api_model import parse_model_name
from windmillmodelv1.client.model_api_modelstore import parse_modelstore_name
from windmilltrainingv1.client.training_api_dataset import parse_dataset_name
from windmilltrainingv1.client.training_api_project import ProjectName


def basic_part(config):
    """
    基础信息
    Returns:

    """
    basic_ok = True
    st_write("基础信息", font_size=16)
    st.markdown("")
    basic_param = {}
    pipeline_resp = get_pipeline(st.session_state.windmill["client"],
                                 request={"workspace_id": config["workspace_id"],
                                          "project_name": config["project_name"],
                                          "pipeline_name": config["pipeline_name"]})
    workspace_id = config["workspace_id"]
    project_name = config["project_name"]
    basic_param["pipeline_category"] = getattr(pipeline_resp, "category", {}).get("category", "")
    basic_param["pipeline_display_name"] = getattr(pipeline_resp, "displayName", "")
    basic_param["workspace_id"] = workspace_id
    basic_param["project_name"] = project_name

    icafe_parameters, icafe_ok = icafe_part(config)
    basic_param.update(icafe_parameters)

    return basic_param, basic_ok and icafe_ok


def train_part(config,
               workspace_id,
               project_name,
               pipeline_category,
               train_advance_parameters):
    """
    模型训练
    Args:
        config:
        workspace_id
        project_name
        train_advance_parameters:
        pipeline_category

    Returns:

    """
    st.markdown("")
    st_write("模型训练", font_size=16)
    st.markdown("")

    train_parameters = {}
    model_store_name, ok_model_store = render_st_model_store(["模型仓库"],
                                                             request={
                                                                 "workspace_id": workspace_id},
                                                             pipeline_param_keys={
                                                                 "model_store_name": "model_store_name"},
                                                             pipeline_params=config["parameters"],
                                                             permission=config["permission"])
    train_parameters.update(model_store_name)

    train_dataset, ok_train_dataset = render_st_dataset(["训练集选择"],
                                                        request={
                                                            "workspace_id": workspace_id,
                                                            "project_name": project_name,
                                                            "categories": [pipeline_category]},
                                                        pipeline_param_keys={
                                                            "dataset_name": "train.train_dataset_name"},
                                                        pipeline_params=config["parameters"],
                                                        permission=config["permission"])
    train_parameters.update(train_dataset)

    val_dataset, ok_eval_dataset = render_st_dataset(["验证集选择"],
                                                     request={
                                                         "workspace_id": workspace_id,
                                                         "project_name": project_name,
                                                         "categories": [pipeline_category]},
                                                     pipeline_param_keys={
                                                         "dataset_name": "train.val_dataset_name"},
                                                     pipeline_params=config["parameters"],
                                                     permission=config["permission"])
    if val_dataset["train.val_dataset_name"] == train_parameters["train.train_dataset_name"]:
        st_write("训练集的数据建议不要出现在验证集中，否则会导致评估指标产生极大的偏差")
    train_parameters.update(val_dataset)
    model, ok_model = render_st_model(["新建模型"],
                                      pipeline_param_keys={"model_name": "train.model_name",
                                                           "model_display_name": "train.model_display_name"},
                                      pipeline_params=config["parameters"],
                                      request={
                                          "model_store_name": model_store_name['model_store_name'],
                                          "workspace_id": workspace_id,
                                          "model_display_name": "",
                                          "categories": [pipeline_category],
                                      },
                                      permission=config["permission"])
    train_parameters.update(model)

    advance_param, is_advance_param_ok = render_st_advanced_parameters("train", train_advance_parameters)
    train_parameters.update(advance_param)

    st.markdown("")
    st_write("算力选择", font_size=16)

    mode_index = 0
    select_mode = st.radio(
        f'',
        ["PaddleCloud", "CV"],
        key='cluster_type',
        index=mode_index
    )

    compute_ok = True
    flavour_list = [
        {"name": "c8m32gpu1", "display_name": "CPU: 8核 内存: 32Gi GPU: 1卡"},
        {"name": "c8m32gpu2", "display_name": "CPU: 8核 内存: 32Gi GPU: 2卡"},
        {"name": "c16m64gpu2", "display_name": "CPU: 16核 内存: 64Gi GPU: 2卡"},
        {"name": "c16m32gpu4", "display_name": "CPU: 16核 内存: 32Gi GPU: 4卡"},
        {"name": "c16m64gpu4", "display_name": "CPU: 16核 内存: 64Gi GPU: 4卡"},
        {"name": "c32m96gpu4", "display_name": "CPU: 32核 内存: 96Gi GPU: 4卡"}]
    if select_mode == "PaddleCloud":
        flavour_list = [{"name": "c16m32", "display_name": "CPU: 16核 内存: 32Gi 无GPU"}]
        pdc_parameters, compute_ok = paddlecloud_part(config)
        train_parameters.update(pdc_parameters)

    # TODO:suggest compute
    train_parameters.update({'train.compute_name': 'workspaces/cv/computes/qcva10'})
    flavour_name, ok_flavour = render_st_flavour(["资源套餐"],
                                                 request={"name": "gpu", "flavour_list": flavour_list},
                                                 pipeline_param_keys={"flavour_name": "train.flavour"},
                                                 pipeline_params=config["parameters"],
                                                 permission=config["permission"])
    train_parameters.update(flavour_name)
    is_ok = (ok_train_dataset and ok_eval_dataset and ok_flavour
             and ok_model and ok_model_store and compute_ok and is_advance_param_ok)

    return train_parameters, is_ok


def _modify_accelerator(accelerator: str):
    if accelerator == "A10":
        return "T4"
    else:
        return accelerator


def transform_part(config,
                   model_store_name,
                   model_name,
                   pipeline_display_name,
                   transform_advance_parameters,
                   train_advance_parameters):
    """
    模型转换
    Args:
        config:
        train_advance_parameters:
        transform_advance_parameters:
        pipeline_display_name:
        model_name
        model_store_name
    Returns:

    """
    st.markdown("")
    st_write("模型转换", font_size=16)
    st.markdown("")
    param_trans = {}
    model_name_resp = parse_model_name(model_name)
    if model_name_resp is not None:
        model_name = model_name_resp.local_name
    accelerator_tips = ["T4", "R200"]
    if config['workspace_id'] == 'cv':
        accelerator_tips = ["A10"]

    accelerator = st.selectbox("目标显卡类型",
                               options=[config["parameters"]["transform.accelerator"]]
                               if config.get("parameters", {})
                               else accelerator_tips,
                               key="transform.accelerator")

    shadow_accelerator = _modify_accelerator(accelerator)
    accelerator = get_accelerator(accelerator)
    flavour_name = accelerator.suggest_flavours()[0]["name"]
    if parse_model_name(model_name) is not None:
        model_name = parse_model_name(model_name).local_name

    model_display_name = st.text_input("目标模型", f'{pipeline_display_name}'
                                                   f'-{accelerator.name}',
                                       key=f"transform.transform_model_display_name", max_chars=80, disabled=True)
    param_trans["transform.transform_model_display_name"] = model_display_name
    param_trans["transform.transform_model_name"] = model_store_name + "/models/" + model_name

    advance_param, is_advance_param_ok = render_st_advanced_parameters("transform",
                                                  transform_advance_parameters,
                                                  train_advance_parameters)
    param_trans.update(advance_param)

    param_trans["transform.accelerator"] = shadow_accelerator
    param_trans["transform.flavour"] = flavour_name

    # TODO :use suggest compute
    compute_name = {'transform.compute_name': 'workspaces/cv/computes/qcva10'}
    param_trans.update(compute_name)

    return param_trans, is_advance_param_ok


def package_part(config,
                 workspace_id,
                 model_store_name,
                 model_name,
                 model_display_name,
                 accelerator,
                 compute_name,
                 pipeline_category,
                 icafe_id):
    """
    模型包组装
    Returns:

    """
    st.markdown("")
    st_write("模型组装", font_size=16)
    st.markdown("")

    if model_name is not None and parse_model_name(model_name) is not None:
        model_name = parse_model_name(model_name).local_name

    ensemble_model_name = f"{model_display_name}-模型包-{icafe_id}" if icafe_id != "" else f"{model_display_name}-模型包"
    model, ok_model = render_st_model(["新建模型包"],
                                      pipeline_param_keys={"model_name": "package.ensemble_model_name",
                                                           "model_display_name": "package.ensemble_model_display_name"},
                                      pipeline_params=config["parameters"],
                                      request={
                                          "model_store_name": model_store_name,
                                          "model_display_name": ensemble_model_name,
                                          "model_name": f"{model_name}-ensemble"
                                          if model_name else f"-ensemble",
                                          "workspace_id": workspace_id,
                                          "categories": [pipeline_category],
                                          "icafe_id": icafe_id},
                                      permission=config["permission"])

    model.update({"package.compute_name": compute_name,
                  "package.accelerator": accelerator})
    return model, ok_model


def icafe_part(config):
    """
    icafe 卡片信息同步
    Args:
        None
    Returns:
        Dict
        :param config:
    """
    config_paramerters = config['parameters']
    icafe_parameters = {}
    is_icafe_ok = True

    if_icafe_id_disabled = False
    icafe_id = ""
    if config_paramerters.get("icafe_id"):
        icafe_id = config_paramerters.get("icafe_id")
        if_icafe_id_disabled = True

    icafe_id = st.text_input("[必填]卡片 ID", icafe_id, key=f"icafe_id", max_chars=80, disabled=if_icafe_id_disabled)
    if not validate_icafe_id_input(icafe_id):
        is_icafe_ok = False
        st.error("请输入正确的卡片 ID，支持仅输入卡片数字编号（如 477 ）或完整卡片名称（如 cv-algorithm-477 ）")

    icafe_parameters["icafe_id"] = icafe_id

    if_icafe_operator_disabled = False
    icafe_operator = ""
    if config_paramerters.get("icafe_operator"):
        icafe_operator = config_paramerters.get("icafe_operator")
        if_icafe_operator_disabled = True

    icafe_operator_input = st.text_input("[必填]操作人（邮箱前缀）", icafe_operator,
                                         key=f"icafe_operator", max_chars=80, disabled=if_icafe_operator_disabled)
    if icafe_operator_input:
        validate_operator_result = validate_icafe_operator_input(icafe_operator_input)
        if validate_operator_result:
            icafe_parameters["icafe_operator"] = icafe_operator_input
        else:
            icafe_parameters["icafe_operator"] = ""
            is_icafe_ok = False
            st.error("请输入正确的操作人（邮箱前缀）")

    icafe_parameters["icafe_operator"] = icafe_operator_input
    return icafe_parameters, is_icafe_ok


def validate_icafe_id_input(icafe_id_input):
    """
    验证输入的ICafe ID是否合法，如果合法则返回对应的整数，否则返回None。
    支持以下两种格式：
        1. 纯数字形式，例如"1234567890"；
        2. "cv-algorithm-{number}"形式，其中{number}为一个正整数，例如"cv-algorithm-1234567890"。

    Args:
        icafe_id_input (str): ICafe ID的输入字符串，可以是纯数字或者包含"cv-algorithm-{number}"形式的字符串。

    Returns:
        Union[int, None]: 如果输入的ICafe ID合法，则返回对应的整数；如果不合法，则返回None。
    """
    number_pattern = r'^\d+$'
    cv_pattern = r'^cv-algorithm-(\d+)$'

    # 判断并提取数字
    if re.match(number_pattern, icafe_id_input):
        return int(icafe_id_input)
    elif match := re.match(cv_pattern, icafe_id_input):
        return int(match.group(1))
    else:
        return None


def validate_icafe_operator_input(icafe_operator_input):
    """
    验证ICAFE操作员输入是否符合要求，返回True或None。

    Args:
        icafe_operator_input (str): ICAFE操作员的输入字符串，必须为非空字符串且只包含英文、数字和特殊符号（._-）。

    Returns:
        Union[bool, None]: 如果输入字符串符合要求，返回True；否则返回None。
    """
    pattern = r'^[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*$'

    # 使用正则表达式进行匹配
    if re.match(pattern, icafe_operator_input):
        return True
    else:
        return None


def paddlecloud_part(config):
    """
    pdc 提交任务
    Args:
        None
    Returns:
        Dict
    """
    st.markdown("")
    st_write("PaddleCloud 配置", font_size=14)
    st.markdown("")

    config_paramerters = config['parameters']
    pdc_parameters = {}

    if_pdc_ak_disabled = False
    pdc_ak = ""
    if config_paramerters.get("pdc_ak"):
        pdc_ak = config_paramerters.get("pdc_ak")
        if_pdc_ak_disabled = True
    pdc_ak = st.text_input("[必填]PaddleCloud 提交任务 个人AK", value=pdc_ak, max_chars=80, disabled=if_pdc_ak_disabled)

    if_pdc_sk_disabled = False
    pdc_sk = ""
    if config_paramerters.get("pdc_ak"):
        pdc_sk = config_paramerters.get("pdc_sk")
        if_pdc_sk_disabled = True
    pdc_sk = st.text_input("[必填]PaddleCloud 提交任务 个人SK", value=pdc_sk, max_chars=80, disabled=if_pdc_sk_disabled)

    if_algo_id_disabled = False
    algo_id = ""
    if config_paramerters.get("algo_id"):
        algo_id = config_paramerters.get("algo_id")
        if_algo_id_disabled = True
    algo_id = st.text_input("[必填]算法ID，需由个人创建，并确认与AK/SK绑定", value=algo_id, max_chars=80,
                            disabled=if_algo_id_disabled)

    if_train_group_name_disabled = False
    train_group_name = ""
    if config_paramerters.get("train_group_name"):
        train_group_name = config_paramerters.get("train_group_name")
        if_train_group_name_disabled = True
    train_group_name = st.text_input("[必填]训练资源Group", value=train_group_name, max_chars=80,
                                     disabled=if_train_group_name_disabled)

    if_k8s_gpu_cards_disabled = False
    k8s_gpu_cards = 4
    if config_paramerters.get("k8s_gpu_cards"):
        k8s_gpu_cards = config_paramerters.get("k8s_gpu_cards")
        if_k8s_gpu_cards_disabled = True
    k8s_gpu_cards = st.text_input("[必填]PDC任务占用卡数，注意是否为可选择卡数，否则可能会导致提交任务失败",
                                  value=k8s_gpu_cards, disabled=if_k8s_gpu_cards_disabled)

    pdc_parameters["pdc_ak"] = pdc_ak
    pdc_parameters["pdc_sk"] = pdc_sk
    pdc_parameters["algo_id"] = algo_id
    pdc_parameters["train_group_name"] = train_group_name
    pdc_parameters["k8s_gpu_cards"] = k8s_gpu_cards
    pdc_ok = True
    if pdc_ak == "" or pdc_sk == "" or algo_id == "" or train_group_name == "" or k8s_gpu_cards == "":
        pdc_ok = False

    return pdc_parameters, pdc_ok


def get_parts(config, basic_parameter):
    """
    get_parts
    Args:
        config:
        basic_parameter:

    Returns:

    """
    train_advance_parameters = get_advance_parameters("train_parameter.yaml")
    if train_advance_parameters is None:
        print(f"none advanced parameters")
        return
    transform_advance_parameters = get_advance_parameters("transform_parameter.yaml")
    train_parameter, train_ok = train_part(config,
                                           basic_parameter["workspace_id"],
                                           basic_parameter["project_name"],
                                           basic_parameter["pipeline_category"],
                                           train_advance_parameters)
    train_parameter.update(
        {"icafe_id": basic_parameter["icafe_id"], "icafe_operator": basic_parameter["icafe_operator"]})

    eval_parameter, eval_ok = eval_part(basic_parameter["workspace_id"],
                                        basic_parameter["project_name"],
                                        #                                        train_parameter["train.compute_name"],
                                        basic_parameter["pipeline_category"])
    trans_parameter, transform_ok = transform_part(config,
                                     train_parameter["model_store_name"],
                                     train_parameter["train.model_name"],
                                     train_parameter["train.model_display_name"],
                                     transform_advance_parameters,
                                     train_advance_parameters
                                     )
    trans_eval_parameter = transform_eval_part(trans_parameter["transform.compute_name"],
                                               trans_parameter["transform.accelerator"],
                                               basic_parameter['workspace_id'],
                                               basic_parameter['project_name'],
                                               basic_parameter['pipeline_category'])
    package_parameter, package_ok = package_part(config,
                                                 basic_parameter["workspace_id"],
                                                 train_parameter["model_store_name"],
                                                 trans_parameter["transform.transform_model_name"],
                                                 trans_parameter["transform.transform_model_display_name"],
                                                 trans_parameter["transform.accelerator"],
                                                 trans_parameter["transform.compute_name"],
                                                 basic_parameter["pipeline_category"],
                                                 basic_parameter["icafe_id"])
    inference_parameter = inference_part(trans_parameter["transform.compute_name"],
                                         package_parameter["package.ensemble_model_name"],
                                         trans_parameter["transform.flavour"],
                                         get_accelerator(trans_parameter["transform.accelerator"]),
                                         basic_parameter['workspace_id'],
                                         basic_parameter['project_name'],
                                         basic_parameter['pipeline_category'])

    return train_parameter, train_ok, \
        eval_parameter, eval_ok, \
        trans_parameter, transform_ok, \
        trans_eval_parameter, \
        package_parameter, package_ok, \
        inference_parameter


def main():
    """
    Args:
    Returns:

    """
    config = st.session_state.config
    set_pipeline_params()

    basic_parameter, basic_ok = basic_part(config)

    train_parameter, train_ok, \
        eval_parameter, eval_ok, \
        trans_parameter, tansform_ok, \
        trans_eval_parameter, \
        package_parameter, package_ok, \
        inference_parameter = get_parts(config, basic_parameter)

    parameters = {}
    parameters.update(train_parameter)
    parameters.update(eval_parameter)
    parameters.update(trans_parameter)
    parameters.update(trans_eval_parameter)
    parameters.update(package_parameter)
    parameters.update(inference_parameter)

    parameters["windmill_ak"] = st.session_state.windmill["client"].config.credentials.access_key_id.decode('utf-8')
    parameters["windmill_sk"] = st.session_state.windmill["client"].config.credentials.secret_access_key.decode('utf-8')
    parameters["windmill_endpoint"] = st.secrets.windmill.endpoint
    project_name = ProjectName(workspace_id=basic_parameter["workspace_id"], local_name=basic_parameter["project_name"])
    parameters["project_name"] = project_name.get_name()
    parameters["model_store_name"] = train_parameter["model_store_name"]

    artifact_resp = get_artifact(st.session_state.windmill["client"], st.session_state.config["artifact_name"])
    if getattr(artifact_resp, "tags") and artifact_resp.tags.get("scene"):
        parameters["scene"] = artifact_resp.tags.get("scene")
    is_ok = basic_ok and train_ok and eval_ok and package_ok and tansform_ok

    if config["permission"] == "readwrite":
        spec_raw = get_spec_raw(trans_parameter["transform.accelerator"])
        request = {"parameters": parameters,
                   "version": config["version"],
                   "object_name": config["object_name"],
                   "pipeline": config["pipeline_name"],
                   "workspace_id": basic_parameter["workspace_id"],
                   "project_name": basic_parameter["project_name"],
                   "artifact_name": config["artifact_name"],
                   "spec_raw": spec_raw}

        job_component = CreateJobComponent(st.session_state.windmill["client"],
                                           config["permission"],
                                           pipeline_params=config["parameters"],
                                           pipeline_param_keys={"job_name": "local_name",
                                                                "experiment_name": "job_experiment_name"})

        job_component.ok = is_ok
        job_component.render(request)


# overwirite CreateJobComponent
class CreateJobComponent(WindmillComponent):
    """
    JobComponent
    """

    def __init__(self, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        JobComponent
        Args:
            client:
        """
        super(CreateJobComponent, self).__init__(client=client,
                                                 pipeline_params=pipeline_params,
                                                 permission=permission)
        if pipeline_param_keys is None:
            pipeline_param_keys = {"job_name": "job_local_name", "experiment_name": "experiment_name"}
        self.job_key = pipeline_param_keys["job_name"]
        self.experiment_key = pipeline_param_keys["experiment_name"]

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """
        st.markdown("")
        st_write("创建作业", font_size=18)
        st.markdown("")
        st_write("基本配置", font_size=16)
        if "random_job_name" not in st.session_state:
            st.session_state['random_job_name'] = "job" + random_string()
        display_name = st.text_input(
            '作业名称',
            max_chars=100,
            value=self.pipeline_params.get("display_name", ""),
            key=f"{self.job_key} + _display_name"
        )
        if display_name == "":
            st.error("请填写作业名称")
            self.ok = False

        local_name = st.session_state.get('random_job_name', "")

        request["display_name"] = display_name
        request["local_name"] = local_name
        if local_name == "":
            st.error("请填写作业名称")
            self.ok = False
        if local_name:
            if not local_name_validator(local_name):
                self.show_error('任务名称仅以字母或下划线 "_" 开头，后续可以包含字母、数字、连字符 "-"')
            else:
                st.session_state['random_job_name'] = local_name
        description = st.text_input(
            '作业描述',
            max_chars=255,
            placeholder="请输入作业描述",
            value=self.pipeline_params.get("description", ""),
            key="job_description")
        request["description"] = description

        st.session_state['random_experiment_name'] = 'exp' + random_string()
        experiment_name = st.session_state['random_experiment_name']
        if experiment_name:
            if not local_name_validator(experiment_name):
                self.show_error('实验名称仅以字母或下划线 "_" 开头，后续可以包含字母、数字、连字符 "-"')
                self.ok = False

        request["experiment_name"] = experiment_name
        if st.button("创建任务", key="job_start", disabled=not self.ok, use_container_width=True):
            if request["local_name"] != "" and request["experiment_name"] != "":
                response = create_job(self.client, request)
                if response.message:
                    st.toast(f'创建失败: {response.message} 请稍后重试')

                else:
                    st.toast(f'创建成功，请至『作业管理』查看作业详情')

    def render_with_readonly(self):
        """
        渲染界面
        Args:
            pipeline_params:

        Returns:

        """
        return


def render_st_dataset(labels,
                      request,
                      client=None,
                      pipeline_param_keys=None,
                      pipeline_params=None,
                      permission=None):
    """
    render_st_dataset
    Args:
        labels:
        client:
        request:
        pipeline_param_keys:
        pipeline_params:
        permission:

    Returns:

    """
    return DatasetComponent(labels,
                            client,
                            permission,
                            pipeline_params,
                            pipeline_param_keys).render(request)


# override DatasetComponent
class DatasetComponent(WindmillComponent):
    """
    DatasetComponent
    """

    def __init__(self, labels, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        DatasetComponent
        Args:
            client:
        """
        super(DatasetComponent, self).__init__(client=client,
                                               pipeline_params=pipeline_params,
                                               permission=permission)
        self.labels = labels
        if pipeline_param_keys is None:
            pipeline_param_keys = {"dataset_name": "WINDMILL_DATASET_NAME"}
        self.dataset_name_key = pipeline_param_keys["dataset_name"]

    def render_with_readonly(self):
        """
        渲染界面
        Returns:

        """
        dataset_col = st.columns([4])[0]  # 只需要一个列，所以只定义一个列

        pre_dataset_object_name = ""
        pre_dataset_version = ""
        if self.pipeline_params.get(self.dataset_name_key):
            pre_dataset_object_name = parse_artifact(self.pipeline_params.get(self.dataset_name_key)).naming.object_name
            pre_dataset_version = str(parse_artifact(self.pipeline_params.get(self.dataset_name_key)).version)

        # TODO: get dataset artifact version
        with dataset_col:
            n = parse_artifact(self.pipeline_params[self.dataset_name_key])
            object_name = n.naming.object_name
            dataset_name = parse_dataset_name(object_name)
            dataset_resp = get_dataset(self.client, dataset_name)
            ds_selected = st.selectbox(
                f':red[*]{self.labels[0]}: ',
                options=[dataset_resp],
                format_func=object_format,
                key=self.dataset_name_key
            )

        return {self.dataset_name_key: self.pipeline_params[self.dataset_name_key]}, self.ok

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """
        dataset_col = st.columns([4])[0]  # 只需要一个列，所以只定义一个列

        pre_dataset_object_name = ""
        pre_dataset_version = ""
        if self.pipeline_params.get(self.dataset_name_key):
            pre_dataset_object_name = parse_artifact(self.pipeline_params.get(self.dataset_name_key)).naming.object_name
            pre_dataset_version = str(parse_artifact(self.pipeline_params.get(self.dataset_name_key)).version)

        with dataset_col:
            dataset_list = list_dataset(self.client, request)

            # 获取所有数据集和版本的组合
            dataset_version_list = []
            for dataset in dataset_list:
                artifact_list = list_artifact(self.client, dataset['name'])
                for artifact in artifact_list:
                    display_name = f"{dataset['displayName']} (v{artifact['version']})"
                    dataset_version_list.append((display_name, dataset['name'], artifact['version']))

            # 查找预选的索引
            pre_selected = f"{pre_dataset_object_name} (v{pre_dataset_version})"
            index = next((i for i, (name, _, version) in enumerate(dataset_version_list) if
                          f"{name} (v{version})" == pre_selected), 0)

            # 创建选择框
            selected_option = st.selectbox(
                f':red[*]{self.labels[0]}:',
                options=dataset_version_list,
                format_func=lambda x: x[0],  # 只显示名称+版本
                key=self.dataset_name_key,
                index=index
            )

            if not selected_option:
                st.error("数据集不存在")
                self.ok = False
                return {self.dataset_name_key: ''}, self.ok

        # 解析选中的数据集名称和版本
        selected_name = selected_option[1]
        selected_version = selected_option[2]

        return {self.dataset_name_key: get_dataset_name(selected_name, selected_version)}, self.ok


def eval_part(workspace_id,
              project_name,
              pipeline_category):
    """
    模型评估
    Args:

    Returns:

    """
    st.markdown("")
    st_write("模型评估", font_size=16)
    st.markdown("")
    eval_param = {}
    dataset, ok_dataset = render_st_dataset(["测试集选择"],
                                            request={"workspace_id": workspace_id,
                                                     "project_name": project_name,
                                                     "categories": [pipeline_category]},
                                            pipeline_param_keys={"dataset_name": "eval.dataset_name"},
                                            pipeline_params=st.session_state.config["parameters"],
                                            permission=st.session_state.config["permission"])
    eval_param.update(dataset)
    # TODO: suggest compute
    eval_param["eval.compute_name"] = "workspaces/cv/computes/qcva10"

    return eval_param, ok_dataset


def render_st_model_store(labels,
                          request,
                          client=None,
                          pipeline_param_keys=None,
                          pipeline_params=None,
                          permission=None):
    """
    render_st_model_store
    Args:
        labels:
        client:
        request:
        pipeline_param_keys:
        pipeline_params:
        permission:

    Returns:

    """
    return ModelStoreComponent(labels,
                               client,
                               permission,
                               pipeline_params,
                               pipeline_param_keys).render(request)


class ModelStoreComponent(WindmillComponent):
    """
    ModelStoreComponent
    """

    def __init__(self, labels, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        ModelStoreComponent
        Args:
            client:
        """
        super(ModelStoreComponent, self).__init__(client=client,
                                                  pipeline_params=pipeline_params,
                                                  permission=permission)
        self.labels = labels
        if pipeline_param_keys is None:
            pipeline_param_keys = {"model_store_name": "MODEL_STORE_NAME"}
        self.model_store_name_key = pipeline_param_keys["model_store_name"]

    def render_with_readonly(self):
        """
        渲染界面
        Returns:

        """
        model_store_name = parse_modelstore_name(self.pipeline_params[self.model_store_name_key])
        if model_store_name is not None:
            model_store_resp = get_model_store(self.client, model_store_name)
        model_store_selected = st.selectbox(
            f':red[*]{self.labels[0]}: ',
            options=[model_store_resp],
            format_func=object_format,
            key=self.model_store_name_key
        )

        return {self.model_store_name_key: self.pipeline_params[self.model_store_name_key]}, self.ok

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """
        if request.get("model_store_name") is not None:
            model_store_name = parse_modelstore_name(request.get("model_store_name"))
            model_store_resp = get_model_store(self.client, model_store_name)
            model_store_selected = st.text_input(
                f':red[*]{self.labels[0]}: ',
                value=object_format(model_store_resp.__dict__),
                key=self.model_store_name_key,
                disabled=True
            )
            return {self.model_store_name_key: model_store_resp.__dict__["name"]}, self.ok

        model_store_list = list_model_store(self.client, request)

        model_store_selected = st.selectbox(
            f':red[*]{self.labels[0]}: ',
            options=model_store_list,
            format_func=object_format,
            key=self.model_store_name_key,
            index=find_index(model_store_list, "name", self.pipeline_params.get(self.model_store_name_key, ""))
        )
        if model_store_selected is None:
            st.error("请选择模型仓库")
            self.ok = False

        return {self.model_store_name_key: model_store_selected["name"]}, self.ok


def render_st_model(labels,
                    request,
                    client=None,
                    pipeline_param_keys=None,
                    pipeline_params=None,
                    permission=None):
    """
    render_st_model
    Args:
        labels:
        client:
        request:
        pipeline_param_keys:
        pipeline_params:
        permission:

    Returns:

    """
    return ModelComponent(labels,
                          client,
                          permission,
                          pipeline_params,
                          pipeline_param_keys).render(request)


class ModelComponent(WindmillComponent):
    """
    ModelComponent
    """

    def __init__(self, labels, client,
                 permission,
                 pipeline_params={},
                 pipeline_param_keys=None):
        """
        ModelComponent
        Args:
            client:
        """
        super(ModelComponent, self).__init__(client=client,
                                             pipeline_params=pipeline_params,
                                             permission=permission)
        self.labels = labels
        if pipeline_param_keys is None:
            pipeline_param_keys = {"model_name": "MODEL_NAME",
                                   "model_display_name": "train.MODEL_DISPLAYNAME_NAME"}
        self.model_name_key = pipeline_param_keys["model_name"]
        self.display_name_key = pipeline_param_keys["model_display_name"]

    def render_with_readonly(self):
        """
        渲染界面
        Returns:

        """
        config = {}
        if self.display_name_key in self.pipeline_params:
            st.selectbox(f':red[*]模型名称:', [self.pipeline_params[self.display_name_key]], key=self.display_name_key)
            config[self.display_name_key] = self.pipeline_params[self.display_name_key]

        config[self.model_name_key] = self.pipeline_params[self.model_name_key]
        model_name = parse_model_name(self.pipeline_params[self.model_name_key])

        st.selectbox(f':red[*]系统名称:', [model_name.local_name], key=self.model_name_key)

        return config, self.ok

    def render_with_readwrite(self, request):
        """
        渲染界面
        Args:

        Returns:

        """

        mode_index = 1
        if self.pipeline_params.get(self.model_name_key):
            mode_index = 0
            response = get_model(self.client, parse_model_name(self.pipeline_params[self.model_name_key]))
            if response.message:
                mode_index = 1

        if request.get("model_name", "") and parse_model_name(request["model_name"]) is not None:
            request["model_name"] = parse_model_name(request["model_name"]).local_name

        new_model_name = request.get("model_display_name", "") if request.get("model_display_name", "") else ""
        display_name = st.text_input(f':red[*]新模型名称',
                                     value=new_model_name,
                                     key=self.display_name_key, max_chars=80)
        if display_name == "":
            st.error('请输入模型名称')
            self.ok = False

        if f"random_{self.model_name_key}" not in st.session_state:
            setattr(st.session_state, f"random_{self.model_name_key}", "model" + random_string())

        if self.pipeline_params.get(self.model_name_key) and mode_index != 0:
            value = parse_model_name(self.pipeline_params[self.model_name_key]).local_name
        else:
            value = request.get("model_name") if request.get("model_name") \
                else getattr(st.session_state, f"random_{self.model_name_key}", None)

        model_name = value
        return {self.model_name_key: request["model_store_name"] + "/models/" + model_name,
                self.display_name_key: display_name}, self.ok


def transform_eval_part(flavour,
                        accelerator,
                        workspace_id,
                        project_name,
                        pipeline_category):
    """
    模型转换评估
    Args:
        flavour:
        workspace_id:
        accelerator:
        project_name:
        pipeline_category:

    Returns:

    """
    st.markdown("")
    st_write("模型转换评估", font_size=16)
    st.markdown("")

    col_dataset = st.columns([4])[0]
    transform_eval_dataset, ok_dataset = render_st_dataset(["测试集选择"],
                                                           request={"workspace_id": workspace_id,
                                                                    "project_name": project_name,
                                                                    "categories": [pipeline_category]},
                                                           pipeline_param_keys={
                                                               "dataset_name": "transform-eval.dataset_name"},
                                                           pipeline_params=st.session_state.config["parameters"],
                                                           permission=st.session_state.config["permission"])
    # TODO: suggest compute
    transform_eval_params = {
        "transform-eval.compute_name": "workspaces/cv/computes/qcva10",
        "transform-eval.flavour": flavour,
        "transform-eval.accelerator": accelerator
    }
    transform_eval_params.update(transform_eval_dataset)
    return transform_eval_params


def inference_part(compute_name, model_name, flavour, accelerator, workspace_id, project_name, pipeline_category):
    """
    模型包评估
    Args:
        accelerator:
        flavour:
        compute_name
        model_name

    Returns:

    """
    st.markdown("")
    st_write("模型包评估", font_size=16)
    render_st_model_detail(labels=["模型包评估信息详情"], client=st.session_state.windmill["client"],
                           pipeline_param_keys={"model_detail_key": "model_detail_key"},
                           request={"model_name": model_name,
                                    "accelerator": accelerator})
    st.markdown("")

    inference_dataset, ok_dataset = render_st_dataset(["测试集选择"],
                                                      request={"workspace_id": workspace_id,
                                                               "project_name": project_name,
                                                               "categories": [pipeline_category]},
                                                      pipeline_param_keys={"dataset_name": "infer.dataset_name"},
                                                      pipeline_params=st.session_state.config["parameters"],
                                                      permission=st.session_state.config["permission"])

    # TODO: suggest compute
    inference_params = {"inference.compute_name": "workspaces/cv/computes/qcva10",
                        "inference.flavour": flavour,
                        "inference.accelerator": accelerator.name}
    inference_params.update(inference_dataset)

    return inference_params


def list_dataset(client: WindmillClient, request):
    """
    list dataset
    Args:
        client:
        request:
    """
    return list_items(client, client.list_dataset,
                      workspace_id=request["workspace_id"],
                      project_name=request["project_name"],
                      categories=request.get("categories"))


def object_format(obj):
    """
    格式化对象
    Args:
        obj:
    """
    if obj is None or obj == "" or obj == {} or obj == []:
        return ''
    if isinstance(obj, dict):
        display_name = obj.get('displayName', '')
        artifact = obj.get('artifact', '')
        version = ""
        if artifact:
            version = artifact.get('version', '')
    else:
        display_name = getattr(obj, 'displayName', '')
        artifact = getattr(obj, 'artifact', '')
        version = getattr(artifact, 'version', '')
    return str(display_name) + "-v" + str(version) if version != "" else display_name


if __name__ == '__main__':
    main()
